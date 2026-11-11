from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1050_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1050_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1050-v1",
        "reviewer": "Before OSS Batch 1050 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1050_is_complete_terminal_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 8
    assert len(payload["organizations"]) == 8
    assert len(payload["affiliations"]) == 18
    assert len(payload["claims"]) == 20
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 33,
        "occupation_only_found": 9,
        "verified_employer_found": 3,
        "conflicting_sources": 1,
    }
    assert all(
        item["research_status"]
        not in {"not_started", "in_progress", "candidate_found", "needs_identity_review", "needs_temporal_review"}
        for item in payload["person_updates"]
    )


def test_batch1050_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1050_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    student_rows = {16, 19, 28, 29}
    assert len(module.ARMY_ASSOCIATIONS) == 10
    assert 23 not in module.ARMY_ASSOCIATIONS
    for row in module.ARMY_ASSOCIATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["relationship_type"] == (
            "student" if row in student_rows else "unknown"
        )
    oscar = next(
        item
        for item in module.person_updates()
        if item["person_id"] == module.PEOPLE[23][0]
    )
    assert oscar["research_status"] == "requires_archival_review"
    assert "27 April 1946" in oscar["next_action"]


def test_batch1050_keeps_immediate_and_last_civilian_affiliations_separate() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}

    mellon = affiliations["stewart-mcclintic-mellon-b1050"]
    bomber = affiliations["stewart-mcclintic-viii-bomber-command-b1050"]
    assert mellon["relationship_type"] == "employment"
    assert mellon["last_civilian_pre_service"] is True
    assert mellon["immediate_pre_oss"] is False
    assert bomber["relationship_type"] == "military_assignment"
    assert bomber["last_civilian_pre_service"] is False
    assert bomber["immediate_pre_oss"] is True

    wesleyan = affiliations["james-mcconaughy-wesleyan-b1050"]
    relief = affiliations["james-mcconaughy-united-china-relief-b1050"]
    assert wesleyan["relationship_type"] == "employment"
    assert wesleyan["last_civilian_pre_service"] is True
    assert wesleyan["immediate_pre_oss"] is False
    assert relief["relationship_type"] == "professional_affiliation"
    assert relief["last_civilian_pre_service"] is False
    assert relief["immediate_pre_oss"] is True


def test_batch1050_repeated_rows_remain_separate_and_archival() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for rows in ((7, 8), (38, 39, 40)):
        group = {updates[module.PEOPLE[row][0]]["possible_duplicate_group"] for row in rows}
        assert len(group) == 1
        assert len({module.PEOPLE[row][0] for row in rows}) == len(rows)
        assert all(
            updates[module.PEOPLE[row][0]]["research_status"]
            == "requires_archival_review"
            for row in rows
        )
    elmer = updates[module.PEOPLE[21][0]]
    assert elmer["identity_status"] == "conflicting"
    assert elmer["research_status"] == "conflicting_sources"


def test_batch1050_has_no_private_identifier_or_raw_api_content() -> None:
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


def test_batch1050_public_excerpts_are_short() -> None:
    module = load_generator()
    excerpts = [
        source["excerpt_override"]
        for claim in module.claims()
        for source in claim.get("sources", [])
        if source.get("excerpt_override")
    ]
    assert excerpts
    assert all(len(excerpt.split()) <= 25 for excerpt in excerpts)
