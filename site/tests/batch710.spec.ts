import { expect, test } from "@playwright/test";

const profiles = [
  ["90e6a40f-a48b-544d-8244-c0aff59ee875", "Francis J Novak"],
  ["51b16e17-0094-58ac-bd0c-d1cacf2b7b2e", "John J Novak"],
  ["8f7927e7-dcb1-5e14-a924-3c834e8cbfe8", "Joseph A Novatnik"],
  ["5d211b1e-eff0-58cb-b4a9-a768338e5870", "Leonard Nover"],
  ["fe2092f3-8c87-5469-bd5d-e85a40ca6783", "Michael J Novosel"],
  ["7637fe4b-ceff-522c-9278-fbe11c59c6ff", "Joseph A Novotnik"],
  ["b358b69e-2538-58aa-b2cd-6deb24f828ee", "Irene M Nowak"],
  ["d69d0769-f276-56bf-8383-b0d369a7c12a", "Adolph R Nowakowski"],
  ["dc2a924d-d601-50d8-b7ab-4e9b328d58b4", "Robert S Nowell"],
  ["b1871a40-8c63-57f2-86dd-d6fce4c32809", "Robin S Nowell"],
  ["81ba3ad7-ab7e-56c5-8a9a-6f846e1493e7", "Gernard Nowicki"],
  ["6d268331-23ff-5885-9eb9-8d53c6cc8f9a", "Leonard M Nowicki"],
  ["f6845d2d-db9f-54ad-8fc1-5895900e13be", "Chester S Nowik"],
  ["c6f26574-9da7-555d-84d5-74aa795e0198", "Dorothy Q Noyes"],
  ["75d1d21b-41c1-5ebf-8679-6eb3c0a71bd0", "Robert P Noyes"],
  ["5cf44c0f-49d7-5efe-ad42-f531cef2e441", "Amelia O Nuessle"],
  ["84ba41e5-9e02-509d-9352-e85fd5b46da7", "Benjamin B Null"],
  ["7c089205-41e5-5186-8e91-3a08cd626b28", "Jose R Nunez"],
  ["4e4625fa-bfac-5620-a0df-86b095ffbdd6", "Grace A Nunn"],
  ["b9621159-bd04-5121-806e-814acbb14381", "Guy T Nunn"],
  ["fce5ed82-cd6e-5ba8-9dd3-2804af647fd7", "Jean C Nunn"],
  ["a3967b7e-bc18-5259-89f1-339e4299b9dd", "Jeane M Nunn"],
  ["68ccf903-8893-547e-830f-1771d48acab8", "Edly D Nupen"],
] as const;

test("Batch 710 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 710 publishes Novosel's military pathway without calling it a civilian employer", async ({ page }) => {
  await page.goto("./people/fe2092f3-8c87-5469-bd5d-e85a40ca6783/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("United States Army Air Forces");
  await expect(main).toContainText("Army Air Corps");
  await expect(main).toContainText("First Lieutenant and military aviator");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("four months of OSS special duty");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 710 qualifies Nupen's identity while preserving the unresolved chronology", async ({ page }) => {
  await page.goto("./people/68ccf903-8893-547e-830f-1771d48acab8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("Edly Daniel Nupen");
  await expect(main).toContainText("Little Norway");
  await expect(main).toContainText("sequence relative to OSS service is unresolved");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Embassy of Nicaragua was his employer");
});

test("Batch 710 withholds the low-confidence Dorothy Noyes professional lead", async ({ page }) => {
  await page.goto("./people/c6f26574-9da7-555d-84d5-74aa795e0198/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("plausible exact-name lead");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("New Design Inc.");
  await expect(main).not.toContainText("National Housing Authority");
});

test("Batch 710 preserves both shared-identifier pairs without merging people", async ({ page }) => {
  for (const id of [
    "8f7927e7-dcb1-5e14-a924-3c834e8cbfe8",
    "7637fe4b-ceff-522c-9278-fbe11c59c6ff",
    "dc2a924d-d601-50d8-b7ab-4e9b328d58b4",
    "b1871a40-8c63-57f2-86dd-d6fce4c32809",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusprobable");
    await expect(main).toContainText("Duplicate groupduplicate-");
    await expect(main).toContainText("conflicting sources");
  }

  await page.goto("./people/8f7927e7-dcb1-5e14-a924-3c834e8cbfe8/");
  await expect(page.locator("main")).toContainText("Joseph A Novotnik");
  await page.goto("./people/dc2a924d-d601-50d8-b7ab-4e9b328d58b4/");
  await expect(page.locator("main")).toContainText("Robin S Nowell");
});

test("Batch 710 publishes identifier-backed identities without occupation-code inference", async ({ page }) => {
  for (const [id, name] of [
    ["51b16e17-0094-58ac-bd0c-d1cacf2b7b2e", "John J Novak"],
    ["f6845d2d-db9f-54ad-8fc1-5895900e13be", "Chester S Nowik"],
    ["75d1d21b-41c1-5ebf-8679-6eb3c0a71bd0", "Robert P Noyes"],
    ["84ba41e5-9e02-509d-9352-e85fd5b46da7", "Benjamin B Null"],
    ["7c089205-41e5-5186-8e91-3a08cd626b28", "Jose R Nunez"],
    ["b9621159-bd04-5121-806e-814acbb14381", "Guy T Nunn"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("Batch 710 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,369");
  await expect(main).toContainText("39.14%");
  await expect(main).toContainText("716");
  await expect(main).toContainText("323");
  await expect(main).toContainText("14,565");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
