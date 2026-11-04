from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1024_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1024_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1024-v1",
        "reviewer": "Before OSS Batch 1024 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1024_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert len(payload["affiliations"]) == 15
    assert len(payload["claims"]) == 29
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])


def test_batch1024_separates_student_volunteer_and_occupation_evidence() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    emily = by_key["emily-workum-northern-westchester-b1024"]
    edwin = by_key["edwin-wright-columbia-student-b1024"]
    assert emily["relationship_type"] == "volunteer"
    assert emily["last_civilian_pre_service"] is False
    assert edwin["relationship_type"] == "student"
    assert edwin["immediate_pre_oss"] is True
    assert edwin["last_civilian_pre_service"] is False
    assert "organization_key" not in by_key["edwin-wright-iran-educator-b1024"]


def test_batch1024_preserves_initial_conflict_and_post_oss_boundary() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    wrachford = updates[module.PEOPLE[22][0]]
    kenneth = updates[module.PEOPLE[42][0]]
    assert wrachford["identity_status"] == "high_confidence"
    assert "George F Wrachford" in wrachford["name_variants"]
    assert kenneth["identity_status"] == "confirmed"
    assert kenneth["research_status"] == "requires_archival_review"
    assert not any(item["person_id"] == module.PEOPLE[42][0] for item in module.affiliations())


def test_batch1024_does_not_publish_hijacked_detachment_document() -> None:
    module = load_generator()
    payload = bundle(module)
    assert not any("javadc.org" in (item.get("stable_url") or "") for item in payload["sources"])
    claims = payload["claims"]
    assert not any(item["person_id"] == module.PEOPLE[2][0] for item in claims)
    assert not any(item["person_id"] == module.PEOPLE[24][0] for item in claims)


def test_batch1024_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = ("serial_number", "service_number", "candidate_identifier", "bulk_record_ordinal", "NARA_API_KEY", "x-api-key")
    assert not any(value in payload for value in forbidden)
