from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1040_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-05_batch1040.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1040_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1040-v1",
        "reviewer": "Before OSS Batch 1040 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1040_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 11
    assert len(payload["organizations"]) == 4
    assert len(payload["affiliations"]) == 21
    assert len(payload["claims"]) == 26
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 23,
        "occupation_only_found": 17,
        "conflicting_sources": 2,
        "verified_employer_found": 2,
        "completed": 1,
        "needs_identity_review": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1040_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1040_army_decisions_are_explicit_and_conflict_safe() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 24
    assert Counter(row["decision"] for row in rows) == {"accepted": 20, "rejected": 4}
    assert all(row["decision_version"] == "batch-1040-v1" for row in rows)
    rejected_ids = {
        "48f7dcaf-b86e-550f-a28a-ea88b17b1248",
        "586715e3-c975-5a26-b288-19a94b3f3b5c",
        "3a9d30fb-3bfb-5b46-b5a8-3627f94a437a",
        "d600ab08-900e-5f8e-9a89-ee1ace733878",
    }
    assert {row["target_id"] for row in rows if row["decision"] == "rejected"} == rejected_ids
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    for row in (15, 22):
        assert module.PEOPLE[row][0] not in affiliation_people


def test_batch1040_undefined_and_late_army_rows_do_not_become_affiliations() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    for row in (9, 12, 34):
        assert module.PEOPLE[row][0] not in affiliation_people
    identity_claim_people = {
        item["person_id"] for item in module.claims() if item["claim_type"] == "identity"
    }
    for row in (9, 12, 34):
        assert module.PEOPLE[row][0] in identity_claim_people


def test_batch1040_named_roles_preserve_relationship_and_temporal_distinctions() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    maritz = affiliations["raymond-e-maritz-firm-b1040"]
    markoutsas = affiliations["george-c-markoutsas-army-b1040"]
    marlin_fsa = affiliations["ervin-r-marlin-fsa-b1040"]
    marlin_trinity = affiliations["ervin-r-marlin-trinity-b1040"]
    assert maritz["relationship_type"] == "employment"
    assert maritz["immediate_pre_oss"] is True
    assert maritz["last_civilian_pre_service"] is True
    assert maritz["pre_oss_temporal_basis"] == "explicit_immediate"
    assert markoutsas["relationship_type"] == "military_assignment"
    assert markoutsas["immediate_pre_oss"] is True
    assert markoutsas["last_civilian_pre_service"] is False
    assert marlin_fsa["relationship_type"] == "government_assignment"
    assert marlin_fsa["last_civilian_pre_service"] is True
    assert marlin_fsa["immediate_pre_oss"] is False
    assert marlin_trinity["relationship_type"] == "student"
    assert marlin_trinity["last_civilian_pre_service"] is False


def test_batch1040_clipped_and_conflicting_names_stay_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    marmande = updates[module.PEOPLE[45][0]]
    marnocaa = updates[module.PEOPLE[46][0]]
    assert module.PEOPLE[45][1] == "Raymond-Jea Marmande"
    assert "Raymond Marmande" in marmande["name_variants"]
    assert marmande["identity_status"] == "high_confidence"
    assert marnocaa["identity_status"] == "ambiguous"
    assert marnocaa["research_status"] == "needs_identity_review"
    assert marnocaa["possible_duplicate_group"] == "batch1040-richard-s-marnocaa-identity-conflict"


def test_batch1040_bundle_has_no_private_identifier_or_raw_record() -> None:
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
