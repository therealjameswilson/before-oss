import { expect, test } from "@playwright/test";

const profiles = [
  ["e3e4263a-a991-5945-87df-47ecfc4aaadf", "Fillmore H Sanford"],
  ["1de55cbe-a56b-5ed3-96d4-ae21dd52a2b5", "Henry C Sanford"],
  ["006c432e-db48-55e2-adfc-85efc522f1cc", "Jay R Sanford"],
  ["4253f566-1fbc-5985-881f-847aaae3f226", "Lyle Sanford"],
  ["30fc6f2b-2ecb-5b58-9092-8dd28524e262", "Robert N Sanford"],
  ["4a8b7072-911d-5363-8c7a-a15077ad2a83", "Thomas J Sanford"],
  ["ccda3ab9-f651-5dde-b757-227cca8a4532", "Alfred N Sangari"],
  ["c3a05a64-75ed-5930-ae4e-db7c7e0215c3", "Eugene Sanguinetti"],
  ["25f3b963-4544-592b-adc2-3269a284cb3d", "Melvin E Sangwin"],
  ["c7625ad1-e65a-5bc0-ab1a-af6163346a93", "Virginia B Sangwin"],
  ["3e5bb795-44c1-5076-8733-53bb10d6cbd7", "William C Sankey"],
  ["f0ef41b8-1f22-5cde-b5c0-1cc5d7b406ac", "Victor L Sanko"],
  ["9f45f820-05ab-5251-94ef-4eca1771d4a2", "Charles R Sanneman"],
  ["88b6fb87-473e-5788-a5c7-61cc0b7b0330", "Daniel M Sannit"],
  ["808a5479-4dfe-5df8-b49e-ec37fdb261a2", "Thomas R Sansone"],
  ["a485132d-3c69-5174-ab85-380af10dd4f0", "Edward G Santangelo"],
  ["f945c19f-3c14-5ab8-aeb0-a843d66f5180", "Marcello L Santarelli"],
  ["939cc4a6-c933-5cd4-8f56-f1ec2b804993", "Jordan F Santina"],
  ["5cae3b90-965a-57d2-a992-fc3bb7210a01", "Idilia Santini"],
  ["b05d4479-7cc9-5f0f-a2fa-c66c4203a44e", "Joseph Santora"],
  ["cba07b7f-16d4-5e97-ad71-d9d5d6cedda5", "Charles J Santoro"],
  ["fd973cbd-3fdd-5969-84d7-c58a757504a0", "Joseph A Santry"],
  ["5bf8243c-4373-51e4-943c-7cc4523aeb1e", "Anthony Santucci"],
] as const;

test("Batch 837 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Fillmore Sanford publishes Harvard student status as documented prewar, not employment", async ({ page }) => {
  await page.goto("./people/e3e4263a-a991-5945-87df-47ecfc4aaadf/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("doctoral student in psychology");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("not shown to be the immediate predecessor relationship");
  await expect(main).not.toContainText("Harvard University employed");
});

test("accepted Army crosswalks publish identity only and keep protected fields private", async ({ page }) => {
  for (const id of [
    "1de55cbe-a56b-5ed3-96d4-ae21dd52a2b5",
    "4253f566-1fbc-5985-881f-847aaae3f226",
    "4a8b7072-911d-5363-8c7a-a15077ad2a83",
    "25f3b963-4544-592b-adc2-3269a284cb3d",
    "f0ef41b8-1f22-5cde-b5c0-1cc5d7b406ac",
    "808a5479-4dfe-5df8-b49e-ec37fdb261a2",
    "b05d4479-7cc9-5f0f-a2fa-c66c4203a44e",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Army occupation code");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("middle-initial disagreements remain visible and require archival review", async ({ page }) => {
  for (const [id, indexedInitial, armyInitial] of [
    ["88b6fb87-473e-5788-a5c7-61cc0b7b0330", "middle initial M", "prints N"],
    ["939cc4a6-c933-5cd4-8f56-f1ec2b804993", "middle initial F", "prints E"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(indexedInitial);
    await expect(main).toContainText(armyInitial);
    await expect(main).toContainText("requires archival review");
  }
});

test("Army name conflicts remain visible without publishing the candidate names", async ({ page }) => {
  for (const id of [
    "a485132d-3c69-5174-ab85-380af10dd4f0",
    "5bf8243c-4373-51e4-943c-7cc4523aeb1e",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("completely different name");
    await expect(main).toContainText("no Army biography, occupation or employer is assigned");
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("Joseph Santry keeps unsupported namesake careers unassigned", async ({ page }) => {
  await page.goto("./people/fd973cbd-3fdd-5969-84d7-c58a757504a0/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Federal Reserve Bank employee");
  await expect(main).toContainText("Neither career is assigned");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationFederal Reserve");
});
