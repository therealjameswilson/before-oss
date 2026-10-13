import { expect, test } from "@playwright/test";

const profiles = [
  ["09110d0e-9c6c-55c4-816f-5954904d77ef", "Thomas G Presutti"],
  ["24eb8a43-9348-564b-b252-2321ae1883a4", "Samuel J Prete"],
  ["0ac1d76a-6ec3-58dc-afa1-f61a49e8897f", "Walter Pretzat"],
  ["8d9cf9f1-220b-544e-b554-fe0336ec23dc", "Joseph J Previte"],
  ["5342ffd6-a5b1-51f6-ab66-32e1cb3d347b", "Francis H Prevost"],
  ["704233e7-be52-58bd-9c45-d4f0c5b27c34", "John C Prevost"],
  ["ee95457e-77fe-5618-8cb2-797cadbf93d3", "Roger Prevost"],
  ["0f40043f-5852-5c99-a601-55972f49cfa2", "George D Prewitt"],
  ["fb9e56f3-bfe8-530b-9308-fb658fc3a162", "Michele P Priano"],
  ["d355c9e1-add4-593c-b6d3-8b0b35daff15", "Barney L Priar"],
  ["51e712c2-632e-5ca3-8fc0-44432b173289", "Venda A Pribramsky"],
  ["9aef9e41-0ff5-5b56-bc24-b4b9f8b290bd", "Allan B Price"],
  ["0b1e74da-dbc6-5af6-b26c-1bc55f08bdd4", "Alvina M Price"],
  ["84661f42-adec-533b-a8c3-e66f25af9510", "Analouise C Price"],
  ["ef399d65-e4d1-5e24-8ed6-338e5f7c6e5e", "Arnold H Price"],
  ["c523dbb2-c8f8-55bb-8dc9-b0ee9b8925cd", "Blanche E Price"],
  ["72db0814-2850-5d61-b5d6-62a1f7dada69", "Brenizer L Price"],
  ["8d881d39-2019-5fbd-ab94-819260ba4238", "Elizabeth M Price"],
  ["93022574-242d-5d6f-90d5-032ac5158bd1", "Elizabeth W Price"],
  ["bfbcedc1-eded-5e06-abfe-389c2a429229", "Ernest B Price"],
  ["a5904ca7-4a85-5d3c-883d-173a9452513f", "Francis B Price"],
  ["4d97bbc7-2317-551b-8de3-8ccc57d3592c", "Frederick E Price"],
  ["49bf7b84-0980-5ea6-8473-537ef7e05b04", "Harvey O Price"],
] as const;

test("Batch 774 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 774 publishes Ernest B Price's documented prewar university role without claiming immediacy", async ({ page }) => {
  await page.goto("./people/bfbcedc1-eded-5e06-abfe-389c2a429229/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Chicago");
  await expect(main).toContainText("director of International House and professor");
  await expect(main).toContainText("documented prewar");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "A single last civilian employer before wartime or military service has not yet been established",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).not.toContainText("Standard Vacuum Oil");
});

test("Batch 774 exposes Roger Prevost's military-status conflict without treating it as a pre-OSS affiliation", async ({ page }) => {
  await page.goto("./people/ee95457e-77fe-5618-8cb2-797cadbf93d3/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("Free French Army lieutenant");
  await expect(main).toContainText("entry grade of private");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 774 retains Francis B Price's protected-identifier conflict", async ({ page }) => {
  await page.goto("./people/a5904ca7-4a85-5d3c-883d-173a9452513f/");
  const main = page.locator("main");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("PRICE FRANCIS B");
  await expect(main).toContainText("CLARK ROLAND E");
  await expect(main).toContainText("conflicting");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 774 publishes accepted Army identities without converting coded occupations into employers", async ({ page }) => {
  for (const id of [
    "24eb8a43-9348-564b-b252-2321ae1883a4",
    "0ac1d76a-6ec3-58dc-afa1-f61a49e8897f",
    "8d9cf9f1-220b-544e-b554-fe0336ec23dc",
    "5342ffd6-a5b1-51f6-ab66-32e1cb3d347b",
    "704233e7-be52-58bd-9c45-d4f0c5b27c34",
    "0f40043f-5852-5c99-a601-55972f49cfa2",
    "d355c9e1-add4-593c-b6d3-8b0b35daff15",
    "51e712c2-632e-5ca3-8fc0-44432b173289",
    "ef399d65-e4d1-5e24-8ed6-338e5f7c6e5e",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("enlisted army personnel");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
    await expect(main).toContainText("coded occupation is not employer evidence");
  }
});

test("Batch 774 keeps rejected common-name employment candidates out of public claims", async ({ page }) => {
  await page.goto("./people/09110d0e-9c6c-55c4-816f-5954904d77ef/");
  const presutti = page.locator("main");
  await expect(presutti).toContainText("requires archival review");
  await expect(presutti).not.toContainText("Wilder Building");
  await expect(presutti).not.toContainText("Harvard Law School");

  await page.goto("./people/c523dbb2-c8f8-55bb-8dc9-b0ee9b8925cd/");
  const blanche = page.locator("main");
  await expect(blanche).toContainText("requires archival review");
  await expect(blanche).not.toContainText("Pioneer Hall");
});

test("Batch 774 preserves indexed commissioned and civilian classifications", async ({ page }) => {
  await page.goto("./people/9aef9e41-0ff5-5b56-bc24-b4b9f8b290bd/");
  await expect(page.locator("main")).toContainText("commissioned army officer");

  await page.goto("./people/84661f42-adec-533b-a8c3-e66f25af9510/");
  await expect(page.locator("main")).toContainText("civilian professional or administrative grade");
});

test("home page exposes the rebuilt Batch 774 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,804");
  await expect(home).toContainText("45.13%");
  await expect(home).toContainText("13,130");
  await expect(home).toContainText("792");
  await expect(home).toContainText("353");
  await expect(home).toContainText("9,262");
});
