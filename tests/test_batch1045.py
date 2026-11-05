from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path

from oss_research.evidence import EvidenceBundle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_batch1045_bundle.py"
DECISIONS = ROOT / "research" / "army_entity_review_decisions_2026-11-05_batch1045.csv"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_batch1045_bundle", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bundle(module):
    return {
        "bundle_version": "batch-1045-v1",
        "reviewer": "Before OSS Batch 1045 evidence review",
        "sources": module.sources(),
        "organizations": module.organizations(),
        "affiliations": module.affiliations(),
        "claims": module.claims(),
        "person_updates": module.person_updates(),
        "research_attempts": module.research_attempts(),
    }


def test_batch1045_is_complete_and_schema_valid() -> None:
    module = load_generator()
    payload = bundle(module)
    EvidenceBundle.model_validate(payload)
    assert len(module.PEOPLE) == 46
    assert len(payload["sources"]) == 9
    assert len(payload["organizations"]) == 2
    assert len(payload["affiliations"]) == 18
    assert len(payload["claims"]) == 23
    assert len(payload["person_updates"]) == 46
    assert len(payload["research_attempts"]) == 46
    assert Counter(item["research_status"] for item in payload["person_updates"]) == {
        "requires_archival_review": 28,
        "occupation_only_found": 16,
        "needs_identity_review": 2,
    }
    assert all(
        update["research_status"] not in {"not_started", "in_progress"}
        for update in payload["person_updates"]
    )


def test_batch1045_every_public_affiliation_has_a_claim() -> None:
    module = load_generator()
    public_affiliations = {
        item["key"]
        for item in module.affiliations()
        if item["publication_status"] in {"published", "publish_qualified"}
    }
    claimed = {item["affiliation_key"] for item in module.claims() if item.get("affiliation_key")}
    assert public_affiliations == claimed


def test_batch1045_army_decisions_are_explicit() -> None:
    module = load_generator()
    with DECISIONS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 15
    assert Counter(row["decision"] for row in rows) == {"accepted": 15}
    assert all(row["decision_version"] == "batch-1045-v1" for row in rows)
    assert {row["target_id"] for row in rows} == {
        "571d97ea-6868-58f4-b6be-81d9c1094f4c",
        "709fa998-0b52-5bed-a5e2-5f1900d7d7af",
        "dfe1a5a1-512c-55e4-a66e-f3a1ff9936e6",
        "c6696220-9358-5835-a7e9-a3bfe42d1c3e",
        "27ce6e75-b925-54de-83f3-3b1117cc9d51",
        "33016af1-4978-5a2c-ba86-2c96afde8b78",
        "94154b18-3d44-5220-9c02-a2cb6fca31b3",
        "db7b4c53-8726-593b-92c0-9ec5620fcf8c",
        "0d8cacdb-e9b9-5bc9-9b27-057037f4bfd0",
        "a1e2cdbb-5012-5273-ac07-6a62a8d499b1",
        "2b7d228c-8e42-5a24-8645-469ac709fce1",
        "77053891-87b0-521a-9f4f-8e22247ccf30",
        "5fa8f34a-48e6-587e-8f6c-705efc7f1af2",
        "e8a1def5-73ef-59eb-81ad-60dbb24dc3ce",
        "43e4a74a-f72c-57d1-94b9-79cdad413fab",
    }


def test_batch1045_army_categories_stay_broad_and_nonemployer() -> None:
    module = load_generator()
    affiliations = {item["key"]: item for item in module.affiliations()}
    army_keys = {module.army_affiliation_key(row) for row in module.ARMY_ASSOCIATIONS}
    assert len(army_keys) == 15
    for key in army_keys:
        affiliation = affiliations[key]
        assert "organization_key" not in affiliation
        assert "organization_name_as_found" not in affiliation
        assert affiliation["claim_confidence"] == "medium"
        assert affiliation["publication_status"] == "publish_qualified"
        assert affiliation["immediate_pre_oss"] is False
        assert affiliation["last_civilian_pre_service"] is False


def test_batch1045_matsunaka_has_only_a_qualified_army_pathway() -> None:
    module = load_generator()
    person_id = module.PEOPLE[20][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == person_id]
    assert len(affiliations) == 2
    immediate = next(item for item in affiliations if item["immediate_pre_oss"])
    occupation = next(item for item in affiliations if not item["immediate_pre_oss"])
    assert immediate["relationship_type"] == "military_assignment"
    assert immediate["organization_key"] == module.ORG_ARMY
    assert immediate["pre_oss_temporal_basis"] == "probable_immediate"
    assert immediate["claim_confidence"] == "high"
    assert "SEATIC" not in immediate["organization_name_as_found"]
    assert occupation["occupation"] == "radio operator"
    assert occupation["claim_confidence"] == "medium"


def test_batch1045_mathieu_keeps_student_and_occupation_separate() -> None:
    module = load_generator()
    person_id = module.PEOPLE[5][0]
    affiliations = [item for item in module.affiliations() if item["person_id"] == person_id]
    assert len(affiliations) == 2
    teacher = next(item for item in affiliations if item["relationship_type"] == "employment")
    student = next(item for item in affiliations if item["relationship_type"] == "student")
    assert "organization_key" not in teacher
    assert teacher["occupation"] == "language teacher"
    assert teacher["immediate_pre_oss"] is False
    assert teacher["last_civilian_pre_service"] is False
    assert student["organization_key"] == module.ORG_PRINCETON
    assert student["last_civilian_pre_service"] is False
    assert student["claim_confidence"] == "medium"


def test_batch1045_duplicate_eugene_rows_remain_separate_and_conflicted() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    captain = updates[module.PEOPLE[29][0]]
    lieutenant = updates[module.PEOPLE[30][0]]
    assert captain["identity_status"] == "ambiguous"
    assert lieutenant["identity_status"] == "conflicting"
    assert captain["research_status"] == "needs_identity_review"
    assert lieutenant["research_status"] == "needs_identity_review"
    affiliation_people = {item["person_id"] for item in module.affiliations()}
    assert module.PEOPLE[29][0] not in affiliation_people
    assert module.PEOPLE[30][0] not in affiliation_people
    assert module.PEOPLE[29][0] != module.PEOPLE[30][0]


def test_batch1045_preserves_supported_variants() -> None:
    module = load_generator()
    updates = {item["person_id"]: item for item in module.person_updates()}
    assert updates[module.PEOPLE[5][0]]["name_variants"] == [
        "Arturo Carlo Felice Mathieu",
        "Arturo Carlo-Felice Mathieu",
    ]
    assert updates[module.PEOPLE[9][0]]["name_variants"] == ["John H Mathis Sr."]
    assert updates[module.PEOPLE[13][0]]["name_variants"] == ["Lesley M Mathwig"]
    assert updates[module.PEOPLE[22][0]]["name_variants"] == ["Andrew J Matta Jr."]


def test_batch1045_bundle_has_no_private_identifier_or_raw_record() -> None:
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


def test_batch1045_public_excerpts_are_short() -> None:
    module = load_generator()
    excerpts = [
        source["excerpt_override"]
        for claim in module.claims()
        for source in claim.get("sources", [])
        if source.get("excerpt_override")
    ]
    assert excerpts
    assert all(len(excerpt.split()) <= 25 for excerpt in excerpts)
