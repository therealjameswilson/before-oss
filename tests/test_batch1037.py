from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1037_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1037.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1037_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1037-v1",
        "reviewer": "Before OSS Batch 1037 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1037_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 3
    assert len(payload["affiliations"]) == 19
    assert len(payload["claims"]) == 25
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 23,
        "occupation_only_found": 15,
        "needs_identity_review": 4,
        "verified_employer_found": 2,
        "needs_temporal_review": 1,
        "completed": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1037_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1037_army_review_decisions_are_bounded_and_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 21
    assert Counter(row["decision"] for row in rows) == {"accepted": 18, "rejected": 3}
    assert all(row["decision_version"] == "batch-1037-v1" for row in rows)
    rejected = {row["target_id"] for row in rows if row["decision"] == "rejected"}
    assert rejected == {
        "18d45091-2703-5f90-b57e-90a959b1726e",
        "218c5989-0871-5797-ad27-81a5dbaade3b",
        "598bbc55-741f-5fc4-b795-5a6a8ef8b264",
    }


def test_batch1037_unsafe_army_codes_and_conflicts_transfer_no_affiliation() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claims = module.claims()
    for row in (15, 23):
        person_id = module.PEOPLE[row][0]
        assert person_id not in affiliation_people
        identity_claim = next(item for item in claims if item["person_id"] == person_id)
        assert identity_claim["claim_type"] == "identity"
        assert "affiliation_key" not in identity_claim
    for row in (9, 10):
        person_id = module.PEOPLE[row][0]
        assert person_id not in affiliation_people
        assert person_id not in {item["person_id"] for item in claims}


def test_batch1037_named_affiliations_preserve_temporal_distinctions() -> None:
    module = load_generator()
    affiliations = module.affiliations()
    david = next(item for item in affiliations if item["person_id"] == module.PEOPLE[17][0])
    erika = next(item for item in affiliations if item["person_id"] == module.PEOPLE[45][0])
    golo = next(
        item
        for item in affiliations
        if item["person_id"] == module.PEOPLE[46][0] and item.get("organization_key")
    )
    assert david["relationship_type"] == "employment"
    assert david["immediate_pre_oss"] is True
    assert david["last_civilian_pre_service"] is True
    assert david["pre_oss_temporal_basis"] == "explicit_immediate"
    assert erika["relationship_type"] == "government_assignment"
    assert erika["immediate_pre_oss"] is False
    assert erika["last_civilian_pre_service"] is False
    assert erika["claim_confidence"] == "medium"
    assert golo["relationship_type"] == "employment"
    assert golo["immediate_pre_oss"] is True
    assert golo["last_civilian_pre_service"] is True
    assert golo["pre_oss_temporal_basis"] == "strongly_date_bounded"


def test_batch1037_identity_and_parser_edge_cases_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    marcus = updates[module.PEOPLE[9][0]]
    morton = updates[module.PEOPLE[10][0]]
    nicholas = updates[module.PEOPLE[13][0]]
    assert marcus["identity_status"] == "conflicting"
    assert marcus["possible_duplicate_group"]
    assert morton["identity_status"] == "conflicting"
    assert "rejected" in morton["identity_evidence"]
    assert "rank column" in nicholas["next_action"]


def test_batch1037_bundle_has_no_private_identifier_or_raw_record() -> None:
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

