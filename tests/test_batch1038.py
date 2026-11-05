from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1038_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1038.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1038_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1038-v1",
        "reviewer": "Before OSS Batch 1038 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1038_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(module.REVIEW_ROWS) == 45
    assert len(payload["sources"]) == 9
    assert len(payload["organizations"]) == 1
    assert len(payload["affiliations"]) == 12
    assert len(payload["claims"]) == 18
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 25,
        "occupation_only_found": 10,
        "needs_identity_review": 5,
        "conflicting_sources": 3,
        "verified_employer_found": 1,
        "documented_prewar_employer_found": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1038_preserves_existing_howard_manning_profile() -> None:
    module = load_generator()
    howard = module.PEOPLE[11][0]
    assert howard not in {item["person_id"] for item in module.person_updates()}
    assert howard not in {item["person_id"] for item in module.research_attempts()}
    assert howard not in {item["person_id"] for item in module.affiliations()}
    assert howard not in {item["person_id"] for item in module.claims()}


def test_batch1038_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1038_army_decisions_are_explicit_and_duplicate_safe() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 19
    assert Counter(row["decision"] for row in rows) == {"accepted": 12, "rejected": 7}
    assert all(row["decision_version"] == "batch-1038-v1" for row in rows)
    michael_candidates = {
        "2d1dc802-e636-5253-9122-403d5613a3e8",
        "36ad4734-d14d-5108-aa5f-bc18f6f6bfaa",
    }
    assert {
        row["target_id"]
        for row in rows
        if row["target_id"] in michael_candidates and row["decision"] == "accepted"
    } == michael_candidates
    michael_id = module.PEOPLE[14][0]
    assert len([item for item in module.affiliations() if item["person_id"] == michael_id]) == 1
    assert len([item for item in module.claims() if item["person_id"] == michael_id]) == 1


def test_batch1038_conflicts_and_unsupported_code_transfer_no_affiliation() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claim_people = {item["person_id"] for item in module.claims()}
    for row in (15, 24, 31, 46):
        assert module.PEOPLE[row][0] not in affiliation_people
        assert module.PEOPLE[row][0] not in claim_people
    john_manula = module.PEOPLE[35][0]
    assert john_manula not in affiliation_people
    identity_claim = next(item for item in module.claims() if item["person_id"] == john_manula)
    assert identity_claim["claim_type"] == "identity"
    assert "047" in identity_claim["temporal_assessment"]


def test_batch1038_named_employment_keeps_temporal_distinctions() -> None:
    module = load_generator()
    affiliations = module.affiliations()
    jacques = next(item for item in affiliations if item["person_id"] == module.PEOPLE[22][0])
    max_manus = next(item for item in affiliations if item["person_id"] == module.PEOPLE[36][0])
    assert jacques["organization_name_as_found"] == "Service Vente de Renault à Paris"
    assert jacques["last_civilian_pre_service"] is True
    assert jacques["immediate_pre_oss"] is False
    assert jacques["pre_oss_temporal_basis"] == "strongly_date_bounded"
    assert max_manus["organization_name_as_found"] == "his father's flower business"
    assert "organization_key" not in max_manus
    assert max_manus["last_civilian_pre_service"] is True
    assert max_manus["immediate_pre_oss"] is False


def test_batch1038_edge_cases_remain_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    cyrus = updates[module.PEOPLE[8][0]]
    manthos = updates[module.PEOPLE[25][0]]
    emile = updates[module.PEOPLE[34][0]]
    jack = updates[module.PEOPLE[44][0]]
    assert cyrus["identity_status"] == "ambiguous"
    assert cyrus["possible_duplicate_group"]
    assert "rank-column" in cyrus["next_action"]
    assert manthos["research_status"] == "needs_identity_review"
    assert "no first name" in manthos["identity_evidence"].lower()
    assert emile["identity_status"] == "probable"
    assert emile["research_status"] == "needs_identity_review"
    assert jack["identity_status"] == "ambiguous"
    assert "Mapes/March" in jack["next_action"]


def test_batch1038_bundle_has_no_private_identifier_or_raw_record() -> None:
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
