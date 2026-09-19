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
    "../../research/evidence-page-one-hundred-and-fifteen-frank-j-desuta-through-richard-b-deufson_batch-574_2026-09-19.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["918c8146-4378-5171-b6a6-71f0a185c63a", "Frank J Desuta", "8e99426c-9467-564d-a791-6ffc2429dfa8", false],
  ["868897f3-0cca-51f9-8b95-a4a1f83ae8f4", "Lloyd A Dethlefson", "956708c6-2006-5a00-8849-fc326ff782c6", false],
  ["e955ac9f-4cf9-5a0e-b0ed-c78d88aea9e1", "Victor Detibertis", "fbd12a98-eb23-5a29-8c1e-e445c70069c8", true],
  ["33309601-43ca-5faa-8b49-1d9f51a41874", "Henry C Detmer", "9d2a5799-b1fa-5768-8fe6-95ef37289b7d", true],
  ["d3155b0e-fb0c-522c-b643-bd54d86b56bd", "Mary F Detmer", "9e6f89a7-549e-5efb-aff8-a3fb4524fd36", false],
  ["ddce3f23-b4cd-5104-819b-4380082f793f", "Louis M Detore", "c6adb2e8-b33c-5b78-99d3-d3063051ae78", true],
  ["466a5387-1fe3-5f5b-aad3-d732d6c0a520", "Alan W Detweiler", "6da89363-1006-51b5-b2d5-4e91d3a53d25", false],
  ["3e6f059d-c02e-53ee-b26a-bea085f4dc1c", "Albert Deuble", "f6bcb48e-98ef-530b-a4d6-12f73cde0b3d", false],
  ["a3ddbbc7-cd72-5a18-b315-10d558b89fd5", "Wallace R Deuel", "c22b1827-9d75-56c3-8e11-f01714dc8719", false],
  ["792b43b2-3fe0-5fd3-a4d9-a6eee4080296", "Richard B Deufson", "2b4ae3fc-29fb-5656-9897-863c310a5045", false],
] as const;

test("Batch 574 preserves ten distinct indexed rows and masks three private identifiers", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    const record = person.source_records.find(
      (row: { source_record_id: string }) => row.source_record_id === sourceRecordId,
    );
    expect(record).toMatchObject({
      pdf_page: 115,
      box: "183",
      archive_location: "230/86/30/01",
    });
    if (hasPrivateIdentifier) {
      expect(record.serial_masked).toMatch(/^•+\d{4}$/);
    } else {
      expect(record.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
  expect(evidence).not.toMatch(/"serial_number"|"serial_number_raw"|"serial_number_normalized"/);
});

test("Batch 574 separates Deuel's COI assignment, last civilian employer and earlier teaching", () => {
  const wallace = profile("a3ddbbc7-cd72-5a18-b315-10d558b89fd5");
  expect(wallace).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(wallace.name_variants).toContain("Wallace Rankin Deuel");
  expect(wallace.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Coordinator of Information",
      relationship_type: "government_assignment",
      start_date: "1941",
      end_date: "1942",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(wallace.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Chicago Daily News",
      relationship_type: "employment",
      start_date: "1929",
      end_date: "1941",
      immediate_pre_oss: false,
    }),
  ]);
  expect(wallace.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "American University of Beirut",
      organization_name_as_found: "American University, Beirut, Syria (now Lebanon)",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      start_date: "1926",
      end_date: "1929",
    }),
  ]);
  expect(wallace.claims.find((claim: { claim_type: string }) =>
    claim.claim_type === "immediate_pre_oss_affiliation",
  ).sources).toHaveLength(3);
  expect(wallace.claims.filter((claim: { claim_type: string }) =>
    claim.claim_type === "immediate_pre_oss_affiliation",
  )).toHaveLength(1);
  expect(JSON.stringify(wallace)).toContain("Coordinator of Information");
});

test("Batch 574 does not promote namesakes, postwar jobs or mismatched Army identifiers", () => {
  for (const [id] of cohort.filter(([id]) => id !== "a3ddbbc7-cd72-5a18-b315-10d558b89fd5")) {
    const person = profile(id);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
  const desota = profile("92bf4459-408e-5f1e-a69a-f5f05cf58f9b");
  const desuta = profile("918c8146-4378-5171-b6a6-71f0a185c63a");
  expect(desota.possible_duplicate_group).toBe(desuta.possible_duplicate_group);
  expect(desota.person_id).not.toBe(desuta.person_id);
});

test("Batch 574 exact aggregate counters remain reproducible", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 256,
    research_attempted_people: 5505,
    verified_affiliation_people: 597,
    verified_employer_people: 261,
    archival_review_assessed_people: 5460,
    public_sources: 3670,
    published_claims: 4504,
  });
});

test("Batch 574 direct person and employer pages render evidence and archival guidance", async ({ page }) => {
  await page.goto("people/a3ddbbc7-cd72-5a18-b315-10d558b89fd5/");
  await expect(page.getByRole("heading", { name: "Wallace R Deuel", exact: true })).toBeVisible();
  await expect(page.getByText("Chicago Daily News", { exact: true }).first()).toBeVisible();
  await expect(page.getByText(/Coordinator of Information/).first()).toBeVisible();

  await page.goto("organizations/ef8f9192-943e-5396-a904-62ba002b9beb/");
  await expect(page.getByRole("heading", { name: "Chicago Daily News", exact: true })).toBeVisible();
  await expect(page.getByText("Wallace R Deuel", { exact: true }).first()).toBeVisible();

  await page.goto("organizations/7717ee63-f94b-59b6-a06e-5b0f44350338/");
  await expect(page.getByRole("heading", { name: "Coordinator of Information", exact: true })).toBeVisible();
  await expect(page.getByText("Wallace R Deuel", { exact: true }).first()).toBeVisible();

  await page.goto("people/918c8146-4378-5171-b6a6-71f0a185c63a/");
  await expect(page.getByRole("heading", { name: "Frank J Desuta", exact: true })).toBeVisible();
  await expect(page.getByText(/No reliable pre-OSS employer has yet been identified/).first()).toBeVisible();
});
