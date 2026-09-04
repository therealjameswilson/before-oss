import copy
import sqlite3
import unittest

from oss_research.analytics import VERIFIED_SQL, build_analytics, eligible_affiliation


class AnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.item = {
            'affiliation_id': 'a1', 'organization_id': 'o1',
            'canonical_organization': 'Example University',
            'relationship_type': 'employment', 'sector': 'academia_and_research',
            'identity_confidence': 'high_confidence', 'claim_confidence': 'high',
            'publication_status': 'published', 'temporal_basis': 'explicit_immediate',
            'immediate_pre_oss': True, 'last_civilian_pre_service': True,
            'country': 'United States', 'state_or_region': 'Massachusetts',
        }
        self.profile = {
            'person_id': 'p1', 'display_name': 'Example Person',
            'identity_status': 'confirmed', 'research_status': 'completed',
            'immediate_pre_oss_affiliations': [self.item],
            'last_civilian_pre_service': [self.item], 'other_pre_oss_affiliations': [],
        }
        self.org = {'organization_id': 'o1', 'sector': 'academia_and_research'}
        self.stats = {'data_version': 'test', 'generated_at': '2026-09-04',
                      'research_attempted_people': 1, 'research_attempt_percent': 100.0}

    def charts(self, profiles=None):
        result = build_analytics(profiles or [self.profile], [self.org], self.stats)
        return {c['key']: c for c in result['charts']}

    def test_deduplicates_person_and_keeps_auditable_pointers(self):
        chart = self.charts()['last_civilian']
        self.assertEqual(chart['denominator'], 1)
        self.assertEqual(chart['rows'][0]['count'], 1)
        self.assertEqual(chart['rows'][0]['person_ids'], ['p1'])
        self.assertEqual(chart['rows'][0]['organization_id'], 'o1')

    def test_excludes_uncertain_timing_but_preserves_source_object(self):
        self.item['temporal_basis'] = 'temporal_relation_uncertain'
        self.assertFalse(eligible_affiliation(self.profile, self.item))
        self.assertTrue(all(c['denominator'] == 0 for c in self.charts().values()))
        self.assertEqual(self.profile['immediate_pre_oss_affiliations'], [self.item])

    def test_requires_both_identity_assessments_and_no_conflict(self):
        for target, field, value in [
            ('profile', 'identity_status', 'probable'),
            ('profile', 'research_status', 'conflicting_sources'),
            ('item', 'identity_confidence', 'ambiguous'),
            ('item', 'claim_confidence', 'medium'),
            ('item', 'publication_status', 'conflicting'),
            ('item', 'temporal_basis', None),
        ]:
            with self.subTest(field=field, value=value):
                p, a = copy.deepcopy(self.profile), copy.deepcopy(self.item)
                (p if target == 'profile' else a)[field] = value
                self.assertFalse(eligible_affiliation(p, a))

    def test_student_is_not_an_employer(self):
        self.item['relationship_type'] = 'student'
        charts = self.charts()
        self.assertEqual(charts['last_civilian']['denominator'], 0)
        self.assertEqual(charts['sectors']['denominator'], 0)
        self.assertIn('student', charts['academic']['rows'][0]['label'])

    def test_probable_immediate_is_not_in_immediate_chart(self):
        self.item['temporal_basis'] = 'probable_immediate'
        self.assertTrue(eligible_affiliation(self.profile, self.item))
        self.assertEqual(self.charts()['immediate']['denominator'], 0)

    def test_same_person_can_appear_in_separate_academic_groups(self):
        student = {**self.item, 'affiliation_id': 'a2', 'relationship_type': 'student'}
        self.profile['other_pre_oss_affiliations'] = [student]
        chart = self.charts()['academic']
        self.assertEqual(chart['denominator'], 1)
        self.assertEqual(sum(r['count'] for r in chart['rows']), 2)

    def test_sql_and_python_eligibility_agree(self):
        db = sqlite3.connect(':memory:')
        db.executescript('''CREATE TABLE person_entities(person_id, identity_status, research_status);
            CREATE TABLE affiliations(person_id, identity_confidence, claim_confidence,
                publication_status, pre_oss_temporal_basis);''')
        for basis in ['explicit_immediate', 'strongly_date_bounded', 'probable_immediate',
                      'documented_prewar', 'temporal_relation_uncertain', None]:
            for identity in ['confirmed', 'high_confidence', 'probable', None]:
                with self.subTest(basis=basis, identity=identity):
                    db.execute('DELETE FROM affiliations'); db.execute('DELETE FROM person_entities')
                    db.execute('INSERT INTO person_entities VALUES (?,?,?)', ('p1', identity, 'completed'))
                    db.execute('INSERT INTO affiliations VALUES (?,?,?,?,?)',
                               ('p1', 'high_confidence', 'high', 'published', basis))
                    sql = db.execute(f'SELECT count(*) FROM affiliations a JOIN person_entities pe USING(person_id) WHERE {VERIFIED_SQL}').fetchone()[0]
                    python = eligible_affiliation({**self.profile, 'identity_status': identity},
                                                  {**self.item, 'temporal_basis': basis})
                    self.assertEqual(bool(sql), python)
        db.close()
