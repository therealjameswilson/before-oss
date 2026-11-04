from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1034_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1034.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1034_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1034-v1",
        "reviewer": "Before OSS Batch 1034 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1034_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(module.ACTIVE_ROWS) == 45
    assert 27 not in module.ACTIVE_ROWS
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 6
    assert len(payload["affiliations"]) == 16
    assert len(payload["claims"]) == 16
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1034_preserves_prior_macriyanni_outcome() -> None:
    module = load_generator()
    prior_person_id = module.PEOPLE[27][0]
    assert prior_person_id not in {item["person_id"] for item in module.person_updates()}
    assert prior_person_id not in {item["person_id"] for item in module.research_attempts()}


def test_batch1034_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations <= claimed


def test_batch1034_keeps_three_robert_macleod_rows_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    rows = [updates[module.PEOPLE[row][0]] for row in (2, 3, 4)]
    assert all(item["identity_status"] == "ambiguous" for item in rows)
    assert all(item["research_status"] == "needs_identity_review" for item in rows)
    assert len({item["possible_duplicate_group"] for item in rows}) == 1
    robert_ids = {module.PEOPLE[row][0] for row in (2, 3, 4)}
    assert not robert_ids & {item["person_id"] for item in module.affiliations()}


def test_batch1034_macomber_separates_student_and_military_pathway() -> None:
    module = load_generator()
    items = [item for item in module.affiliations() if item["person_id"] == module.PEOPLE[21][0]]
    assert {item["relationship_type"] for item in items} == {"student", "military_assignment"}
    immediate = next(item for item in items if item["immediate_pre_oss"])
    student = next(item for item in items if item["relationship_type"] == "student")
    assert immediate["organization_name_as_found"] == "Class III Marine Corps Reserve"
    assert immediate["pre_oss_temporal_basis"] == "explicit_immediate"
    assert immediate["last_civilian_pre_service"] is False
    assert student["organization_name_as_found"] == "Yale"
    assert student["last_civilian_pre_service"] is False


def test_batch1034_madison_separates_employer_military_and_student() -> None:
    module = load_generator()
    items = [item for item in module.affiliations() if item["person_id"] == module.PEOPLE[40][0]]
    by_relationship = {item["relationship_type"]: item for item in items}
    assert set(by_relationship) == {"employment", "military_assignment", "student"}
    assert by_relationship["employment"]["organization_name_as_found"] == "U.S. Department of Labor"
    assert by_relationship["employment"]["last_civilian_pre_service"] is True
    assert by_relationship["employment"]["immediate_pre_oss"] is False
    assert by_relationship["military_assignment"]["immediate_pre_oss"] is True
    assert by_relationship["student"]["last_civilian_pre_service"] is False


def test_batch1034_madson_does_not_overstate_immediacy() -> None:
    module = load_generator()
    item = next(item for item in module.affiliations() if item["person_id"] == module.PEOPLE[44][0])
    assert item["organization_name_as_found"] == "Motion Picture Service of the U. S. Dept. of Agriculture"
    assert item["last_civilian_pre_service"] is True
    assert item["immediate_pre_oss"] is False
    assert item["pre_oss_temporal_basis"] == "strongly_date_bounded"


def test_batch1034_army_review_decisions_are_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 10
    assert all(row["decision"] == "accepted" for row in rows)
    assert all(row["decision_version"] == "batch-1034-v1" for row in rows)


def test_batch1034_bundle_has_no_private_identifier_or_raw_record() -> None:
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
