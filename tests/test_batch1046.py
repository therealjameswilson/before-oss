from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1046_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1046_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1046-v1",
        "reviewer": "Before OSS Batch 1046 evidence review",
        "sources": module.sources(),
        "organizations": [],
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1046_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 45
    assert len(payload["sources"]) == 5
    assert payload["organizations"] == []
    assert len(payload["affiliations"]) == 14
    assert len(payload["claims"]) == 19
    assert len(payload["person_updates"]) == 45
    assert len(payload["research_attempts"]) == 45
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 28,
        "occupation_only_found": 14,
        "needs_identity_review": 2,
        "conflicting_sources": 1,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1046_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1046_army_categories_stay_broad_and_nonemployer() -> None:
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


def test_batch1046_keeps_duplicate_and_same_name_rows_visible() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}

    joseph = updates[module.PEOPLE[18][0]]
    assert joseph["identity_status"] == "high_confidence"
    assert joseph["possible_duplicate_group"] == "page301-joseph-p-mauro-two-source-rows"

    officer = updates[module.PEOPLE[36][0]]
    enlisted = updates[module.PEOPLE[37][0]]
    assert officer["person_id"] != enlisted["person_id"]
    assert officer["identity_status"] == "ambiguous"
    assert officer["research_status"] == "needs_identity_review"
    assert enlisted["identity_status"] == "high_confidence"
    assert enlisted["name_variants"] == ["Georges C May"]
    assert officer["possible_duplicate_group"] == enlisted["possible_duplicate_group"]
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    assert officer["person_id"] not in affiliation_people
    assert enlisted["person_id"] in affiliation_people


def test_batch1046_conflicts_do_not_transfer_candidate_data() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    affiliations = {item["person_id"] for item in module.affiliations()}

    erwin = updates[module.PEOPLE[22][0]]
    assert erwin["identity_status"] == "conflicting"
    assert erwin["research_status"] == "conflicting_sources"
    assert erwin["person_id"] not in affiliations

    charles = updates[module.PEOPLE[29][0]]
    assert charles["identity_status"] == "probable"
    assert charles["research_status"] == "needs_identity_review"
    assert charles["person_id"] not in affiliations
    candidate_claim = next(
        item for item in module.claims() if item["key"] == "identity-charles-maxwell-maxwelc-candidate-b1046"
    )
    assert candidate_claim["claim_confidence"] == "low"
    assert candidate_claim["publication_status"] == "withheld_low_confidence"


def test_batch1046_code_993_is_not_interpreted() -> None:
    module = load_generator()
    person_id = module.PEOPLE[23][0]
    assert person_id not in {item["person_id"] for item in module.affiliations()}
    update = next(item for item in module.person_updates() if item["person_id"] == person_id)
    assert update["identity_status"] == "high_confidence"
    assert update["research_status"] == "requires_archival_review"
    assert "not interpreted" in update["next_action"]


def test_batch1046_floyd_maves_has_direct_identity_evidence_not_employer_claim() -> None:
    module = load_generator()
    person_id = module.PEOPLE[24][0]
    update = next(item for item in module.person_updates() if item["person_id"] == person_id)
    assert update["identity_status"] == "confirmed"
    claims = [item for item in module.claims() if item["person_id"] == person_id]
    assert {item["claim_type"] for item in claims} == {"identity", "occupation"}
    identity = next(item for item in claims if item["claim_type"] == "identity")
    assert identity["claim_confidence"] == "confirmed"
    assert "Detachment 101" in identity["claim_text"]
    affiliation = next(item for item in module.affiliations() if item["person_id"] == person_id)
    assert "organization_key" not in affiliation
    assert affiliation["immediate_pre_oss"] is False


def test_batch1046_bundle_has_no_private_identifier_or_raw_record() -> None:
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


def test_batch1046_public_excerpts_are_short() -> None:
    module = load_generator()
    excerpts = [
        source["excerpt_override"]
        for claim in module.claims()
        for source in claim.get("sources", [])
        if source.get("excerpt_override")
    ]
    assert excerpts == ["Maves, Floyd E | Cpl | Sgt"]
    assert all(len(excerpt.split()) <= 25 for excerpt in excerpts)
