from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1048_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-05_batch1048.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1048_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1048-v1",
        "reviewer": "Before OSS Batch 1048 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1048_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 43
    assert len(payload["sources"]) == 14
    assert len(payload["organizations"]) == 7
    assert len(payload["affiliations"]) == 20
    assert len(payload["claims"]) == 26
    assert len(payload["person_updates"]) == 43
    assert len(payload["research_attempts"]) == 43
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 29,
        "occupation_only_found": 8,
        "needs_identity_review": 2,
        "verified_employer_found": 2,
        "documented_prewar_employer_found": 1,
        "needs_temporal_review": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1048_preserves_existing_terminal_conflicts() -> None:
    module = load_generator()
    protected = {
        "6b4b6e22-e835-55ae-b7a6-40a112ecb5b7",  # Ward McCabe
        "d7c03613-c5e1-5938-ba61-e2e48cd4941b",  # William W McCabe
        "ba27c39f-9e25-58ff-a2d7-d5e2d4b64304",  # Curtis B McCammon
    }
    assert protected.isdisjoint(item[0] for item in module.PEOPLE.values())
    assert protected.isdisjoint(item["person_id"] for item in module.person_updates())
    assert protected.isdisjoint(item["person_id"] for item in module.research_attempts())


def test_batch1048_army_review_decisions_are_explicit() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 9
    assert Counter(row["decision"] for row in rows) == {"accepted": 8, "conflicting": 1}
    assert all(row["decision_version"] == "batch-1048-v1" for row in rows)
    assert {row["target_id"] for row in rows} == {
        "7a969748-c172-578a-8218-10b60a1e0eb9",
        "eb83a3c7-a668-5833-a77f-5b51652df503",
        "a2c0a8b9-c1dc-5d4c-a079-2c7b03810a5d",
        "100d5500-4970-5a3f-bcea-24df6269cb7b",
        "6f142ed7-19e3-58c9-934c-e4bbb0a4ee25",
        "bf12d417-355c-5c58-b886-9b8922eeb992",
        "961c289f-dfdc-5820-b7e5-daeb83f11a52",
        "c15a3958-bcf9-5cb0-a665-a9e60512924f",
        "42d60cea-53d8-5478-a771-2c3d52f21583",
    }


def test_batch1048_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1048_army_categories_stay_broad_and_nonemployer() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    assert len(army_keys) == 7
    for key in army_keys:
        affiliation = affiliations[key]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False
    affiliation_people = {item["person_id"] for item in affiliations.values()}
    assert module.PEOPLE[12][0] not in affiliation_people
    assert module.PEOPLE[23][0] not in affiliation_people


def test_batch1048_luigi_mazzone_separates_navy_and_unnamed_civilian_job() -> None:
    module = load_generator()
    affiliations = {
        item["key"]: item
        for item in module.affiliations()
        if item["person_id"] == module.PEOPLE[1][0]
    }
    assert set(affiliations) == {
        "luigi-mazzone-us-navy-b1048",
        "luigi-mazzone-truck-driver-b1048",
    }
    navy = affiliations["luigi-mazzone-us-navy-b1048"]
    truck = affiliations["luigi-mazzone-truck-driver-b1048"]
    assert navy["relationship_type"] == "military_assignment"
    assert navy["immediate_pre_oss"] is True
    assert truck["relationship_type"] == "employment"
    assert truck["last_civilian_pre_service"] is True
    assert "organization_key" not in truck
    assert truck["occupation"] == "truck driver"


def test_batch1048_turner_mcbaine_keeps_employer_and_navy_path_separate() -> None:
    module = load_generator()
    affiliations = {
        item["key"]: item
        for item in module.affiliations()
        if item["person_id"] == module.PEOPLE[20][0]
    }
    navy = affiliations["turner-mcbaine-us-navy-b1048"]
    neylan = affiliations["turner-mcbaine-neylan-b1048"]
    orrick = affiliations["turner-mcbaine-orrick-b1048"]
    assert navy["relationship_type"] == "military_assignment"
    assert navy["immediate_pre_oss"] is True
    assert navy["pre_oss_temporal_basis"] == "probable_immediate"
    assert neylan["relationship_type"] == "employment"
    assert neylan["last_civilian_pre_service"] is True
    assert neylan["pre_oss_temporal_basis"] == "strongly_date_bounded"
    assert orrick["last_civilian_pre_service"] is False
    assert orrick["pre_oss_temporal_basis"] == "documented_prewar"


def test_batch1048_william_mcafee_preserves_named_and_unnamed_teaching_roles() -> None:
    module = load_generator()
    affiliations = [
        item for item in module.affiliations() if item["person_id"] == module.PEOPLE[9][0]
    ]
    assert len(affiliations) == 6
    immediate = next(item for item in affiliations if item["immediate_pre_oss"])
    last_civilian = next(item for item in affiliations if item["last_civilian_pre_service"])
    ewing = next(item for item in affiliations if item["key"] == "william-mcafee-ewing-b1048")
    assert immediate["relationship_type"] == "military_assignment"
    assert immediate["organization_key"] == module.ORG_ARMY
    assert immediate["pre_oss_temporal_basis"] == "explicit_immediate"
    assert last_civilian["organization_name_as_found"] == "local high school"
    assert "organization_key" not in last_civilian
    assert ewing["organization_key"] == module.ORG_EWING
    assert ewing["start_date"] == "1932"
    assert ewing["end_date"] == "1935"


def test_batch1048_nancy_rows_remain_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    mcanolish = updates[module.PEOPLE[13][0]]
    mccandlish = updates[module.PEOPLE[41][0]]
    assert mcanolish["person_id"] != mccandlish["person_id"]
    assert mcanolish["identity_status"] == "ambiguous"
    assert mcanolish["research_status"] == "needs_identity_review"
    assert mccandlish["identity_status"] == "high_confidence"
    assert mccandlish["research_status"] == "verified_employer_found"
    assert mcanolish["possible_duplicate_group"] == mccandlish["possible_duplicate_group"]
    sao = next(item for item in module.affiliations() if item["key"] == "nancy-mccandlish-sao-b1048")
    assert sao["person_id"] == mccandlish["person_id"]
    assert sao["immediate_pre_oss"] is True
    assert sao["last_civilian_pre_service"] is True


def test_batch1048_frederica_mcafee_is_civilian_and_qualified() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    frederica = updates[module.PEOPLE[7][0]]
    assert frederica["personnel_category"] == "civilian_professional_or_administrative_grade"
    assert frederica["commissioned_officer"] is False
    assert frederica["research_status"] == "needs_temporal_review"
    wasp = next(item for item in module.affiliations() if item["key"] == "frederica-mcafee-wasp-b1048")
    assert wasp["relationship_type"] == "government_assignment"
    assert wasp["claim_confidence"] == "medium"
    assert wasp["publication_status"] == "publish_qualified"


def test_batch1048_bundle_has_no_private_identifier_or_raw_record() -> None:
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


def test_batch1048_public_excerpts_are_short() -> None:
    module = load_generator()
    excerpts = [
        source["excerpt_override"]
        for claim in module.claims()
        for source in claim.get("sources", [])
        if source.get("excerpt_override")
    ]
    assert excerpts
    assert all(len(excerpt.split()) <= 25 for excerpt in excerpts)
