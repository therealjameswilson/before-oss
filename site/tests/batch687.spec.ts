import { expect, test } from "@playwright/test";

const profiles = [
  ["d98f0498-fe46-51b8-bfca-571abe2bb1af", "Edward P Mullen"],
  ["afb46587-4395-5db2-a82b-74f4bfb5c1ba", "Grace M Mullen"],
  ["5d3b7dca-1036-5ac3-a9cc-62ff8a16c730", "Irving L Mullen"],
  ["dcb46380-7ead-55f2-96d0-4bcd894da51f", "Patrick A Mullen"],
  ["74261bdb-04d7-5cd7-a013-e80a33e3cd2a", "Floyd M Muller"],
  ["23ec3ffc-9bea-5de5-83cf-2531355a2d5b", "Robert Muller"],
  ["a21a7067-eafa-5d7a-a5a2-023da3c13b4d", "August J Mullich"],
  ["0ed39823-a672-591b-b076-d9edc7bd54e3", "Eugene G Mulling"],
  ["ec0a1692-1293-5922-8e66-2d7dc03d64a5", "Bennie Mullins"],
  ["91b1c9c3-e429-5137-b258-0829cb125de5", "James H Mullins"],
  ["0da9790b-dab1-52ab-abda-9ad999ef66b9", "Dorothy Mulloly"],
  ["777b74aa-bcd9-51aa-a8d4-4d927bb2cf94", "Donna E Mulloy"],
  ["afb67e49-482c-5c65-9c64-9d8ff3ebe10c", "Joseph E Mulroy"],
  ["ea9048ef-7c41-54f9-a60a-b4f524841daf", "Thomas P Mulvey"],
  ["a7ac682c-5f5f-5994-b7c3-e2a4bd28014d", "Lewis Mumford"],
  ["910fb101-1abd-5511-904d-aec738575104", "Walther Mumm"],
  ["1888afda-308e-5623-8fa9-4b3b1111cd98", "Van I Mumma"],
  ["fa2b9c64-7351-57fd-833f-a97932e41995", "Kaye M Munari"],
  ["3765bb4f-3fc0-50b9-b502-adcdd0b7fe3f", "Ebbe Munck"],
  ["dbbb4282-da8b-5951-852f-2758c5c5c39c", "Jack E Mundell"],
  ["1395be4e-115f-5669-a026-51ab90051ff9", "Gerhardt H Mundinger"],
  ["356e399a-7ab6-5f68-968f-34ac324c2431", "Robert G Mundinger"],
  ["ce3ceaf4-0490-573e-b9fe-e11b60c0a70a", "Roy L Mundy"],
] as const;

test("Batch 687 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Page 334");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
  }
});

test("Batch 687 publishes three protected-identifier matches without inventing employers", async ({ page }) => {
  for (const id of [
    "dcb46380-7ead-55f2-96d0-4bcd894da51f",
    "ec0a1692-1293-5922-8e66-2d7dc03d64a5",
    "afb67e49-482c-5c65-9c64-9d8ff3ebe10c",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 687 keeps Lewis Mumford's New Yorker role earlier, not immediate or last civilian", async ({ page }) => {
  await page.goto("./people/a7ac682c-5f5f-5994-b7c3-e2a4bd28014d/");
  const main = page.locator("main");
  await expect(main).toContainText("The New Yorker");
  await expect(main).toContainText("Staff writer and columnist");
  await expect(main).toContainText("documented prewar");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("The New Yorker");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("The New Yorker");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("The New Yorker");
});

test("Batch 687 publishes Ebbe Munck's last civilian employer without making it immediate", async ({ page }) => {
  await page.goto("./people/3765bb4f-3fc0-50b9-b502-adcdd0b7fe3f/");
  const main = page.locator("main");
  await expect(main).toContainText("Hans Ebbe Munck");
  await expect(main).toContainText("Berlingske Tidende");
  await expect(main).toContainText("strongly date bounded");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Berlingske Tidende");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Berlingske Tidende");
});

test("Batch 687 uses Van Mumma's Team YIELD record for identity, not predecessor employment", async ({ page }) => {
  await page.goto("./people/1888afda-308e-5623-8fa9-4b3b1111cd98/");
  const main = page.locator("main");
  await expect(main).toContainText("SO Team YIELD");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Team YIELD");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Team YIELD");
});

test("Batch 687 preserves all three identifier conflicts without merging people", async ({ page }) => {
  for (const [id, indexed, conflictingName] of [
    ["d98f0498-fe46-51b8-bfca-571abe2bb1af", "Edward P Mullen", "Edward B Mullen"],
    ["1395be4e-115f-5669-a026-51ab90051ff9", "Gerhardt H Mundinger", "Robert G Mundinger"],
    ["356e399a-7ab6-5f68-968f-34ac324c2431", "Robert G Mundinger", "Gerhardt H Mundinger"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: indexed, level: 1 })).toBeVisible();
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(conflictingName);
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 687 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,850");
  await expect(body).toContainText("36.97%");
  await expect(body).toContainText("310");
  await expect(body).toContainText("15,084");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
