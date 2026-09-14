import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const organizations = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["0692c9cf-1da3-563d-a770-e02009a24993", "Richard T Culp", "3e2d91af-5a5a-5129-9c21-badcbc7b7895", 100, "158", true],
  ["c467f545-d6f7-57d3-8364-b77a8d596cab", "William C Culp", "be37cad1-2ec8-5bc0-bf0d-6bb15c0ee222", 100, "158", false],
  ["139c1b9e-ce49-5fd4-9866-bbb91ac5f56f", "David J Culver", "ff8c9fb6-2e00-58d4-810c-08cfb4717303", 100, "158", false],
  ["d021843b-e1c8-5db3-ad4b-520b98412e2f", "Lester E Culverson", "687183ab-2a94-591f-8a42-f6c61430f01d", 100, "158", true],
  ["0176cbfb-b3b9-5a6c-b3bc-2b2f44935efd", "Tom S Culverwell", "21ec8554-fe4b-5276-b8f7-36b2cf7a592f", 100, "159", true],
  ["a4523911-114b-5b29-ae5b-c3461fe9b313", "Maynard L Cumbers", "b5efef16-c6ce-562c-95f9-bfd3806b3422", 100, "159", true],
  ["59cde9ee-1465-5b6a-a804-519a5fd2e759", "William J Cummens", "84194ee7-fe5a-5bba-80f0-80f79fa40425", 100, "159", true],
  ["01806674-fc26-5cff-bae6-1f9d06c106f7", "Louise D Cumming", "7f75b574-a2c2-56ef-9bdf-c295192acd2b", 101, "159", false],
  ["9f273439-0924-5ddf-86ab-abd95e047641", "Josephine C Cummings", "3db9f92f-413f-5ba7-adbc-db0ebdea09ce", 101, "159", false],
  ["a376bfae-80ec-55e2-bb04-4a4cf143eba3", "Philip H Cummings", "075db828-b0cc-56e3-8010-3fc55b99f07c", 101, "159", false],
] as const;

test("Batch 506 preserves the audited page 100-101 sequence and masks every private identifier", () => {
  for (const [id, name, sourceRecordId, page, box, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box,
      archive_location: "230/86/29/04",
      pdf_page: page,
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

test("Batch 506 confirms Culverwell without turning enlisted service into officer status", () => {
  const culverwell = profile("0176cbfb-b3b9-5a6c-b3bc-2b2f44935efd");
  expect(culverwell).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(culverwell.name_variants).toEqual(
    expect.arrayContaining(["Tom S. Culverwell", "Thomas Speiden Culverwell"]),
  );
  expect(culverwell.claims.some((claim: { claim_text: string }) =>
    claim.claim_text.includes("wartime OSS map specialist"),
  )).toBe(true);
});

test("Batch 506 separates Culverwell's military pathway from his last civilian employer", () => {
  const culverwell = profile("0176cbfb-b3b9-5a6c-b3bc-2b2f44935efd");
  expect(culverwell.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  );
  expect(culverwell.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Forest Service",
      relationship_type: "employment",
      end_date: "1942",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(culverwell.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Commercial artist",
      relationship_type: "unknown",
    }),
  );
});

test("Batch 506 preserves the Washington Daily News as a non-employer relationship", () => {
  const culverwell = profile("0176cbfb-b3b9-5a6c-b3bc-2b2f44935efd");
  expect(culverwell.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Washington Daily News",
      role_title: "Supplier of illustrations, comics and political cartoons",
      relationship_type: "unknown",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );
  const forestService = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "United States Forest Service",
  );
  expect(forestService).toMatchObject({ documented_person_count: 1 });
});

test("Batch 506 retains five ambiguous identities without public affiliations", () => {
  const ambiguousIds = [
    "0692c9cf-1da3-563d-a770-e02009a24993",
    "c467f545-d6f7-57d3-8364-b77a8d596cab",
    "139c1b9e-ce49-5fd4-9866-bbb91ac5f56f",
    "d021843b-e1c8-5db3-ad4b-520b98412e2f",
    "a376bfae-80ec-55e2-bb04-4a4cf143eba3",
  ];
  for (const id of ambiguousIds) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      commissioned_officer: null,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 506 leaves four unresolved identities with explicit archival guidance", () => {
  const unresolvedIds = [
    "a4523911-114b-5b29-ae5b-c3461fe9b313",
    "59cde9ee-1465-5b6a-a804-519a5fd2e759",
    "01806674-fc26-5cff-bae6-1f9d06c106f7",
    "9f273439-0924-5ddf-86ab-abd95e047641",
  ];
  for (const id of unresolvedIds) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
    expect(profile(id).next_action).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 506 exact coverage and direct routes expose evidence and uncertainty", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4828);
  expect(stats.verified_affiliation_people).toBe(550);
  expect(stats.verified_employer_people).toBe(245);
  expect(stats.archival_review_assessed_people).toBe(4783);

  await page.goto("./people/0176cbfb-b3b9-5a6c-b3bc-2b2f44935efd/");
  await expect(page.getByRole("heading", { name: "Tom S Culverwell", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Forest Service");
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("Thomas Speiden Culverwell");
  await expect(page.locator("main")).toContainText("probable immediate");
  await expect(page.locator("main")).toContainText("The Mapping of Our National Forests");

  await page.goto("./people/c467f545-d6f7-57d3-8364-b77a8d596cab/");
  await expect(page.getByRole("heading", { name: "William C Culp", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Box 158");

  const forestService = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "United States Forest Service",
  );
  await page.goto(`./organizations/${forestService.organization_id}/`);
  await expect(page.getByRole("heading", { name: "United States Forest Service", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Tom S Culverwell");
});
