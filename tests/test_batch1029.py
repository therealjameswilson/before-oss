from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1029_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1029.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1029_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1029-v1",
        "reviewer": "Before OSS Batch 1029 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1029_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 17
    assert len(payload["organizations"]) == 7
    assert len(payload["affiliations"]) == 26
    assert len(payload["claims"]) == 42
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])


def test_batch1029_every_public_affiliation_has_a_claim() -> None:
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
    assert public_affiliations <= claimed


def test_batch1029_separates_students_work_and_military_assignments() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert affiliations["sylvia-zagoria-brooklyn-college-b1029"]["relationship_type"] == "student"
    assert affiliations["sylvia-zagoria-brooklyn-college-b1029"]["last_civilian_pre_service"] is False
    assert affiliations["sylvia-zagoria-dance-instructor-b1029"]["relationship_type"] == "employment"
    assert affiliations["wilhelm-zagorski-railway-worker-b1029"]["last_civilian_pre_service"] is True
    assert affiliations["wilhelm-zagorski-german-army-b1029"]["relationship_type"] == "military_assignment"
    assert affiliations["edward-zarembo-usma-b1029"]["relationship_type"] == "student"
    assert affiliations["edward-zarembo-quartermaster-b1029"]["relationship_type"] == "military_assignment"
    assert affiliations["daniel-zaret-lincoln-brigade-b1029"]["relationship_type"] == "volunteer"


def test_batch1029_keeps_shared_postwar_undefined_and_conflicting_records_out_of_occupation_claims() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claim_keys = {item["key"] for item in module.claims()}
    assert module.PEOPLE[3][0] not in affiliation_people
    assert "conflict-frank-zabatta-b1029" in claim_keys
    assert "occupation-david-d-zagier-b1029" not in claim_keys
    assert module.PEOPLE[26][0] not in affiliation_people
    assert module.PEOPLE[33][0] not in affiliation_people
    assert module.PEOPLE[43][0] not in affiliation_people
    assert "conflict-asa-zatz-b1029" in claim_keys


def test_batch1029_preserves_duplicate_rows_and_name_variants() -> None:
    module = load_generator()
    assert module.PEOPLE[19][1] == module.PEOPLE[20][1] == "David L Zakon"
    assert module.PEOPLE[19][0] != module.PEOPLE[20][0]
    updates = {item["person_id"]: item for item in module.person_updates()}
    frank = updates[module.PEOPLE[3][0]]
    assert frank["identity_status"] == "conflicting"
    assert frank["possible_duplicate_group"] == "batch1029-frank-zabatta-zobatta-duplicate"
    assert "Dante T Zaccagnini" in updates[module.PEOPLE[5][0]]["name_variants"]
    assert "Henry G Zander III" in updates[module.PEOPLE[28][0]]["name_variants"]
    assert "Emanuel Nick Zaphiris" in updates[module.PEOPLE[31][0]]["name_variants"]
    assert "Wilhelm Zagórski" in updates[module.PEOPLE[12][0]]["name_variants"]


def test_batch1029_commissioned_status_is_evidence_bounded() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    commissioned = {
        person_id
        for person_id, item in updates.items()
        if item.get("commissioned_officer") is True
    }
    assert commissioned == {module.PEOPLE[35][0]}
    assert updates[module.PEOPLE[35][0]]["personnel_category"] == "commissioned_army_officer"
    assert updates[module.PEOPLE[38][0]].get("commissioned_officer") is None


def test_batch1029_army_review_decisions_are_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 22
    assert sum(row["decision"] == "accepted" for row in rows) == 18
    assert sum(row["decision"] == "rejected" for row in rows) == 2
    assert sum(row["decision"] == "conflicting" for row in rows) == 2
    assert all(row["decision_version"] == "batch-1029-v1" for row in rows)


def test_batch1029_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "raw_record",
        "serial-conflict:",
        "NARA_API_KEY",
        "x-api-key",
    )
    assert not any(value in payload for value in forbidden)
