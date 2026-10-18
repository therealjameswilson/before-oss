import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page433-smith-review_batch-886_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["43712fc3-015e-5d43-985f-26791e23df56", "Betty Smith"],
  ["ee3109bf-716c-5d84-b02b-adcae40e77fc", "Betty M Smith"],
  ["29161151-4e98-5cb3-948e-1392344bc4de", "Bradish J Smith"],
  ["fa313ef2-5261-573a-b3d4-a77792e4724c", "Brewster M Smith"],
  ["4a241564-acb3-5cf4-861f-3632c4c0f69b", "Brooks C Smith"],
  ["a4964eb0-1eae-55d2-824d-35e486de2049", "Bruce L Smith"],
  ["cc867672-9cd7-5dd9-b6f0-37ecfe209aff", "Bynum E Smith"],
  ["945aedcb-4131-5842-8114-b94c98a5f7db", "Carleton Smith"],
  ["bfbe3bfe-8c7d-50eb-b28f-b332d1ba6b4c", "Carman H Smith"],
  ["cf602dca-13d2-5c49-aa0c-9db3dc5249a4", "Carter M Smith"],
  ["efba9703-0f0b-5bd3-93d0-295f4e001fd8", "Catherine L Smith"],
  ["c66dba52-1482-56e0-a8c3-48547b42067d", "Charles T Smith"],
  ["fdeac0e0-8f8c-5757-9867-779154b2b62e", "Charles B Smith"],
  ["e3da5f93-ebf6-5592-95f8-5dd34a595051", "Charles S Smith"],
  ["2c5c896c-2d6d-5687-9699-6c7db7cdcfd3", "Clarence E Smith"],
  ["52df0b8c-9709-5dd3-bd81-492afa53deb8", "Claude W Smith"],
  ["357af4bd-1863-55bf-a2b3-db72c3646398", "Clayton R Smith"],
  ["2de8ce00-50f6-5b1a-9731-d45fef5d8654", "Daniel T Smith"],
  ["2cdf14ec-df2f-5503-bb28-a9dff7b35e39", "David R Smith"],
  ["ffc871c9-a1d0-5796-8e3f-f13d6b2187b5", "Dawn E Smith"],
  ["6a7d440c-fdfb-5edc-a959-fc3c58e222ce", "Dewey J Smith"],
  ["6c0b995c-5eb7-5b78-847e-78a63284e5c5", "Donald G Smith"],
  ["c45c5e29-0593-548d-80fa-95fb25cdc91e", "Dorothy B Smith"],
] as const;

test("Batch 886 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("721");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 886 publishes qualified Army occupations without inventing employers", async ({ page }) => {
  const checks = [
    ["4a241564-acb3-5cf4-861f-3632c4c0f69b", "Clerks, general office"],
    ["cc867672-9cd7-5dd9-b6f0-37ecfe209aff", "Student"],
    ["2c5c896c-2d6d-5687-9699-6c7db7cdcfd3", "Job pressman or casting-machine operator"],
    ["357af4bd-1863-55bf-a2b3-db72c3646398", "Student"],
    ["6c0b995c-5eb7-5b78-847e-78a63284e5c5", "Chauffeurs and drivers"],
  ] as const;
  for (const [id, occupation] of checks) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(occupation);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 886 excludes Daniel T Smith's 1946 occupation from pre-OSS evidence", async ({ page }) => {
  await page.goto("./people/2de8ce00-50f6-5b1a-9731-d45fef5d8654/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("1946");
  await expect(main).toContainText("excluded from pre-OSS evidence");
  await expect(main).not.toContainText("Sales clerk");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 886 preserves printed notes without expanding them", async ({ page }) => {
  await page.goto("./people/945aedcb-4131-5842-8114-b94c98a5f7db/");
  await expect(page.locator("main")).toContainText("docume");
  await expect(page.locator("main")).not.toContainText("documented employer");

  await page.goto("./people/2cdf14ec-df2f-5503-bb28-a9dff7b35e39/");
  await expect(page.locator("main")).toContainText("File sent");
  await expect(page.locator("main")).toContainText("trace the printed File sent notation");
});

test("Batch 886 keeps the printed officer and enlisted classifications", async ({ page }) => {
  await page.goto("./people/e3da5f93-ebf6-5592-95f8-5dd34a595051/");
  const officer = page.locator("main");
  await expect(officer).toContainText("commissioned army officer");
  await expect(officer).toContainText("Commissioned officerYes");
  await expect(officer).toContainText("Identity statusunresolved");

  await page.goto("./people/6a7d440c-fdfb-5edc-a959-fc3c58e222ce/");
  const enlisted = page.locator("main");
  await expect(enlisted).toContainText("enlisted army personnel");
  await expect(enlisted).toContainText("Pfc");
  await expect(enlisted).toContainText("Identity statusunresolved");
});

test("Batch 886 evidence inputs exclude private identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 886 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 585,
    research_attempted_people: 13_339,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_807,
    published_claims: 8_073,
    public_sources: 5_455,
  });
});
