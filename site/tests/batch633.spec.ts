import { expect, test } from "@playwright/test";

test("Batch 633 publishes three qualified Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["5086d94f-a417-54b8-ba0b-0f30e293fc43", "Howard P McCormick"],
    ["cd75924a-d04d-5585-96c4-4f2d4d8f3841", "John F McCormick"],
    ["4917ebd7-ee43-5e3a-9461-7415c965375d", "Charles McCracken Jr."],
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

test("Batch 633 keeps Frank R McCoy probable and temporally qualified", async ({ page }) => {
  await page.goto("./people/adbb1da1-14ea-5d70-9445-9b429be33320/");
  await expect(page.getByRole("heading", { name: "Frank R McCoy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText("Major General Frank R. McCoy probably corresponds");
  await expect(page.locator("main")).toContainText(
    "do not establish when or why an OSS personnel file was created",
  );
  await expect(page.locator('a[href*="sn85060004"]')).toHaveCount(1);
  await expect(page.locator('a[href*="sn82015425"]')).toHaveCount(1);
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 633 exposes the William J McCoy conflict without leaking the other Army name", async ({
  page,
}) => {
  await page.goto("./people/4ee3c4a3-b18c-55e5-a6ae-6605402b86de/");
  await expect(page.getByRole("heading", { name: "William J McCoy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("wholly different name and a different grade");
  await expect(page.locator("main")).toContainText(
    "the number is withheld from public output",
  );
  await expect(page.locator("main")).not.toContainText("Clayton F. Blinkman");
  await expect(page.locator("main")).not.toContainText("Putnam Woolen Corporation");
});

test("rejected Batch 633 newspaper namesakes stay out of public profiles", async ({ page }) => {
  await page.goto("./people/ce1f1a7b-e464-56e3-b497-5061e75aebeb/");
  await expect(page.getByRole("heading", { name: "John I McCormick", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("John L. McCormick");
  await expect(page.locator('a[href*="sn84020662"]')).toHaveCount(0);

  await page.goto("./people/c26ef12a-eaa3-5b80-b868-781e4866491c/");
  await expect(page.getByRole("heading", { name: "Robert W McCormick", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Chicago Tribune");
  await expect(page.locator('a[href*="sn78002169"]')).toHaveCount(0);
});

test("Batch 633 publishes the new coverage checkpoint and retains the oil category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,675");
  await expect(page.locator("body")).toContainText("32.06%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Frank R McCoy");
  await expect(page.locator(".oil-directory__list")).not.toContainText("William J McCoy");
});
