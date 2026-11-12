from __future__ import annotations

import importlib.util
import json
import sqlite3
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1059_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1059_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1059_is_complete_for_page_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len({value[0] for value in module.PEOPLE.values()}) == 46
    assert len(payload["sources"]) == 4
    assert payload["organizations"] == []
    assert len(payload["affiliations"]) == 11
    assert len(payload["claims"]) == 11
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 23,
        "occupation_only_found": 10,
        "needs_identity_review": 7,
        "verified_employer_found": 3,
        "completed": 2,
        "conflicting_sources": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress", "candidate_found"}
        for item in payload["person_updates"]
    )


def test_batch1059_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {1, 2, 9, 12, 13, 25, 30, 33, 40, 41, 45}
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
    assert module.ARMY_OCCUPATIONS[2][1:4] == (
        "948",
        "sailor or deckhand, except U.S. Navy",
        "Sailors and deckhands, except U.S. Navy",
    )
    assert module.ARMY_OCCUPATIONS[9][1] == "768"
    assert "Packing, filling, labeling" in module.ARMY_OCCUPATIONS[9][3]


def test_batch1059_preserves_stronger_results_and_rejects_bad_army_links() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for row in {10, 11, 25}:
        update = updates[module.PEOPLE[row][0]]
        assert update["research_status"] == "verified_employer_found"
        assert "identity_status" not in update
        assert "identity_evidence" not in update
    for row in {37, 43}:
        update = updates[module.PEOPLE[row][0]]
        assert update["research_status"] == "completed"
        assert "identity_status" not in update
        assert "identity_evidence" not in update
    # Robert H. McWilliams's later 1945 Army entry is not used as a pre-OSS
    # occupation, while Edwin E. Meader's dated pre-service category is kept
    # separate from the stronger KVP employer claim.
    assert 11 not in module.ARMY_OCCUPATIONS
    assert 25 in module.ARMY_OCCUPATIONS
    assert not any(item["person_id"] == module.PEOPLE[11][0] for item in module.affiliations())


def test_batch1059_duplicate_and_conflict_boundaries_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for left, right in ((21, 22), (26, 27)):
        assert module.PEOPLE[left][0] != module.PEOPLE[right][0]
        for row in {left, right}:
            update = updates[module.PEOPLE[row][0]]
            assert update["research_status"] == "needs_identity_review"
            assert update["manual_review_required"] is True
            assert not any(item["person_id"] == module.PEOPLE[row][0] for item in module.affiliations())
    for row in {4, 42}:
        update = updates[module.PEOPLE[row][0]]
        assert update["research_status"] == "needs_identity_review"
        assert not any(item["person_id"] == module.PEOPLE[row][0] for item in module.affiliations())
    joseph = updates[module.PEOPLE[36][0]]
    assert joseph["research_status"] == "conflicting_sources"
    assert not any(item["person_id"] == module.PEOPLE[36][0] for item in module.affiliations())


def test_batch1059_adds_only_occupation_claims() -> None:
    module = load_generator()
    assert {item["claim_type"] for item in module.claims()} == {"occupation"}
    public_affiliations = {item["key"] for item in module.affiliations()}
    claimed = {item["affiliation_key"] for item in module.claims()}
    assert public_affiliations == claimed
    assert not any(item["person_id"] == module.PEOPLE[34][0] for item in module.claims())


def test_batch1059_attempts_continue_history_and_omit_private_values() -> None:
    module = load_generator()
    attempts = {item["person_id"]: item["attempt_number"] for item in module.research_attempts()}
    assert attempts[module.PEOPLE[1][0]] == 3
    assert attempts[module.PEOPLE[10][0]] == 14
    assert attempts[module.PEOPLE[11][0]] == 5
    assert attempts[module.PEOPLE[46][0]] == 3
    serialized = json.dumps(module.build_bundle())
    connection = sqlite3.connect(ROOT / "research" / "research.sqlite")
    forbidden_values = {
        str(row[0])
        for row in connection.execute(
            "SELECT serial_number_raw FROM source_records "
            "WHERE source_page = 314 AND serial_number_raw IS NOT NULL "
            "AND TRIM(serial_number_raw) <> ''"
        )
    }
    connection.close()
    assert forbidden_values
    for forbidden in forbidden_values:
        assert forbidden not in serialized
    assert "candidate_identifier" not in serialized
    assert "bulk_record_ordinal" not in serialized
