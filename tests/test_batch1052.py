from __future__ import annotations

import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1052_bundle.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1052_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_batch1052_is_complete_terminal_and_schema_valid() -> None:
    module = load_generator()
    payload = module.build_bundle()
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 4
    assert len(payload["organizations"]) == 0
    assert len(payload["affiliations"]) == 8
    assert len(payload["claims"]) == 17
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 35,
        "occupation_only_found": 8,
        "conflicting_sources": 3,
    }
    assert all(
        item["research_status"]
        not in {
            "not_started",
            "in_progress",
            "candidate_found",
            "needs_identity_review",
            "needs_temporal_review",
        }
        for item in payload["person_updates"]
    )


def test_batch1052_every_public_affiliation_has_one_claim() -> None:
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


def test_batch1052_army_categories_are_qualified_not_employers() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    assert set(module.ARMY_OCCUPATIONS) == {2, 14, 16, 17, 21, 34, 39, 46}
    for row in module.ARMY_OCCUPATIONS:
        affiliation = affiliations[module.army_affiliation_key(row)]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["pre_oss_temporal_basis"] == "temporal_relation_uncertain"
        assert affiliation["relationship_type"] == (
            "student" if row in {2, 14} else "unknown"
        )


def test_batch1052_undefined_code_has_no_affiliation() -> None:
    module = load_generator()
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    paul = module.PEOPLE[43][0]
    assert paul not in affiliation_people
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert updates[paul]["identity_status"] == "high_confidence"
    assert updates[paul]["research_status"] == "requires_archival_review"
    assert "code 993" in updates[paul]["next_action"]


def test_batch1052_duplicate_and_conflict_rows_stay_separate() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    for rows in ((13, 18), (41, 42)):
        assert len({module.PEOPLE[row][0] for row in rows}) == len(rows)
        assert len(
            {updates[module.PEOPLE[row][0]]["possible_duplicate_group"] for row in rows}
        ) == 1
        assert all(
            updates[module.PEOPLE[row][0]]["identity_status"] == "ambiguous"
            for row in rows
        )
    for row in (4, 26, 27):
        assert updates[module.PEOPLE[row][0]]["identity_status"] == "conflicting"
        assert updates[module.PEOPLE[row][0]]["research_status"] == "conflicting_sources"


def test_batch1052_attempt_numbers_continue_existing_history() -> None:
    module = load_generator()
    attempts = {
        item["person_id"]: item["attempt_number"]
        for item in module.research_attempts()
    }
    assert attempts[module.PEOPLE[1][0]] == 2
    assert attempts[module.PEOPLE[2][0]] == 3
    assert attempts[module.PEOPLE[26][0]] == 4
    assert attempts[module.PEOPLE[42][0]] == 4
    assert attempts[module.PEOPLE[46][0]] == 3
    assert set(attempts.values()) <= {2, 3, 4}


def test_batch1052_has_no_private_identifier_or_raw_api_content() -> None:
    module = load_generator()
    payload = json.dumps(module.build_bundle())
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


def test_batch1052_code_sources_cover_every_published_category() -> None:
    module = load_generator()
    code_source = next(item for item in module.sources() if item["key"] == module.CODES)
    assert "173-175 and 304" in code_source["locator"]
    claims = [item for item in module.claims() if item["claim_type"] == "occupation"]
    assert len(claims) == 8
    assert all(
        any(link["source_key"] == module.CODES for link in item["sources"])
        for item in claims
    )
