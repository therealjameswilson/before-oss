import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page438-sokoloff-to-sommer-review_batch-896_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["e21bd845-af70-5e49-8f66-dd6fdf7e9560", "Herbert K Sokoloff"],
  ["43c3be7f-e484-5af2-ab8a-ed4e480a0846", "Harry L Solberg"],
  ["9fc7f4e6-18b2-5117-8c7a-2dedf881f020", "Kemp D Solcher"],
  ["4e1eba73-0c02-5952-80e5-9f6115483350", "Ann Soldano"],
  ["1eff463b-6240-5413-abe6-527038ec6040", "Nicholas J Soldano"],
  ["4b65d53f-34dd-5e91-a5a3-1beec0460f5c", "Katherine R Soldst"],
  ["43aea2b1-20f9-57cb-84cb-e13f4817b9fd", "Harvy T Solee"],
  ["a3f5e84b-ac76-5707-aa46-1b5ac64a722a", "Tony A Solferino"],
  ["2c742367-e83d-5de2-b46d-60cff95ac250", "Donald M Soliday"],
  ["ebed71fa-09af-5ad5-8aae-61b1e7c30fd6", "McCord Sollenberger"],
  ["19e75c0b-0050-5524-952d-7c97565bc636", "Florence H Solomon"],
  ["cd3fc28e-ee4a-5a21-900e-e96a5ff4d1d5", "George J Solomon"],
  ["85496e3c-50fa-54b3-a3f4-26852a39ce39", "Julius H Solomon"],
  ["bcf79e64-9146-5bd7-a7b3-11c5bb9bb1ae", "Myron Solomon"],
  ["52a111fc-b7aa-566c-932b-3875bca5aadf", "Harry Solov"],
  ["0ffab191-9866-5cf0-9f7c-6fe0587e9c71", "Gerald K Solper"],
  ["343b5529-83d5-5154-9608-b187ac0402b4", "Gordon L Soltau"],
  ["165cb00f-f34e-5ccb-9649-c8a1699bda46", "J M Somer"],
  ["28f6f152-3d1f-5b66-9617-685d27b021ad", "Dwight L Somers"],
  ["33507673-150d-5be6-a5a3-405b382dac48", "Robert M Somers"],
  ["f8909416-1e38-5ace-9212-22f155e451b8", "Alexis Sommaripa"],
  ["f591571c-6bea-5b4e-bbe5-17373ec165df", "George Sommaripa"],
  ["fc97b580-efbd-5832-81e9-deef8dff4738", "Francis F Sommer"],
] as const;

test("Batch 896 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("accepted Army bridges publish qualified categories without inventing employers", async ({ page }) => {
  const checks = [
    ["e21bd845-af70-5e49-8f66-dd6fdf7e9560", "Students"],
    ["a3f5e84b-ac76-5707-aa46-1b5ac64a722a", "building of aircraft"],
    ["cd3fc28e-ee4a-5a21-900e-e96a5ff4d1d5", "fabrication of metal products"],
    ["0ffab191-9866-5cf0-9f7c-6fe0587e9c71", "Students"],
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

test("Solee and Somers identity conflicts remain visible without occupation transfer", async ({ page }) => {
  await page.goto("./people/43aea2b1-20f9-57cb-84cb-e13f4817b9fd/");
  const solee = page.locator("main");
  await expect(solee).toContainText("conflicting");
  await expect(solee).toContainText("Harvey T Selee");
  await expect(solee).toContainText("serial-conflict:[private identifier omitted]");
  await expect(solee).not.toContainText("manufacture of automobiles");

  await page.goto("./people/33507673-150d-5be6-a5a3-405b382dac48/");
  const somers = page.locator("main");
  await expect(somers).toContainText("conflicting");
  await expect(somers).toContainText("Robert N Somers");
  await expect(somers).toContainText("middle-initial conflict");
  await expect(somers).not.toContainText("Chauffeurs and drivers");
});

test("McCord Sollenberger publishes law-school student status but no employer", async ({ page }) => {
  await page.goto("./people/ebed71fa-09af-5ad5-8aae-61b1e7c30fd6/");
  const main = page.locator("main");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("University of Maryland School of Law");
  await expect(main).toContainText("First-Year Evening Class student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Alexis Sommaripa keeps employer, government assignments, education and civilian status distinct", async ({ page }) => {
  await page.goto("./people/f8909416-1e38-5ace-9212-22f155e451b8/");
  const main = page.locator("main");
  await expect(main).toContainText("civilian professional or administrative grade");
  await expect(
    main.locator("dt").filter({ hasText: /^Commissioned officer$/ })
      .locator("xpath=following-sibling::dd[1]"),
  ).toHaveText("No");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Office of War Information",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "E. I. du Pont de Nemours Company (DuPont)",
  );
  await expect(main).toContainText("Army's Quartermaster Board");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("assimilated captain rank was not a commission");
});

test("George Sommaripa does not inherit Alexis Sommaripa evidence", async ({ page }) => {
  await page.goto("./people/f591571c-6bea-5b4e-bbe5-17373ec165df/");
  const main = page.locator("main");
  await expect(main).toContainText("unresolved");
  await expect(main).toContainText("shared surname with Alexis Sommaripa is not treated as evidence");
  await expect(main).not.toContainText("DuPont");
  await expect(main).not.toContainText("Office of War Information");
});

test("Batch 896 evidence and public projection exclude protected identifiers and credentials", () => {
  const people = fs.readFileSync(
    new URL("../src/data/generated/people.json", import.meta.url),
    "utf8",
  );
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("17106958");
});

test("Batch 896 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 598,
    research_attempted_people: 13_565,
    verified_affiliation_people: 973,
    verified_employer_people: 437,
    archival_review_assessed_people: 12_036,
    published_claims: 8_214,
    public_sources: 5_519,
  });
});
