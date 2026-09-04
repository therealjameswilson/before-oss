"""Conservative, unique-person summaries of the reviewed public projection."""
from __future__ import annotations

from collections import Counter, defaultdict


VERIFIED_SQL = """
    a.publication_status IN ('published', 'publish_qualified')
    AND a.claim_confidence IN ('confirmed', 'high')
    AND a.identity_confidence IN ('confirmed', 'high_confidence')
    AND pe.identity_status IN ('confirmed', 'high_confidence')
    AND pe.research_status <> 'conflicting_sources'
    AND a.pre_oss_temporal_basis IN (
        'explicit_immediate', 'strongly_date_bounded',
        'probable_immediate', 'documented_prewar'
    )
"""


def eligible_affiliation(profile: dict, item: dict) -> bool:
    """Missing assessments fail closed; historical evidence remains public."""
    return (
        profile.get('identity_status') in {'confirmed', 'high_confidence'}
        and profile.get('research_status') != 'conflicting_sources'
        and item.get('identity_confidence') in {'confirmed', 'high_confidence'}
        and item.get('claim_confidence') in {'confirmed', 'high'}
        and item.get('publication_status') in {'published', 'publish_qualified'}
        and item.get('temporal_basis') in {
            'explicit_immediate', 'strongly_date_bounded',
            'probable_immediate', 'documented_prewar',
        }
    )


def profile_affiliations(profile: dict) -> list[dict]:
    # One affiliation can appear in both immediate and last-civilian fields.
    unique = {}
    for field in ('immediate_pre_oss_affiliations', 'last_civilian_pre_service',
                  'other_pre_oss_affiliations'):
        for item in profile.get(field, []):
            unique[item['affiliation_id']] = item
    return list(unique.values())


def build_analytics(profiles: list[dict], organizations: list[dict], stats: dict) -> dict:
    orgs = {o['organization_id']: o for o in organizations}
    definitions = [
        ('immediate', 'Documented immediate affiliations',
         'Explicit-immediate or strongly date-bounded affiliations only.'),
        ('last_civilian', 'Documented last civilian employers',
         'Employment or self-employment explicitly marked last civilian before service.'),
        ('sectors', 'Sectors of documented civilian employers',
         'All accepted pre-OSS employment and self-employment, including earlier jobs.'),
        ('pathways', 'Civilian and military pathways immediately before OSS',
         'Relationship types of explicit-immediate or strongly date-bounded affiliations.'),
        ('academic', 'Academic institutions: employment versus study',
         'Academia-and-research institutions; student status is never employment.'),
        ('geography', 'Documented employer locations',
         'Country and region attached to accepted employment; unknown locations remain visible.'),
    ]
    buckets = {key: defaultdict(set) for key, _, _ in definitions}
    metadata = {key: {} for key, _, _ in definitions}

    def add(chart, key, label, pid, organization_id=None):
        buckets[chart][key].add(pid)
        metadata[chart][key] = {'label': label, 'organization_id': organization_id}

    for profile in profiles:
        pid = profile['person_id']
        for a in profile_affiliations(profile):
            if not eligible_affiliation(profile, a):
                continue
            org = orgs.get(a.get('organization_id'), {})
            name = a.get('canonical_organization') or a.get('organization_name_as_found')
            oid = org.get('organization_id')
            label = name or ('Self-employment' if a['relationship_type'] == 'self_employment'
                             else 'Organization not identified')
            key = oid or label
            employment = a['relationship_type'] in {'employment', 'self_employment'}
            immediate = a.get('immediate_pre_oss') and a['temporal_basis'] in {
                'explicit_immediate', 'strongly_date_bounded'}
            if immediate:
                add('immediate', key, label, pid, oid)
                pathway = a['relationship_type'].replace('_', ' ')
                add('pathways', pathway, pathway, pid)
            if employment and a.get('last_civilian_pre_service'):
                add('last_civilian', key, label, pid, oid)
            if employment:
                sector = a.get('sector') or org.get('sector') or 'unknown'
                add('sectors', sector, sector.replace('_', ' '), pid)
                location = ', '.join(str(v) for v in [a.get('state_or_region'),
                    a.get('country') or org.get('country')] if v) or 'Location not established'
                add('geography', location, location, pid)
            if org.get('sector') == 'academia_and_research' and (
                employment or a['relationship_type'] == 'student'
            ):
                relationship = 'employment' if employment else 'student'
                add('academic', (key, relationship), f'{label} — {relationship}', pid, oid)

    featured = []
    for profile in profiles:
        choices = [a for a in profile_affiliations(profile)
                   if eligible_affiliation(profile, a)
                   and a['relationship_type'] in {'employment', 'self_employment'}
                   and a.get('last_civilian_pre_service')]
        if choices:
            a = sorted(choices, key=lambda x: (x['claim_confidence'] != 'confirmed', x['affiliation_id']))[0]
            featured.append({'person_id': profile['person_id'], 'name': profile['display_name'],
                'organization': a.get('canonical_organization') or a.get('organization_name_as_found') or 'Self-employment',
                'role': a.get('role_title') or a.get('occupation'), 'confidence': a['claim_confidence']})
    featured.sort(key=lambda p: (p['confidence'] != 'confirmed', p['name'], p['person_id']))
    charts = []
    for key, title, scope in definitions:
        rows = sorted([
            {**metadata[key][group], 'count': len(people), 'person_ids': sorted(people)}
            for group, people in buckets[key].items()
        ], key=lambda r: (-r['count'], r['label']))
        denominator = len(set().union(*buckets[key].values())) if buckets[key] else 0
        charts.append({'key': key, 'title': title, 'scope': scope,
                       'denominator': denominator, 'rows': rows})
    return {
        'data_version': stats['data_version'], 'generated_at': stats['generated_at'],
        'person_entities': len(profiles),
        'research_attempted_people': stats['research_attempted_people'],
        'research_attempt_percent': stats['research_attempt_percent'],
        'confidence_rule': 'Confirmed/high claims and confirmed/high-confidence identities; '
            'conflicts and uncertain temporal relationships excluded.',
        'counting_rule': 'Unique person entities within each group, never source rows. '
            'A person can belong to several groups; group counts must not be summed.',
        'featured_profiles': featured[:3],
        'archival_priorities': dict(sorted(Counter(
            p.get('archival_file', {}).get('review_priority', 'unassessed')
            for p in profiles).items())),
        'public_claim_confidence': dict(sorted(Counter(
            c['claim_confidence'] for p in profiles for c in p.get('claims', [])
        ).items())),
        'charts': charts,
    }
