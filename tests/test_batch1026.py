from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1026_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1026_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1026-v1",
        "reviewer": "Before OSS Batch 1026 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1026_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert len(payload["affiliations"]) == 25
    assert len(payload["claims"]) == 34
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])


def test_batch1026_preserves_yarmey_identifier_conflict() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    yarmey = updates[module.PEOPLE[39][0]]
    assert yarmey["identity_status"] == "conflicting"
    assert yarmey["research_status"] == "conflicting_sources"
    assert "Louis M Fossarelli" in yarmey["identity_evidence"]
    assert not any(item["person_id"] == module.PEOPLE[39][0] for item in module.affiliations())


def test_batch1026_keeps_student_and_military_pathways_out_of_employment() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    assert by_key["sumner-yaffe-harvard-student-b1026"]["relationship_type"] == "student"
    assert by_key["sumner-yaffe-harvard-student-b1026"]["last_civilian_pre_service"] is False
    assert by_key["adam-yarmolinsky-harvard-b1026"]["relationship_type"] == "student"
    assert by_key["adam-yarmolinsky-army-air-corps-b1026"]["relationship_type"] == "military_assignment"
    assert by_key["tomomasa-yamazaki-navy-school-b1026"]["relationship_type"] == "employment"


def test_batch1026_models_yanaga_sequence_and_original_spelling() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert by_key["chitoshi-yanaga-fbis-b1026"]["immediate_pre_oss"] is True
    assert by_key["chitoshi-yanaga-berkeley-b1026"]["last_civilian_pre_service"] is True
    assert by_key["chitoshi-yanaga-owi-b1026"]["relationship_type"] == "government_assignment"
    yanaga = updates[module.PEOPLE[29][0]]
    assert yanaga["identity_status"] == "high_confidence"
    assert "Chitoshi Yanaga" in yanaga["name_variants"]
    assert module.PEOPLE[29][1] == "Ohitoshi Yanaga"


def test_batch1026_keeps_temporal_qualification_visible() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    assert by_key["sannosuke-yamamoto-navy-league-b1026"]["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
    assert by_key["sannosuke-yamamoto-navy-league-b1026"]["publication_status"] == "publish_qualified"
    assert by_key["bernard-yarrow-nyc-da-b1026"]["pre_oss_temporal_basis"] == "explicit_immediate"
    assert by_key["bernard-yarrow-nyc-da-b1026"]["immediate_pre_oss"] is True


def test_batch1026_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "NARA_API_KEY",
        "x-api-key",
        "31039207",
        "15102393",
        "31457763",
    )
    assert not any(value in payload for value in forbidden)
