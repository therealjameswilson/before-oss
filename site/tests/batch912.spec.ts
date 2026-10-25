import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page446-steimack-to-steinhope-review_batch-912_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c6a7b342-9551-5eec-bab7-b95ae4981530", "Theodore Steimack"],
  ["77e95da9-071e-58f8-b5e2-f0218fb5d89e", "Albert S Stein"],
  ["4dce7c6c-557a-5b04-aef4-5c51d29cfd43", "Bernard Stein"],
  ["c6598120-2c01-5d17-a876-ece8081ea846", "Eleanor M Stein"],
  ["9c5efdc8-8458-5270-9aeb-ffdc7d20df81", "Jack A Stein"],
  ["864446d9-ba48-57af-bc44-e0c02c5cedee", "Kenneth W Stein"],
  ["255dd371-c020-5c58-97bc-e44dd2b96d93", "Maldwin Stein"],
  ["e16dba7c-16bf-5d05-a5c2-42fb83dc898c", "Morris I Stein"],
  ["a03e0a85-ed90-5c32-95ae-4f9eeac67d52", "Patricia A Stein"],
  ["2c67d0ee-c122-5434-96c7-9af43c5f5851", "Robert L Stein"],
  ["da2cb9ac-f157-5a0e-90ce-429701e02d73", "Sol W Stein"],
  ["4207d44f-23cb-50c9-a2af-23364fc27ea8", "Wilbur Stein"],
  ["261cc632-397a-5da6-ac09-a882f8083d4f", "Estelle H Steinacker"],
  ["04322751-2c25-5ebe-8db3-34ea6aec83a1", "Frederick E Steinbach"],
  ["d7b1da2b-2d3e-5f23-9df1-f045454bb82f", "Rudolph R Steinbeck"],
  ["823c8e93-d093-5e58-81d3-07824cf70242", "Arthur J Steinberg"],
  ["85a03501-8259-5429-af9f-b190d1c12023", "Howard O Steinberg"],
  ["8a130c89-6739-5907-94aa-51585f2357ca", "Saul Steinberg"],
  ["6b35c00e-1b60-5c6e-ad65-c75d75d1151d", "Ernest W Steinbrenner"],
  ["7ea3504a-e340-5d4e-ad4c-3fc9dd9452e2", "Alvin E Steiner"],
  ["0ebec71e-c319-51ee-988d-b9ce407517ff", "Francis B Steiner"],
  ["95f2e133-a840-560a-b645-e12240b78db7", "Stephen Steinhardt"],
  ["bf41eb6f-66b8-589c-be73-586322325bbe", "Edwards G Steinhope"],
] as const;

test("Batch 912 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Army occupation findings remain distinct from employers", async ({ page }) => {
  await page.goto("./people/c6a7b342-9551-5eec-bab7-b95ae4981530/");
  let main = page.locator("main");
  await expect(main).toContainText("Theodore Stelmack");
  await expect(main).toContainText("mechanical treatment of metals");
  await expect(main).toContainText("no employer is identified");

  await page.goto("./people/da2cb9ac-f157-5a0e-90ce-429701e02d73/");
  main = page.locator("main");
  await expect(main).toContainText("manufacture of miscellaneous products");
  await expect(main).toContainText("malformed Army grade value");
  await expect(main).toContainText("no employer is identified");
});

test("Morris I Stein keeps unmapped code 037 unresolved", async ({ page }) => {
  await page.goto("./people/e16dba7c-16bf-5d05-a5c2-42fb83dc898c/");
  const main = page.locator("main");
  await expect(main).toContainText("code 037 remains unmapped");
  await expect(main).toContainText("no occupation label, employer or OSS transition is assigned");
  await expect(main).not.toContainText("If the qualified identity match is correct");
});

test("Estelle H Steinacker employment remains qualified and temporally unresolved", async ({ page }) => {
  await page.goto("./people/261cc632-397a-5da6-ac09-a882f8083d4f/");
  const main = page.locator("main");
  await expect(main).toContainText("probable match");
  await expect(main).toContainText("Civilian Pilot Training Division");
  await expect(main).toContainText("employee; title not stated");
  await expect(main).toContainText("not proven to be the immediate pre-OSS assignment or last civilian employer");
});

test("Saul Steinberg separates military pathway, publishing, and student status", async ({ page }) => {
  await page.goto("./people/8a130c89-6739-5907-94aa-51585f2357ca/");
  const main = page.locator("main");
  await expect(main).toContainText("commission as an ensign in the U.S. Naval Reserve");
  await expect(main).toContainText("contributing cartoonist and illustrator for The New Yorker");
  await expect(main).toContainText("student status is not employment");
  await expect(main).toContainText("current sources establish affiliations but not a last civilian employer");
});

test("NARA file leads for Maldwin and Wilbur Stein do not become employer claims", async ({ page }) => {
  for (const id of [
    "255dd371-c020-5c58-97bc-e44dd2b96d93",
    "4207d44f-23cb-50c9-a2af-23364fc27ea8",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main.locator("section[aria-labelledby='evidence']")).toHaveCount(0);
  }
});

test("Batch 912 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 912 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 614,
    research_attempted_people: 13_925,
    verified_affiliation_people: 998,
    verified_employer_people: 450,
    archival_review_assessed_people: 12_398,
    published_claims: 8_525,
    public_sources: 5_685,
  });
});
