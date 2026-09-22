import { expect, test } from "@playwright/test";

test("William McBride receives only the supported Army identity crosswalk", async ({ page }) => {
  await page.goto("./people/3a333fe9-a009-5306-a4d3-415c7d8b07c5/");
  await expect(page.getByRole("heading", { name: "William H McBride", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText("nonshared protected identifier");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.locator("main")).not.toContainText("William E. McBride");
  await expect(page.locator("main")).not.toContainText("William J. McBride");
});

test("Curtis McCammon preserves the middle-initial conflict", async ({ page }) => {
  await page.goto("./people/ba27c39f-9e25-58ff-a2d7-d5e2d4b64304/");
  await expect(page.getByRole("heading", { name: "Curtis B McCammon", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("needs identity review");
  await expect(page.locator("main")).toContainText("indexed B versus Army P");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("the two McCabe index rows remain separate conflicting profiles", async ({ page }) => {
  await page.goto("./people/6b4b6e22-e835-55ae-b7a6-40a112ecb5b7/");
  await expect(page.getByRole("heading", { name: "Ward McCabe", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("same protected identifier");
  await expect(page.locator("main")).toContainText("conflicting sources");

  await page.goto("./people/d7c03613-c5e1-5938-ba61-e2e48cd4941b/");
  await expect(page.getByRole("heading", { name: "William W McCabe", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("same protected identifier");
  await expect(page.locator("main")).toContainText("conflicting sources");
});

test("Batch 628 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,557");
  await expect(page.locator("body")).toContainText("31.57%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("William H McBride");
});
