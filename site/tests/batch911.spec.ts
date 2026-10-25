import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page446-steele-to-steiker-review_batch-911_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
) as Array<{ person_id: string; display_name: string; research_status: string; claims: unknown[] }>;

const profiles = [
  ["bbbd4757-0a81-5450-bc6e-916c018f177f", "Leroy Steele"],
  ["d11bb24e-11a5-5a60-838a-9f94a5349443", "Richard J Steele"],
  ["1c396a67-7acc-5ede-bdd5-38d665600b68", "Robert L Steele"],
  ["fb49b3e8-8903-538b-8edc-ec824f4d9e08", "Benjamin F Steely"],
  ["b01fb41c-7382-5dbf-963e-d783d61ce4a5", "Barry Steen"],
  ["2b0a2730-bae9-561e-a5b6-227e666cba3d", "Henry V Steenberghe"],
  ["0cfa6a06-2cdc-5659-84dc-37a909d120dd", "Ernest W Stees"],
  ["fb261687-3eae-59fd-af2e-3bae5b7c8086", "Thomas E Stefan"],
  ["9422efef-ffce-5906-90e8-0a371c147543", "Michael J Stefancich"],
  ["38ccaa39-1ff4-5080-97dd-734397c60d56", "Rino C Stefani"],
  ["97691c35-acb6-5ac8-bc15-9777a225754b", "John Stefen"],
  ["5e9ca4a9-8f38-5ade-a2e8-d2ed7c70f03f", "George E Stefo"],
  ["146e3441-81a5-52ff-95a7-d342205fa719", "Charles L Stegman"],
  ["56b1a29e-0aac-5706-b3be-7b56982ffc13", "Golda I Stegner"],
  ["b58a981b-bec0-5212-bec0-b044dd904d6d", "Henry E Stehli"],
  ["cbd7ba3e-326a-50c7-b47d-5d3c47ddce58", "Armand D Steholm"],
  ["8afaf29b-607d-594d-b33f-4fc376a858e3", "Jerome E Steholm"],
  ["1fdf2d00-716b-5267-9dc8-1d6308a5e536", "Nicholas J Steichen"],
  ["bba51774-77c2-58a6-9a5d-d637bc2b9e0f", "Nicholas J Steichen"],
  ["fc427301-8f5e-5e33-b8b9-4ab8d630cc17", "Sidney G Steifel"],
  ["6530a8a7-2ac5-5a9d-a112-b66572c96ba2", "Seymour Steiger"],
  ["155216f5-9e40-5a4c-8bd8-305dbf61c714", "Jonas Steigman"],
  ["91a1d7f6-7034-5945-b739-ea27df2fa688", "Jerome A Steiker"],
] as const;

test("Batch 911 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Thomas E Stefan separates the Army pathway from civilian employment", async ({ page }) => {
  await page.goto("./people/fb261687-3eae-59fd-af2e-3bae5b7c8086/");
  const main = page.locator("main");
  await expect(main).toContainText("Arch Street Tavern");
  await expect(main).toContainText("immediate pre-OSS pathway was U.S. Army service");
  await expect(main).toContainText("last named civilian work before Army entry");
});

test("Henry E Stehli preserves probable temporal immediacy", async ({ page }) => {
  await page.goto("./people/b58a981b-bec0-5212-bec0-b044dd904d6d/");
  const main = page.locator("main");
  await expect(main).toContainText("Stehli Silks Corporation");
  await expect(main).toContainText("Probable immediate");
  await expect(main).toContainText("do not explicitly state the exact date he left the firm");
});

test("the two Nicholas J Steichen rows remain separate", async ({ page }) => {
  const matched = people.filter((person) => person.display_name === "Nicholas J Steichen");
  expect(matched).toHaveLength(2);
  expect(matched.map((person) => person.research_status).sort()).toEqual([
    "occupation_only_found",
    "requires_archival_review",
  ]);

  await page.goto("./people/1fdf2d00-716b-5267-9dc8-1d6308a5e536/");
  let main = page.locator("main");
  await expect(main).toContainText("Army Air Forces");
  await expect(main).toContainText("finance work in March 1943");

  await page.goto("./people/bba51774-77c2-58a6-9a5d-d637bc2b9e0f/");
  main = page.locator("main");
  await expect(main).toContainText("Review the indexed personnel file");
  await expect(main).toContainText("This second Nicholas J. Steichen row");
  await expect(main).not.toContainText("finance work in March 1943");
});

test("qualified directory matches remain visibly qualified", async ({ page }) => {
  await page.goto("./people/56b1a29e-0aac-5706-b3be-7b56982ffc13/");
  let main = page.locator("main");
  await expect(main).toContainText("University of Minnesota Department of Animal Husbandry");
  await expect(main).toContainText("If the qualified identity match is correct");

  await page.goto("./people/fc427301-8f5e-5e33-b8b9-4ab8d630cc17/");
  main = page.locator("main");
  await expect(main).toContainText("Steifel Mattress Company");
  await expect(main).toContainText("If the qualified identity match is correct");
});

test("Barry Steen conflict is not published as an occupation", async ({ page }) => {
  await page.goto("./people/b01fb41c-7382-5dbf-963e-d783d61ce4a5/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main.locator("section[aria-labelledby='evidence']")).toHaveCount(0);
});

test("Batch 911 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 911 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 614,
    research_attempted_people: 13_902,
    verified_affiliation_people: 997,
    verified_employer_people: 450,
    archival_review_assessed_people: 12_375,
    published_claims: 8_506,
    public_sources: 5_676,
  });
});
