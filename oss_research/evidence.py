from __future__ import annotations

import json
import sqlite3
import uuid
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .constants import NAMESPACE_GENERIC
from .db import utc_now

GENERIC_NAMESPACE = uuid.UUID(NAMESPACE_GENERIC)


def _stable_id(kind: str, key: str) -> str:
    return str(uuid.uuid5(GENERIC_NAMESPACE, f"reviewed-evidence:{kind}:{key}"))


def _word_count(value: str | None) -> int:
    return len((value or "").split())


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SourceInput(StrictModel):
    key: str = Field(min_length=1)
    stable_url: str | None = None
    archival_identifier: str | None = None
    title: str = Field(min_length=1)
    author_creator: str | None = None
    repository_publisher: str = Field(min_length=1)
    publication_record_date: str | None = None
    locator: str | None = None
    access_date: str = Field(min_length=1)
    source_quality: Literal[
        "A_direct_official",
        "B_authoritative_institutional",
        "C_reputable_contemporary_or_scholarly",
        "D_correlative_or_secondary",
        "E_discovery_only",
    ]
    collection_name: str | None = None
    document_number: str | None = None
    rights_notes: str | None = None

    @model_validator(mode="after")
    def require_pointer(self) -> SourceInput:
        if not self.stable_url and not self.archival_identifier:
            raise ValueError("A source needs a stable URL or archival identifier.")
        return self


class OrganizationInput(StrictModel):
    key: str = Field(min_length=1)
    canonical_name: str = Field(min_length=1)
    historical_name: str | None = None
    aliases: list[str] = Field(default_factory=list)
    organization_type: str | None = None
    sector: Literal[
        "academia_and_research",
        "federal_government",
        "state_or_local_government",
        "military",
        "law",
        "journalism_and_media",
        "finance_and_banking",
        "business_and_industry",
        "advertising_and_public_relations",
        "medicine_and_public_health",
        "engineering_science_and_technology",
        "arts_and_culture",
        "labor_nonprofit_and_religion",
        "self_employed",
        "student",
        "unemployed_or_retired",
        "unknown",
    ]
    city: str | None = None
    state_or_region: str | None = None
    country: str | None = None
    active_dates: str | None = None
    normalization_notes: str | None = None


class AffiliationInput(StrictModel):
    key: str = Field(min_length=1)
    person_id: str = Field(min_length=1)
    organization_key: str | None = None
    organization_name_as_found: str | None = None
    role_title: str | None = None
    occupation: str | None = None
    relationship_type: Literal[
        "employment",
        "self_employment",
        "military_assignment",
        "government_assignment",
        "student",
        "unemployed",
        "retired",
        "volunteer",
        "professional_affiliation",
        "unknown",
    ]
    start_date: str | None = None
    end_date: str | None = None
    date_precision: str | None = None
    city: str | None = None
    state_or_region: str | None = None
    country: str | None = None
    immediate_pre_oss: bool = False
    last_civilian_pre_service: bool = False
    pre_oss_temporal_basis: Literal[
        "explicit_immediate",
        "strongly_date_bounded",
        "probable_immediate",
        "documented_prewar",
        "temporal_relation_uncertain",
    ]
    identity_confidence: Literal[
        "confirmed",
        "high_confidence",
        "probable",
        "ambiguous",
        "conflicting",
        "unresolved",
    ]
    claim_confidence: Literal[
        "confirmed", "high", "medium", "low", "unresolved", "conflicting"
    ]
    source_quality: Literal[
        "A_direct_official",
        "B_authoritative_institutional",
        "C_reputable_contemporary_or_scholarly",
        "D_correlative_or_secondary",
        "E_discovery_only",
    ]
    publication_status: Literal[
        "draft",
        "needs_review",
        "publish_qualified",
        "published",
        "withheld_low_confidence",
        "conflicting",
        "rejected",
    ]
    research_notes: str | None = None


class ClaimSourceInput(StrictModel):
    source_key: str = Field(min_length=1)
    support_type: Literal["supports", "contradicts", "context_only"] = "supports"
    locator_override: str | None = None
    excerpt_override: str | None = None

    @model_validator(mode="after")
    def limit_excerpt(self) -> ClaimSourceInput:
        if _word_count(self.excerpt_override) > 25:
            raise ValueError("Public source excerpts may not exceed 25 words.")
        return self


class ClaimInput(StrictModel):
    key: str = Field(min_length=1)
    person_id: str = Field(min_length=1)
    affiliation_key: str | None = None
    claim_type: Literal[
        "identity",
        "immediate_pre_oss_affiliation",
        "last_civilian_pre_service",
        "other_pre_oss_affiliation",
        "occupation",
        "archival_file_status",
        "organization_normalization",
    ]
    claim_text: str = Field(min_length=1)
    evidence_excerpt: str | None = None
    evidence_paraphrase: str = Field(min_length=1)
    identity_match_assessment: str = Field(min_length=1)
    temporal_assessment: str = Field(min_length=1)
    source_quality: Literal[
        "A_direct_official",
        "B_authoritative_institutional",
        "C_reputable_contemporary_or_scholarly",
        "D_correlative_or_secondary",
        "E_discovery_only",
    ]
    claim_confidence: Literal[
        "confirmed", "high", "medium", "low", "unresolved", "conflicting"
    ]
    publication_status: Literal[
        "draft",
        "needs_review",
        "publish_qualified",
        "published",
        "withheld_low_confidence",
        "conflicting",
        "rejected",
    ]
    match_notes: str = Field(min_length=1)
    sources: list[ClaimSourceInput] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_public_claim(self) -> ClaimInput:
        if _word_count(self.evidence_excerpt) > 25:
            raise ValueError("Public evidence excerpts may not exceed 25 words.")
        if self.publication_status in {"published", "publish_qualified"}:
            if not self.sources:
                raise ValueError("A public claim must link to at least one source.")
            if self.claim_confidence not in {"confirmed", "high", "medium"}:
                raise ValueError("Low or unresolved claims cannot be public facts.")
        return self


class PersonUpdateInput(StrictModel):
    person_id: str = Field(min_length=1)
    identity_status: Literal[
        "confirmed",
        "high_confidence",
        "probable",
        "ambiguous",
        "conflicting",
        "unresolved",
    ] | None = None
    identity_evidence: str | None = None
    research_status: Literal[
        "not_started",
        "in_progress",
        "candidate_found",
        "needs_identity_review",
        "needs_temporal_review",
        "verified_employer_found",
        "documented_prewar_employer_found",
        "occupation_only_found",
        "conflicting_sources",
        "no_reliable_result_after_protocol",
        "blocked_by_source_access",
        "requires_archival_review",
        "completed",
    ] | None = None
    next_action: str | None = None


class EvidenceBundle(StrictModel):
    bundle_version: str = Field(min_length=1)
    reviewer: str = Field(min_length=1)
    sources: list[SourceInput] = Field(default_factory=list)
    organizations: list[OrganizationInput] = Field(default_factory=list)
    affiliations: list[AffiliationInput] = Field(default_factory=list)
    claims: list[ClaimInput] = Field(default_factory=list)
    person_updates: list[PersonUpdateInput] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_keys(self) -> EvidenceBundle:
        for label, values in (
            ("source", self.sources),
            ("organization", self.organizations),
            ("affiliation", self.affiliations),
            ("claim", self.claims),
        ):
            keys = [value.key for value in values]
            if len(keys) != len(set(keys)):
                raise ValueError(f"Duplicate {label} keys in evidence bundle.")
        source_keys = {value.key for value in self.sources}
        organization_keys = {value.key for value in self.organizations}
        affiliation_keys = {value.key for value in self.affiliations}
        for affiliation in self.affiliations:
            if (
                affiliation.organization_key
                and affiliation.organization_key not in organization_keys
            ):
                raise ValueError("Affiliation references an unknown organization key.")
        for claim in self.claims:
            if claim.affiliation_key and claim.affiliation_key not in affiliation_keys:
                raise ValueError("Claim references an unknown affiliation key.")
            if any(link.source_key not in source_keys for link in claim.sources):
                raise ValueError("Claim references an unknown source key.")
        return self


def import_reviewed_evidence(
    connection: sqlite3.Connection,
    path: Path,
) -> dict[str, int]:
    bundle = EvidenceBundle.model_validate_json(path.read_text(encoding="utf-8"))
    now = utc_now()
    source_ids = {value.key: _stable_id("source", value.key) for value in bundle.sources}
    organization_ids = {
        value.key: _stable_id("organization", value.key)
        for value in bundle.organizations
    }
    affiliation_ids = {
        value.key: _stable_id("affiliation", value.key)
        for value in bundle.affiliations
    }
    claim_ids = {value.key: _stable_id("claim", value.key) for value in bundle.claims}

    referenced_people = {
        *(value.person_id for value in bundle.affiliations),
        *(value.person_id for value in bundle.claims),
        *(value.person_id for value in bundle.person_updates),
    }
    referenced_people_params = tuple(sorted(referenced_people))
    people = {
        row["person_id"]
        for row in connection.execute(
            "SELECT person_id FROM person_entities WHERE person_id IN ({})".format(
                ",".join("?" for _ in referenced_people_params)
                or "NULL"
            ),
            referenced_people_params,
        )
    }
    missing_people = referenced_people - people
    if missing_people:
        raise ValueError(f"Unknown person IDs: {sorted(missing_people)}")

    with connection:
        for source in bundle.sources:
            connection.execute(
                """
                INSERT INTO sources(
                    source_id, stable_url, archival_identifier, title,
                    author_creator, repository_publisher, publication_record_date,
                    locator, access_date, source_quality, collection_name,
                    document_number, rights_notes, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(source_id) DO UPDATE SET
                    stable_url=excluded.stable_url,
                    archival_identifier=excluded.archival_identifier,
                    title=excluded.title,
                    author_creator=excluded.author_creator,
                    repository_publisher=excluded.repository_publisher,
                    publication_record_date=excluded.publication_record_date,
                    locator=excluded.locator,
                    access_date=excluded.access_date,
                    source_quality=excluded.source_quality,
                    collection_name=excluded.collection_name,
                    document_number=excluded.document_number,
                    rights_notes=excluded.rights_notes
                """,
                (
                    source_ids[source.key],
                    source.stable_url,
                    source.archival_identifier,
                    source.title,
                    source.author_creator,
                    source.repository_publisher,
                    source.publication_record_date,
                    source.locator,
                    source.access_date,
                    source.source_quality,
                    source.collection_name,
                    source.document_number,
                    source.rights_notes,
                    now,
                ),
            )
        for organization in bundle.organizations:
            connection.execute(
                """
                INSERT INTO organizations(
                    organization_id, canonical_name, historical_name, aliases_json,
                    organization_type, sector, city, state_or_region, country,
                    active_dates, normalization_notes, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(organization_id) DO UPDATE SET
                    canonical_name=excluded.canonical_name,
                    historical_name=excluded.historical_name,
                    aliases_json=excluded.aliases_json,
                    organization_type=excluded.organization_type,
                    sector=excluded.sector,
                    city=excluded.city,
                    state_or_region=excluded.state_or_region,
                    country=excluded.country,
                    active_dates=excluded.active_dates,
                    normalization_notes=excluded.normalization_notes,
                    updated_at=excluded.updated_at
                """,
                (
                    organization_ids[organization.key],
                    organization.canonical_name,
                    organization.historical_name,
                    json.dumps(organization.aliases, ensure_ascii=False),
                    organization.organization_type,
                    organization.sector,
                    organization.city,
                    organization.state_or_region,
                    organization.country,
                    organization.active_dates,
                    organization.normalization_notes,
                    now,
                    now,
                ),
            )
        for affiliation in bundle.affiliations:
            connection.execute(
                """
                INSERT INTO affiliations(
                    affiliation_id, person_id, organization_id,
                    organization_name_as_found, role_title, occupation,
                    relationship_type, start_date, end_date, date_precision,
                    city, state_or_region, country, immediate_pre_oss,
                    last_civilian_pre_service, pre_oss_temporal_basis,
                    identity_confidence, claim_confidence, source_quality,
                    publication_status, research_notes, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(affiliation_id) DO UPDATE SET
                    organization_id=excluded.organization_id,
                    organization_name_as_found=excluded.organization_name_as_found,
                    role_title=excluded.role_title,
                    occupation=excluded.occupation,
                    relationship_type=excluded.relationship_type,
                    start_date=excluded.start_date,
                    end_date=excluded.end_date,
                    date_precision=excluded.date_precision,
                    city=excluded.city,
                    state_or_region=excluded.state_or_region,
                    country=excluded.country,
                    immediate_pre_oss=excluded.immediate_pre_oss,
                    last_civilian_pre_service=excluded.last_civilian_pre_service,
                    pre_oss_temporal_basis=excluded.pre_oss_temporal_basis,
                    identity_confidence=excluded.identity_confidence,
                    claim_confidence=excluded.claim_confidence,
                    source_quality=excluded.source_quality,
                    publication_status=excluded.publication_status,
                    research_notes=excluded.research_notes,
                    updated_at=excluded.updated_at
                """,
                (
                    affiliation_ids[affiliation.key],
                    affiliation.person_id,
                    (
                        organization_ids[affiliation.organization_key]
                        if affiliation.organization_key
                        else None
                    ),
                    affiliation.organization_name_as_found,
                    affiliation.role_title,
                    affiliation.occupation,
                    affiliation.relationship_type,
                    affiliation.start_date,
                    affiliation.end_date,
                    affiliation.date_precision,
                    affiliation.city,
                    affiliation.state_or_region,
                    affiliation.country,
                    int(affiliation.immediate_pre_oss),
                    int(affiliation.last_civilian_pre_service),
                    affiliation.pre_oss_temporal_basis,
                    affiliation.identity_confidence,
                    affiliation.claim_confidence,
                    affiliation.source_quality,
                    affiliation.publication_status,
                    affiliation.research_notes,
                    now,
                    now,
                ),
            )
        for claim in bundle.claims:
            connection.execute(
                """
                INSERT INTO claims(
                    claim_id, person_id, affiliation_id, claim_type, claim_text,
                    evidence_excerpt, evidence_paraphrase,
                    identity_match_assessment, temporal_assessment,
                    source_quality, claim_confidence, publication_status,
                    match_notes, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(claim_id) DO UPDATE SET
                    affiliation_id=excluded.affiliation_id,
                    claim_type=excluded.claim_type,
                    claim_text=excluded.claim_text,
                    evidence_excerpt=excluded.evidence_excerpt,
                    evidence_paraphrase=excluded.evidence_paraphrase,
                    identity_match_assessment=excluded.identity_match_assessment,
                    temporal_assessment=excluded.temporal_assessment,
                    source_quality=excluded.source_quality,
                    claim_confidence=excluded.claim_confidence,
                    publication_status=excluded.publication_status,
                    match_notes=excluded.match_notes,
                    updated_at=excluded.updated_at
                """,
                (
                    claim_ids[claim.key],
                    claim.person_id,
                    affiliation_ids[claim.affiliation_key]
                    if claim.affiliation_key
                    else None,
                    claim.claim_type,
                    claim.claim_text,
                    claim.evidence_excerpt,
                    claim.evidence_paraphrase,
                    claim.identity_match_assessment,
                    claim.temporal_assessment,
                    claim.source_quality,
                    claim.claim_confidence,
                    claim.publication_status,
                    claim.match_notes,
                    now,
                    now,
                ),
            )
            connection.execute(
                "DELETE FROM claim_sources WHERE claim_id = ?",
                (claim_ids[claim.key],),
            )
            for link in claim.sources:
                connection.execute(
                    """
                    INSERT INTO claim_sources(
                        claim_id, source_id, support_type,
                        locator_override, excerpt_override
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        claim_ids[claim.key],
                        source_ids[link.source_key],
                        link.support_type,
                        link.locator_override,
                        link.excerpt_override,
                    ),
                )
        for update in bundle.person_updates:
            current = connection.execute(
                """
                SELECT identity_status, identity_evidence, research_status, next_action
                FROM person_entities WHERE person_id = ?
                """,
                (update.person_id,),
            ).fetchone()
            connection.execute(
                """
                UPDATE person_entities
                SET identity_status=?, identity_evidence=?, research_status=?,
                    next_action=?, updated_at=?
                WHERE person_id=?
                """,
                (
                    update.identity_status or current["identity_status"],
                    (
                        update.identity_evidence
                        if update.identity_evidence is not None
                        else current["identity_evidence"]
                    ),
                    update.research_status or current["research_status"],
                    (
                        update.next_action
                        if update.next_action is not None
                        else current["next_action"]
                    ),
                    now,
                    update.person_id,
                ),
            )
            connection.execute(
                """
                UPDATE research_queue
                SET research_status=?, next_action=?, updated_at=?
                WHERE person_id=?
                """,
                (
                    update.research_status or current["research_status"],
                    (
                        update.next_action
                        if update.next_action is not None
                        else current["next_action"]
                    ),
                    now,
                    update.person_id,
                ),
            )
    return {
        "sources": len(bundle.sources),
        "organizations": len(bundle.organizations),
        "affiliations": len(bundle.affiliations),
        "claims": len(bundle.claims),
        "claim_source_links": sum(len(value.sources) for value in bundle.claims),
        "person_updates": len(bundle.person_updates),
    }
