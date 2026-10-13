import { expect, test } from "@playwright/test";

const profiles = [
  ["f1a54e7f-bc7f-5474-a4c7-5712b5c9f0bc", "William A Pye"],
  ["57ca2496-f727-5aeb-a638-b5157045f779", "Choon H Pyen"],
  ["47ce6b78-c13c-5983-82ad-99d98519e5b5", "Edwin L Pyle"],
  ["514f0747-ba8b-5ba9-a4d8-b14719fc9f23", "Harold P Pyle"],
  ["72f62dc7-ea6a-5a7d-9538-e3785b51df04", "Elizabeth Pyle-Jones"],
  ["0ff73a81-6a48-5228-99c5-40a89e6930a5", "Michelle Pynchon"],
  ["423085ec-7848-50d2-8bcb-0f633ae98056", "Ted S Pytlinski"],
  ["b2e78cb1-4974-546a-917b-213d9f722c4f", "Patsy A Quagliato"],
  ["8e7f46ab-05e3-563b-a3e7-48e8c7135418", "Thomas W Quaife"],
  ["1c60856f-730c-5268-81d8-f4eb75a81a71", "Donald L Quale"],
  ["490f56be-276e-58f1-930a-0673a3c32124", "Marjorie B Quay"],
  ["bdaaf15d-0e02-5224-81c7-c45c115c012f", "Richard R Quay"],
  ["5a54e46f-e1e9-51fe-8d14-5e7b76f31ae1", "Richard R Quay"],
  ["0b0cd791-0961-5e0c-b507-34f54ff22282", "Emil J Quayle"],
  ["45340717-222b-5988-ab83-e316be43da2a", "Paul P Quayle"],
  ["365dfe9a-6681-5f7f-9257-9106eec2944c", "Elene C Queen"],
  ["4bb08eeb-4491-5255-8cae-bba3e7fc7730", "Elene S Queen"],
  ["1c2b194d-eb0f-5822-b277-14b834016843", "Roberta L Queen"],
  ["a22396fb-2da3-5fb4-aa14-289979eab21f", "Jean Y Quentel"],
  ["850c3862-a966-5df3-86d8-b1a8e1115fcd", "Jean Y Quentel"],
  ["be0c0a5b-1f81-5d1a-90ce-8cfffe15ced4", "Vincent J Quercia"],
  ["bd05f2f8-7f25-565c-b05b-94a94a2c5c72", "Edmund P Quereau"],
  ["9f639850-e123-5ad2-a672-4717b7584d67", "Edmund P Quereau"],
] as const;

test("Batch 782 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 782 publishes Army identity evidence without inventing employers", async ({ page }) => {
  for (const id of [
    "423085ec-7848-50d2-8bcb-0f633ae98056",
    "0b0cd791-0961-5e0c-b507-34f54ff22282",
    "be0c0a5b-1f81-5d1a-90ce-8cfffe15ced4",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
  }
});

test("Batch 782 keeps all three same-name pairs visible and separate", async ({ page }) => {
  for (const id of [
    "bdaaf15d-0e02-5224-81c7-c45c115c012f",
    "5a54e46f-e1e9-51fe-8d14-5e7b76f31ae1",
    "a22396fb-2da3-5fb4-aa14-289979eab21f",
    "850c3862-a966-5df3-86d8-b1a8e1115fcd",
    "bd05f2f8-7f25-565c-b05b-94a94a2c5c72",
    "9f639850-e123-5ad2-a672-4717b7584d67",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("Duplicate group");
  }
});

test("Batch 782 qualifies Quereau's shared-person chronology and excludes it from settled affiliations", async ({ page }) => {
  for (const id of [
    "bd05f2f8-7f25-565c-b05b-94a94a2c5c72",
    "9f639850-e123-5ad2-a672-4717b7584d67",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("probable shared Edmund Packard Quereau identity");
    await expect(main).toContainText("Army Signal Security Service");
    await expect(main).toContainText("University of Texas");
    await expect(main).toContainText("not assigned as a settled row-specific employer");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
  }
});

test("Batch 782 preserves literal index notes", async ({ page }) => {
  await page.goto("./people/bdaaf15d-0e02-5224-81c7-c45c115c012f/");
  await expect(page.locator("main")).toContainText("Also 337");

  for (const id of [
    "a22396fb-2da3-5fb4-aa14-289979eab21f",
    "850c3862-a966-5df3-86d8-b1a8e1115fcd",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("French");
  }
});

test("home page exposes the rebuilt Batch 782 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,986");
  await expect(home).toContainText("45.89%");
  await expect(home).toContainText("12,948");
  await expect(home).toContainText("800");
  await expect(home).toContainText("357");
  await expect(home).toContainText("9,445");
});
