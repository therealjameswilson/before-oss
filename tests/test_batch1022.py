from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1022_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1022_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1022-v1",
        "reviewer": "Before OSS Batch 1022 evidence review",
        "sources": module.sources(),
        "organizations": [],
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1022_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert len(payload["affiliations"]) == 9
    assert len(payload["claims"]) == 20
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])


def test_batch1022_preserves_identity_and_employment_boundaries() -> None:
    module = load_generator()
    payload = bundle(module)
    updates = {item["person_id"]: item for item in payload["person_updates"]}
    shen = updates[module.PEOPLE[13][0]]
    shew = updates[module.PEOPLE[14][0]]
    assert shen["identity_status"] == shew["identity_status"] == "conflicting"
    assert shen["possible_duplicate_group"] == shew["possible_duplicate_group"]
    assert not any(item["person_id"] in {module.PEOPLE[13][0], module.PEOPLE[14][0]} for item in payload["affiliations"])

    students = [item for item in payload["affiliations"] if item["relationship_type"] == "student"]
    assert {item["person_id"] for item in students} == {module.PEOPLE[8][0], module.PEOPLE[40][0]}
    assert all("organization_key" not in item for item in payload["affiliations"])
    assert all(item.get("immediate_pre_oss") is not True for item in payload["affiliations"])
    assert all(item.get("last_civilian_pre_service") is not True for item in payload["affiliations"])


def test_batch1022_rejects_unbridged_namesakes() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for row in (3, 21, 25, 28, 33, 34):
        assert updates[module.PEOPLE[row][0]]["identity_status"] == "unresolved"
        assert updates[module.PEOPLE[row][0]]["research_status"] == "requires_archival_review"
    assert "famous Garfield Wood Jr." in updates[module.PEOPLE[25][0]]["identity_evidence"]


def test_batch1022_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "NARA_API_KEY",
        "x-api-key",
    )
    assert not any(value in payload for value in forbidden)
