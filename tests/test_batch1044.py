from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1044_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-05_batch1044.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1044_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1044-v1",
        "reviewer": "Before OSS Batch 1044 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1044_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 2
    assert len(payload["affiliations"]) == 16
    assert len(payload["claims"]) == 21
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 28,
        "occupation_only_found": 14,
        "verified_employer_found": 2,
        "needs_identity_review": 2,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1044_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1044_army_decisions_are_explicit_and_conflict_safe() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 15
    assert Counter(row["decision"] for row in rows) == {"accepted": 14, "rejected": 1}
    assert all(row["decision_version"] == "batch-1044-v1" for row in rows)
    assert {row["target_id"] for row in rows if row["decision"] == "rejected"} == {
        "c39d650f-942a-57c1-a008-27304d39ead6"
    }
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    assert module.PEOPLE[42][0] not in affiliation_people


def test_batch1044_army_affiliations_stay_broad_and_nonemployer() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    assert len(army_keys) == 14
    for key in army_keys:
        affiliation = affiliations[key]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False


def test_batch1044_materazzi_keeps_military_and_civilian_pathways_separate() -> None:
    module = load_generator()
    materazzi_id = module.PEOPLE[35][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == materazzi_id]
    assert len(affiliations) == 2
    immediate = next(item for item in affiliations if item["immediate_pre_oss"])
    civilian = next(item for item in affiliations if item["last_civilian_pre_service"])
    assert immediate["relationship_type"] == "military_assignment"
    assert immediate["organization_key"] == module.ORG_ARMY_ENGINEERS
    assert immediate["pre_oss_temporal_basis"] == "strongly_date_bounded"
    assert immediate["claim_confidence"] == "high"
    assert civilian["relationship_type"] == "employment"
    assert civilian["organization_key"] == module.ORG_ARMY_MAP_SERVICE
    assert civilian["pre_oss_temporal_basis"] == "documented_prewar"
    assert civilian["claim_confidence"] == "medium"


def test_batch1044_preserves_existing_mason_evidence_and_ambiguous_candidates() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claim_people = {item["person_id"] for item in module.claims()}
    mason_id = module.PEOPLE[6][0]
    thomas_id = module.PEOPLE[31][0]
    eugene_id = module.PEOPLE[42][0]
    assert updates[mason_id]["research_status"] == "verified_employer_found"
    assert mason_id not in affiliation_people
    assert mason_id not in claim_people
    assert updates[thomas_id]["identity_status"] == "ambiguous"
    assert updates[thomas_id]["research_status"] == "needs_identity_review"
    assert thomas_id not in affiliation_people
    assert updates[eugene_id]["identity_status"] == "ambiguous"
    assert updates[eugene_id]["research_status"] == "needs_identity_review"
    assert eugene_id not in affiliation_people


def test_batch1044_preserves_index_spellings_and_supported_variants() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert module.PEOPLE[18][1] == "Evelyn D Massie Jr."
    assert module.PEOPLE[33][1] == "Brunislaw J Matejcak"
    assert module.PEOPLE[36][1] == "Dimitrious Matheos"
    assert updates[module.PEOPLE[33][0]]["name_variants"] == ["Bronislaw J Matejczak"]
    assert updates[module.PEOPLE[36][0]]["name_variants"] == ["Dimtrious Matheos"]
    assert updates[module.PEOPLE[39][0]]["name_variants"] == ["Frederick G Matheson"]
    assert updates[module.PEOPLE[41][0]]["name_variants"] == ["Elwood K Mathew"]
    assert "name_variants" not in updates[module.PEOPLE[21][0]]


def test_batch1044_bundle_has_no_private_identifier_or_raw_record() -> None:
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
