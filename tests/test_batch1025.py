from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1025_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1025_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1025-v1",
        "reviewer": "Before OSS Batch 1025 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1025_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert len(payload["affiliations"]) == 18
    assert len(payload["claims"]) == 35
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])
    assert not any(update["person_id"] == module.PEOPLE[19][0] for update in payload["person_updates"])


def test_batch1025_preserves_shared_identifier_conflict_and_separate_robert_g() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    robert_c = updates[module.PEOPLE[6][0]]
    robert_g_conflict = updates[module.PEOPLE[7][0]]
    robert_g_separate = updates[module.PEOPLE[8][0]]
    assert robert_c["identity_status"] == "conflicting"
    assert robert_g_conflict["identity_status"] == "conflicting"
    assert robert_c["possible_duplicate_group"] == "batch1025-robert-wright-identifier-conflict"
    assert robert_g_conflict["possible_duplicate_group"] == "batch1025-robert-wright-identifier-conflict"
    assert robert_g_separate["identity_status"] == "unresolved"
    assert "different protected identifier" in robert_g_separate["identity_evidence"]


def test_batch1025_distinguishes_employer_and_military_pathways() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    wuorinen = by_key["john-wuorinen-columbia-b1025"]
    betty = by_key["betty-wylie-general-mills-b1025"]
    wynberg_pfizer = by_key["hans-wynberg-pfizer-b1025"]
    wynberg_army = by_key["hans-wynberg-army-b1025"]
    wylly = by_key["richard-wylly-usmc-b1025"]
    assert wuorinen["relationship_type"] == "employment"
    assert wuorinen["immediate_pre_oss"] is True
    assert betty["pre_oss_temporal_basis"] == "explicit_immediate"
    assert betty["last_civilian_pre_service"] is True
    assert wynberg_pfizer["relationship_type"] == "employment"
    assert wynberg_pfizer["immediate_pre_oss"] is False
    assert wynberg_army["relationship_type"] == "military_assignment"
    assert wynberg_army["immediate_pre_oss"] is True
    assert wylly["relationship_type"] == "military_assignment"


def test_batch1025_keeps_army_codes_broad_and_999_uninterpreted() -> None:
    module = load_generator()
    affiliations = module.affiliations()
    claims = module.claims()
    for row in module.ARMY_OCCUPATIONS:
        key = f"{module.slug(module.PEOPLE[row][1])}-army-occupation-b1025"
        item = next(value for value in affiliations if value["key"] == key)
        assert "organization_key" not in item
        assert item["last_civilian_pre_service"] is False
    assert not any(item["person_id"] == module.PEOPLE[34][0] for item in affiliations)
    assert not any(
        item["person_id"] == module.PEOPLE[34][0] and item["claim_type"] == "occupation"
        for item in claims
    )
    francis = next(item for item in claims if item["key"] == "identity-francis-wyeth-b1025")
    assert "uninterpreted" in francis["match_notes"]


def test_batch1025_claim_confidence_and_classification_boundaries() -> None:
    module = load_generator()
    claims = {item["key"]: item for item in module.claims()}
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert claims["immediate-john-wuorinen-b1025"]["claim_confidence"] == "high"
    assert claims["immediate-betty-wylie-b1025"]["claim_confidence"] == "medium"
    assert claims["pfizer-hans-wynberg-b1025"]["claim_confidence"] == "high"
    assert updates[module.PEOPLE[18][0]]["allied_or_foreign_personnel"] is True
    assert "commissioned_officer" not in updates[module.PEOPLE[18][0]]
    assert updates[module.PEOPLE[37][0]]["personnel_category"] == "foreign_or_allied_military_personnel"
    assert updates[module.PEOPLE[42][0]]["personnel_category"] == "commissioned_marine_corps_officer"


def test_batch1025_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "NARA_API_KEY",
        "x-api-key",
        "1579324",
    )
    assert not any(value in payload for value in forbidden)
