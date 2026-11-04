from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1020_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1020_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1020_bundle_is_complete_and_valid() -> None:
    module = load_generator()
    bundle = {
        "bundle_version": "batch-1020-v1",
        "reviewer": "Before OSS Batch 1020 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }
    EvidenceBundle.model_validate(bundle)

    assert len(bundle["person_updates"]) == 46
    assert len(bundle["research_attempts"]) == 46
    assert {attempt["person_id"] for attempt in bundle["research_attempts"]} == {
        update["person_id"] for update in bundle["person_updates"]
    }
    assert all(update["research_status"] != "not_started" for update in bundle["person_updates"])


def test_batch1020_preserves_evidence_boundaries() -> None:
    module = load_generator()
    affiliations = module.affiliations()
    claims = module.claims()

    occupation_affiliations = [
        item for item in affiliations if "army-occupation" in item["key"]
    ]
    assert len(occupation_affiliations) == 9
    assert all(item["relationship_type"] == "unknown" for item in occupation_affiliations)
    assert all("organization_key" not in item for item in occupation_affiliations)
    assert not any("609" in claim["claim_text"] for claim in claims)
    assert not any("590" in claim["claim_text"] for claim in claims)
    assert not any("144" in claim["claim_text"] for claim in claims)

    withrow = next(
        item for item in affiliations if item["key"] == "james-withrow-donovan-firm-b1020"
    )
    assert withrow["immediate_pre_oss"] is True
    assert withrow["last_civilian_pre_service"] is True
    assert withrow["relationship_type"] == "employment"

    wittmann_portland = next(
        item for item in affiliations if item["key"] == "otto-wittmann-portland-b1020"
    )
    wittmann_atc = next(
        item for item in affiliations if item["key"] == "otto-wittmann-atc-b1020"
    )
    assert wittmann_portland["last_civilian_pre_service"] is True
    assert wittmann_portland.get("immediate_pre_oss", False) is False
    assert wittmann_atc["immediate_pre_oss"] is True
    assert wittmann_atc["relationship_type"] == "military_assignment"

    wludyka = next(
        item for item in affiliations if item["key"] == "peter-wludyka-army-b1020"
    )
    assert wludyka["immediate_pre_oss"] is True
    assert wludyka["relationship_type"] == "military_assignment"


def test_batch1020_public_bundle_contains_no_full_private_identifier() -> None:
    module = load_generator()
    payload = json.dumps(
        {
            "sources": module.sources(),
            "affiliations": module.affiliations(),
            "claims": module.claims(),
            "person_updates": module.person_updates(),
            "research_attempts": module.research_attempts(),
        }
    )

    # The Peter S. Wludyka report contains a full protected service number,
    # but the reviewed bundle must retain only a description of the match.
    assert "12008822" not in payload
    assert "bulk_record_ordinal" not in payload


def test_batch1020_duplicate_and_famous_namesake_stay_unresolved() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}

    wisynski = updates[module.PEOPLE[15][0]]
    wixynski = updates[module.PEOPLE[41][0]]
    carl_wittke = updates[module.PEOPLE[33][0]]

    assert wisynski["identity_status"] == "unresolved"
    assert wixynski["identity_status"] == "unresolved"
    assert wisynski["possible_duplicate_group"] == wixynski["possible_duplicate_group"]
    assert carl_wittke["identity_status"] == "unresolved"
    assert "famous-biography candidate is rejected" in carl_wittke["identity_evidence"]
