from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1028_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-04_batch1028.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1028_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1028-v1",
        "reviewer": "Before OSS Batch 1028 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1028_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 10
    assert len(payload["organizations"]) == 4
    assert len(payload["affiliations"]) == 17
    assert len(payload["claims"]) == 25
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert all(update["research_status"] != "not_started" for update in payload["person_updates"])


def test_batch1028_separates_employment_volunteer_and_professional_status() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    assert by_key["cuyler-young-university-toronto-b1028"]["relationship_type"] == "employment"
    assert by_key["evelle-younger-fbi-b1028"]["relationship_type"] == "government_assignment"
    assert by_key["rodney-young-greek-red-cross-b1028"]["relationship_type"] == "volunteer"
    assert by_key["rodney-young-ascsa-b1028"]["relationship_type"] == "professional_affiliation"
    assert by_key["peter-yovanovich-physician-b1028"]["relationship_type"] == "unknown"


def test_batch1028_preserves_immediate_and_last_civilian_distinctions() -> None:
    module = load_generator()
    by_key = {item["key"]: item for item in module.affiliations()}
    for key in ("cuyler-young-university-toronto-b1028", "evelle-younger-fbi-b1028"):
        assert by_key[key]["immediate_pre_oss"] is True
        assert by_key[key]["last_civilian_pre_service"] is True
        assert by_key[key]["pre_oss_temporal_basis"] == "explicit_immediate"
    assert by_key["rodney-young-greek-red-cross-b1028"]["immediate_pre_oss"] is True
    assert by_key["rodney-young-greek-red-cross-b1028"]["last_civilian_pre_service"] is False
    assert by_key["rodney-young-ascsa-b1028"]["immediate_pre_oss"] is False


def test_batch1028_does_not_turn_petroleum_codes_into_oil_companies() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    for key in (
        "richard-k-young-army-occupation-b1028",
        "william-e-youngs-army-occupation-b1028",
    ):
        item = affiliations[key]
        assert item.get("organization_key") is None
        assert item["relationship_type"] == "unknown"
        assert item["last_civilian_pre_service"] is False
        assert item["publication_status"] == "publish_qualified"


def test_batch1028_keeps_postwar_and_undefined_army_codes_identity_only() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    claims = {item["key"]: item for item in module.claims()}
    assert module.PEOPLE[9][0] not in affiliation_people
    assert module.PEOPLE[20][0] not in affiliation_people
    assert claims["identity-billy-young-b1028"]["claim_type"] == "identity"
    assert claims["identity-james-b-young-b1028"]["claim_type"] == "identity"


def test_batch1028_preserves_indexed_and_documented_name_forms() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    peter = updates[module.PEOPLE[44][0]]
    assert module.PEOPLE[44][1] == "Peter, Dr. Yovanovich"
    assert "Dr. Peter Yovanovich" in peter["name_variants"]
    assert "Peter Yovanovich" in peter["name_variants"]
    assert "T. Cuyler Young" in updates[module.PEOPLE[12][0]]["name_variants"]
    assert "Rodney Stuart Young" in updates[module.PEOPLE[32][0]]["name_variants"]


def test_batch1028_army_review_decisions_are_bounded() -> None:
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 14
    assert all(row["decision"] == "accepted" for row in rows)
    assert all(row["decision_version"] == "batch-1028-v1" for row in rows)


def test_batch1028_bundle_has_no_private_identifier_or_raw_record() -> None:
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
