from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1032_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1032.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1032_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1032-v1",
        "reviewer": "Before OSS Batch 1032 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1032_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 12
    assert len(payload["sources"]) == 8
    assert len(payload["organizations"]) == 1
    assert len(payload["affiliations"]) == 9
    assert len(payload["claims"]) == 13
    assert len(payload["person_updates"]) == 12
    assert len(payload["research_attempts"]) == 12
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1032_every_public_affiliation_has_a_claim() -> None:
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


def test_batch1032_cecilia_zung_categories_remain_distinct() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    law = affiliations["cecilia-zung-shanghai-law-practice-b1032"]
    nyu = affiliations["cecilia-zung-nyu-student-b1032"]
    postal = affiliations["cecilia-zung-postal-censor-translator-b1032"]
    assert law["relationship_type"] == "self_employment"
    assert law["pre_oss_temporal_basis"] == "documented_prewar"
    assert law["immediate_pre_oss"] is False
    assert law["last_civilian_pre_service"] is False
    assert nyu["relationship_type"] == "student"
    assert nyu["organization_name_as_found"] == "New York University Law School"
    assert nyu["last_civilian_pre_service"] is False
    assert postal["relationship_type"] == "government_assignment"
    assert postal["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
    assert postal["immediate_pre_oss"] is False


def test_batch1032_keeps_zuckerman_rows_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    first = updates[module.PEOPLE[2][0]]
    second = updates[module.PEOPLE[3][0]]
    assert module.PEOPLE[2][1] == module.PEOPLE[3][1] == "John V Zuckerman"
    assert first["identity_status"] == "confirmed"
    assert first["research_status"] == "occupation_only_found"
    assert second["identity_status"] == "ambiguous"
    assert second["research_status"] == "needs_identity_review"
    assert first["possible_duplicate_group"] == second["possible_duplicate_group"]
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    assert module.PEOPLE[2][0] in affiliation_people
    assert module.PEOPLE[3][0] not in affiliation_people


def test_batch1032_classifies_zurlo_without_inventing_a_pre_oss_role() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    zurlo = updates[module.PEOPLE[8][0]]
    assert zurlo["identity_status"] == "high_confidence"
    assert zurlo["personnel_category"] == "commissioned_army_officer"
    assert zurlo["commissioned_officer"] is True
    assert zurlo["research_status"] == "requires_archival_review"
    assert module.PEOPLE[8][0] not in {item["person_id"] for item in module.affiliations()}


def test_batch1032_withholds_undefined_code_999() -> None:
    module = load_generator()
    assert 7 not in module.ARMY_OCCUPATIONS
    assert module.PEOPLE[7][0] not in {item["person_id"] for item in module.affiliations()}
    update = next(item for item in module.person_updates() if item["person_id"] == module.PEOPLE[7][0])
    assert update["identity_status"] == "confirmed"
    assert update["research_status"] == "requires_archival_review"


def test_batch1032_preserves_reviewed_name_variants() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert "John M Zucker" in updates[module.PEOPLE[4][0]]["name_variants"]
    assert "Cecilia Sieu-ling Zung" in updates[module.PEOPLE[5][0]]["name_variants"]
    assert "François J Zwakhals" in updates[module.PEOPLE[10][0]]["name_variants"]


def test_batch1032_army_review_decisions_are_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 7
    assert all(row["decision"] == "accepted" for row in rows)
    assert all(row["decision_version"] == "batch-1032-v1" for row in rows)


def test_batch1032_attempts_cover_every_person() -> None:
    module = load_generator()
    attempts = module.research_attempts()
    assert {item["person_id"] for item in attempts} == {
        person_id for person_id, _name, _box in module.PEOPLE.values()
    }
    assert all(item["outcome"] not in {"planned", "error", "blocked"} for item in attempts)
    assert all("employer and occupation 1940" in item["query_text"] for item in attempts)


def test_batch1032_bundle_has_no_private_identifier_or_raw_record() -> None:
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
