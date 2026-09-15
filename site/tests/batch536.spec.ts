import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page-one-hundred-and-seven-emiscah-davis-through-howard-davis-pathways_batch-536_2026-09-15.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["ac89e00d-bd19-55d7-9342-24a122f2dcdb", "Emiscah Davis", "a8d00562-2247-592d-9e13-d287fc74d96a", false],
  ["476d9a5d-e132-5b78-8336-a46a9a4950a2", "Eugene M Davis", "c1244923-ac6e-559e-9a0a-3cb921081eb0", true],
  ["7fb64342-8abf-5f75-8668-b6266abb5960", "Eugenia C Davis", "3b559076-947f-5c44-b9b4-d3822fe39106", false],
  ["6463307a-2601-5028-b44c-6ec4210b318a", "Farrell J Davis", "ce1aa599-873d-51da-868d-6e488e3ab1db", false],
  ["e11a8ba2-cb1b-5800-b728-791675e191e0", "Foster E Davis", "773c5119-25dd-5476-b724-5590939f6d95", false],
  ["8891eafe-66e5-575e-aa07-d4e696da7ed7", "Fred C Davis", "b9910bb2-683f-5dbd-b93b-b458b3321fff", true],
  ["20fb2c0f-8822-5fe7-b16b-7eab8fdb989f", "Gerald W Davis", "ee106dd8-7b69-5769-9567-39e6dfa4dc59", false],
  ["444d0582-9c7f-581a-b238-8b9bcd606db7", "Grover C Davis", "74712ff7-5f61-56ec-9e5e-ef62a57b8130", false],
  ["f85dd22c-2d96-5e89-8647-6e16e659f3bc", "Horace B Davis", "370860bd-d161-5bd5-a876-82598673a73a", true],
  ["b177d735-c33c-5d00-95ff-f00fc4d186d6", "Howard Davis", "cab45e7c-f0fd-51df-b369-0a0fa7439275", true],
] as const;

test("Batch 536 preserves ten page 107 rows and masks four private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/06",
      box: "170",
      pdf_page: 107,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 536 confirms two Army identities and publishes occupation only", () => {
  const accepted = [
    ["8891eafe-66e5-575e-aa07-d4e696da7ed7", "1943-06-09"],
    ["b177d735-c33c-5d00-95ff-f00fc4d186d6", "1941-03-20"],
  ] as const;

  for (const [id, entryDate] of accepted) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      research_attempt_count: 6,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "high" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      role_title: "Cook, except private family",
      relationship_type: "unknown",
      end_date: entryDate,
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    });
    expect(person.claims).toHaveLength(2);
    const identityClaim = person.claims.find(
      (claim: { claim_type: string }) => claim.claim_type === "identity",
    );
    const occupationClaim = person.claims.find(
      (claim: { claim_type: string }) => claim.claim_type === "occupation",
    );
    expect(identityClaim).toMatchObject({
      claim_confidence: "confirmed",
      publication_status: "published",
    });
    expect(occupationClaim).toMatchObject({
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
    expect(identityClaim.sources).toHaveLength(2);
    expect(occupationClaim.sources).toHaveLength(2);
    expect(person.next_action).toContain("no employer");
  }
});

test("Batch 536 preserves Gerald W Davis's indexed Major classification without resolving him", () => {
  const person = profile("20fb2c0f-8822-5fe7-b16b-7eab8fdb989f");
  expect(person).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "no_reliable_result_after_protocol",
  });
  expect(person.source_records[0]).toMatchObject({ rank_as_indexed: "Maj" });
  expect(person.claims).toEqual([]);
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toEqual([]);
});

test("Batch 536 leaves eight identities unresolved and withholds unbridged biographical leads", () => {
  const unresolvedIds = cohort
    .map(([id]) => id)
    .filter(
      (id) =>
        id !== "8891eafe-66e5-575e-aa07-d4e696da7ed7" &&
        id !== "b177d735-c33c-5d00-95ff-f00fc4d186d6",
    );
  for (const id of unresolvedIds) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "no_reliable_result_after_protocol",
      research_attempt_count: 6,
    });
    expect(person.archival_file).toMatchObject({ review_priority: "critical" });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
    expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  }

  const horace = profile("f85dd22c-2d96-5e89-8647-6e16e659f3bc");
  expect(horace.identity_evidence).toContain("Horace Bancroft Davis");
  expect(JSON.stringify(horace)).not.toMatch(/Federated Press|Simmons professor|CIO News/);
});

test("Batch 536 advances attempted and archival coverage without inflating employer coverage", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 5128,
    research_attempt_percent: 21.4202,
    verified_affiliation_people: 569,
    verified_affiliation_percent: 2.3768,
    verified_employer_people: 253,
    verified_employer_percent: 1.0568,
    archival_review_assessed_people: 5083,
    archival_review_percent: 21.2322,
    public_sources: 3432,
    published_claims: 4030,
  });
  expect(stats.research_status_counts).toMatchObject({
    not_started: 18812,
    conflicting_sources: 97,
    no_reliable_result_after_protocol: 138,
    occupation_only_found: 944,
    documented_prewar_employer_found: 101,
    requires_archival_review: 3112,
  });
});

test("Batch 536 evidence is citation-linked, idempotent, and private-value free", () => {
  const bundle = JSON.parse(evidence);
  expect(bundle).toMatchObject({ bundle_version: "1.0" });
  expect(bundle.sources).toHaveLength(3);
  expect(bundle.organizations).toHaveLength(0);
  expect(bundle.affiliations).toHaveLength(2);
  expect(bundle.claims).toHaveLength(4);
  expect(bundle.claims.flatMap((claim: { sources: unknown[] }) => claim.sources)).toHaveLength(8);
  expect(bundle.person_updates).toHaveLength(10);
  expect(bundle.research_attempts).toHaveLength(10);
  expect(bundle.claims.filter((claim: { claim_type: string }) => claim.claim_type === "identity")).toHaveLength(2);
  expect(bundle.claims.filter((claim: { claim_type: string }) => claim.claim_type === "occupation")).toHaveLength(2);
  expect(evidence).toContain("2-26. Cooks, except private family");
  expect(evidence).toContain("Federated Press writer, Simmons professor, and CIO News managing editor");
  expect(evidence).not.toMatch(/serial_number|service_number/);
});

test.describe("Batch 536 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} ${id.slice(0, 8)} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box170");
      await expect(page.locator("body")).toContainText("Archival-review priority");
    });
  }
});
