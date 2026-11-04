from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1033_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1033.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1033_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1033-v1",
        "reviewer": "Before OSS Batch 1033 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1033_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 13
    assert len(payload["organizations"]) == 4
    assert len(payload["affiliations"]) == 15
    assert len(payload["claims"]) == 16
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1033_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations <= claimed


def test_batch1033_macfarland_does_not_overstate_immediacy() -> None:
    module = load_generator()
    item = next(a for a in module.affiliations() if a["person_id"] == module.PEOPLE[5][0])
    assert item["organization_name_as_found"] == "Northern Trust Company"
    assert item["last_civilian_pre_service"] is True
    assert item["immediate_pre_oss"] is False
    assert item["pre_oss_temporal_basis"] == "strongly_date_bounded"


def test_batch1033_keeps_macgregor_rows_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    ranked = updates[module.PEOPLE[7][0]]
    unranked = updates[module.PEOPLE[8][0]]
    assert ranked["identity_status"] == "confirmed"
    assert ranked["commissioned_officer"] is True
    assert ranked["personnel_category"] == "enlisted_army_personnel"
    assert unranked["identity_status"] == "ambiguous"
    assert unranked["research_status"] == "needs_identity_review"
    assert ranked["possible_duplicate_group"] == unranked["possible_duplicate_group"]
    ranked_affiliations = [a for a in module.affiliations() if a["person_id"] == module.PEOPLE[7][0]]
    assert {a["relationship_type"] for a in ranked_affiliations} == {"student", "military_assignment"}
    assert any(a["immediate_pre_oss"] for a in ranked_affiliations)
    assert module.PEOPLE[8][0] not in {a["person_id"] for a in module.affiliations()}


def test_batch1033_gerstle_mack_is_occupation_only() -> None:
    module = load_generator()
    item = next(a for a in module.affiliations() if a["person_id"] == module.PEOPLE[22][0])
    assert item["occupation"] == "writer and biographer"
    assert item["relationship_type"] == "unknown"
    assert item.get("organization_key") is None
    assert item["immediate_pre_oss"] is False


def test_batch1033_mackinnon_has_explicit_bryn_mawr_predecessor() -> None:
    module = load_generator()
    item = next(a for a in module.affiliations() if a["person_id"] == module.PEOPLE[39][0])
    assert item["organization_name_as_found"] == "Bryn Mawr College"
    assert item["role_title"] == "professor of psychology"
    assert item["immediate_pre_oss"] is True
    assert item["last_civilian_pre_service"] is True
    assert item["pre_oss_temporal_basis"] == "explicit_immediate"


def test_batch1033_keeps_malcolm_mackenzie_rows_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    first = updates[module.PEOPLE[31][0]]
    second = updates[module.PEOPLE[32][0]]
    assert first["identity_status"] == second["identity_status"] == "ambiguous"
    assert first["possible_duplicate_group"] == second["possible_duplicate_group"]
    assert first["research_status"] == second["research_status"] == "needs_identity_review"


def test_batch1033_army_review_decisions_are_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 12
    assert sum(row["decision"] == "accepted" for row in rows) == 11
    assert sum(row["decision"] == "rejected" for row in rows) == 1
    assert all(row["decision_version"] == "batch-1033-v1" for row in rows)


def test_batch1033_bundle_has_no_private_identifier_or_raw_record() -> None:
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
