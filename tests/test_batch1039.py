from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1039_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1039.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1039_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1039-v1",
        "reviewer": "Before OSS Batch 1039 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1039_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(module.REVIEW_ROWS) == 44
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 4
    assert len(payload["affiliations"]) == 23
    assert len(payload["claims"]) == 23
    assert len(payload["person_updates"]) == 44
    assert len(payload["research_attempts"]) == 44
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "occupation_only_found": 18,
        "requires_archival_review": 15,
        "needs_identity_review": 4,
        "documented_prewar_employer_found": 3,
        "conflicting_sources": 2,
        "completed": 1,
        "verified_employer_found": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1039_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1039_army_decisions_are_explicit_and_duplicate_safe() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 21
    assert Counter(row["decision"] for row in rows) == {"accepted": 19, "rejected": 2}
    assert all(row["decision_version"] == "batch-1039-v1" for row in rows)
    edward_candidates = {
        "1c933742-a6b2-5eb9-96bc-d1b0b39edb83",
        "61a5e3db-2bf1-5eda-aa9c-bae1ae3f2120",
    }
    assert {
        row["target_id"]
        for row in rows
        if row["target_id"] in edward_candidates and row["decision"] == "accepted"
    } == edward_candidates
    edward_id = module.PEOPLE[20][0]
    assert len([item for item in module.affiliations() if item["person_id"] == edward_id]) == 1
    assert len([item for item in module.claims() if item["person_id"] == edward_id]) == 1


def test_batch1039_rejected_conflicts_transfer_no_affiliation() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claim_people = {item["person_id"] for item in module.claims()}
    for row in (33, 41):
        assert module.PEOPLE[row][0] not in affiliation_people
        assert module.PEOPLE[row][0] not in claim_people
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert updates[module.PEOPLE[33][0]]["research_status"] == "conflicting_sources"
    assert updates[module.PEOPLE[41][0]]["research_status"] == "conflicting_sources"


def test_batch1039_temporal_and_relationship_distinctions() -> None:
    module = load_generator()
    affiliations = {item["person_id"]: item for item in module.affiliations() if item["person_id"] in {
        module.PEOPLE[16][0], module.PEOPLE[35][0], module.PEOPLE[37][0], module.PEOPLE[42][0], module.PEOPLE[43][0]
    }}
    paul = affiliations[module.PEOPLE[16][0]]
    elwin = affiliations[module.PEOPLE[37][0]]
    daniel = affiliations[module.PEOPLE[42][0]]
    arnold = affiliations[module.PEOPLE[43][0]]
    greer = affiliations[module.PEOPLE[35][0]]
    assert paul["relationship_type"] == "military_assignment"
    assert paul["immediate_pre_oss"] is False
    assert elwin["relationship_type"] == "employment"
    assert elwin["last_civilian_pre_service"] is True
    assert daniel["relationship_type"] == "government_assignment"
    assert daniel["immediate_pre_oss"] is True
    assert daniel["last_civilian_pre_service"] is True
    assert arnold["relationship_type"] == "self_employment"
    assert arnold["pre_oss_temporal_basis"] == "documented_prewar"
    assert greer["claim_confidence"] == "medium"
    assert greer["publication_status"] == "publish_qualified"


def test_batch1039_ambiguous_index_cases_stay_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for row in (8, 10, 14, 24):
        assert updates[module.PEOPLE[row][0]]["research_status"] == "needs_identity_review"
        assert updates[module.PEOPLE[row][0]]["identity_status"] == "ambiguous"
    assert module.PEOPLE[14][0] != module.PEOPLE[24][0]
    assert updates[module.PEOPLE[14][0]]["possible_duplicate_group"] == "batch1039-robert-k-march-marck"
    assert updates[module.PEOPLE[24][0]]["possible_duplicate_group"] == "batch1039-robert-k-march-marck"


def test_batch1039_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "raw_record",
        "x-api-key",
    )
    assert not any(value in payload for value in forbidden)
