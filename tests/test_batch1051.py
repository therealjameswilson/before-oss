from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1051_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1051_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1051_is_complete_terminal_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 9
    assert len(payload["organizations"]) == 5
    assert len(payload["affiliations"]) == 10
    assert len(payload["claims"]) == 21
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 39,
        "occupation_only_found": 5,
        "conflicting_sources": 1,
        "verified_employer_found": 1,
    }
    assert all(
        item["research_status"]
        not in {
            "not_started",
            "in_progress",
            "candidate_found",
            "needs_identity_review",
            "needs_temporal_review",
        }
        for item in payload["person_updates"]
    )


def test_batch1051_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1051_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {1, 2, 33, 38, 45}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["relationship_type"] == (
            "student" if row == 33 else "unknown"
        )


def test_batch1051_postwar_and_indeterminate_army_rows_have_no_affiliation() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    for row in (23, 30, 31, 40):
        assert module.PEOPLE[row][0] not in affiliation_people
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert "10 July 1946" in updates[module.PEOPLE[23][0]]["next_action"]
    assert "28 June 1946" in updates[module.PEOPLE[40][0]]["next_action"]
    assert "code 999" in updates[module.PEOPLE[30][0]]["next_action"]
    assert "code 999" in updates[module.PEOPLE[31][0]]["next_action"]


def test_batch1051_occidental_is_explicit_immediate_and_last_civilian() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    occidental = affiliations["george-mcafee-mccune-occidental-b1051"]
    assert occidental["relationship_type"] == "employment"
    assert occidental["immediate_pre_oss"] is True
    assert occidental["last_civilian_pre_service"] is True
    assert occidental["pre_oss_temporal_basis"] == "explicit_immediate"
    assert occidental["claim_confidence"] == "confirmed"


def test_batch1051_military_and_student_roles_are_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    army = affiliations["thomas-f-mccoy-army-b1051"]
    harvard = affiliations["joseph-feder-mccrindle-harvard-b1051"]
    special_services = affiliations[
        "marshall-lockhart-mccune-army-special-services-b1051"
    ]
    assert army["relationship_type"] == "military_assignment"
    assert army["immediate_pre_oss"] is True
    assert army["last_civilian_pre_service"] is False
    assert harvard["relationship_type"] == "student"
    assert harvard["last_civilian_pre_service"] is False
    assert special_services["relationship_type"] == "military_assignment"
    assert special_services["immediate_pre_oss"] is False
    assert special_services["pre_oss_temporal_basis"] == "temporal_relation_uncertain"


def test_batch1051_duplicate_and_conflict_rows_stay_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for rows in ((7, 8), (24, 27), (33, 34)):
        assert len({module.PEOPLE[row][0] for row in rows}) == len(rows)
        assert len(
            {updates[module.PEOPLE[row][0]]["possible_duplicate_group"] for row in rows}
        ) == 1
    assert updates[module.PEOPLE[24][0]]["research_status"] == "requires_archival_review"
    assert updates[module.PEOPLE[27][0]]["research_status"] == "requires_archival_review"
    assert updates[module.PEOPLE[33][0]]["identity_status"] == "high_confidence"
    assert updates[module.PEOPLE[34][0]]["identity_status"] == "confirmed"
    assert updates[module.PEOPLE[22][0]]["research_status"] == "conflicting_sources"


def test_batch1051_attempt_numbers_continue_existing_history() -> None:
    module = load_generator()
    attempts = {
        item["person_id"]: item["attempt_number"]
        for item in module.research_attempts()
    }
    assert attempts[module.PEOPLE[1][0]] == 3
    assert attempts[module.PEOPLE[9][0]] == 3
    assert attempts[module.PEOPLE[23][0]] == 3
    assert attempts[module.PEOPLE[24][0]] == 1
    assert attempts[module.PEOPLE[45][0]] == 2
    assert set(attempts.values()) <= {1, 2, 3}


def test_batch1051_has_no_private_identifier_or_raw_api_content() -> None:
    module = load_generator()
    payload = json.dumps(module.build_bundle())
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


def test_batch1051_public_excerpts_are_short() -> None:
    module = load_generator()
    excerpts = [
        source["excerpt_override"]
        for claim in module.claims()
        for source in claim.get("sources", [])
        if source.get("excerpt_override")
    ]
    assert excerpts
    assert all(len(excerpt.split()) <= 25 for excerpt in excerpts)
