from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1053_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1053_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1053_preserves_46_rows_and_updates_44_people() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert module.PEOPLE[19][0] == module.PEOPLE[20][0]
    assert module.PEOPLE[21][0] == module.PEOPLE[22][0]
    assert len({value[0] for value in module.PEOPLE.values()}) == 44
    assert len(payload["sources"]) == 8
    assert len(payload["organizations"]) == 4
    assert len(payload["affiliations"]) == 14
    assert len(payload["claims"]) == 15
    assert len(payload["person_updates"]) == 44
    assert len(payload["research_attempts"]) == 44
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 28,
        "occupation_only_found": 11,
        "needs_identity_review": 3,
        "conflicting_sources": 1,
        "documented_prewar_employer_found": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1053_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1053_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {16, 21, 25, 28, 37, 38, 40, 44, 45, 46}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["relationship_type"] == (
            "student" if row in {25, 37} else "unknown"
        )


def test_batch1053_undefined_codes_are_not_interpreted() -> None:
    module = load_generator()
    occupation_claim_people = {
        item["person_id"]
        for item in module.claims()
        if item["claim_type"] == "occupation"
    }
    lawrence = module.PEOPLE[24][0]
    dallas = module.PEOPLE[26][0]
    assert lawrence not in occupation_claim_people
    assert dallas not in occupation_claim_people
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert "code 993" in updates[lawrence]["next_action"]
    assert "code 999" in updates[dallas]["next_action"]


def test_batch1053_lawrence_is_student_and_fraternity_affiliate_not_employee() -> None:
    module = load_generator()
    lawrence = module.PEOPLE[24][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == lawrence]
    assert {item["relationship_type"] for item in affiliations} == {
        "student",
        "professional_affiliation",
    }
    assert all(item["immediate_pre_oss"] is False for item in affiliations)
    assert all(item["last_civilian_pre_service"] is False for item in affiliations)
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert "Lawrence B McFaddin" in updates[lawrence]["name_variants"]


def test_batch1053_darel_distinguishes_earlier_and_last_civilian_roles() -> None:
    module = load_generator()
    darel = module.PEOPLE[32][0]
    affiliations = {item["key"]: item for item in module.affiliations() if item["person_id"] == darel}
    gordon = affiliations["darel-d-mcferren-gordon-high-school-b1053"]
    medan = affiliations["darel-d-mcferren-methodist-mission-school-b1053"]
    assert gordon["relationship_type"] == "employment"
    assert gordon["pre_oss_temporal_basis"] == "documented_prewar"
    assert gordon["last_civilian_pre_service"] is False
    assert gordon["claim_confidence"] == "high"
    assert medan["relationship_type"] == "employment"
    assert medan["pre_oss_temporal_basis"] == "strongly_date_bounded"
    assert medan["last_civilian_pre_service"] is True
    assert medan["immediate_pre_oss"] is False
    assert medan["claim_confidence"] == "medium"
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert updates[darel]["research_status"] == "documented_prewar_employer_found"


def test_batch1053_cross_page_conflicts_stay_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert updates[module.PEOPLE[6][0]]["identity_status"] == "conflicting"
    for row in (33, 35, 36):
        update = updates[module.PEOPLE[row][0]]
        assert update["identity_status"] == "ambiguous"
        assert update["research_status"] == "needs_identity_review"
        assert update["possible_duplicate_group"]
    assert module.PEOPLE[35][0] != module.PEOPLE[36][0]


def test_batch1053_attempt_numbers_continue_existing_history() -> None:
    module = load_generator()
    attempts = {
        item["person_id"]: item["attempt_number"]
        for item in module.research_attempts()
    }
    assert attempts[module.PEOPLE[1][0]] == 2
    assert attempts[module.PEOPLE[6][0]] == 3
    assert attempts[module.PEOPLE[16][0]] == 4
    assert attempts[module.PEOPLE[40][0]] == 4
    assert attempts[module.PEOPLE[46][0]] == 4
    assert len(attempts) == 44


def test_batch1053_has_no_private_identifier_or_raw_api_content() -> None:
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


def test_batch1053_code_sources_cover_every_published_category() -> None:
    module = load_generator()
    code_source = next(item for item in module.sources() if item["key"] == module.CODES)
    assert "171, 173, 175, and 304" in code_source["locator"]
    claims = [item for item in module.claims() if item["claim_type"] == "occupation"]
    assert len(claims) == 10
    assert all(
        any(link["source_key"] == module.CODES for link in item["sources"])
        for item in claims
    )
