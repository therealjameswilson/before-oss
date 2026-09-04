# Occupation timing review

Review opened: 2026-09-04 UTC, during the final Batch 399 evidence audit.

An Army entry date establishes when an occupation was recorded. It does not,
without an independently established OSS chronology, satisfy this project's
`strongly_date_bounded` definition: a close sequence from the prior affiliation
to OSS with no known intervening affiliation.

Batch 399 corrects the four occupation-only affiliations of Andre B. Charise,
Ruben Charles, Morton L. Charleston, and Samuel S. Charlon to
`temporal_relation_uncertain`. Their dated Army-entry occupation evidence is
retained with medium confidence, and neither an employer nor an immediate
pre-OSS role is inferred. Joseph E. Charles's separately sourced Harvard-to-OSS
chronology and Charise's dated Broadway production affiliation are unchanged.

The profile presentation now uses a neutral heading and an explicit timing
notice when other affiliations include uncertain chronology. An occupation-only
record with one date is described as "Recorded at", not an asserted employment
end date; its source-specific date explanation is visible beside the date.

## Follow-up review queue

After those four corrections, the following reproducible triage query returns
468 older affiliations. This is a candidate set, not a finding that every one
is wrong, and not a completed historical review:

```sql
SELECT affiliation_id, person_id, pre_oss_temporal_basis
FROM affiliations
WHERE relationship_type = 'unknown'
  AND pre_oss_temporal_basis = 'strongly_date_bounded'
ORDER BY person_id, affiliation_id;
```

For each candidate, inspect its linked claims and dated source notes, check
whether OSS entry is independently established, and correct the reviewed
evidence bundle if necessary. Preserve the occupation evidence and separate
identity, claim, and temporal confidence. Do not alter all rows automatically
from a keyword match or infer that an Army entry must precede OSS entry.

This audit remains open. It does not increase research-attempt coverage, resolve
an identity, or count as a new completed personnel research protocol.

## Default aggregate inclusion correction

The final Batch 399 projection additionally excludes affiliations with uncertain
timing from default verified coverage and charts. The SQL and public-projection
rules now both require confirmed/high-confidence person and affiliation
identities and exclude people whose current research status is conflicting.
Missing assessments fail closed. Immediate-affiliation charts further exclude
`probable_immediate` relationships; their exact sequence remains qualified.

Nineteen already-published military affiliations have an explicitly uncertain
temporal relation to OSS. They remain visible on profiles, but removing them
from the aggregate removes eight people who had no other qualifying affiliation.
Excluding the current conflicting research status of Harry X. Boosel removes
one further person. Verified-affiliation coverage is therefore corrected from
494 to 485 people; verified-employer coverage remains 211 people. No historical
evidence was removed and no research status was advanced by this counting
correction.
