from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass

SPACE_RE = re.compile(r"\s+")
NON_NAME_RE = re.compile(r"[^A-Z0-9]+")
SERIAL_RE = re.compile(r"[^A-Z0-9]+")
SUFFIX_RE = re.compile(
    r"(?:,\s*)?\b(JR\.?|SR\.?|II|III|IV)\b\.?",
    re.IGNORECASE,
)

ARMY_OFFICER_RANKS = {
    "2ND LT",
    "1ST LT",
    "LT",
    "CAPT",
    "MAJ",
    "LT COL",
    "COL",
    "BRIG GEN",
    "MAJ GEN",
    "GEN",
}
NAVAL_OFFICER_RANKS = {
    "ENS",
    "ENSIGN",
    "LT (JG)",
    "LT JG",
    "LCDR",
    "LT COMDR",
    "CDR",
    "COMDR",
    "REAR ADM",
    "ADM",
}
WARRANT_RANKS = {"WO", "W/O", "CWO", "CHIEF WO", "WARRANT OFFICER"}
ARMY_ENLISTED_RANKS = {
    "PVT",
    "PFC",
    "CPL",
    "SGT",
    "S/SGT",
    "SSGT",
    "T/SGT",
    "TSGT",
    "M/SGT",
    "MSGT",
    "T-3",
    "T-4",
    "T-5",
    "TEC 3",
    "TEC 4",
    "TEC 5",
}
NAVAL_ENLISTED_PREFIXES = (
    "S 1/C",
    "S 2/C",
    "S 3/C",
    "SP 1/C",
    "SP 2/C",
    "SP 3/C",
    "Y 1/C",
    "Y 2/C",
    "RM ",
    "RT ",
    "BM ",
    "GM ",
    "SK ",
)
CIVILIAN_GRADE_RE = re.compile(r"^(?:CAF|P|CPC|SP)-?\d+[A-Z]?$", re.IGNORECASE)
TEMPORARY_GRADE_RE = re.compile(r"^(?:TEMP|CONTRACT|SPECIAL|CONSULTANT)\b", re.IGNORECASE)
FOREIGN_NOTE_RE = re.compile(
    r"\b(?:POLISH|FRENCH|BRITISH|CANADIAN|DUTCH|BELGIAN|NORWEGIAN|"
    r"GREEK|ITALIAN|CHINESE|CZECH|YUGOSLAV|ALLIED|FOREIGN)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class NameParts:
    display_name: str
    normalized_name: str
    last_name: str
    first_name: str | None
    middle: str | None
    suffix: str | None
    variants_json: str
    notes: str | None


@dataclass(frozen=True)
class PersonnelClassification:
    rank_normalized: str | None
    category: str
    commissioned_officer: bool | None
    allied_or_foreign: bool | None
    note: str | None = None


def clean(value: str | None) -> str | None:
    if value is None:
        return None
    value = SPACE_RE.sub(" ", value).strip()
    return value or None


def name_key(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value)
    folded = "".join(char for char in folded if not unicodedata.combining(char))
    return NON_NAME_RE.sub(" ", folded.upper()).strip()


def normalize_name(
    last_raw: str,
    first_raw: str | None,
    middle_raw: str | None,
) -> NameParts:
    last = clean(last_raw) or ""
    first = clean(first_raw)
    middle = clean(middle_raw)
    suffix: str | None = None
    notes: list[str] = []

    for field_name, field_value in (
        ("last", last),
        ("first", first or ""),
        ("middle", middle or ""),
    ):
        match = SUFFIX_RE.search(field_value)
        if match:
            suffix = match.group(1).upper().replace(".", "")
            if suffix == "JR":
                suffix = "Jr."
            elif suffix == "SR":
                suffix = "Sr."
            if field_name == "last":
                last = SUFFIX_RE.sub("", last).strip(" ,")
            elif field_name == "first":
                first = SUFFIX_RE.sub("", first or "").strip(" ,") or None
            else:
                middle = SUFFIX_RE.sub("", middle or "").strip(" ,") or None
            notes.append(f"Suffix parsed from {field_name}-name column.")
            break

    ordered = [part for part in (first, middle, last, suffix) if part]
    display = " ".join(ordered) if ordered else last_raw
    normalized = name_key(display)
    variants = [f"{last_raw}, {' '.join(x for x in (first_raw, middle_raw) if x)}".strip()]
    variants = [value.rstrip(", ") for value in variants if value.rstrip(", ")]
    return NameParts(
        display_name=display,
        normalized_name=normalized,
        last_name=last,
        first_name=first,
        middle=middle,
        suffix=suffix,
        variants_json=json.dumps(sorted(set(variants)), ensure_ascii=False),
        notes=" ".join(notes) or None,
    )


def normalize_rank(value: str | None) -> str | None:
    value = clean(value)
    if value is None:
        return None
    normalized = value.upper().replace(".", "")
    normalized = SPACE_RE.sub(" ", normalized).strip()
    normalized = normalized.replace("1STLT", "1ST LT").replace("2NDLT", "2ND LT")
    return normalized


def normalize_serial(value: str | None) -> str | None:
    value = clean(value)
    if value is None:
        return None
    normalized = SERIAL_RE.sub("", value.upper())
    return normalized or None


def classify_personnel(rank_raw: str | None, notes_raw: str | None) -> PersonnelClassification:
    rank = normalize_rank(rank_raw)
    notes = clean(notes_raw) or ""
    foreign = bool(FOREIGN_NOTE_RE.search(notes)) if notes else None
    note: str | None = None
    naval_rank = rank
    if rank:
        for suffix in (" USNR", " USN"):
            if rank.endswith(suffix):
                naval_rank = rank[: -len(suffix)].strip()
                break
    if notes.upper().startswith("COAST G"):
        if rank in ARMY_OFFICER_RANKS or rank in NAVAL_OFFICER_RANKS:
            return PersonnelClassification(
                rank, "commissioned_coast_guard_officer", True, False,
                "Coast Guard branch is based on the printed notes field."
            )
        if rank in ARMY_ENLISTED_RANKS or (
            rank and rank.startswith(NAVAL_ENLISTED_PREFIXES)
        ):
            return PersonnelClassification(
                rank, "enlisted_coast_guard_personnel", False, False,
                "Coast Guard branch is based on the printed notes field."
            )
    if foreign and rank:
        return PersonnelClassification(
            rank, "foreign_or_allied_military_personnel", None, True,
            "Foreign or Allied classification is based on the printed notes field."
        )
    if naval_rank != rank and naval_rank in NAVAL_OFFICER_RANKS.union({"LT"}):
        return PersonnelClassification(
            rank,
            "commissioned_naval_officer",
            True,
            foreign,
            "Naval branch is based on the printed USN or USNR rank suffix.",
        )
    if rank in ARMY_OFFICER_RANKS:
        return PersonnelClassification(rank, "commissioned_army_officer", True, foreign)
    if rank in NAVAL_OFFICER_RANKS:
        return PersonnelClassification(rank, "commissioned_naval_officer", True, foreign)
    if rank in WARRANT_RANKS:
        return PersonnelClassification(rank, "warrant_officer", False, foreign)
    if rank in ARMY_ENLISTED_RANKS:
        return PersonnelClassification(rank, "enlisted_army_personnel", False, foreign)
    if rank and rank.startswith(NAVAL_ENLISTED_PREFIXES):
        return PersonnelClassification(rank, "enlisted_naval_personnel", False, foreign)
    if rank and CIVILIAN_GRADE_RE.match(rank):
        return PersonnelClassification(
            rank, "civilian_professional_or_administrative_grade", False, foreign
        )
    if rank and TEMPORARY_GRADE_RE.match(rank):
        return PersonnelClassification(
            rank, "temporary_contract_or_special_personnel", False, foreign
        )
    if rank:
        note = "Printed rank or grade is preserved but not classified by the current rule set."
    return PersonnelClassification(
        rank, "unknown_or_indeterminate", None, foreign, note
    )
