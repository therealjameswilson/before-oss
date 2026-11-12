from __future__ import annotations

import importlib.util
import json
import sqlite3
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1057_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1057_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1057_is_complete_for_page_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len({value[0] for value in module.PEOPLE.values()}) == 45
    assert module.PEOPLE[6][0] == module.PEOPLE[8][0]
    assert len(payload["sources"]) == 5
    assert len(payload["organizations"]) == 1
    assert len(payload["affiliations"]) == 9
    assert len(payload["claims"]) == 18
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 28,
        "occupation_only_found": 7,
        "conflicting_sources": 5,
        "needs_identity_review": 3,
        "verified_employer_found": 1,
        "completed": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1057_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1057_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {5, 18, 23, 25, 40, 43, 45, 46}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False
    assert affiliations[module.army_affiliation_key(5)]["relationship_type"] == "student"
    assert affiliations[module.army_affiliation_key(18)]["relationship_type"] == "student"
    assert affiliations[module.army_affiliation_key(40)]["relationship_type"] == "student"


def test_batch1057_post_oss_army_entry_is_identity_only() -> None:
    module = load_generator()
    james = module.PEOPLE[19][0]
    claims = [item for item in module.claims() if item["person_id"] == james]
    assert claims == []
    assert not any(item["person_id"] == james for item in module.affiliations())
    update = next(item for item in module.person_updates() if item["person_id"] == james)
    assert update["identity_status"] == "high_confidence"
    assert "1946" in update["identity_evidence"]


def test_batch1057_emmett_mcnamara_has_explicit_signal_corps_transition() -> None:
    module = load_generator()
    emmett = module.PEOPLE[45][0]
    affiliation = next(
        item for item in module.affiliations()
        if item["key"] == "emmett-mcnamara-signal-corps-b1057"
    )
    assert affiliation["person_id"] == emmett
    assert affiliation["relationship_type"] == "military_assignment"
    assert affiliation["immediate_pre_oss"] is True
    assert affiliation["last_civilian_pre_service"] is False
    assert affiliation["pre_oss_temporal_basis"] == "explicit_immediate"
    assert affiliation["claim_confidence"] == "high"
    claim = next(
        item for item in module.claims()
        if item.get("affiliation_key") == "emmett-mcnamara-signal-corps-b1057"
    )
    assert claim["claim_type"] == "immediate_pre_oss_affiliation"
    assert {link["source_key"] for link in claim["sources"]} == {module.NPS}
    update = next(item for item in module.person_updates() if item["person_id"] == emmett)
    assert update["identity_status"] == "high_confidence"
    assert update["research_status"] == "completed"


def test_batch1057_donal_mclaughlin_keeps_existing_employer_result() -> None:
    module = load_generator()
    donal = module.PEOPLE[2][0]
    update = next(item for item in module.person_updates() if item["person_id"] == donal)
    assert update["research_status"] == "verified_employer_found"
    assert update["identity_status"] == "high_confidence"
    assert not any(item["person_id"] == donal for item in module.affiliations())
    assert not any(item["person_id"] == donal for item in module.claims())


def test_batch1057_conflicts_and_duplicate_boundaries_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    john = updates[module.PEOPLE[6][0]]
    assert module.PEOPLE[6][0] == module.PEOPLE[8][0]
    assert john["identity_status"] == "high_confidence"
    assert john["possible_duplicate_group"]
    for row in module.IDENTIFIER_CONFLICT_ROWS:
        assert updates[module.PEOPLE[row][0]]["identity_status"] == "conflicting"
        assert updates[module.PEOPLE[row][0]]["research_status"] == "conflicting_sources"
    for row in module.MIDDLE_INITIAL_CONFLICT_ROWS:
        assert updates[module.PEOPLE[row][0]]["identity_status"] == "ambiguous"
        assert updates[module.PEOPLE[row][0]]["research_status"] == "needs_identity_review"
        assert not any(item["person_id"] == module.PEOPLE[row][0] for item in module.affiliations())


def test_batch1057_cyril_mcleod_warning_is_not_silently_normalized() -> None:
    module = load_generator()
    cyril = module.PEOPLE[14][0]
    update = next(item for item in module.person_updates() if item["person_id"] == cyril)
    assert update["identity_status"] == "unresolved"
    assert update["research_status"] == "requires_archival_review"
    assert "middle-initial column" in update["identity_evidence"]
    assert "no silent" in update["identity_evidence"]
    assert not any(item["person_id"] == cyril for item in module.affiliations())


def test_batch1057_attempts_continue_history_and_omit_private_values() -> None:
    module = load_generator()
    attempts = {item["person_id"]: item["attempt_number"] for item in module.research_attempts()}
    assert attempts[module.PEOPLE[1][0]] == 3
    assert attempts[module.PEOPLE[6][0]] == 4
    assert attempts[module.PEOPLE[24][0]] == 1
    assert attempts[module.PEOPLE[46][0]] == 1
    serialized = json.dumps(module.build_bundle())
    connection = sqlite3.connect(ROOT / "research" / "research.sqlite")
    forbidden_values = {
        str(row[0])
        for row in connection.execute(
            "SELECT serial_number_raw FROM source_records "
            "WHERE source_page = 312 AND serial_number_raw IS NOT NULL "
            "AND TRIM(serial_number_raw) <> ''"
        )
    }
    connection.close()
    assert forbidden_values
    for forbidden in forbidden_values:
        assert forbidden not in serialized
    assert "full service number" not in serialized.lower()
