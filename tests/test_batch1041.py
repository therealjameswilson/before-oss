from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1041_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-05_batch1041.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1041_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1041-v1",
        "reviewer": "Before OSS Batch 1041 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1041_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 14
    assert len(payload["organizations"]) == 7
    assert len(payload["affiliations"]) == 22
    assert len(payload["claims"]) == 26
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 23,
        "occupation_only_found": 15,
        "needs_identity_review": 3,
        "verified_employer_found": 2,
        "documented_prewar_employer_found": 2,
        "conflicting_sources": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1041_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1041_army_decisions_are_explicit_and_conflict_safe() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 16
    assert Counter(row["decision"] for row in rows) == {"accepted": 15, "rejected": 1}
    assert all(row["decision_version"] == "batch-1041-v1" for row in rows)
    assert {row["target_id"] for row in rows if row["decision"] == "rejected"} == {
        "b874b696-a08f-51d8-926e-4fa49c34895a"
    }
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    assert module.PEOPLE[13][0] not in affiliation_people


def test_batch1041_army_affiliations_stay_broad_and_nonemployer() -> None:
    module = load_generator()
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert len(army_keys) == 15
    for key in army_keys:
        affiliation = affiliations[key]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False


def test_batch1041_named_roles_preserve_temporal_and_relationship_distinctions() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    mascot = affiliations["carl-f-marquard-mascot-b1041"]
    uw = affiliations["hildegarde-r-marsales-uw-b1041"]
    knox = affiliations["hildegarde-r-marsales-knox-b1041"]
    nbc = affiliations["john-h-marsching-nbc-b1041"]
    cap = affiliations["maclean-marshall-cap-b1041"]
    soe = affiliations["james-h-marshall-corn-soe-b1041"]

    assert mascot["relationship_type"] == "employment"
    assert mascot["immediate_pre_oss"] is False
    assert mascot["pre_oss_temporal_basis"] == "documented_prewar"
    assert uw["relationship_type"] == "employment"
    assert uw["immediate_pre_oss"] is True
    assert uw["last_civilian_pre_service"] is True
    assert uw["pre_oss_temporal_basis"] == "probable_immediate"
    assert knox["immediate_pre_oss"] is False
    assert nbc["identity_confidence"] == "probable"
    assert nbc["claim_confidence"] == "medium"
    assert cap["relationship_type"] == "volunteer"
    assert cap["last_civilian_pre_service"] is False
    assert soe["relationship_type"] == "government_assignment"
    assert soe["pre_oss_temporal_basis"] == "temporal_relation_uncertain"


def test_batch1041_conflicts_and_variants_stay_visible_and_unmerged() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    marnocha = updates[module.PEOPLE[1][0]]
    marritts = updates[module.PEOPLE[13][0]]
    cornwall = updates[module.PEOPLE[28][0]]
    maclean = updates[module.PEOPLE[35][0]]
    marshall_corn = updates[module.PEOPLE[43][0]]

    assert marnocha["possible_duplicate_group"] == "p295-296-richard-s-marnocaa-marnocha-b622"
    assert marritts["identity_status"] == "conflicting"
    assert marritts["research_status"] == "conflicting_sources"
    assert cornwall["identity_status"] == "ambiguous"
    assert cornwall["person_id"] != marshall_corn["person_id"]
    assert cornwall["possible_duplicate_group"] == marshall_corn["possible_duplicate_group"]
    assert marshall_corn["identity_status"] == "high_confidence"
    assert marshall_corn["research_status"] == "needs_identity_review"
    assert module.PEOPLE[35][1] == "Maclean Marshall"
    assert maclean["name_variants"] == ["MacLean Marshall", "Mac Lean Marshall"]


def test_batch1041_preserves_existing_reviewed_people_without_downgrade() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    attempts = {item["person_id"]: item for item in module.research_attempts()}
    timothy = updates[module.PEOPLE[24][0]]
    carl = updates[module.PEOPLE[27][0]]
    assert timothy["research_status"] == "verified_employer_found"
    assert attempts[module.PEOPLE[24][0]]["attempt_number"] == 2
    assert carl["research_status"] == "requires_archival_review"
    assert attempts[module.PEOPLE[27][0]]["attempt_number"] == 19


def test_batch1041_bundle_has_no_private_identifier_or_raw_record() -> None:
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
