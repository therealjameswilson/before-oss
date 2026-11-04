from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1021_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1021_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle_from(module):
    return {
        "bundle_version": "batch-1021-v1",
        "reviewer": "Before OSS Batch 1021 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1021_bundle_is_complete_and_valid() -> None:
    module = load_generator()
    bundle = bundle_from(module)
    EvidenceBundle.model_validate(bundle)

    assert len(bundle["person_updates"]) == 46
    assert len(bundle["research_attempts"]) == 46
    assert {attempt["person_id"] for attempt in bundle["research_attempts"]} == {
        update["person_id"] for update in bundle["person_updates"]
    }
    assert all(update["research_status"] != "not_started" for update in bundle["person_updates"])


def test_batch1021_preserves_affiliation_boundaries() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}

    assert affiliations["charles-wolf-harvard-student-b1021"]["relationship_type"] == "student"
    assert affiliations["charles-wolf-harvard-student-b1021"].get("last_civilian_pre_service", False) is False
    assert affiliations["charles-wolf-army-b1021"]["relationship_type"] == "military_assignment"
    assert affiliations["charles-wolf-army-b1021"]["immediate_pre_oss"] is True

    robert = affiliations["robert-wolff-harvard-teaching-assistant"]
    assert robert["relationship_type"] == "employment"
    assert robert["immediate_pre_oss"] is True
    assert robert["last_civilian_pre_service"] is True
    assert robert["claim_confidence"] == "high"

    peter = affiliations["peter-wolkonsky-library-congress-b1021"]
    assert peter["relationship_type"] == "employment"
    assert peter["last_civilian_pre_service"] is True
    assert peter["claim_confidence"] == "medium"
    assert peter["publication_status"] == "publish_qualified"


def test_batch1021_bundle_contains_no_full_service_identifier() -> None:
    module = load_generator()
    payload = json.dumps(bundle_from(module))

    # Compare against the ingested source rows so the protected values never
    # need to be duplicated in test code or a review note.
    source_rows = ROOT / "data" / "derived" / "personnel_source_rows.jsonl"
    protected_identifiers = {
        row["serial_number_raw"]
        for line in source_rows.read_text(encoding="utf-8").splitlines()
        if (row := json.loads(line))["source_page"] == 511
        and row["serial_number_raw"]
    }
    assert protected_identifiers
    assert all(identifier not in payload for identifier in protected_identifiers)
    assert "serial_number_raw" not in payload


def test_batch1021_unbridged_candidates_remain_unresolved() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}

    dorothy = updates[module.PEOPLE[37][0]]
    dimitri = updates[module.PEOPLE[39][0]]
    anthony = updates[module.PEOPLE[42][0]]
    for update in (dorothy, dimitri, anthony):
        assert update["identity_status"] == "unresolved"
        assert update["research_status"] == "requires_archival_review"
        assert "No reliable pre-OSS employer has yet been identified" in update["next_action"]


def test_batch1021_special_outcomes_are_conservative() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}

    assert updates[module.PEOPLE[14][0]]["research_status"] == "completed"
    assert updates[module.PEOPLE[33][0]]["research_status"] == "completed"
    assert updates[module.PEOPLE[34][0]]["research_status"] == "verified_employer_found"
    assert updates[module.PEOPLE[40][0]]["research_status"] == "documented_prewar_employer_found"
    assert updates[module.PEOPLE[10][0]]["research_status"] == "requires_archival_review"
