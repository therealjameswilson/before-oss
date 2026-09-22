import { expect, test } from "@playwright/test";

test("Batch 631 publishes seven Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["7d2e664b-6cf3-5488-9009-cacef28f868d", "Douglas T McClure"],
    ["15d5ee70-c60d-5dc3-a5f1-0471d0b78929", "Floyd F McClintock"],
    ["51b951af-5498-5e4a-8fad-f116c358817a", "Harold C McCollom"],
    ["376a2dba-15b5-5be8-8f4c-5d2de233d6c2", "Jack M McClintock"],
    ["2e2830de-b4c5-5f7a-abb6-f8f8d4d0bb72", "James I McCollum"],
    ["70ff13d0-273c-5aaa-8d83-0d327aab6067", "John J McCole"],
    ["24491f3b-b7bd-5973-94fd-2a0a38b14cf1", "Oscar D McCollum"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("nonshared protected identifier");
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Army suffix variants remain separate from the indexed display names", async ({ page }) => {
  await page.goto("./people/51b951af-5498-5e4a-8fad-f116c358817a/");
  await expect(page.getByRole("heading", { name: "Harold C McCollom", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Harold C McCollom Jr.");
  await expect(page.locator("main")).toContainText("retained as a variant");

  await page.goto("./people/24491f3b-b7bd-5973-94fd-2a0a38b14cf1/");
  await expect(page.getByRole("heading", { name: "Oscar D McCollum", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Oscar D McCollum Jr.");
  await expect(page.locator("main")).toContainText("blank index rank remains unchanged");
});

test("rejected McClelland and McClure newspaper namesakes stay out of public profiles", async ({
  page,
}) => {
  await page.goto("./people/4ea55cbd-0640-5854-9ec4-7eed327cea5d/");
  await expect(page.getByRole("heading", { name: "John P McClelland", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Rev. John J. McClelland");
  await expect(page.locator('a[href*="sn83045462"]')).toHaveCount(0);

  await page.goto("./people/98f1b9e9-918e-5a77-8408-6d6be06e3138/");
  await expect(page.getByRole("heading", { name: "Russell S McClure", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("rodeo cowboy");
  await expect(page.locator('a[href*="sn85053223"]')).toHaveCount(0);
});

test("Batch 631 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,629");
  await expect(page.locator("body")).toContainText("31.87%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Harold C McCollom");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Oscar D McCollum");
});
