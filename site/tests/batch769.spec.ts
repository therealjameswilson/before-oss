import { expect, test } from "@playwright/test";

const profiles = [
  ["55b65ef9-0620-579a-af71-3929b1b446bb", "Philip Poskanzer"],
  ["a939f517-51a6-5ca0-a0c2-c14bb0b8a171", "Edward G Posniak"],
  ["d62daae0-cb50-5bbe-9e0e-681181f35c5c", "Edward G Posniak"],
  ["c8b942df-fc77-5ecd-a2a1-1bb49e962065", "Donald L Posson"],
  ["1bf0d418-137d-5e19-b4d6-4ae2c8333ed6", "August A Post"],
  ["cf2e819e-47dd-530a-9d71-d76f917b51aa", "Harry W Post"],
  ["dbb41055-5548-5c53-a353-358d9149fd76", "Larry Post"],
  ["62f0e6c0-aaf5-56de-8b2b-83abf1942e01", "Lloyd F Postel"],
  ["ca309825-cea2-5105-8636-4ee687f30971", "Virgil Postlethwait"],
  ["a9b7bf2b-9801-5b02-81c0-968b919ec0dd", "Leendert Pot"],
  ["e779e7f1-ec5c-508d-9aee-52aa778b2461", "Harry M Pote"],
  ["9fa45346-e4a6-5465-b305-56f76c38eb15", "Stanley Potochnik"],
  ["107e8f80-90bf-5d32-ae75-0d8ee078ed57", "Stanley Potochnik"],
  ["e40df0fa-3208-5d27-8046-c3375ce26abe", "James H Pott"],
  ["9b76a328-11de-5d87-b7d7-2bf90e0a8274", "Alric C. T. Pottberg"],
  ["149f1b22-ab4b-582e-bd4d-53477a21b94b", "David Potter"],
  ["f81b1308-e203-5c5b-90e1-f2a4e0a99d1e", "Gail M Potter"],
  ["47e6cb8b-36ec-5fb7-bc63-d9fbc86b7d67", "Genevieve Potter"],
  ["c30e19d1-1214-5cad-bfc3-50feac54fc25", "George E Potter"],
  ["01c847e5-da45-56d3-86c3-0c88c79fa94d", "George R Potter"],
  ["78a2dd25-17e4-57dd-85cb-4821caaac9cc", "James L Potter"],
  ["5150d932-0b6d-5308-8a44-a08629efad44", "John F Potter"],
] as const;

test("Batch 769 publishes all 22 page profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 769 publishes Leendert Pot's civilian employer separately from his qualified liaison assignment", async ({ page }) => {
  await page.goto("./people/a9b7bf2b-9801-5b02-81c0-968b919ec0dd/");
  const main = page.locator("main");
  await expect(main).toContainText("Leen Pot");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("N.V. Cemsto");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("bedrijfsleider (manager)");
  await expect(main).toContainText("Bureau Inlichtingen");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Museum Engelandvaarders");
});

test("Batch 769 preserves the two duplicate-name pairs without merging their profiles", async ({ page }) => {
  await page.goto("./people/a939f517-51a6-5ca0-a0c2-c14bb0b8a171/");
  await expect(page.locator("main")).toContainText("Compare both Edward G Posniak files");
  await page.goto("./people/d62daae0-cb50-5bbe-9e0e-681181f35c5c/");
  await expect(page.locator("main")).toContainText("Compare both Edward G Posniak files");

  await page.goto("./people/9fa45346-e4a6-5465-b305-56f76c38eb15/");
  await expect(page.locator("main")).toContainText("Box 615 Stanley Potochnik file");
  await page.goto("./people/107e8f80-90bf-5d32-ae75-0d8ee078ed57/");
  await expect(page.locator("main")).toContainText("Box 614 Stanley Potochnik file");
});

test("Batch 769 identity evidence does not expose protected identifiers or infer employers", async ({ page }) => {
  for (const [id] of [profiles[0], profiles[1], profiles[3], profiles[7], profiles[10], profiles[14]]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("official Army");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
  }
});

test("home page exposes the rebuilt Batch 769 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,689");
  await expect(home).toContainText("44.65%");
  await expect(home).toContainText("13,245");
  await expect(home).toContainText("787");
  await expect(home).toContainText("350");
  await expect(home).toContainText("9,147");
});
