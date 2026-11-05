from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1036_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1036.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1036_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1036-v1",
        "reviewer": "Before OSS Batch 1036 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1036_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 8
    assert len(payload["organizations"]) == 2
    assert len(payload["affiliations"]) == 17
    assert len(payload["claims"]) == 22
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 23,
        "occupation_only_found": 15,
        "needs_identity_review": 7,
        "completed": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1036_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1036_army_review_decisions_are_bounded_and_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 18
    assert Counter(row["decision"] for row in rows) == {"accepted": 17, "rejected": 1}
    assert all(row["decision_version"] == "batch-1036-v1" for row in rows)
    rejected = next(row for row in rows if row["decision"] == "rejected")
    assert rejected["target_id"] == "1a076cdb-f90d-5a18-82f1-76581ad43406"
    assert "materially different" in rejected["rationale"]


def test_batch1036_does_not_transfer_rejected_majure_candidate() -> None:
    module = load_generator()
    majure_id = module.PEOPLE[5][0]
    update = next(item for item in module.person_updates() if item["person_id"] == majure_id)
    assert update["identity_status"] == "unresolved"
    assert update["research_status"] == "requires_archival_review"
    assert "rejected" in update["identity_evidence"]
    assert majure_id not in {item["person_id"] for item in module.affiliations()}
    assert majure_id not in {item["person_id"] for item in module.claims()}


def test_batch1036_identity_only_army_records_do_not_become_affiliations() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claims = module.claims()
    for row in (8, 12):
        person_id = module.PEOPLE[row][0]
        assert person_id not in affiliation_people
        identity_claims = [
            item for item in claims if item["person_id"] == person_id and item["claim_type"] == "identity"
        ]
        assert len(identity_claims) == 1
        assert "affiliation_key" not in identity_claims[0]
    payload = json.dumps(bundle(module))
    assert "code 999 is undefined" in payload
    assert "not used as pre-OSS evidence" in payload


def test_batch1036_malenbaum_separates_opa_from_harvard_student_status() -> None:
    module = load_generator()
    person_id = module.PEOPLE[20][0]
    update = next(item for item in module.person_updates() if item["person_id"] == person_id)
    assert update["identity_status"] == "high_confidence"
    assert update["research_status"] == "completed"
    affiliations = [item for item in module.affiliations() if item["person_id"] == person_id]
    assert len(affiliations) == 2
    opa = next(item for item in affiliations if item["organization_key"] == module.ORG_OPA)
    harvard = next(item for item in affiliations if item["organization_key"] == module.ORG_HARVARD)
    assert opa["relationship_type"] == "government_assignment"
    assert opa["immediate_pre_oss"] is True
    assert opa["last_civilian_pre_service"] is False
    assert opa["pre_oss_temporal_basis"] == "probable_immediate"
    assert harvard["relationship_type"] == "student"
    assert harvard["immediate_pre_oss"] is False
    assert harvard["last_civilian_pre_service"] is False


def test_batch1036_preserves_spelling_variants_without_merging() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    expected_groups = {
        (13, 14): "page291-john-malandre-malanore-b1036",
        (15, 26): "page291-victor-malaspina-malispino-b1036",
        (38, 39): "page291-patricia-malmsted-malmstedt-b1036",
    }
    for rows, group in expected_groups.items():
        assert {updates[module.PEOPLE[row][0]]["possible_duplicate_group"] for row in rows} == {group}
        assert len({module.PEOPLE[row][0] for row in rows}) == 2
    assert updates[module.PEOPLE[6][0]]["name_variants"] == ["Paul Makanowitsky"]
    assert updates[module.PEOPLE[8][0]]["name_variants"] == ["Toivo W Maki"]
    assert updates[module.PEOPLE[23][0]]["name_variants"] == ["John J Malia"]
    assert updates[module.PEOPLE[44][0]]["name_variants"] == ["Morrill E Malone"]


def test_batch1036_makris_is_confirmed_without_publishing_identifier() -> None:
    module = load_generator()
    person_id = module.PEOPLE[10][0]
    update = next(item for item in module.person_updates() if item["person_id"] == person_id)
    claim = next(item for item in module.claims() if item["person_id"] == person_id)
    assert update["identity_status"] == "confirmed"
    assert update["research_status"] == "requires_archival_review"
    assert claim["claim_type"] == "identity"
    assert claim["claim_confidence"] == "confirmed"
    assert person_id not in {item["person_id"] for item in module.affiliations()}


def test_batch1036_bundle_has_no_private_identifier_or_raw_record() -> None:
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
    assert "39120808" not in payload
