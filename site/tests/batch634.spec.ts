import { expect, test } from "@playwright/test";

test("Batch 634 publishes five qualified Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["718ff7d4-e469-544e-993c-1f77cc15c5ab", "Gene A McDaniel"],
    ["646b8baa-726e-5da5-9373-5d3515172cad", "Dewey E McDonald"],
    ["f90d6015-81a6-5a84-9aa7-cdd915fd85d8", "George S McDonald"],
    ["71d34770-f8fd-58ce-af88-2e1ec03f3cdb", "Georgie R McDonald"],
    ["37afadbd-0cb9-57cf-bd84-3226c1cec7c6", "Jasper N McDonald"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("nonshared protected identifier");
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("Batch 634 exposes the James E McDaniel conflict without leaking the other Army name", async ({
  page,
}) => {
  await page.goto("./people/38ffc93e-398c-5040-839b-16e2d30592d7/");
  await expect(page.getByRole("heading", { name: "James E McDaniel", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("wholly different name");
  await expect(page.locator("main")).toContainText(
    "the number and other person's name are withheld from public output",
  );
  await expect(page.locator("main")).not.toContainText("Turner Donald G");
});

test("Batch 634 preserves Dervey and Hervey as separate ambiguous profiles", async ({ page }) => {
  const profiles = [
    ["24c85fe3-ff5a-5a8d-a9fd-14eeac196896", "Dervey A McDonald"],
    ["7498979d-3069-5bd2-8ab0-748855fec83d", "Hervey A McDonald"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText("different ranks");
    await expect(page.locator("main")).toContainText("remain separate entities");
  }
});

test("rejected Batch 634 newspaper namesakes stay out of public profiles", async ({ page }) => {
  await page.goto("./people/3a39a26c-73bb-57c3-bdef-a51432ef2aea/");
  await expect(page.getByRole("heading", { name: "James E McDonald", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("commissioner of agriculture of Texas");
  await expect(page.locator('a[href*="sn83045462/1953-01-31"]')).toHaveCount(0);

  await page.goto("./people/6b65de24-e2b7-542c-a082-6c955d02ddf2/");
  await expect(page.getByRole("heading", { name: "Joseph E McDonald", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Joseph B. McDonald");
  await expect(page.locator('a[href*="sn83045462/1938-08-13"]')).toHaveCount(0);
});

test("Batch 634 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,698");
  await expect(page.locator("body")).toContainText("32.16%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("James E McDaniel");
  await expect(page.locator(".oil-directory__list")).not.toContainText("George S McDonald");
});
