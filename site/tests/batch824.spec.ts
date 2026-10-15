import { expect, test } from "@playwright/test";

const profiles = [
  ["b6319395-8af9-531c-baa5-bc624e962f11", "Maurice H Rottersmann"],
  ["4600ba5d-9a5b-5e6f-98d4-922d3489ce32", "Lars N Rottinger"],
  ["1a8a558e-f332-530a-9f10-99b46a6ec279", "Marcello G Rotundo"],
  ["66411067-ceeb-5dd8-b01d-529e149b6650", "Dorothy Rouden"],
  ["d2089639-305b-53c1-bc42-30329693d98e", "Leland L Rounds"],
  ["e8d2bc67-6b8f-5d16-8a3a-857bc307cc8b", "Scott S Rouse"],
  ["7d27af9f-026d-5591-8424-ee06e18fef92", "Howard P Roush"],
  ["cc9ad061-c134-5d44-8fbe-46ef6a11d564", "Raymond Rousseau"],
  ["29b45c50-ab50-572e-b6a5-5de049261dd9", "Theodore Rousseau"],
  ["239beda7-ef58-5884-8986-53dd5a3d03f0", "Theodore J Rousses"],
  ["8ac10da2-d889-58a6-9c93-e2f4951e4a0c", "George Routis"],
  ["68a1b908-b98d-511d-bf3d-b6e959093e40", "Kostas Routis"],
  ["a7d7d4de-45c0-5f35-b669-3cae20a8c396", "William B Routt"],
  ["0babead9-145f-53c0-9573-2ca3a7047f13", "Peter J Rovang"],
  ["0143e173-76b0-5fa4-b2ab-e8cf8ee3790d", "John Rovello"],
  ["6a0b270a-ba6d-5253-b9f9-3c4d253fea3e", "Robert R Rovzar"],
  ["c0fb8629-69d8-5a73-9917-fb56cb4ad718", "Wesley J Rowan"],
  ["beb9634f-62f5-5748-9be5-cb2319f43543", "Charles A Rowan Jr."],
  ["ece4a54f-4b9e-5072-9587-864c934a5e38", "John W Roward Jr."],
  ["8c31386d-898e-57f5-b6f9-afe24d84f85b", "Alvin T Rowe"],
  ["0ae56377-47e6-5278-8c31-e6e10fbff78e", "David N Rowe"],
  ["cd78d413-1add-547d-9de0-f4748b33a216", "Harrison A Rowe"],
  ["869acdea-9df8-51ba-84e0-54d034df3ab2", "Thora H Rowe"],
] as const;

test("Batch 824 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Lars Rottinger profile labels the 99th Battalion as a military pathway", async ({ page }) => {
  await page.goto("./people/4600ba5d-9a5b-5e6f-98d4-922d3489ce32/");
  const main = page.locator("main");
  await expect(main).toContainText("99th Infantry Battalion");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
});

test("Theodore Rousseau profile separates civilian Gallery work from naval service", async ({ page }) => {
  await page.goto("./people/29b45c50-ab50-572e-b6a5-5de049261dd9/");
  const main = page.locator("main");
  await expect(main).toContainText("National Gallery of Art");
  await expect(main).toContainText("Assistant Curator of Painting");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("United States Naval Reserve");
  await expect(main).toContainText("probable immediate");
});

test("David Rowe profile preserves overlapping university and federal roles", async ({ page }) => {
  await page.goto("./people/0ae56377-47e6-5278-8c31-e6e10fbff78e/");
  const main = page.locator("main");
  await expect(main).toContainText("David Nelson Rowe");
  await expect(main).toContainText("Princeton University");
  await expect(main).toContainText("Department of Justice");
  await expect(main).toContainText("Library of Congress");
  await expect(main).toContainText("overlap");
});

test("Robert Rovzar profile treats Georgetown as study and Airborne service as qualified", async ({ page }) => {
  await page.goto("./people/6a0b270a-ba6d-5253-b9f9-3c4d253fea3e/");
  const main = page.locator("main");
  await expect(main).toContainText("Georgetown University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("82nd Airborne Division");
  await expect(main).toContainText("medium");
});

test("Army identity-only matches remain without invented employers", async ({ page }) => {
  for (const id of [
    "1a8a558e-f332-530a-9f10-99b46a6ec279",
    "c0fb8629-69d8-5a73-9917-fb56cb4ad718",
    "8c31386d-898e-57f5-b6f9-afe24d84f85b",
    "cd78d413-1add-547d-9de0-f4748b33a216",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Maurice Rottersmann duplicate conflict remains visible and unmerged", async ({ page }) => {
  await page.goto("./people/b6319395-8af9-531c-baa5-bc624e962f11/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Maurice H Rottersmann", level: 1 })).toBeVisible();
  await expect(main).toContainText("Maurice H. Rettersmann");
  await expect(main).toContainText("different printed surnames");
  await expect(main).toContainText("conflicting sources");
});

test("Rejected Army spelling conflicts remain qualified", async ({ page }) => {
  const cases = [
    ["239beda7-ef58-5884-8986-53dd5a3d03f0", "Theodore J. Roussos"],
    ["8ac10da2-d889-58a6-9c93-e2f4951e4a0c", "George Reutsis"],
    ["68a1b908-b98d-511d-bf3d-b6e959093e40", "Oostas Routsis"],
    ["0babead9-145f-53c0-9573-2ca3a7047f13", "Peter J. Rovano"],
    ["ece4a54f-4b9e-5072-9587-864c934a5e38", "Robert J. King"],
  ] as const;
  for (const [id, conflictingName] of cases) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText(/rejected/i);
  }
});
