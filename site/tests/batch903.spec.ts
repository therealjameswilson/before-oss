import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page441-spiro-to-sporborg-review_batch-903_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["11cec430-f1ae-54a7-a7f8-88bcf9e56e3f", "Grace M Spiro"],
  ["530dee8f-d811-52b3-9ce6-947fd8437f20", "Peter Spiro"],
  ["e320d8b6-f26d-571e-8c55-cf3d3a467fd6", "Boris Spiroff"],
  ["5bb9f08a-0dc5-5b05-bf5c-3501904dd704", "William J Spiropoulos"],
  ["444d1c7f-7f85-5878-b878-d132b50891b3", "Milton A Spitz"],
  ["196e731e-4de0-5486-a7a0-7b145ea2cba7", "Walter F Spitzform"],
  ["797c8fe4-dfef-5653-a86c-7a7f6691b0f1", "Leo X Spitzmiller"],
  ["9900da1b-432b-5534-8360-6cdd50145779", "Louis Spivack"],
  ["d4181030-6808-51e2-b300-b1b68df03c83", "Sydney S Spivack"],
  ["369d1bb2-2282-5067-a13b-bf14bb63c9c2", "Joel T Spivey"],
  ["a8fc7cbb-2157-578d-8c17-e61621c439c7", "Price C Spivey"],
  ["aa59166b-a63b-5de3-b1a8-67f72c9eae9a", "Robert D Splain"],
  ["013a1f06-583e-5f24-900b-332459b484db", "Chester J Splawski"],
  ["398dbd77-1516-521b-b9a9-10a0f179f94b", "William Spoeleof"],
  ["13f8243d-e6dc-521a-b442-65065c364571", "Evalea Spoesser"],
  ["0f562200-3554-5fdc-9dcd-7994d1b3a83f", "Carlton W Spohn"],
  ["e7e1f08f-2602-5c99-a721-fcc5cd0e439f", "John Spondike"],
  ["7e5fad17-c743-5fef-8091-40fa9dddc734", "Chester L Spooner"],
  ["38e803b7-7115-5fcc-a55c-7e49d04dfb43", "Henry N Sporborg"],
] as const;

test("Batch 903 publishes all 19 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 903 Army occupation bridges stay qualified", async ({ page }) => {
  const checks = [
    ["530dee8f-d811-52b3-9ce6-947fd8437f20", "mechanical treatment of metals"],
    ["5bb9f08a-0dc5-5b05-bf5c-3501904dd704", "Radio operators"],
    ["9900da1b-432b-5534-8360-6cdd50145779", "Retail managers"],
    ["369d1bb2-2282-5067-a13b-bf14bb63c9c2", "Bartenders"],
    ["013a1f06-583e-5f24-900b-332459b484db", "Chauffeurs and drivers"],
    ["e7e1f08f-2602-5c99-a721-fcc5cd0e439f", "Student; institution not recorded"],
  ] as const;

  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("qualified lead");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Boris Spiroff publishes the Army as an immediate military affiliation", async ({ page }) => {
  await page.goto("./people/e320d8b6-f26d-571e-8c55-cf3d3a467fd6/");
  const main = page.locator("main");
  await expect(main).toContainText("Boris Robert Spiroff");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "United States Army",
  );
  await expect(main).toContainText("1937");
  await expect(main).toContainText("1943");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Henry Sporborg remains an allied SOE liaison with qualified civilian employment", async ({ page }) => {
  await page.goto("./people/38e803b7-7115-5fcc-a55c-7e49d04dfb43/");
  const main = page.locator("main");
  await expect(main).toContainText("Henry Nathan Sporborg");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Special Operations Executive",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Slaughter and May",
  );
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("U.S. OSS employment");
});

test("the two Grace Spiro rows remain separate and jointly flagged", async ({ page }) => {
  for (const id of [
    "c5c624f4-500f-5e4c-96a2-703c98460a04",
    "11cec430-f1ae-54a7-a7f8-88bcf9e56e3f",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("identity review");
    await expect(main).toContainText("Grace M Spiro row");
    await expect(main).not.toContainText("same-name:grace-m-spiro-page441");
  }
});

test("Chester Spooner conflict withholds the Army occupation", async ({ page }) => {
  await page.goto("./people/7e5fad17-c743-5fef-8091-40fa9dddc734/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("materially different name Peter Messinger");
  await expect(main).not.toContainText("Semiskilled occupations in production of rubber goods");
  await expect(main).not.toContainText("identifier-conflict:chester-l-spooner-peter-messinger");
});

test("Batch 903 evidence and public projection exclude credential fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("same-name:grace-m-spiro-page441");
  expect(people).not.toContain("identifier-conflict:chester-l-spooner-peter-messinger");
});

test("Batch 903 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 607,
    research_attempted_people: 13_721,
    verified_affiliation_people: 985,
    verified_employer_people: 444,
    archival_review_assessed_people: 12_192,
    published_claims: 8_356,
    public_sources: 5_591,
  });
});
