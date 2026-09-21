import { expect, test } from "@playwright/test";

test("page 281 exposes the three-name identifier conflict without merging", async ({ page }) => {
  const cases = [
    ["889b2f82-4339-50fe-add5-0c208048563f", "Patsy W Loconto"],
    ["668221c0-1ef1-54c9-b4f0-d39a94fd5b68", "Max Loeb"],
    ["21858b21-d332-58a9-a33f-626d75015d79", "Robert D Loeb"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator("main")).toContainText(/same private identifier|repeats the private identifier/i);
    await expect(page.locator("main")).toContainText("critical");
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("the second Max Loeb remains a separate ambiguous officer row", async ({ page }) => {
  await page.goto("./people/e72db339-4d72-57f9-a2b9-246185825383/");
  await expect(page.getByRole("heading", { name: "Max Loeb", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("ambiguous");
  await expect(page.locator("main")).toContainText(/private identifier different from/i);
  await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
});

test("same-identifier spelling variants remain separate", async ({ page }) => {
  const cases = [
    ["faa590d7-cc71-5602-a8f8-516ea5b54623", "David R Longenecker"],
    ["1fa20bda-ad58-5b76-a918-151b5f25e3d7", "David R Longnecker"],
    ["8c728c9f-3a0c-53d5-81e0-c217275ac1c9", "John P Macaulay"],
    ["ecae53bf-2a5b-5976-b7fd-a95f621b5c95", "John P Macauley"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/same private identifier|repeats the private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Luciani and Luciano expose the alias question without a merge", async ({ page }) => {
  const cases = [
    ["ba835265-1966-5cf9-8dc5-13415bef2f33", "John P Luciani"],
    ["bc591ef6-448b-5086-affe-2c7eb88f412b", "Michael Luciano"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/alias|index conflict|\?Lucky\?|private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Mackay and McCay retain cross-page source spellings", async ({ page }) => {
  const cases = [
    ["b2da3b89-0942-5b61-a402-b17d1759dc16", "Robert Mackay"],
    ["3cc38cc5-733b-5dbc-9bfb-c8f6f210bed2", "Robert McCay"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/same private identifier|repeats the private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("all three Robert B MacLeod entries remain separate", async ({ page }) => {
  const ids = [
    "ac210fe4-e532-5413-990b-fc09d1a4e1ef",
    "2c9c428b-91e7-5b97-a6e3-6176c1b5cd73",
    "94c14a7e-15b8-522c-b58f-dc6feb24f43d",
  ];
  for (const id of ids) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Robert B MacLeod", level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/Box 472|Box 510/);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Batch 621 keeps the oil-company evidence set unchanged", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Max Loeb");
});
