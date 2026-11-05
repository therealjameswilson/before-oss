from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1042_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-05_batch1042.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1042_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1042-v1",
        "reviewer": "Before OSS Batch 1042 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1042_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 9
    assert len(payload["organizations"]) == 2
    assert len(payload["affiliations"]) == 12
    assert len(payload["claims"]) == 17
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 31,
        "occupation_only_found": 10,
        "needs_identity_review": 3,
        "needs_temporal_review": 1,
        "verified_employer_found": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1042_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1042_army_decisions_are_explicit_and_conflict_safe() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 14
    assert Counter(row["decision"] for row in rows) == {"accepted": 11, "rejected": 3}
    assert all(row["decision_version"] == "batch-1042-v1" for row in rows)
    assert {row["target_id"] for row in rows if row["decision"] == "rejected"} == {
        "8136844d-de04-5e59-93ff-682a9a1dfe1e",
        "6ffb25b3-a279-59c5-8eba-c22650ff980f",
        "e30b3589-45a1-57ef-a4fd-93de3d19f806",
    }
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    assert module.PEOPLE[2][0] not in affiliation_people
    assert module.PEOPLE[12][0] not in affiliation_people
    assert module.PEOPLE[44][0] not in affiliation_people


def test_batch1042_army_affiliations_stay_broad_and_nonemployer() -> None:
    module = load_generator()
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert len(army_keys) == 10
    for key in army_keys:
        affiliation = affiliations[key]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False


def test_batch1042_preserves_relationship_and_temporal_distinctions() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    mazzini = affiliations["garibaldi-martellacci-mazzini-b1042"]
    wpb = affiliations["edwin-m-martin-wpb-b1042"]

    assert mazzini["relationship_type"] == "professional_affiliation"
    assert mazzini["immediate_pre_oss"] is False
    assert mazzini["last_civilian_pre_service"] is False
    assert mazzini["pre_oss_temporal_basis"] == "documented_prewar"
    assert wpb["relationship_type"] == "government_assignment"
    assert wpb["immediate_pre_oss"] is True
    assert wpb["last_civilian_pre_service"] is True
    assert wpb["pre_oss_temporal_basis"] == "explicit_immediate"


def test_batch1042_identity_and_temporal_limits_stay_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    paulette = updates[module.PEOPLE[5][0]]
    kaj = updates[module.PEOPLE[8][0]]
    charles_h = updates[module.PEOPLE[15][0]]
    edwin = updates[module.PEOPLE[23][0]]
    maurice = updates[module.PEOPLE[46][0]]

    assert paulette["identity_status"] == "high_confidence"
    assert paulette["research_status"] == "requires_archival_review"
    assert kaj["identity_status"] == "high_confidence"
    assert kaj["research_status"] == "requires_archival_review"
    assert "post-OSS Army-entry date" in charles_h["next_action"]
    assert charles_h["research_status"] == "needs_temporal_review"
    assert edwin["identity_status"] == "high_confidence"
    assert edwin["research_status"] == "verified_employer_found"
    assert maurice["research_status"] == "occupation_only_found"
    assert "Beggar" in maurice["next_action"]


def test_batch1042_existing_pilot_attempt_is_continued() -> None:
    module = load_generator()
    attempts = {item["person_id"]: item for item in module.research_attempts()}
    assert attempts[module.PEOPLE[42][0]]["attempt_number"] == 17
    assert all(
        item["attempt_number"] == 1
        for row, item in (
            (row, attempts[module.PEOPLE[row][0]]) for row in module.PEOPLE if row != 42
        )
    )


def test_batch1042_bundle_has_no_private_identifier_or_raw_record() -> None:
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
