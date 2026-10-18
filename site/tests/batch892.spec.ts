import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page436-smith-review_batch-892_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["dcc93d54-a060-5bf7-b1c0-1d9124ad7299", "Susan Smith", "725"],
  ["05476034-b73b-50ef-a221-b97837fb5fca", "Thomas J Smith", "725"],
  ["3c9ff555-1615-5324-b1b6-e25c40aa0e17", "Thomas R Smith", "725"],
  ["e794dbca-f53d-5846-ac82-69643cd2de0f", "Thomas R Smith", "725"],
  ["d5d13d64-00b2-536c-94f6-f00935cc36b7", "Thomas M Smith", "725"],
  ["8c2623b6-d26a-52c0-878a-b9194386cff9", "Thomas F Smith", "725"],
  ["94c002a2-0d19-505f-8996-46462ad2a93a", "Thomas A Smith", "725"],
  ["bb64788e-1247-50a2-8f5a-c0496897f046", "Thomas R Smith", "725"],
  ["b1c65d73-fc8f-519e-a938-918d5a3ccc51", "Turner T Smith", "725"],
  ["44551848-8a85-5be0-a0a2-6e5f4efbd218", "Vera M Smith", "725"],
  ["47bd39c3-4f1c-5acd-a478-23d0bc4cd564", "Vincent R Smith", "725"],
  ["0492bc5a-30e7-55e6-8fa7-367b195c7cf4", "Vincent P Smith", "725"],
  ["7afe8d58-0e2b-5b1e-a59d-b53bd37d49e1", "Virginia K Smith", "725"],
  ["4ba2b47a-19da-5df3-9d36-4957f151c2af", "Walter Smith", "725"],
  ["851304d8-5106-5a3f-a7de-5a92c0a7487d", "Walter M Smith", "725"],
  ["c846f651-e6d8-5f65-a725-b1fcb019c602", "Warren D Smith", "725"],
  ["b4c7ef21-37da-55d7-9fdc-90d0299ce416", "Warren J Smith", "725"],
  ["eec8967f-b662-59ad-9979-3eed5928a476", "Warren O Smith", "725"],
  ["4230e29d-43a8-55ce-80c7-159e3cce96d3", "Wilfred A Smith", "726"],
  ["2b45880b-4e22-5d6a-b043-798f5842b44f", "Wilfred J Smith", "726"],
  ["033ce195-83cd-5c62-bd5d-645268a735fc", "Willard A Smith", "726"],
  ["c95a4d6c-44b9-5016-8cec-7d0d75452f98", "William F Smith", "726"],
  ["4cae9929-a8d0-59b7-8f7b-3f2c39f55d74", "William W Smith", "726"],
] as const;

test("Batch 892 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 892 publishes seven qualified non-employer findings", async ({ page }) => {
  const checks = [
    ["05476034-b73b-50ef-a221-b97837fb5fca", "Chauffeurs and drivers, bus, taxi, truck, and tractor"],
    ["3c9ff555-1615-5324-b1b6-e25c40aa0e17", "Teachers (secondary school) and principals"],
    ["e794dbca-f53d-5846-ac82-69643cd2de0f", "Photoengravers"],
    ["8c2623b6-d26a-52c0-878a-b9194386cff9", "historical student category"],
    ["b4c7ef21-37da-55d7-9fdc-90d0299ce416", "historical student category"],
    ["033ce195-83cd-5c62-bd5d-645268a735fc", "Teachers (secondary school) and principals"],
    ["4cae9929-a8d0-59b7-8f7b-3f2c39f55d74", "Chauffeurs and drivers, bus, taxi, truck, and tractor"],
  ] as const;
  for (const [id, finding] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(finding);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("the three Thomas R Smith rows remain separate and visibly grouped", async ({ page, request }) => {
  const ids = [
    "3c9ff555-1615-5324-b1b6-e25c40aa0e17",
    "e794dbca-f53d-5846-ac82-69643cd2de0f",
    "bb64788e-1247-50a2-8f5a-c0496897f046",
  ];
  for (const id of ids) {
    const response = await request.get(`./people/${id}/`);
    expect(response.ok()).toBeTruthy();
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("duplicate-a8414db200db");
  }
  expect(new Set(ids).size).toBe(ids.length);
});

test("damaged Army name evidence remains qualified rather than silently corrected", async ({ page }) => {
  await page.goto("./people/e794dbca-f53d-5846-ac82-69643cd2de0f/");
  const main = page.locator("main");
  await expect(main).toContainText("Indexed formThomas R Smith");
  await expect(main).toContainText("Thomas R Smith Jr");
  await expect(main).toContainText("damaged Army source form omits the initial T");
});

test("Warren J Smith has official OSS assignment corroboration without an invented employer", async ({ page }) => {
  await page.goto("./people/b4c7ef21-37da-55d7-9fdc-90d0299ce416/");
  const main = page.locator("main");
  await expect(main).toContainText("Company B, Special Reconnaissance Battalion");
  await expect(main).toContainText("Special Orders Number 9");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("printed officer ranks remain commissioned while their identities remain unresolved", async ({ page }) => {
  for (const id of [
    "b1c65d73-fc8f-519e-a938-918d5a3ccc51",
    "851304d8-5106-5a3f-a7de-5a92c0a7487d",
    "2b45880b-4e22-5d6a-b043-798f5842b44f",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("commissioned army officer");
    await expect(main).toContainText("unresolved");
  }
});

test("Batch 892 evidence inputs exclude protected identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 892 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 595,
    research_attempted_people: 13_474,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_944,
    published_claims: 8_147,
    public_sources: 5_481,
  });
});
