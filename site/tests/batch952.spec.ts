import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page466-janet-f-thompson-to-theodore-j-thompson-review_batch-952_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["486640ca-c038-582b-b4df-dbd512dffb45", "Janet F Thompson"],
  ["1bc19839-6f39-5e04-b28f-72afa5fd5a3c", "Jewell B Thompson"],
  ["b12727ad-b305-5c2c-bd8a-9786837272b3", "John T Thompson"],
  ["90a9f102-232c-55fc-a275-ca7ca82c1b38", "John W Thompson"],
  ["3cfd83a9-5e1d-5920-98aa-cf7630fdddec", "Joseph E Thompson"],
  ["d7944d1c-7b93-5a35-98f2-8cb6737a1a96", "Lamont L Thompson"],
  ["a5c0ee99-b8e4-5f70-9074-d113e79440cb", "Laurence M Thompson"],
  ["9945b7ec-9ab9-56fc-a484-94becd5fbcd4", "LeeRoy Thompson"],
  ["0619c540-23cf-5697-87f7-fc058871e222", "Marion D Thompson"],
  ["5bbd054a-e820-5c74-880c-9d85235342a1", "Mary A Thompson"],
  ["2660465b-63d6-59c1-91d4-aca054d72759", "Mary E Thompson"],
  ["e3590a5f-1007-5f0a-b106-3cd81c58bd33", "Nancy Thompson"],
  ["5fba512f-eb22-5ebe-a53c-b0c4217cea38", "Opal P Thompson"],
  ["db62cb8f-a017-52ec-ab96-dff3b9f0b147", "Paul A Thompson"],
  ["a137be31-3157-5cfa-becf-f2423659260b", "Pauline A Thompson"],
  ["316ee217-052d-5203-9c80-8e70dbe46774", "Phyllis A Thompson"],
  ["227b24f6-fef9-5e1e-869b-bce9ca091e47", "Ralph Thompson"],
  ["b148c9ce-6792-5234-a0ee-31c9ab74c08d", "Raymond L Thompson"],
  ["6fb2c556-c7fa-554b-ae71-fb622729f5ab", "Robert E Thompson"],
  ["e2993cc7-b644-5a99-a169-2d65da695dbc", "Robert G Thompson"],
  ["1df0f65e-1f98-54cb-8ffc-bc9fc1f32bd7", "Robert J Thompson"],
  ["d3720510-804f-551f-a937-ca629f97c340", "Russell D Thompson"],
  ["80bf6dfc-a271-5271-9c32-efb46e068114", "Theodore J Thompson"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

async function publicPerson(
  request: APIRequestContext,
  id: string,
  displayName: string,
) {
  const shard = await peopleShard(request, displayName[0].toLowerCase());
  return shard.find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 952 publishes all 23 audited rows with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) {
      expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
    }
  }
});

test("Paul A Thompson publishes only a qualified machinist category", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "db62cb8f-a017-52ec-ab96-dff3b9f0b147",
    "Paul A Thompson",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "machinist",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto("./people/db62cb8f-a017-52ec-ab96-dff3b9f0b147/");
  const main = page.locator("main");
  await expect(main).toContainText("Machinists");
  await expect(main).toContainText("no employer or workplace is identified");
});

test("Nancy Thompson retains a qualified private lead without public facts", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "e3590a5f-1007-5f0a-b106-3cd81c58bd33",
    "Nancy Thompson",
  );
  expect(person).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.name_variants).toContain("Thompson, Nancy");
  expect(person.name_variants).not.toContain("Nancy Adams");
  expect(person.name_variants).not.toContain("Nancy Sweezy");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toHaveLength(0);
  await page.goto("./people/e3590a5f-1007-5f0a-b106-3cd81c58bd33/");
  const main = page.locator("main");
  await expect(main).toContainText("Review Box 775");
  await expect(main).toContainText("before merging the Nancy Sweezy candidate");
});

test("the remaining 21 people retain explicit archival-review outcomes", async ({ request }) => {
  const exceptions = new Set([
    "e3590a5f-1007-5f0a-b106-3cd81c58bd33",
    "db62cb8f-a017-52ec-ab96-dff3b9f0b147",
  ]);
  for (const [id, name] of profiles) {
    if (exceptions.has(id)) continue;
    expect(await publicPerson(request, id, name)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      personnel_category: "unknown_or_indeterminate",
    });
  }
});

test("Batch 952 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("withheld Nancy Thompson sources do not enter the public source register", async ({ request }) => {
  const response = await request.get("./data/sources.json");
  expect(response.ok()).toBeTruthy();
  const sources = await response.json();
  const urls = new Set(sources.map((source: { stable_url: string }) => source.stable_url));
  expect(urls.has("https://www.nytimes.com/2010/02/26/arts/design/26sweezy.html")).toBeFalsy();
  expect(urls.has("https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/af020001/af020001.pdf")).toBeFalsy();
  expect(urls.has("https://www.theguardian.com/p/2fj64")).toBeFalsy();
  expect(urls.has("https://catalog.archives.gov/id/1263923")).toBeTruthy();
});

test("Batch 952 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_835,
    verified_affiliation_people: 1_050,
    verified_employer_people: 471,
    archival_review_assessed_people: 13_311,
    published_claims: 9_205,
    public_sources: 6_036,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("United States Army");
});
