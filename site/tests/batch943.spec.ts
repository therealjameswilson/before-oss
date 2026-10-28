import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page462-john-f-taylor-to-francis-m-tchitcherine-review_batch-943_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["f45e1881-7443-544c-a6d2-61ae21a9fcb5", "John F Taylor"],
  ["533a164e-8c23-5183-af61-1b542b8be527", "John G Taylor"],
  ["d750f344-9f0b-50a4-9260-8eeb12ffc64b", "John G Taylor"],
  ["a9f8d91f-2069-5e3c-82ed-b266ab54eaf8", "John H Taylor"],
  ["4b6e0700-4a21-5dc0-90b4-97967938e904", "John C Taylor"],
  ["659e745e-754d-59db-a8cb-1d3e1d5a8d0b", "Joseph O Taylor"],
  ["249a43c1-086c-5c0f-995f-aa29391cb4e0", "Kathleen Taylor"],
  ["b4d879fd-dfdb-5f98-b62c-9957787b631f", "Leonard P Taylor"],
  ["89e6570c-e0e9-537e-b537-ec1551970c79", "Lily R Taylor"],
  ["c61380d6-bfbb-5863-ad3e-69cc4486db70", "Louis L Taylor"],
  ["333ae34d-97a1-592e-bddd-36de0c6602b5", "Norma J Taylor"],
  ["8f23d067-f742-541c-a4f0-a647430198c6", "Parks T Taylor"],
  ["4ca0144a-5859-5df2-ac19-df87c9d76a55", "Phillip W Taylor"],
  ["9dd1d344-9994-5ea4-b22e-af95a2a41ef4", "Prentiss T Taylor"],
  ["e21e7798-ab38-54ca-a7b2-e07133fdf4cc", "Rawleigh W Taylor"],
  ["3778e767-0ebf-528d-ac11-03fb71134621", "Robert L Taylor"],
  ["3910749d-7a9e-53a9-b624-64b46bcf4bac", "Robert W Taylor"],
  ["dda141ab-cf75-57bb-9452-c63e5895db8e", "Roy L Taylor"],
  ["0f550df6-3515-5c5e-834c-93fcaea5ddd3", "Thomas R Taylor"],
  ["6390416d-1aa7-5a26-88a4-bc41ebf62699", "Vernon E Taylor"],
  ["8157c091-5fcf-571b-aa0c-da0e00d3c274", "Walter Taylor"],
  ["b3a97353-9e07-5c12-a7dd-dfec882ae56a", "William W Taylor"],
  ["a93e6139-511f-5b46-bf56-77cd1bb3c73b", "Francis M Tchitcherine"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 943 publishes all 23 indexed-row entities with reviewed outcomes", async ({ page }) => {
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

test("dated Army occupation categories remain unnamed and qualified", async ({ request }) => {
  const people = await peopleShard(request, "j");
  const john = people.find((item: { person_id: string }) => item.person_id === "f45e1881-7443-544c-a6d2-61ae21a9fcb5");
  expect(john.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    organization_name_as_found: null,
    occupation: "shipping and receiving clerk",
    relationship_type: "employment",
    claim_confidence: "medium",
  });
  expect(john.last_civilian_pre_service).toHaveLength(0);
  expect(john.immediate_pre_oss_affiliations).toHaveLength(0);
});

test("Leonard Taylor preserves the Lenord spelling variant without interpreting code 999", async ({ request, page }) => {
  const person = (await peopleShard(request, "l")).find((item: { person_id: string }) => item.person_id === "b4d879fd-dfdb-5f98-b62c-9957787b631f");
  expect(person.identity_status).toBe("high_confidence");
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto("./people/b4d879fd-dfdb-5f98-b62c-9957787b631f/");
  const main = page.locator("main");
  await expect(main).toContainText("Lenord");
  await expect(main).toContainText("code 999 is undefined");
});

test("Rawleigh Taylor publishes student status without turning it into employment", async ({ request, page }) => {
  const person = (await peopleShard(request, "r")).find((item: { person_id: string }) => item.person_id === "e21e7798-ab38-54ca-a7b2-e07133fdf4cc");
  expect(person.commissioned_officer).toBe(true);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Woodberry Forest School",
    relationship_type: "student",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto("./people/e21e7798-ab38-54ca-a7b2-e07133fdf4cc/");
  await expect(page.locator("main")).toContainText("Mission Roanoke");
  await expect(page.locator("main")).toContainText("class of 1938");
});

test("Francis Tchitcherine has an official OSS identity but no invented predecessor", async ({ request, page }) => {
  const person = (await peopleShard(request, "f")).find((item: { person_id: string }) => item.person_id === "a93e6139-511f-5b46-bf56-77cd1bb3c73b");
  expect(person.identity_status).toBe("high_confidence");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims.some((item: { claim_text: string }) => item.claim_text.includes("CD Branch administrator"))).toBeTruthy();
  await page.goto("./people/a93e6139-511f-5b46-bf56-77cd1bb3c73b/");
  const main = page.locator("main");
  await expect(main).toContainText("Censorship Division");
  await expect(main).toContainText("redirected to maintenance");
});

test("adjacent John G Taylor rows remain separate possible duplicates", async ({ request }) => {
  const people = await peopleShard(request, "j");
  const groups = [];
  for (const id of ["533a164e-8c23-5183-af61-1b542b8be527", "d750f344-9f0b-50a4-9260-8eeb12ffc64b"]) {
    const person = people.find((item: { person_id: string }) => item.person_id === id);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.possible_duplicate_group).toBeTruthy();
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    groups.push(person.possible_duplicate_group);
  }
  expect(new Set(groups).size).toBe(1);
});

test("Thomas Taylor preserves the R versus W middle-initial conflict", async ({ request, page }) => {
  const person = (await peopleShard(request, "t")).find((item: { person_id: string }) => item.person_id === "0f550df6-3515-5c5e-834c-93fcaea5ddd3");
  expect(person.identity_status).toBe("conflicting");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims.some((item: { claim_confidence: string }) => item.claim_confidence === "conflicting")).toBeTruthy();
  await page.goto("./people/0f550df6-3515-5c5e-834c-93fcaea5ddd3/");
  await expect(page.locator("main")).toContainText("Thomas W. Taylor");
  await expect(page.locator("main")).toContainText("middle initials conflict");
});

test("Prentiss Taylor remains ambiguous instead of borrowing the artist biography", async ({ request, page }) => {
  const person = (await peopleShard(request, "p")).find((item: { person_id: string }) => item.person_id === "9dd1d344-9994-5ea4-b22e-af95a2a41ef4");
  expect(person.identity_status).toBe("ambiguous");
  expect(person.research_status).toBe("needs_identity_review");
  expect(person.claims).toHaveLength(0);
  await page.goto("./people/9dd1d344-9994-5ea4-b22e-af95a2a41ef4/");
  await expect(page.locator("main")).toContainText("needs identity review");
  await expect(page.locator("main")).not.toContainText("Smithsonian American Art Museum");
});

test("Batch 943 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Woodberry Forest School");
});

test("Batch 943 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 943 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 641,
    research_attempted_people: 14_631,
    verified_affiliation_people: 1_039,
    verified_employer_people: 466,
    archival_review_assessed_people: 13_105,
    published_claims: 9_060,
    public_sources: 5_968,
  });
});
