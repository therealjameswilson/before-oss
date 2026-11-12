from __future__ import annotations

import csv
import importlib.util
import json
import sqlite3
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1060_bundle.py"
REVIEW = ROOT / (
    "research/review-decisions-page315-joseph-meegan-name_"
    "batch-1060_2026-11-11.csv"
)


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1060_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1060_is_complete_for_page_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len({value[0] for value in module.PEOPLE.values()}) == 45
    assert module.PEOPLE[43][0] == module.PEOPLE[44][0]
    assert len(payload["sources"]) == 4
    assert payload["organizations"] == []
    assert len(payload["affiliations"]) == 13
    assert len(payload["claims"]) == 13
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 22,
        "occupation_only_found": 12,
        "conflicting_sources": 6,
        "verified_employer_found": 3,
        "documented_prewar_employer_found": 1,
        "needs_identity_review": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1060_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {
        3, 6, 15, 16, 20, 28, 30, 31, 34, 36, 37, 40, 46
    }
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["relationship_type"] == "unknown"
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False
    assert module.ARMY_OCCUPATIONS[37][1:4] == (
        "017",
        "electrical engineer",
        "Engineers, electrical",
    )
    assert module.ARMY_OCCUPATIONS[30][1:4] == (
        "748",
        "sailor or deckhand, except U.S. Navy",
        "Sailors and deckhands, except U.S. Navy",
    )


def test_batch1060_preserves_stronger_results_and_withholds_unsafe_codes() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    attempts = {
        item["person_id"]: item for item in module.research_attempts()
    }
    for row in module.VERIFIED_EMPLOYER_ROWS:
        update = updates[module.PEOPLE[row][0]]
        assert update["research_status"] == "verified_employer_found"
        assert "identity_status" not in update
        assert "identity_evidence" not in update
    leif = updates[module.PEOPLE[30][0]]
    assert leif["research_status"] == "documented_prewar_employer_found"
    assert 30 in module.ARMY_OCCUPATIONS
    # The accepted Army links for Henry and Richard Meigs carry an occupation
    # code absent from the reviewed official list. Keep it out of public fields.
    for row in {21, 22}:
        assert row not in module.ARMY_OCCUPATIONS
        update = updates[module.PEOPLE[row][0]]
        assert update["research_status"] == "requires_archival_review"
        assert "identity_status" not in update
        assert "occupation code" in update["next_action"]
        assert "992" not in update["next_action"]
        assert "code 992" in attempts[module.PEOPLE[row][0]]["research_notes"]


def test_batch1060_duplicate_and_conflict_boundaries_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    michael_id = module.PEOPLE[43][0]
    assert module.PEOPLE[44][0] == michael_id
    michael = updates[michael_id]
    assert michael["research_status"] == "conflicting_sources"
    assert michael["manual_review_required"] is True
    for row in module.CONFLICT_ROWS:
        update = updates[module.PEOPLE[row][0]]
        assert update["research_status"] == "conflicting_sources"
        assert not any(
            item["person_id"] == module.PEOPLE[row][0]
            for item in module.affiliations()
        )
    lincoln = updates[module.PEOPLE[19][0]]
    assert lincoln["research_status"] == "needs_identity_review"


def test_batch1060_name_correction_is_audited_and_raw_preserving() -> None:
    module = load_generator()
    assert module.PEOPLE[1][1] == "Joseph Meegan"
    with REVIEW.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert [row["target_type"] for row in rows] == ["source_record", "person_entity"]
    source_decision = json.loads(rows[0]["decision"].removeprefix("normalized_name:"))
    entity_decision = json.loads(rows[1]["decision"].removeprefix("display_name:"))
    assert source_decision == {
        "expected": "Jospeh Meegan",
        "last": "Meegan",
        "first": "Joseph",
        "middle": None,
    }
    assert entity_decision == {
        "expected": "Jospeh Meegan",
        "replacement": "Joseph Meegan",
    }
    assert all("immutable" in row["rationale"] for row in rows)


def test_batch1060_adds_only_occupation_claims() -> None:
    module = load_generator()
    assert {item["claim_type"] for item in module.claims()} == {"occupation"}
    public_affiliations = {item["key"] for item in module.affiliations()}
    claimed = {item["affiliation_key"] for item in module.claims()}
    assert public_affiliations == claimed


def test_batch1060_attempts_continue_history_and_omit_private_values() -> None:
    module = load_generator()
    attempts = module.research_attempts()
    assert {item["attempt_number"] for item in attempts} == {6}
    assert len({item["person_id"] for item in attempts}) == 45
    serialized = json.dumps(module.build_bundle())
    connection = sqlite3.connect(ROOT / "research" / "research.sqlite")
    forbidden_values = {
        str(row[0])
        for row in connection.execute(
            "SELECT serial_number_raw FROM source_records "
            "WHERE source_page = 315 AND serial_number_raw IS NOT NULL "
            "AND TRIM(serial_number_raw) <> ''"
        )
    }
    connection.close()
    assert forbidden_values
    for forbidden in forbidden_values:
        assert forbidden not in serialized
    assert "candidate_identifier" not in serialized
    assert "bulk_record_ordinal" not in serialized
