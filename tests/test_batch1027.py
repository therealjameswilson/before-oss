from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1027_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1027.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1027_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1027-v1",
        "reviewer": "Before OSS Batch 1027 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1027_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 7
    assert len(payload["affiliations"]) == 17
    assert len(payload["claims"]) == 24
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])


def test_batch1027_separates_yempuku_employment_and_military_pathway() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    university = by_key["ralph-yempuku-university-hawaii-b1027"]
    military = by_key["ralph-yempuku-442-rct-b1027"]
    assert university["relationship_type"] == "employment"
    assert university["last_civilian_pre_service"] is True
    assert university["immediate_pre_oss"] is False
    assert military["relationship_type"] == "military_assignment"
    assert military["pre_oss_temporal_basis"] == "explicit_immediate"
    assert military["immediate_pre_oss"] is True


def test_batch1027_qualifies_yerkes_sequence_and_yale_student_status() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    yale = by_key["david-yerkes-yale-b1027"]
    engineers = by_key["david-yerkes-army-engineers-b1027"]
    assert yale["relationship_type"] == "student"
    assert yale["last_civilian_pre_service"] is False
    assert engineers["relationship_type"] == "military_assignment"
    assert engineers["pre_oss_temporal_basis"] == "probable_immediate"
    assert engineers["publication_status"] == "publish_qualified"


def test_batch1027_preserves_temporal_uncertainty_for_government_roles() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    for key in ("arden-yinkley-wpb-b1027", "takehiko-yoshihashi-owi-b1027"):
        assert by_key[key]["relationship_type"] == "government_assignment"
        assert by_key[key]["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert by_key[key]["immediate_pre_oss"] is False
        assert by_key[key]["publication_status"] == "publish_qualified"


def test_batch1027_models_yokoi_as_professional_affiliation_not_employment() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    yokoi = by_key["jutaro-yokoi-sage-methodist-b1027"]
    assert yokoi["relationship_type"] == "professional_affiliation"
    assert yokoi["last_civilian_pre_service"] is False
    assert yokoi["publication_status"] == "publish_qualified"


def test_batch1027_uses_travel_order_for_identity_only() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claims = {item["key"]: item for item in module.claims()}
    assert claims["identity-shizuo-yoshida-b1027"]["claim_type"] == "identity"
    assert claims["identity-yoshisada-usuda-b1027"]["claim_type"] == "identity"
    assert module.PEOPLE[34][0] not in affiliation_people
    assert module.PEOPLE[39][0] not in affiliation_people
    updates = {item["person_id"]: item for item in module.person_updates()}
    usuda = updates[module.PEOPLE[39][0]]
    assert module.PEOPLE[39][1] == "Usuda Yoshisada"
    assert "Yoshisada Katoi Usuda" in usuda["name_variants"]


def test_batch1027_preserves_youkers_identifier_conflict() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    youkers = updates[module.PEOPLE[46][0]]
    assert youkers["identity_status"] == "conflicting"
    assert youkers["research_status"] == "conflicting_sources"
    assert "Roger E McCarren" in youkers["identity_evidence"]
    assert not any(item["person_id"] == module.PEOPLE[46][0] for item in module.affiliations())


def test_batch1027_army_review_decisions_are_bounded() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 11
    assert sum(row["decision"] == "accepted" for row in rows) == 10
    assert sum(row["decision"] == "rejected" for row in rows) == 1
    assert all(row["decision_version"] == "batch-1027-v1" for row in rows)


def test_batch1027_bundle_has_no_private_identifier_or_raw_record() -> None:
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
