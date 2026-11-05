from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1043_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-05_batch1043.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1043_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1043-v1",
        "reviewer": "Before OSS Batch 1043 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1043_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 8
    assert payload["organizations"] == []
    assert len(payload["affiliations"]) == 14
    assert len(payload["claims"]) == 19
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 30,
        "occupation_only_found": 14,
        "needs_identity_review": 2,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1043_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1043_army_decisions_are_explicit_and_conflict_safe() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 16
    assert Counter(row["decision"] for row in rows) == {"accepted": 15, "rejected": 1}
    assert all(row["decision_version"] == "batch-1043-v1" for row in rows)
    assert {row["target_id"] for row in rows if row["decision"] == "rejected"} == {
        "527cd656-c0f5-54a0-a579-5441ab78f99f"
    }
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    assert module.PEOPLE[22][0] not in affiliation_people
    assert module.PEOPLE[34][0] not in affiliation_people


def test_batch1043_army_affiliations_stay_broad_and_nonemployer() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    assert len(army_keys) == 13
    for key in army_keys:
        affiliation = affiliations[key]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False


def test_batch1043_undefined_and_conflicting_army_codes_are_withheld() -> None:
    module = load_generator()
    affiliations = {item["person_id"] for item in module.affiliations()}
    claims = {item["person_id"]: item for item in module.claims() if item["claim_type"] == "identity"}
    assert module.PEOPLE[3][0] not in affiliations
    assert module.PEOPLE[22][0] not in affiliations
    assert claims[module.PEOPLE[3][0]]["claim_confidence"] == "confirmed"
    assert "undefined" in claims[module.PEOPLE[3][0]]["match_notes"]
    assert claims[module.PEOPLE[22][0]]["claim_confidence"] == "conflicting"
    assert claims[module.PEOPLE[22][0]]["publication_status"] == "conflicting"


def test_batch1043_distinctive_identities_do_not_invent_employers() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    affiliations = {item["person_id"]: item for item in module.affiliations()}

    maurice = updates[module.PEOPLE[1][0]]
    pierre = updates[module.PEOPLE[29][0]]
    carl = updates[module.PEOPLE[40][0]]
    assert maurice["identity_status"] == "high_confidence"
    assert maurice["research_status"] == "requires_archival_review"
    assert module.PEOPLE[1][0] not in affiliations
    assert pierre["identity_status"] == "confirmed"
    assert pierre["research_status"] == "requires_archival_review"
    assert module.PEOPLE[29][0] not in affiliations
    assert carl["identity_status"] == "confirmed"
    assert carl["research_status"] == "occupation_only_found"

    marzani = affiliations[module.PEOPLE[40][0]]
    assert marzani["occupation"] == "private pursuits (source wording)"
    assert marzani["relationship_type"] == "unknown"
    assert marzani["pre_oss_temporal_basis"] == "probable_immediate"
    assert marzani["immediate_pre_oss"] is True
    assert marzani["last_civilian_pre_service"] is False
    assert "organization_key" not in marzani


def test_batch1043_preserves_index_spellings_and_variants() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert module.PEOPLE[24][1] == "Rigiberto Martinez Sr."
    assert module.PEOPLE[26][1] == "Russel D Martinko"
    assert module.PEOPLE[38][1] == "Mirian F Marx"
    assert module.PEOPLE[42][1] == "Williiam L Maschmeyer"
    assert module.PEOPLE[43][1] == "Egenia Masciarelli"
    assert updates[module.PEOPLE[24][0]]["name_variants"] == ["Rigoberto Martinez Sr."]
    assert updates[module.PEOPLE[45][0]]["name_variants"] == ["Roger W Masenoir"]


def test_batch1043_bundle_has_no_private_identifier_or_raw_record() -> None:
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
