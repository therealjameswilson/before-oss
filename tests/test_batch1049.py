from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1049_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1049_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1049-v1",
        "reviewer": "Before OSS Batch 1049 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1049_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 5
    assert len(payload["organizations"]) == 2
    assert len(payload["affiliations"]) == 12
    assert len(payload["claims"]) == 13
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 24,
        "needs_identity_review": 10,
        "occupation_only_found": 10,
        "documented_prewar_employer_found": 1,
        "conflicting_sources": 1,
    }
    assert all(
        item["research_status"] not in {"not_started", "in_progress"}
        for item in payload["person_updates"]
    )


def test_batch1049_every_public_affiliation_has_one_claim() -> None:
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
    assert public_affiliations == claimed


def test_batch1049_army_categories_are_qualified_and_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    assert len(army_keys) == 10
    student_rows = {8, 13, 17, 23}
    for row in module.ARMY_ASSOCIATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False
        assert affiliation["relationship_type"] == (
            "student" if row in student_rows else "unknown"
        )


def test_batch1049_thomas_mccart_separates_army_path_and_rca() -> None:
    module = load_generator()
    affiliations = {
        item["key"]: item
        for item in module.affiliations()
        if item["person_id"] == module.PEOPLE[6][0]
    }
    assert set(affiliations) == {
        "thomas-mccart-fifth-army-b1049",
        "thomas-mccart-rca-b1049",
    }
    army = affiliations["thomas-mccart-fifth-army-b1049"]
    rca = affiliations["thomas-mccart-rca-b1049"]
    assert army["relationship_type"] == "military_assignment"
    assert army["immediate_pre_oss"] is True
    assert army["last_civilian_pre_service"] is False
    assert army["pre_oss_temporal_basis"] == "explicit_immediate"
    assert army["organization_name_as_found"] == "Vth Army Replacement Center"
    assert rca["relationship_type"] == "employment"
    assert rca["immediate_pre_oss"] is False
    assert rca["last_civilian_pre_service"] is False
    assert rca["pre_oss_temporal_basis"] == "documented_prewar"
    assert rca["organization_name_as_found"] == "RCA"
    update = next(
        item for item in module.person_updates() if item["person_id"] == module.PEOPLE[6][0]
    )
    assert update["identity_status"] == "confirmed"
    assert update["research_status"] == "documented_prewar_employer_found"


def test_batch1049_conflict_and_variants_remain_unmerged() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    rex = updates[module.PEOPLE[33][0]]
    assert rex["identity_status"] == "conflicting"
    assert rex["research_status"] == "conflicting_sources"
    assert all(item["person_id"] != module.PEOPLE[33][0] for item in module.affiliations())
    for left, right in ((3, 4), (35, 44)):
        first = updates[module.PEOPLE[left][0]]
        second = updates[module.PEOPLE[right][0]]
        assert first["person_id"] != second["person_id"]
        assert first["research_status"] == "needs_identity_review"
        assert second["research_status"] == "needs_identity_review"
        assert first["possible_duplicate_group"] == second["possible_duplicate_group"]


def test_batch1049_has_no_private_identifier_or_raw_api_content() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "raw_record",
        "x-api-key",
        "NARA_API_KEY",
    )
    assert not any(value in payload for value in forbidden)


def test_batch1049_public_excerpts_are_short() -> None:
    module = load_generator()
    excerpts = [
        source["excerpt_override"]
        for claim in module.claims()
        for source in claim.get("sources", [])
        if source.get("excerpt_override")
    ]
    assert excerpts
    assert all(len(excerpt.split()) <= 25 for excerpt in excerpts)
