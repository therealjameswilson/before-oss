from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1035_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1035.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1035_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1035-v1",
        "reviewer": "Before OSS Batch 1035 evidence review",
        "sources": module.sources(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1035_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(module.ACTIVE_ROWS) == 45
    assert 20 not in module.ACTIVE_ROWS
    assert len(payload["sources"]) == 5
    assert len(payload["affiliations"]) == 15
    assert len(payload["claims"]) == 16
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "occupation_only_found": 15,
        "requires_archival_review": 30,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1035_preserves_completed_john_magruder_profile() -> None:
    module = load_generator()
    prior_person_id = module.PEOPLE[20][0]
    assert prior_person_id not in {item["person_id"] for item in module.person_updates()}
    assert prior_person_id not in {item["person_id"] for item in module.research_attempts()}


def test_batch1035_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1035_army_review_decisions_include_one_explicit_rejection() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 16
    assert Counter(row["decision"] for row in rows) == {"accepted": 15, "rejected": 1}
    assert all(row["decision_version"] == "batch-1035-v1" for row in rows)
    rejected = next(row for row in rows if row["decision"] == "rejected")
    assert rejected["target_id"] == "f74a5d90-4398-5071-905a-a8169a7a2766"


def test_batch1035_does_not_transfer_rejected_maffin_occupation() -> None:
    module = load_generator()
    maffin_id = module.PEOPLE[2][0]
    update = next(item for item in module.person_updates() if item["person_id"] == maffin_id)
    assert update["identity_status"] == "unresolved"
    assert update["research_status"] == "requires_archival_review"
    assert "rejected" in update["identity_evidence"]
    assert maffin_id not in {item["person_id"] for item in module.affiliations()}
    assert maffin_id not in {item["person_id"] for item in module.claims()}


def test_batch1035_maharg_identity_is_direct_but_employer_is_unresolved() -> None:
    module = load_generator()
    maharg_id = module.PEOPLE[26][0]
    update = next(item for item in module.person_updates() if item["person_id"] == maharg_id)
    assert update["identity_status"] == "high_confidence"
    assert update["research_status"] == "requires_archival_review"
    claims = [item for item in module.claims() if item["person_id"] == maharg_id]
    assert len(claims) == 1
    assert claims[0]["claim_type"] == "identity"
    assert "Detachment 101" in claims[0]["claim_text"]
    assert maharg_id not in {item["person_id"] for item in module.affiliations()}


def test_batch1035_preserves_alias_and_conflict_variants_without_merging() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    magill = updates[module.PEOPLE[9][0]]
    mains = updates[module.PEOPLE[42][0]]
    assert magill["name_variants"] == ["Orrin F Magill Jr."]
    assert "reconcile" in magill["next_action"]
    assert mains["name_variants"] == ["Shirley K Ray"]
    assert "Aka Ray" in mains["next_action"]


def test_batch1035_bundle_has_no_private_identifier_or_raw_record() -> None:
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
