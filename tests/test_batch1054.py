from __future__ import annotations

import importlib.util
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1054_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1054_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1054_is_complete_terminal_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len({value[0] for value in module.PEOPLE.values()}) == 46
    assert len(payload["sources"]) == 9
    assert len(payload["organizations"]) == 7
    assert len(payload["affiliations"]) == 19
    assert len(payload["claims"]) == 22
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 27,
        "occupation_only_found": 12,
        "needs_identity_review": 4,
        "verified_employer_found": 2,
        "conflicting_sources": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1054_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1054_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {1, 3, 4, 12, 16, 19, 20, 22, 24, 34, 45}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["relationship_type"] == (
            "student" if row in {1, 4, 16, 19, 20} else "unknown"
        )


def test_batch1054_post_oss_undefined_and_conflicting_army_rows_not_published() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    for row in (13, 30, 37):
        assert module.PEOPLE[row][0] not in affiliation_people
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert "1945-12-28" in updates[module.PEOPLE[30][0]]["next_action"]
    assert "code 590" in updates[module.PEOPLE[37][0]]["next_action"]
    assert updates[module.PEOPLE[13][0]]["identity_status"] == "conflicting"


def test_batch1054_exact_name_pairs_remain_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for rows in ((8, 9), (26, 27)):
        assert len({module.PEOPLE[row][0] for row in rows}) == 2
        groups = {
            updates[module.PEOPLE[row][0]]["possible_duplicate_group"]
            for row in rows
        }
        assert len(groups) == 1
        assert all(
            updates[module.PEOPLE[row][0]]["identity_status"] == "ambiguous"
            for row in rows
        )


def test_batch1054_owen_mcgivern_relationships_stay_distinct() -> None:
    module = load_generator()
    owen = module.PEOPLE[14][0]
    affiliations = {
        item["key"]: item for item in module.affiliations() if item["person_id"] == owen
    }
    assert len(affiliations) == 4
    navy = affiliations["owen-mcgivern-united-states-navy-b1054"]
    assembly = affiliations["owen-mcgivern-new-york-state-assembly-b1054"]
    assert navy["relationship_type"] == "military_assignment"
    assert navy["immediate_pre_oss"] is True
    assert assembly["relationship_type"] == "government_assignment"
    assert assembly["last_civilian_pre_service"] is True
    assert sum(item["relationship_type"] == "employment" for item in affiliations.values()) == 2


def test_batch1054_william_mcgovern_separates_last_and_earlier_employers() -> None:
    module = load_generator()
    william = module.PEOPLE[23][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == william]
    assert len(affiliations) == 3
    assert all(item["relationship_type"] == "employment" for item in affiliations)
    assert sum(item["last_civilian_pre_service"] for item in affiliations) == 1
    assert next(item for item in affiliations if item["last_civilian_pre_service"])[
        "organization_name_as_found"
    ] == "Harvard University"


def test_batch1054_donald_mcgranahan_is_qualified_student_not_employee() -> None:
    module = load_generator()
    donald = module.PEOPLE[33][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == donald]
    assert len(affiliations) == 1
    assert affiliations[0]["relationship_type"] == "student"
    assert affiliations[0]["identity_confidence"] == "probable"
    assert affiliations[0]["claim_confidence"] == "medium"
    assert affiliations[0]["publication_status"] == "publish_qualified"
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert updates[donald]["identity_status"] == "probable"
    assert "Donald Vincent McGranahan" in updates[donald]["name_variants"]


def test_batch1054_attempt_numbers_continue_existing_history() -> None:
    module = load_generator()
    attempts = {
        item["person_id"]: item["attempt_number"]
        for item in module.research_attempts()
    }
    assert attempts[module.PEOPLE[1][0]] == 3
    assert attempts[module.PEOPLE[9][0]] == 3
    assert attempts[module.PEOPLE[33][0]] == 2
    assert attempts[module.PEOPLE[46][0]] == 2
