import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page462-ivan-m-tchok-to-harry-m-templeton-review_batch-944_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["51bec465-c44d-5d74-b1d8-0b4fe2308f7e", "Ivan M Tchok"],
  ["ae99d4da-c423-5ce2-a09a-764c1a4d4dcd", "John Teague"],
  ["7322ca21-e1d6-5ca4-9142-8d1755af7ff7", "Clyde V Teasdale"],
  ["9a531f65-6e90-5bd1-b882-b43b45f6b9e6", "Leo Teboul"],
  ["8754b271-e59d-5411-ab7d-3584f0aa445c", "William J Techtmann"],
  ["6ec02784-6748-5597-bbad-a9135fd3b5c3", "Pete Tedeschi"],
  ["8aeb5ab3-cd07-51d1-90a4-0da6cea7597d", "William S Teeter"],
  ["d8f9765d-97f8-53ec-b3cf-180fcba62cf9", "Mary E Teichgraeber"],
  ["fb7f264c-9871-52d7-9c66-07428e4bd1e3", "Kate Teichner"],
  ["3d0678d9-f91e-5283-a68c-9ab560d7a8f4", "Gudrun I Teigen"],
  ["bbcb261e-2496-5956-8fe8-6ec811e96fe3", "Darwin L Teilhet"],
  ["94a92f6d-33ad-5793-82c6-5d3544f9d8a8", "Ina Telberg"],
  ["e8dfe679-56fe-5269-af7e-4e6e84481a6e", "Anastos Telemachus"],
  ["d7be1805-264b-5e86-9d34-d50717002b7f", "Ruby D Telesca"],
  ["2e4a2945-99fb-5abc-aaf5-781d85c3cf1c", "Aram H Tellalian"],
  ["3b8081c4-27ff-5382-b29e-5bf69bbd63e8", "Clarence R Teller"],
  ["b50fd8ff-b5d6-5ecf-bbca-e0fa69bf9bd6", "Rennie L Tellia"],
  ["685f819e-75d4-5aee-a4a2-65ca0b42b999", "Dominic L Telloni"],
  ["f3300ed3-b2fa-5d76-a9cc-e5441bb52d92", "Joseph G Temolo"],
  ["1edf6ee4-65f8-5e18-b87d-11d086ddaf85", "Fay W Temple"],
  ["d391a6b2-3902-57ba-a702-a5c8a8ae87cc", "George H Temple"],
  ["b2d1f2ba-8862-5b16-b620-3ffbbd9c67d6", "Lucille E Temple"],
  ["76095811-68ca-55e1-b76d-074dbd95b7b5", "Harry M Templeton"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 944 publishes all 23 indexed-row entities with terminal reviewed outcomes", async ({ page }) => {
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

test("Ivan Tchok publishes sourced prewar roles without claiming immediacy", async ({ request, page }) => {
  const person = (await peopleShard(request, "i")).find(
    (item: { person_id: string }) => item.person_id === "51bec465-c44d-5d74-b1d8-0b4fe2308f7e",
  );
  expect(person.identity_status).toBe("high_confidence");
  expect(person.name_variants).toContain("Ivan Marija Čok");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(2);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Self-employed legal practice",
    relationship_type: "self_employment",
    occupation: "attorney",
    claim_confidence: "high",
  });
  await page.goto("./people/51bec465-c44d-5d74-b1d8-0b4fe2308f7e/");
  await expect(page.locator("main")).toContainText("Ivan Marija Čok");
  await expect(page.locator("main")).toContainText("attorney in private practice");
});

test("Darwin Teilhet publishes Stanford teaching only as documented prewar employment", async ({ request }) => {
  const person = (await peopleShard(request, "d")).find(
    (item: { person_id: string }) => item.person_id === "bbcb261e-2496-5956-8fe8-6ec811e96fe3",
  );
  expect(person.identity_status).toBe("high_confidence");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Stanford University",
    relationship_type: "employment",
    start_date: "1941",
    end_date: "1942",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  });
});

test("Ina Telberg preserves the gap between Ohio State and OSS service", async ({ request, page }) => {
  const person = (await peopleShard(request, "i")).find(
    (item: { person_id: string }) => item.person_id === "94a92f6d-33ad-5793-82c6-5d3544f9d8a8",
  );
  expect(person.identity_status).toBe("high_confidence");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "The Ohio State University",
    relationship_type: "employment",
    temporal_basis: "documented_prewar",
    claim_confidence: "high",
  });
  await page.goto("./people/94a92f6d-33ad-5793-82c6-5d3544f9d8a8/");
  await expect(page.locator("main")).toContainText("served with OSS in Washington and India");
  await expect(page.locator("main")).toContainText("graduate assistant");
});

test("reviewed Army categories remain unnamed and qualified", async ({ request }) => {
  const clyde = (await peopleShard(request, "c")).find(
    (item: { person_id: string }) => item.person_id === "7322ca21-e1d6-5ca4-9142-8d1755af7ff7",
  );
  expect(clyde.personnel_category).toBe("enlisted_army_personnel");
  expect(clyde.commissioned_officer).toBe(false);
  expect(clyde.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    organization_name_as_found: null,
    occupation: "general farmer",
    relationship_type: "employment",
    claim_confidence: "medium",
  });
  expect(clyde.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(clyde.last_civilian_pre_service).toHaveLength(0);

  const george = (await peopleShard(request, "g")).find(
    (item: { person_id: string }) => item.person_id === "d391a6b2-3902-57ba-a702-a5c8a8ae87cc",
  );
  expect(george.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    organization_name_as_found: null,
    occupation: "student",
    relationship_type: "student",
    claim_confidence: "medium",
  });
  expect(george.last_civilian_pre_service).toHaveLength(0);
});

test("William Techtmann exposes the name conflict without transferring Army fields", async ({ request, page }) => {
  const person = (await peopleShard(request, "w")).find(
    (item: { person_id: string }) => item.person_id === "8754b271-e59d-5411-ab7d-3584f0aa445c",
  );
  expect(person.identity_status).toBe("conflicting");
  expect(person.research_status).toBe("conflicting_sources");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims.some((item: { claim_confidence: string }) => item.claim_confidence === "conflicting")).toBeTruthy();
  await page.goto("./people/8754b271-e59d-5411-ab7d-3584f0aa445c/");
  await expect(page.locator("main")).toContainText("Robert J. Mertes");
  await expect(page.locator("main")).toContainText("no Army field is transferred");
});

test("plausible namesakes remain review leads rather than biographies", async ({ request }) => {
  const people = await peopleShard(request, "l");
  const leo = people.find(
    (item: { person_id: string }) => item.person_id === "9a531f65-6e90-5bd1-b882-b43b45f6b9e6",
  );
  expect(leo.identity_status).toBe("ambiguous");
  expect(leo.research_status).toBe("needs_identity_review");
  expect(leo.other_pre_oss_affiliations).toHaveLength(0);
  expect(leo.claims).toHaveLength(0);

  const anastos = (await peopleShard(request, "a")).find(
    (item: { person_id: string }) => item.person_id === "e8dfe679-56fe-5269-af7e-4e6e84481a6e",
  );
  expect(anastos.identity_status).toBe("ambiguous");
  expect(anastos.other_pre_oss_affiliations).toHaveLength(0);
});

test("Kate Teichner's printed number is preserved privately without reinterpretation", async ({ request, page }) => {
  const person = (await peopleShard(request, "k")).find(
    (item: { person_id: string }) => item.person_id === "fb7f264c-9871-52d7-9c66-07428e4bd1e3",
  );
  expect(person.identity_status).toBe("unresolved");
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto("./people/fb7f264c-9871-52d7-9c66-07428e4bd1e3/");
  await expect(page.locator("main")).toContainText("ineligible for the Army merged-file matcher");
  await expect(page.locator("main")).not.toContainText(/\b\d{6}\b/);
});

test("Batch 944 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Stanford University");
});

test("Batch 944 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 944 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 641,
    research_attempted_people: 14_653,
    verified_affiliation_people: 1_042,
    verified_employer_people: 469,
    archival_review_assessed_people: 13_127,
    published_claims: 9_080,
    public_sources: 5_977,
  });
});
