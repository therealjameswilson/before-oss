from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1023_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1023_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1023-v1",
        "reviewer": "Before OSS Batch 1023 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1023_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert len(payload["affiliations"]) == 12
    assert len(payload["claims"]) == 25
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])


def test_batch1023_preserves_employment_and_temporal_boundaries() -> None:
    module = load_generator()
    payload = bundle(module)
    by_key = {item["key"]: item for item in payload["affiliations"]}
    woolbert = by_key["woolbert-foreign-affairs-b1023"]
    iris = by_key["iris-woolcock-photographer-b1023"]
    assert woolbert["relationship_type"] == "professional_affiliation"
    assert woolbert["last_civilian_pre_service"] is False
    assert iris["relationship_type"] == "unknown"
    assert "organization_key" not in iris
    assert by_key["woolley-royal-navy-b1023"]["immediate_pre_oss"] is True
    assert by_key["woolverton-family-farms-b1023"]["last_civilian_pre_service"] is True
    assert by_key["woolverton-family-farms-b1023"]["relationship_type"] == "self_employment"
    assert by_key["woolverton-new-york-transfer-b1023"]["last_civilian_pre_service"] is False


def test_batch1023_keeps_woolington_rows_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    sam_a = updates[module.PEOPLE[37][0]]
    sam_s = updates[module.PEOPLE[38][0]]
    assert sam_a["possible_duplicate_group"] == sam_s["possible_duplicate_group"]
    assert sam_a["identity_status"] == "ambiguous"
    assert sam_s["identity_status"] == "confirmed"
    assert sam_a["person_id"] != sam_s["person_id"]


def test_batch1023_excludes_post_oss_and_undefined_army_fields() -> None:
    module = load_generator()
    affiliations = module.affiliations()
    assert not any(item["person_id"] == module.PEOPLE[25][0] for item in affiliations)
    assert not any(item["person_id"] == module.PEOPLE[40][0] for item in affiliations)
    claims = module.claims()
    robert = [item for item in claims if item["person_id"] == module.PEOPLE[25][0]]
    henry = [item for item in claims if item["person_id"] == module.PEOPLE[40][0]]
    assert {item["claim_type"] for item in robert} == {"identity"}
    assert {item["claim_type"] for item in henry} == {"identity"}


def test_batch1023_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = ("serial_number", "service_number", "candidate_identifier", "bulk_record_ordinal", "NARA_API_KEY", "x-api-key")
    assert not any(value in payload for value in forbidden)
