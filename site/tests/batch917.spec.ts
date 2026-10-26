import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page449-stewart-to-stiefel-review_batch-917_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c9617d96-7e59-5dfb-becb-b56e55966fe9", "Jack S Stewart"],
  ["424de3fa-57da-5422-a92a-550d3d3cab89", "James R Stewart"],
  ["0ca29a30-7007-5330-b5ca-771fe271362c", "John H Stewart"],
  ["0f68bdcb-c062-5641-904b-740da9e3a3c3", "Joseph C Stewart"],
  ["b4d722ee-4bc5-5c6e-b4d5-e15241c446c2", "Joseph E Stewart"],
  ["01c7dcd8-d894-539c-89d9-dac9c047a162", "Margaret M Stewart"],
  ["55972627-d528-57a7-970f-fbd22d908154", "Mary Stewart"],
  ["b5b5b7f7-19d2-58cd-a62d-d307daa17538", "Oswald Stewart"],
  ["a216ee02-5f8d-59f2-87e2-de5f415e7395", "Susan S Stewart"],
  ["1b7afa81-e3d0-5dde-995a-88d889a470cd", "William D Stewart"],
  ["a174e1da-0c19-511d-8077-713c025c4a44", "William R Stewart"],
  ["4cf845da-4243-52c6-a37e-e59ea3e03ed0", "Martin K Stewen"],
  ["4ff0a066-312a-565a-9c00-89411b79e4e5", "Constantine Stiakakis"],
  ["22a1cfab-ac86-558e-87c6-31fc98b6174c", "Oddberg P Stiansen"],
  ["eaf13bea-cd19-5e19-8433-f2d51325d53d", "Karel C Stiassni"],
  ["97a168bb-761a-5998-b82d-3814fc261154", "Karel C Stiassni"],
  ["ea33c2c9-c603-5fc8-b072-fdff25ca39f2", "Betty A Stich"],
  ["d11d21d0-a731-5b46-9e9b-83d0f950c77b", "Shirlene J Stich"],
  ["581f6054-c633-54e8-a250-b8648f881a73", "Howard L Stickney"],
  ["69267441-cc57-5de4-b128-7cbf3fbb193e", "Ernest C Stiefel"],
  ["8ca1e52d-f2f9-5479-ac6d-74cfd3e4ee59", "Ernest C Stiefel"],
  ["ca0f3cc1-cd83-5041-be1b-9386d6b5592b", "Rudolph C Stiefel"],
  ["5503f49d-9886-520b-b7eb-7b696ab2aedf", "Sidney G Stiefel"],
] as const;

test("Batch 917 publishes all 23 people with saved outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 917 Army categories remain occupations rather than employers", async ({ page }) => {
  const cases = [
    ["b4d722ee-4bc5-5c6e-b4d5-e15241c446c2", "Clerks, general office"],
    ["1b7afa81-e3d0-5dde-995a-88d889a470cd", "General farmers"],
  ] as const;
  for (const [id, label] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(label);
    await expect(main).toContainText("no employer is identified");
    await expect(main).toContainText("occupation only found");
  }
});

test("Oswald Stewart separates immediate Army assignment, student status and civilian-employer uncertainty", async ({ page }) => {
  await page.goto("./people/b5b5b7f7-19d2-58cd-a62d-d307daa17538/");
  const main = page.locator("main");
  await expect(main).toContainText("Army anti-aircraft units in the China-Burma-India theater");
  await expect(main).toContainText("transferring to the OSS in 1945");
  await expect(main).toContainText("Massachusetts Institute of Technology");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Martin Stewen publishes the dated Finnish assignment with visible temporal qualification", async ({ page }) => {
  await page.goto("./people/4cf845da-4243-52c6-a37e-e59ea3e03ed0/");
  const main = page.locator("main");
  await expect(main).toContainText("Martin Kasimir Stewen");
  await expect(main).toContainText("Finnish Defence Forces");
  await expect(main).toContainText("military attache");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Constantine Stiakakis and Oddberg Stiansen retain OSS-unit identity evidence without invented employers", async ({ page }) => {
  await page.goto("./people/4ff0a066-312a-565a-9c00-89411b79e4e5/");
  await expect(page.locator("main")).toContainText("OSS Greek Operational Group");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/22a1cfab-ac86-558e-87c6-31fc98b6174c/");
  await expect(page.locator("main")).toContainText("OSS Norwegian Operational Group");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("same-name Stiassni and Stiefel rows stay separate while low-confidence candidates stay private", async ({ page }) => {
  const cases = [
    [
      "eaf13bea-cd19-5e19-8433-f2d51325d53d",
      "97a168bb-761a-5998-b82d-3814fc261154",
    ],
    [
      "69267441-cc57-5de4-b128-7cbf3fbb193e",
      "8ca1e52d-f2f9-5479-ac6d-74cfd3e4ee59",
    ],
  ] as const;
  for (const pair of cases) {
    expect(pair[0]).not.toBe(pair[1]);
    const publicGroups: string[] = [];
    for (const id of pair) {
      await page.goto(`./people/${id}/`);
      const main = page.locator("main");
      const duplicateGroup = main.locator("dt").filter({ hasText: /^Duplicate group$/ })
        .locator("xpath=following-sibling::dd[1]");
      await expect(duplicateGroup).toHaveText(/^duplicate-[0-9a-f]{12}$/);
      publicGroups.push((await duplicateGroup.textContent()) ?? "");
      await expect(main).toContainText("requires archival review");
      await expect(main).not.toContainText("same-name:");
      await expect(main).not.toContainText("Board of Economic Warfare");
      await expect(main).not.toContainText("first lieutenant");
    }
    expect(publicGroups[0]).toBe(publicGroups[1]);
  }
});

test("Batch 917 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 917 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 617,
    research_attempted_people: 14_040,
    verified_affiliation_people: 1_003,
    verified_employer_people: 451,
    archival_review_assessed_people: 12_513,
    published_claims: 8_606,
    public_sources: 5_721,
  });
});
