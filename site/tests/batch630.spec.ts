import { expect, test } from "@playwright/test";

test("Batch 630 publishes three Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["32ac1b50-5eca-5690-94f1-5ffb7c21472f", "Richard D McCarthy"],
    ["e0f4aa24-f702-52f2-a504-e8f68ff3ba2b", "Lester K McClaflin"],
    ["49607110-dce1-5cc6-baa6-209fcb59625d", "William H McClare"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("nonshared protected identifier");
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Rex McCauley's official-record conflict stays explicit and employment-neutral", async ({
  page,
}) => {
  await page.goto("./people/22ad5999-7308-5fb9-bba2-018ae671ceac/");
  await expect(page.getByRole("heading", { name: "Rex H McCauley", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("Lawrence R. Chambers");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.locator("main")).toContainText("Serial••••7666");
});

test("John McClain's low-confidence occupation lead remains private", async ({ page }) => {
  await page.goto("./people/96af3651-bce6-553d-84d7-1bdddb854c3f/");
  await expect(page.getByRole("heading", { name: "John W McClain", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText("below the project's publication threshold");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.locator("main")).not.toContainText("former reporter");
  await expect(page.locator("main")).not.toContainText("The Ypsilanti Daily Press");
  await expect(page.locator('a[href*="loc.gov/resource/sn97063183"]')).toHaveCount(0);
});

test("the McCaughy, McCcollum, and Mackay variants remain separate", async ({ page }) => {
  const profiles = [
    ["dbbe0d36-756b-5061-87a8-aaab00a15a41", "Edward A McCaughy", "repeated for Sergeant Edward McGaughy"],
    ["b66a5fc2-3989-5316-a346-82a0bf0162a1", "Elmer L McCcollum", "different ranks"],
    ["3cc38cc5-733b-5dbc-9bfb-c8f6f210bed2", "Robert McCay", "Robert Mackay"],
  ];

  for (const [personId, displayName, evidence] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(evidence);
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 630 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,607");
  await expect(page.locator("body")).toContainText("31.78%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("John W McClain");
});
