import { expect, test } from "@playwright/test";

test("Batch 635 publishes four qualified Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["43fafdd6-80a4-5d5d-9d08-bbca38e8a96f", "Michael V McDowell"],
    ["93a587a3-5e94-5c72-a349-009778e2cfe8", "Paul J McDougall"],
    ["229b4fa8-5af4-5b8a-9980-4b643adfa6f9", "Thomas F McDonnell"],
    ["140aaec5-d714-5803-b14c-9ca1269eb1f0", "William P McDonough"],
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

test("Batch 635 exposes identifier conflicts while withholding unrelated Army identities", async ({
  page,
}) => {
  const profiles = [
    ["c9f2ee69-91f5-5e10-a206-2ddef07ccf37", "Raymond W McDonald"],
    ["53e08adb-c626-5a51-8ed8-3e8111c37709", "Roy W McDonald"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator("main")).toContainText("withheld from public output");
    await expect(page.locator("main")).not.toContainText("Franklin Thornton");
  }

  await expect(page.locator("main")).not.toContainText("Southern Methodist");
  await expect(page.locator("main")).not.toContainText("SMU");
});

test("Batch 635 preserves the two Robert L McDougal rows as separate ambiguous profiles", async ({
  page,
}) => {
  const profiles = [
    "7db9f7df-bf95-5c1f-a059-f03c440c517c",
    "c6a74455-3ace-5b0a-9c9a-ddc2c70770c5",
  ];

  for (const personId of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: "Robert L McDougal", level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText("remain separate");
  }
});

test("rejected Batch 635 newspaper namesakes stay out of public profiles", async ({ page }) => {
  await page.goto("./people/1046b337-77db-5a64-b2e1-58a65ef3eb1a/");
  await expect(page.getByRole("heading", { name: "John J McDonough", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("St. Paul mayor");
  await expect(page.locator("main")).not.toContainText("WPA administrator");

  await page.goto("./people/702b036c-dd0d-5d3d-8758-1eb30ea210ff/");
  await expect(page.getByRole("heading", { name: "Mary B McDonald", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("Batch 635 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,721");
  await expect(page.locator("body")).toContainText("32.25%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Roy W McDonald");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Raymond W McDonald");
});
