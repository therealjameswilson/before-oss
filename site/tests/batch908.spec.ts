import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page444-stanley-to-stapleton-review_batch-908_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["9aed898c-c148-53e1-8dce-c278d0cbfd74", "William S Stanley"],
  ["88cbb611-dd65-5035-9b1b-d3418b15977a", "Howard J Stansfield"],
  ["44e39ae5-b6bc-5a61-bfff-6d2c17bcd576", "Lorraine Stant"],
  ["306b7120-8734-5789-ab8a-0190a97d996f", "Joseph Stante"],
  ["36005475-4520-59e1-8883-548cf41633c9", "Alfred Stanton"],
  ["ef6ccf60-373a-5939-9336-aa115874eb7b", "Claude Stanton"],
  ["5c2cf8d6-61f8-5e31-ac69-c2c920da345d", "Edward L Stanton"],
  ["730072c0-79db-58e3-af00-a5ae7c9b58d6", "Edward L Stanton"],
  ["0d6b4de8-b896-57a2-b54e-e75a0a3c48f7", "Edward B Stanton"],
  ["a2dd3c55-6e9d-54df-a00b-62374e5442c6", "Frank Stanton"],
  ["4d9a3ab1-de6b-5e52-bacc-1e0efec1180b", "George H Stanton"],
  ["c7626520-0979-591c-b52a-81a6e57d0cf2", "Gertrude A Stanton"],
  ["ceceb9df-d3fe-515f-82d5-710acd558ac4", "Helena Stanton"],
  ["b68d4197-e62d-5bb1-b260-069478e7f8c4", "Merwin C Stanton"],
  ["bbc8cd90-0769-52e1-9896-c4c7f98d6907", "W T Stanton"],
  ["e5f841ca-fa75-5da8-bdde-10ee0c4a3e0c", "Willis A Stanton"],
  ["517ae32b-7d4d-5e02-b343-3880bce29efd", "Bernard N Stanziola"],
  ["0f7aa741-130b-5311-832d-58695c62ac71", "Henry L Staples"],
  ["462bc961-3e75-53ee-8036-9ffea196cf71", "John H Staples"],
  ["e41c80bc-afa1-560a-9aee-a466721268d5", "Richard F Staples"],
  ["e5ec7abb-9a71-5116-90f4-d2967e8d5e14", "Richard F Staples"],
  ["b74bab57-e9fd-5a9c-9a1d-a7aec253b51a", "Cyril D Stapleton"],
  ["859580c6-0048-552b-977c-e2eb454221cf", "George A Stapleton"],
] as const;

test("Batch 908 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 908 Army bridges publish qualified occupations or student status, not employers", async ({ page }) => {
  const checks = [
    ["88cbb611-dd65-5035-9b1b-d3418b15977a", "Sailors and deckhands"],
    ["b68d4197-e62d-5bb1-b260-069478e7f8c4", "Paymasters, payroll clerks, and timekeepers"],
    ["517ae32b-7d4d-5e02-b343-3880bce29efd", "Students"],
    ["e5ec7abb-9a71-5116-90f4-d2967e8d5e14", "Radio operators"],
  ] as const;

  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer is identified");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Joseph Stante publishes qualified occupations and compulsory military chronology without inventing an employer", async ({ page }) => {
  await page.goto("./people/306b7120-8734-5789-ab8a-0190a97d996f/");
  const main = page.locator("main");
  await expect(main).toContainText("Jože Stante");
  await expect(main).toContainText("Stanley Post");
  await expect(main).toContainText("miner and factory worker");
  await expect(main).toContainText("German Army");
  await expect(main).toContainText("8 September 1942");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("the two Richard F Staples profiles remain separate and evidence-specific", async ({ page }) => {
  await page.goto("./people/e41c80bc-afa1-560a-9aee-a466721268d5/");
  let main = page.locator("main");
  await expect(main).toContainText("communications officer");
  await expect(main).toContainText("Java");
  await expect(main).not.toContainText("Radio operators");

  await page.goto("./people/e5ec7abb-9a71-5116-90f4-d2967e8d5e14/");
  main = page.locator("main");
  await expect(main).toContainText("Radio operators");
  await expect(main).toContainText("omits the final s");
  await expect(main).not.toContainText("communications officer");
});

test("Claude, Frank, and Cyril same-name leads remain private", async ({ page }) => {
  await page.goto("./people/ef6ccf60-373a-5939-9336-aa115874eb7b/");
  await expect(page.locator("main")).not.toContainText("Mazamet");
  await expect(page.locator("main")).not.toContainText("textile business");

  await page.goto("./people/a2dd3c55-6e9d-54df-a00b-62374e5442c6/");
  await expect(page.locator("main")).not.toContainText("CBS");

  await page.goto("./people/b74bab57-e9fd-5a9c-9a1d-a7aec253b51a/");
  await expect(page.locator("main")).not.toContainText("Georgia Tech");
  await expect(page.locator("main")).not.toContainText("Aeronautical Research Laboratory");
});

test("Batch 908 evidence and public projection exclude credentials and private candidates", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("candidate-claude-stanton-france-b908");
  expect(people).not.toContain("candidate-frank-stanton-cbs-b908");
  expect(people).not.toContain("candidate-cyril-d-stapleton-b908");
});

test("Batch 908 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 608,
    research_attempted_people: 13_833,
    verified_affiliation_people: 992,
    verified_employer_people: 447,
    archival_review_assessed_people: 12_306,
    published_claims: 8_451,
    public_sources: 5_638,
  });
});
