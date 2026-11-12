from __future__ import annotations

import importlib.util
import json
import sqlite3
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1058_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1058_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1058_is_complete_for_page_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len({value[0] for value in module.PEOPLE.values()}) == 46
    assert len(payload["sources"]) == 4
    assert payload["organizations"] == []
    assert len(payload["affiliations"]) == 12
    assert len(payload["claims"]) == 12
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 27,
        "occupation_only_found": 12,
        "needs_identity_review": 6,
        "conflicting_sources": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1058_adds_no_duplicate_identity_claims() -> None:
    module = load_generator()
    assert {item["claim_type"] for item in module.claims()} == {"occupation"}
    public_affiliations = {item["key"] for item in module.affiliations()}
    claimed = {item["affiliation_key"] for item in module.claims()}
    assert public_affiliations == claimed


def test_batch1058_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {4, 10, 13, 15, 19, 20, 21, 22, 29, 34, 36, 46}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False
    for row in {10, 20}:
        assert affiliations[module.army_affiliation_key(row)]["relationship_type"] == "student"


def test_batch1058_duplicate_boundaries_and_conflict_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for left, right in module.DUPLICATE_BOUNDARY_PAIRS:
        assert module.PEOPLE[left][0] != module.PEOPLE[right][0]
        for row in {left, right}:
            update = updates[module.PEOPLE[row][0]]
            assert update["identity_status"] == "probable"
            assert update["research_status"] == "needs_identity_review"
            assert update["possible_duplicate_group"]
            assert not any(item["person_id"] == module.PEOPLE[row][0] for item in module.affiliations())
    coy = updates[module.PEOPLE[12][0]]
    assert coy["identity_status"] == "conflicting"
    assert coy["research_status"] == "conflicting_sources"
    assert not any(item["person_id"] == module.PEOPLE[12][0] for item in module.affiliations())


def test_batch1058_camden_candidate_is_not_promoted() -> None:
    module = load_generator()
    for row in {26, 30}:
        person_id = module.PEOPLE[row][0]
        update = next(item for item in module.person_updates() if item["person_id"] == person_id)
        assert "unpromoted" in update["identity_evidence"]
        assert not any(item["person_id"] == person_id for item in module.affiliations())
        assert not any(item["person_id"] == person_id for item in module.claims())


def test_batch1058_attempts_continue_history_and_omit_private_values() -> None:
    module = load_generator()
    attempts = {item["person_id"]: item["attempt_number"] for item in module.research_attempts()}
    assert attempts[module.PEOPLE[1][0]] == 3
    assert attempts[module.PEOPLE[2][0]] == 2
    assert attempts[module.PEOPLE[42][0]] == 5
    serialized = json.dumps(module.build_bundle())
    connection = sqlite3.connect(ROOT / "research" / "research.sqlite")
    forbidden_values = {
        str(row[0])
        for row in connection.execute(
            "SELECT serial_number_raw FROM source_records "
            "WHERE source_page = 313 AND serial_number_raw IS NOT NULL "
            "AND TRIM(serial_number_raw) <> ''"
        )
    }
    connection.close()
    assert forbidden_values
    for forbidden in forbidden_values:
        assert forbidden not in serialized
    assert "candidate_identifier" not in serialized
    assert "bulk_record_ordinal" not in serialized
