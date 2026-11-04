from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1031_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1031.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1031_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1031-v1",
        "reviewer": "Before OSS Batch 1031 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1031_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 14
    assert len(payload["organizations"]) == 6
    assert len(payload["affiliations"]) == 26
    assert len(payload["claims"]) == 31
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1031_every_public_affiliation_has_a_claim() -> None:
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


def test_batch1031_separates_students_and_military_assignments() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    tufts = affiliations["paul-zinner-tufts-student-b1031"]
    army = affiliations["paul-zinner-us-army-b1031"]
    cornell = affiliations["maurice-zubkoff-cornell-student-b1031"]
    assert tufts["relationship_type"] == "student"
    assert tufts["last_civilian_pre_service"] is False
    assert tufts["immediate_pre_oss"] is False
    assert army["relationship_type"] == "military_assignment"
    assert army["immediate_pre_oss"] is True
    assert army["last_civilian_pre_service"] is False
    assert cornell["relationship_type"] == "student"
    assert cornell["organization_name_as_found"] == "Cornell University"
    assert cornell["last_civilian_pre_service"] is False


def test_batch1031_zinder_alias_keeps_military_pathways_distinct() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    legion = affiliations["edmund-zinder-foreign-legion-b1031"]
    british = affiliations["edmund-zinder-british-army-b1031"]
    assert legion["pre_oss_temporal_basis"] == "documented_prewar"
    assert legion["immediate_pre_oss"] is False
    assert british["pre_oss_temporal_basis"] == "explicit_immediate"
    assert british["immediate_pre_oss"] is True
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert "Edmund F Linder" in updates[module.PEOPLE[6][0]]["name_variants"]
    assert updates[module.PEOPLE[7][0]]["identity_status"] == "ambiguous"
    assert updates[module.PEOPLE[6][0]]["possible_duplicate_group"] == updates[module.PEOPLE[7][0]]["possible_duplicate_group"]


def test_batch1031_withholds_undefined_shared_conflicting_and_late_codes() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    for row in {20, 29, 35, 36, 37}:
        assert module.PEOPLE[row][0] not in affiliation_people
    claims = {item["key"]: item for item in module.claims()}
    assert claims["conflict-frank-zobatta-zabatta-b1031"]["publication_status"] == "conflicting"
    assert claims["conflict-james-zonas-tonas-b1031"]["publication_status"] == "conflicting"
    assert claims["conflict-john-zonenberg-army-b1031"]["publication_status"] == "conflicting"


def test_batch1031_professional_membership_is_not_an_employer() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    ire = affiliations["jack-zoschke-ire-b1031"]
    assert ire["relationship_type"] == "professional_affiliation"
    assert ire["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
    assert ire["last_civilian_pre_service"] is False
    assert ire.get("occupation") is None


def test_batch1031_preserves_reviewed_name_variants() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert "John M Zimn" in updates[module.PEOPLE[5][0]]["name_variants"]
    assert "Dominick J Zippilli" in updates[module.PEOPLE[16][0]]["name_variants"]
    assert "Angelo C Zotos" in updates[module.PEOPLE[40][0]]["name_variants"]
    assert module.PEOPLE[40][1] == "Andgelo C Zotos"


def test_batch1031_army_review_decisions_are_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 27
    assert sum(row["decision"] == "accepted" for row in rows) == 22
    assert sum(row["decision"] == "conflicting" for row in rows) == 5
    assert sum(row["decision"] == "rejected" for row in rows) == 0
    assert all(row["decision_version"] == "batch-1031-v1" for row in rows)


def test_batch1031_bundle_has_no_private_identifier_or_raw_record() -> None:
    module = load_generator()
    payload = json.dumps(bundle(module))
    forbidden = (
        "serial_number",
        "service_number",
        "candidate_identifier",
        "bulk_record_ordinal",
        "raw_record",
        "serial-conflict:",
        "x-api-key",
    )
    assert not any(value in payload for value in forbidden)
