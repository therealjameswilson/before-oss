from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1047_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1047_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1047-v1",
        "reviewer": "Before OSS Batch 1047 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1047_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 44
    assert len(payload["sources"]) == 12
    assert len(payload["organizations"]) == 3
    assert len(payload["affiliations"]) == 11
    assert len(payload["claims"]) == 17
    assert len(payload["person_updates"]) == 44
    assert len(payload["research_attempts"]) == 44
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 30,
        "occupation_only_found": 8,
        "needs_identity_review": 3,
        "documented_prewar_employer_found": 2,
        "completed": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1047_preserves_previously_terminal_frederick_mayer_entities() -> None:
    module = load_generator()
    protected = {
        "59f66a94-282a-5f09-b5d1-ea7cdeed4705",
        "ed9e4da5-f917-555a-9fda-052036f02574",
    }
    assert protected.isdisjoint(module.PEOPLE[row][0] for row in module.PEOPLE)
    assert protected.isdisjoint(item["person_id"] for item in module.person_updates())
    assert protected.isdisjoint(item["person_id"] for item in module.research_attempts())


def test_batch1047_every_public_affiliation_has_one_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {
        item["affiliation_key"]
        for item in module.claims()
        if item.get("affiliation_key")
    }
    assert public_affiliations == claimed


def test_batch1047_army_categories_stay_broad_and_nonemployer() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    assert len(army_keys) == 8
    for key in army_keys:
        affiliation = affiliations[key]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False


def test_batch1047_keeps_relationship_categories_separate() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}

    ferdinand = affiliations["ferdinand-l-mayer-state-department-b1047"]
    assert ferdinand["relationship_type"] == "government_assignment"
    assert ferdinand["pre_oss_temporal_basis"] == "documented_prewar"
    assert ferdinand["immediate_pre_oss"] is False
    assert ferdinand["last_civilian_pre_service"] is False

    bruce = affiliations["bruce-h-mazlish-columbia-student-b1047"]
    assert bruce["relationship_type"] == "student"
    assert bruce["last_civilian_pre_service"] is False

    richard = affiliations["richard-mazzarini-pan-american-b1047"]
    assert richard["relationship_type"] == "employment"
    assert richard["pre_oss_temporal_basis"] == "probable_immediate"
    assert richard["immediate_pre_oss"] is False
    assert richard["last_civilian_pre_service"] is True
    assert richard["claim_confidence"] == "medium"


def test_batch1047_candidates_do_not_inherit_affiliations() -> None:
    module = load_generator()
    affiliations = {item["person_id"] for item in module.affiliations()}
    updates = {item["person_id"]: item for item in module.person_updates()}

    for row in (14, 42, 45):
        person_id = module.PEOPLE[row][0]
        assert updates[person_id]["research_status"] == "needs_identity_review"
        assert person_id not in affiliations

    gerald_claim = next(
        item for item in module.claims() if item["key"] == "identity-gerald-mayer-owi-candidate-b1047"
    )
    assert gerald_claim["claim_confidence"] == "low"
    assert gerald_claim["publication_status"] == "withheld_low_confidence"


def test_batch1047_keeps_riccardo_and_richard_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    riccardo = updates[module.PEOPLE[45][0]]
    richard = updates[module.PEOPLE[46][0]]
    assert riccardo["person_id"] != richard["person_id"]
    assert riccardo["identity_status"] == "ambiguous"
    assert richard["identity_status"] == "high_confidence"
    assert riccardo["possible_duplicate_group"] == richard["possible_duplicate_group"]
    panam = next(item for item in module.affiliations() if item["key"] == "richard-mazzarini-pan-american-b1047")
    assert panam["person_id"] == richard["person_id"]


def test_batch1047_uses_stable_reviewed_sources() -> None:
    module = load_generator()
    sources = {item["key"]: item for item in module.sources()}
    assert "time-richard-mazzarini-b1047" not in sources
    assert sources[module.CORVO_MAZZARINI]["source_quality"] == "D_correlative_or_secondary"
    assert sources[module.BAILEY_MAZZARINI]["source_quality"] == "C_reputable_contemporary_or_scholarly"
    assert sources[module.MEDAL_MAZZARINI]["source_quality"] == "A_direct_official"


def test_batch1047_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "raw_record",
        "x-api-key",
        "NARA_API_KEY",
    )
    assert not any(value in payload for value in forbidden)


def test_batch1047_public_excerpts_are_short() -> None:
    module = load_generator()
    excerpts = [
        source["excerpt_override"]
        for claim in module.claims()
        for source in claim.get("sources", [])
        if source.get("excerpt_override")
    ]
    assert len(excerpts) == 5
    assert all(len(excerpt.split()) <= 25 for excerpt in excerpts)

