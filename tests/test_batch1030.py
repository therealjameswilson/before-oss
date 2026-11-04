from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1030_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1030.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1030_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1030-v1",
        "reviewer": "Before OSS Batch 1030 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1030_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 11
    assert len(payload["organizations"]) == 2
    assert len(payload["affiliations"]) == 22
    assert len(payload["claims"]) == 28
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert all(update["research_status"] not in {"not_started", "in_progress"} for update in payload["person_updates"])


def test_batch1030_every_public_affiliation_has_a_claim() -> None:
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


def test_batch1030_separates_students_civilian_work_and_military_assignments() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    zieber = affiliations["allen-g-zieber-army-occupation-b1030"]
    assert zieber["relationship_type"] == "student"
    assert zieber["last_civilian_pre_service"] is False
    film = affiliations["joseph-zigman-film-editor-b1030"]
    navy = affiliations["joseph-zigman-us-navy-b1030"]
    assert film["relationship_type"] == "employment"
    assert film["last_civilian_pre_service"] is True
    assert film["immediate_pre_oss"] is False
    assert navy["relationship_type"] == "military_assignment"
    assert navy["immediate_pre_oss"] is True
    assert navy["last_civilian_pre_service"] is False


def test_batch1030_withholds_undefined_rejected_conflicting_and_late_codes() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    for row in {9, 12, 22, 23, 31, 46}:
        assert module.PEOPLE[row][0] not in affiliation_people
    claim_keys = {item["key"] for item in module.claims()}
    assert "conflict-peter-zerdilla-b1030" in claim_keys
    assert "occupation-paul-f-ziegner-b1030" not in claim_keys


def test_batch1030_preserves_index_spellings_and_search_variants() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert module.PEOPLE[5][1] == "Josepoh L Zeek"
    assert "Joseph L Zeek" in updates[module.PEOPLE[5][0]]["name_variants"]
    assert "Allen G Zieber Jr." in updates[module.PEOPLE[27][0]]["name_variants"]
    assert "Paul F Ziegner Jr." in updates[module.PEOPLE[31][0]]["name_variants"]
    assert "Richard A Zilz" in updates[module.PEOPLE[40][0]]["name_variants"]


def test_batch1030_commissioned_status_is_evidence_bounded() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    commissioned = {
        person_id
        for person_id, item in updates.items()
        if item.get("commissioned_officer") is True
    }
    assert commissioned == {module.PEOPLE[7][0], module.PEOPLE[20][0]}
    assert all(updates[person_id]["personnel_category"] == "commissioned_army_officer" for person_id in commissioned)
    assert updates[module.PEOPLE[25][0]].get("commissioned_officer") is None


def test_batch1030_army_review_decisions_are_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 26
    assert sum(row["decision"] == "accepted" for row in rows) == 23
    assert sum(row["decision"] == "rejected" for row in rows) == 1
    assert sum(row["decision"] == "conflicting" for row in rows) == 2
    assert all(row["decision_version"] == "batch-1030-v1" for row in rows)


def test_batch1030_bundle_has_no_private_identifier_or_raw_record() -> None:
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
