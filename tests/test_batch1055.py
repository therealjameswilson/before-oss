from __future__ import annotations

import importlib.util
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1055_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1055_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1055_is_complete_for_page_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len({value[0] for value in module.PEOPLE.values()}) == 46
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 2
    assert len(payload["affiliations"]) == 6
    assert len(payload["claims"]) == 11
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 35,
        "occupation_only_found": 5,
        "needs_identity_review": 3,
        "conflicting_sources": 2,
        "verified_employer_found": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1055_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1055_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {20, 26, 43}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
    assert affiliations[module.army_affiliation_key(43)]["relationship_type"] == "student"


def test_batch1055_henry_mcintosh_separates_army_from_student_status() -> None:
    module = load_generator()
    henry = module.PEOPLE[23][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == henry]
    assert len(affiliations) == 2
    army = next(item for item in affiliations if item["relationship_type"] == "military_assignment")
    davidson = next(item for item in affiliations if item["relationship_type"] == "student")
    assert army["immediate_pre_oss"] is True
    assert army["pre_oss_temporal_basis"] == "explicit_immediate"
    assert davidson["organization_name_as_found"] == "Davidson College"
    assert davidson["last_civilian_pre_service"] is False
    assert all(item["relationship_type"] != "employment" for item in affiliations)


def test_batch1055_calvin_mckee_army_path_is_qualified() -> None:
    module = load_generator()
    calvin = module.PEOPLE[42][0]
    affiliation = next(item for item in module.affiliations() if item["person_id"] == calvin)
    assert affiliation["relationship_type"] == "military_assignment"
    assert affiliation["immediate_pre_oss"] is True
    assert affiliation["pre_oss_temporal_basis"] == "probable_immediate"
    assert affiliation["claim_confidence"] == "medium"
    assert affiliation["publication_status"] == "publish_qualified"


def test_batch1055_peter_mckeand_remains_probable_identity_only() -> None:
    module = load_generator()
    peter = module.PEOPLE[41][0]
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert updates[peter]["identity_status"] == "probable"
    assert updates[peter]["research_status"] == "needs_identity_review"
    assert "Peter Andrew Hannay McKeand" in updates[peter]["name_variants"]
    assert not any(item["person_id"] == peter for item in module.affiliations())
    peter_claims = [item for item in module.claims() if item["person_id"] == peter]
    assert len(peter_claims) == 1
    assert peter_claims[0]["claim_type"] == "identity"
    assert peter_claims[0]["claim_confidence"] == "medium"


def test_batch1055_duplicate_conflicts_and_post_oss_guard_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    carolyns = [updates[module.PEOPLE[row][0]] for row in (21, 22)]
    assert len({item["possible_duplicate_group"] for item in carolyns}) == 1
    assert all(item["identity_status"] == "ambiguous" for item in carolyns)
    assert all(updates[module.PEOPLE[row][0]]["identity_status"] == "conflicting" for row in (7, 13))
    william = updates[module.PEOPLE[8][0]]
    assert william["identity_status"] == "high_confidence"
    assert "1946-07-25" in william["next_action"]
    assert not any(item["person_id"] == module.PEOPLE[8][0] for item in module.affiliations())


def test_batch1055_attempt_numbers_continue_existing_history() -> None:
    module = load_generator()
    attempts = {
        item["person_id"]: item["attempt_number"]
        for item in module.research_attempts()
    }
    assert attempts[module.PEOPLE[1][0]] == 3
    assert attempts[module.PEOPLE[7][0]] == 4
    assert attempts[module.PEOPLE[23][0]] == 3
    assert attempts[module.PEOPLE[33][0]] == 2
    assert attempts[module.PEOPLE[46][0]] == 1
