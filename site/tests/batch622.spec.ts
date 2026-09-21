import { expect, test } from "@playwright/test";

test("Manaloe and Manoloe remain separate same-identifier variants", async ({ page }) => {
  const cases = [
    ["e48018de-7e7c-55dd-9463-a85918f30847", "Marcus Manaloe"],
    ["e39610c5-3508-5326-b6e8-7bc7f5844670", "Marcus Manoloe"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/same private identifier|repeats the private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Manierre and Manniere expose the shifted-number evidence", async ({ page }) => {
  const cases = [
    ["c8ea75e3-3284-5cde-bad9-dd273eb64ca7", "Cyrus E Manierre"],
    ["392fe164-4c4f-5874-98e4-b5fc5fba6129", "Cyrus E Manniere"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/rank column|identifier placement/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("exact repeated index rows stay linked to one person entity", async ({ page }) => {
  const cases = [
    ["b8ae54d3-5969-5238-a9bb-2300b9407a78", "Augustine J Maratzo"],
    ["04f9bd64-030a-54eb-83e9-97c40d3f1e0d", "Edward Marchigiani"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText(/two .* rows|two immutable source rows/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Robert March and Marck retain the one-digit conflict", async ({ page }) => {
  const cases = [
    ["4db308d3-43af-5fa2-a297-2c27383e429b", "Robert K March"],
    ["ea9d802b-77c3-5615-85ec-b549f52b237e", "Robert K Marck"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/first printed (?:identifier )?digit/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("cross-page identifier conflicts stay visible without merging", async ({ page }) => {
  const cases = [
    ["45a59ffc-eaac-581c-80ff-393af6e87fb4", "Herbert D Marcy"],
    ["48867a9a-9f06-5030-81f9-0dd9653fd321", "Robert S Mantho"],
    ["974a420d-0ec8-5cde-ad74-70357b5d6f2a", "John Manual"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator("main")).toContainText(/same private identifier|repeated private identifier/i);
    await expect(page.locator("main")).toContainText("critical");
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Marnocaa and Marnocha and the three Marritts forms remain explicit variants", async ({ page }) => {
  const cases = [
    ["5f2ac5f3-3165-5f9a-8773-de9beda50d77", "Richard S Marnocaa"],
    ["f2d841bd-ea19-5b97-b16d-7152373af21a", "Richard S Marnocha"],
    ["84cbf17c-b33e-58d2-ab99-4b7aaf44e83c", "William L Marritts"],
    ["7b5cf14b-f5b5-58b4-bab2-a6ff99802643", "William L Meritts"],
    ["e9a37a58-d576-543c-90c0-77421678dadb", "William L Merritts"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/same private identifier|shares a private identifier|repeats the private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Eugene Mathews and Matthews expose both duplicate and conflict evidence", async ({ page }) => {
  const cases = [
    ["5ae134b6-03a7-56fa-9a37-a6077ed848fe", "Eugene K Mathews", "ambiguous"],
    ["25689d5d-02b6-5777-afd0-5053e025dec6", "Eugene K Matthews", "ambiguous"],
    ["c91e6700-1847-531b-9b16-ea7876434623", "Eugene K Matthews", "conflicting"],
    ["e56f66cd-9fe3-5322-926b-a103a02141cf", "Ramond P St. Laurent", "conflicting"],
  ];
  for (const [id, name, status] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText(status);
    await expect(page.locator("main")).toContainText(/Eugene K Mathews|St\. Laurent|private identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Batch 622 keeps the oil-company evidence set unchanged", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Gene Mako");
});
