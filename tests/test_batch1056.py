from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1056_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1056_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1056_is_complete_for_page_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len({value[0] for value in module.PEOPLE.values()}) == 45
    assert module.PEOPLE[40][0] == module.PEOPLE[41][0]
    assert module.PEOPLE[40][0] != module.PEOPLE[42][0]
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 6
    assert len(payload["affiliations"]) == 14
    assert len(payload["claims"]) == 28
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 29,
        "occupation_only_found": 8,
        "needs_identity_review": 5,
        "verified_employer_found": 2,
        "conflicting_sources": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1056_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1056_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {2, 3, 16, 27, 32, 37, 40, 45}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
    assert affiliations[module.army_affiliation_key(27)]["relationship_type"] == "student"
    assert affiliations[module.army_affiliation_key(32)]["relationship_type"] == "student"


def test_batch1056_undefined_army_codes_are_not_published() -> None:
    module = load_generator()
    claims = module.claims()
    for row in module.IDENTITY_ONLY_ARMY:
        person_claims = [item for item in claims if item["person_id"] == module.PEOPLE[row][0]]
        assert len(person_claims) == 1
        assert person_claims[0]["claim_type"] == "identity"
        assert not any(item["person_id"] == module.PEOPLE[row][0] for item in module.affiliations())
        assert not any(item["claim_type"] == "occupation" for item in person_claims)


def test_batch1056_porter_mckeever_separates_owi_from_oss() -> None:
    module = load_generator()
    porter = module.PEOPLE[7][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == porter]
    assert len(affiliations) == 3
    newspapers = [item for item in affiliations if item["relationship_type"] == "employment"]
    assert len(newspapers) == 2
    assert all(item["last_civilian_pre_service"] is True for item in newspapers)
    owi = next(item for item in affiliations if item["relationship_type"] == "government_assignment")
    assert owi["organization_name_as_found"] == "Office of War Information Psychological Warfare Team"
    assert owi["immediate_pre_oss"] is False
    assert owi["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
    assert "distinct from OSS" in next(
        item for item in module.organizations() if item["key"] == "owi-b1056"
    )["normalization_notes"]


def test_batch1056_donald_mackinnon_has_explicit_bryn_mawr_transition() -> None:
    module = load_generator()
    donald = module.PEOPLE[35][0]
    affiliation = next(item for item in module.affiliations() if item["person_id"] == donald)
    assert affiliation["relationship_type"] == "employment"
    assert affiliation["organization_name_as_found"] == "Bryn Mawr College"
    assert affiliation["immediate_pre_oss"] is True
    assert affiliation["last_civilian_pre_service"] is True
    assert affiliation["pre_oss_temporal_basis"] == "explicit_immediate"
    update = next(item for item in module.person_updates() if item["person_id"] == donald)
    assert update["identity_status"] == "high_confidence"
    assert "Donald Wallace MacKinnon" in update["name_variants"]


def test_batch1056_marjorie_mckillop_remains_probable_and_qualified() -> None:
    module = load_generator()
    marjorie = module.PEOPLE[25][0]
    update = next(item for item in module.person_updates() if item["person_id"] == marjorie)
    assert update["identity_status"] == "probable"
    assert update["research_status"] == "needs_identity_review"
    affiliations = [item for item in module.affiliations() if item["person_id"] == marjorie]
    assert {item["relationship_type"] for item in affiliations} == {"student", "military_assignment"}
    assert all(item["claim_confidence"] == "medium" for item in affiliations)
    assert all(item["publication_status"] == "publish_qualified" for item in affiliations)
    assert all(item["immediate_pre_oss"] is False for item in affiliations)


def test_batch1056_duplicate_and_conflict_boundaries_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    stewarts = [updates[module.PEOPLE[row][0]] for row in (10, 11)]
    assert len({item["possible_duplicate_group"] for item in stewarts}) == 1
    assert all(item["identity_status"] == "ambiguous" for item in stewarts)
    assert updates[module.PEOPLE[12][0]]["identity_status"] == "conflicting"
    assert updates[module.PEOPLE[40][0]]["identity_status"] == "high_confidence"
    assert updates[module.PEOPLE[42][0]]["identity_status"] == "ambiguous"
    assert module.PEOPLE[40][0] != module.PEOPLE[42][0]


def test_batch1056_richard_mclallen_identity_does_not_invent_employer() -> None:
    module = load_generator()
    richard = module.PEOPLE[46][0]
    update = next(item for item in module.person_updates() if item["person_id"] == richard)
    assert update["identity_status"] == "high_confidence"
    assert update["research_status"] == "requires_archival_review"
    assert not any(item["person_id"] == richard for item in module.affiliations())
    richard_claims = [item for item in module.claims() if item["person_id"] == richard]
    assert len(richard_claims) == 1
    assert richard_claims[0]["claim_type"] == "identity"


def test_batch1056_attempts_continue_history_and_omit_private_values() -> None:
    module = load_generator()
    attempts = {item["person_id"]: item["attempt_number"] for item in module.research_attempts()}
    assert attempts[module.PEOPLE[2][0]] == 3
    assert attempts[module.PEOPLE[10][0]] == 3
    assert attempts[module.PEOPLE[24][0]] == 1
    assert attempts[module.PEOPLE[40][0]] == 1
    serialized = json.dumps(module.build_bundle())
    for forbidden in ("5975144", "7810340", "7863058", "7254704", "1656275"):
        assert forbidden not in serialized
    assert "full service number" not in serialized.lower()
