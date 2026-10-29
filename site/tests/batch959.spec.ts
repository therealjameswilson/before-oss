import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page470-w-c-toland-to-peter-tomkins-review_batch-959_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c58403db-1d62-5336-a154-ea8d9c28689d", "W C Toland"],
  ["e8456428-18ec-5aa9-9bf2-9d749d5c1063", "Milo Tole"],
  ["ca6487a4-12a3-5b1f-a0db-038bb0fc7aa5", "Ralph R Toledano"],
  ["40c99330-ef90-5354-a820-026560900759", "Albert C Tolie"],
  ["94a2076f-98e1-5098-86e2-157572829d1b", "Joseph E Toliver"],
  ["c4980e40-681d-5c27-a3e9-797e0020f656", "John H Tolleson"],
  ["a524f863-6c5b-53f8-8bc9-3f5bbf4cdf2d", "Edward C Tolman"],
  ["e194d51a-76b6-56f4-b1cf-d287ee858c67", "Lee P Tolman"],
  ["e5593179-d5cd-512b-b341-2ffe1c840824", "Ruth Tolman"],
  ["4962e3ae-1ef2-5276-9605-19ba6a591a68", "Georgia F Tolson"],
  ["30b4e838-5ad9-5f09-b0c0-d34e717cfb0d", "Ilia A Tolstoy"],
  ["4378440e-32f6-523a-b2e9-5fa905a9c9ab", "L L Toman"],
  ["5b7b3a01-151c-5d7a-b020-5fd4aadcc9f0", "Magdeleno G Tomaneng"],
  ["a79b6d3d-3e1e-5aad-b2b4-b86f8f9e613b", "Nicholas J Tomasello"],
  ["210958be-6601-544e-ba50-38daf0946a43", "Adolph L Tomaseski"],
  ["0c4c6599-0859-50b7-9a6a-560131be7e4f", "James Tomasi"],
  ["0a14d941-2388-5b87-8fbf-ca55e5a32bb6", "Helen K Tomb"],
  ["0357b9d8-373a-5ac9-923f-a6dcb5272d8d", "Frank F Tomei"],
  ["32b65c01-de44-579b-83bb-27513f036029", "Edwin Tominack"],
  ["c4a88525-9899-5cf0-8439-2865d96376ef", "Paul Y Tomita"],
  ["7ab094da-086d-5920-9056-cf56ec22a061", "Theodore Tomita"],
  ["bf5306e2-3bf6-519e-a6eb-3557ddee1066", "Harold A Tomkins"],
  ["09a923e0-4bb5-52f6-8ed7-ca5086b6301f", "Peter Tomkins"],
] as const;

const unresolvedIds = new Set([
  "c58403db-1d62-5336-a154-ea8d9c28689d",
  "40c99330-ef90-5354-a820-026560900759",
  "94a2076f-98e1-5098-86e2-157572829d1b",
  "e194d51a-76b6-56f4-b1cf-d287ee858c67",
  "4962e3ae-1ef2-5276-9605-19ba6a591a68",
  "4378440e-32f6-523a-b2e9-5fa905a9c9ab",
  "5b7b3a01-151c-5d7a-b020-5fd4aadcc9f0",
  "0a14d941-2388-5b87-8fbf-ca55e5a32bb6",
  "bf5306e2-3bf6-519e-a6eb-3557ddee1066",
]);

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 959 publishes 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("five verified employer profiles preserve civilian and immediate pathways", async ({ request }) => {
  const cases = [
    ["ca6487a4-12a3-5b1f-a0db-038bb0fc7aa5", "Ralph R Toledano", "The New Leader"],
    ["a524f863-6c5b-53f8-8bc9-3f5bbf4cdf2d", "Edward C Tolman", "University of California, Berkeley"],
    ["30b4e838-5ad9-5f09-b0c0-d34e717cfb0d", "Ilia A Tolstoy", "Marine Studios"],
    ["32b65c01-de44-579b-83bb-27513f036029", "Edwin Tominack", "Cadillac Motor Car Division"],
    ["c4a88525-9899-5cf0-8439-2865d96376ef", "Paul Y Tomita", "West Coast Printing Company"],
  ] as const;
  for (const [id, name, organization] of cases) {
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("verified_employer_found");
    expect(person.last_civilian_pre_service).toEqual([
      expect.objectContaining({ canonical_organization: organization }),
    ]);
  }
  const ralph = await publicPerson(request, cases[0][0], cases[0][1]);
  expect(ralph.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
});

test("coerced confinement, government service and civilian employment remain distinct", async ({ request }) => {
  const paul = await publicPerson(request, "c4a88525-9899-5cf0-8439-2865d96376ef", "Paul Y Tomita");
  expect(paul.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Minidoka War Relocation Center",
      relationship_type: "unknown",
      immediate_pre_oss: true,
      last_civilian_pre_service: false,
    }),
  ]);
  expect(paul.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "West Coast Printing Company",
      relationship_type: "self_employment",
    }),
  ]);
  const ruth = await publicPerson(request, "e5593179-d5cd-512b-b341-2ffe1c840824", "Ruth Tolman");
  expect(ruth.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Office of War Information",
      relationship_type: "government_assignment",
      claim_confidence: "medium",
    }),
  ]);
  expect(ruth.last_civilian_pre_service).toHaveLength(0);
});

test("Army categories publish as occupations without inventing employers", async ({ request }) => {
  for (const [id, name, occupation] of [
    ["e8456428-18ec-5aa9-9bf2-9d749d5c1063", "Milo Tole", "Tailors and tailoresses"],
    ["a79b6d3d-3e1e-5aad-b2b4-b86f8f9e613b", "Nicholas J Tomasello", "Furniture manufacturing occupations, n.e.c."],
    ["210958be-6601-544e-ba50-38daf0946a43", "Adolph L Tomaseski", "Mechanics and repairmen, motor vehicle"],
    ["0c4c6599-0859-50b7-9a6a-560131be7e4f", "James Tomasi", "Stock clerks"],
    ["0357b9d8-373a-5ac9-923f-a6dcb5272d8d", "Frank F Tomei", "Stenographers and typists"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({ canonical_organization: null, occupation }),
    ]);
  }
});

test("Theodore Tomita remains conflicting and Peter Tomkins remains qualified", async ({ request, page }) => {
  const theodore = await publicPerson(request, "7ab094da-086d-5920-9056-cf56ec22a061", "Theodore Tomita");
  expect(theodore).toMatchObject({ identity_status: "ambiguous", research_status: "conflicting_sources" });
  expect(theodore.claims).toHaveLength(0);
  expect(theodore.last_civilian_pre_service).toHaveLength(0);
  const peter = await publicPerson(request, "09a923e0-4bb5-52f6-8ed7-ca5086b6301f", "Peter Tomkins");
  expect(peter).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(peter.name_variants).toContain("Peter Tompkins");
  expect(peter.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "National Broadcasting Company", claim_confidence: "medium" }),
  ]);
  await page.goto("./people/09a923e0-4bb5-52f6-8ed7-ca5086b6301f/");
  await expect(page.locator("main")).toContainText("probable");
});

test("nine unresolved people keep archival outcomes without transferred facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 959 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 959 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 652,
    research_attempted_people: 14_995,
    verified_affiliation_people: 1_076,
    verified_employer_people: 484,
    archival_review_assessed_people: 13_471,
    published_claims: 9_375,
    public_sources: 6_119,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Cadillac Motor Car Division");
});
