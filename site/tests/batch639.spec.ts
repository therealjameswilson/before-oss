import { expect, test } from "@playwright/test";

test("Batch 639 publishes qualified Army identities without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["7e6b3058-a30c-5328-bec0-1deb39bcae80", "Arthur P McGowan"],
    ["7beb9f96-3fa1-509a-9ac4-c62cfd9e9eec", "William H McGowan"],
    ["aff7f748-6f2f-5903-9959-115b25b02d53", "Charles E McGrath"],
    ["3bb3ab9d-4e83-5cd7-840a-8681229a6f70", "William McGrath"],
    ["83cd6e0c-36d4-571f-9a99-fa7c96c24cb3", "Edward J McGuire"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("protected identifier");
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("Batch 639 preserves the McGown variant and archival qualification", async ({ page }) => {
  await page.goto("./people/7e6b3058-a30c-5328-bec0-1deb39bcae80/");
  await expect(page.locator("main")).toContainText("Arthur P McGown");
  await expect(page.locator("main")).toContainText("Box 506");
  await expect(page.locator("main")).toContainText("manual review");
});

test("Batch 639 keeps both John E McGowan rows separate and ambiguous", async ({ page }) => {
  const profiles = [
    ["8cb882e2-137b-5126-96c5-c3415e716d7f", "Lieutenant"],
    ["5b3f8268-a841-5291-8096-84d6bdc48b8d", "Technician Third Grade"],
  ];

  for (const [personId, rank] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: "John E McGowan", level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(rank);
    await expect(page.locator("main")).toContainText("Box 506");
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("rejected Batch 639 namesakes stay out of public profiles", async ({ page }) => {
  await page.goto("./people/32ab45a5-822e-5015-973c-f81f40d74361/");
  await expect(page.locator("main")).not.toContainText("Homer Laughlin");
  await expect(page.locator("main")).not.toContainText("pottery-union");

  await page.goto("./people/83cd6e0c-36d4-571f-9a99-fa7c96c24cb3/");
  await expect(page.locator("main")).not.toContainText("real-estate attorney");
});

test("Batch 639 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,809");
  await expect(page.locator("body")).toContainText("32.62%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("McGowan");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McGrath");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McGuire");
});
