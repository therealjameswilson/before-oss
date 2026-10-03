import { expect, test } from "@playwright/test";

const profiles = [
  ["f9e78b94-4f1c-522e-8a96-858fd04dc896", "Irby E Moree"],
  ["c1ed6da3-3b64-5ed5-ba92-4cdf18638f3b", "Raymound O Morehouse"],
  ["73c016fb-f962-5a4e-9cd4-62a773066a5b", "Obel Moreira Jr."],
  ["04deb36c-72fd-558c-a427-4e82796a7675", "Gerard Moreli"],
  ["a74411a9-1fd9-5537-835f-3263cc6e511c", "Bernard Morelli"],
  ["96a30605-69c7-5653-9083-1449e4ab5104", "Betty Morelli"],
  ["028f4423-3632-5eed-b3d5-ac5ce4159acf", "Emil S Morelli"],
  ["a9c5b01d-9b11-5bf9-9e84-1c32bbc9bf10", "Ettore Morelli"],
  ["ad03d7fa-5ea0-5daf-8961-f2f26bcd30fa", "Courtland C Morelock"],
  ["07d16650-f9c8-52f2-a18d-47f56c486194", "Robert C Moreno"],
  ["e87eba5a-b3ad-52ec-ac07-d2c5d198709f", "Jean Morere"],
  ["1372ab39-0237-5991-8759-4f952a72209a", "Cesare A Moretti"],
  ["702707b1-d944-5652-9c0f-de762f271dd3", "John T Morey"],
  ["4234cd66-9852-5071-9e10-ebd0f3b5715b", "Anna P Morgan"],
  ["34c7f795-525c-5be1-8a98-340d05d3d826", "Benjamin T Morgan"],
  ["4a532ed7-0f12-5ff2-9e21-06cfb2034e2d", "Charles P Morgan"],
  ["45e51449-9a45-57b2-8291-2eaf7324ed1f", "Elliot W Morgan"],
  ["6132aa89-ccf5-5f06-a19c-1e7b0d7c427c", "Elwyn W Morgan"],
  ["5c667566-e44e-5d04-a1ea-4eb25398f71a", "Forrest A Morgan"],
  ["7513e5f6-f9d7-5982-9d70-fa1195a0446e", "Gabriel W Morgan"],
  ["2765a28d-42ab-5d48-84d1-e28a05d4bb55", "George M Morgan"],
  ["93cb2bc3-f15d-5665-acf3-be9a31f4fdb1", "Glen Morgan"],
  ["290e2ee9-ab5f-58c6-bf45-91bfc4e48eb0", "Harry S Morgan"],
  ["3c41b7ee-ab55-5b8e-97b3-9964110dd196", "Helen E Morgan"],
] as const;

const armyMatches = [
  ["c1ed6da3-3b64-5ed5-ba92-4cdf18638f3b", "Raymound O Morehouse", "999"],
  ["a74411a9-1fd9-5537-835f-3263cc6e511c", "Bernard Morelli", "401"],
  ["028f4423-3632-5eed-b3d5-ac5ce4159acf", "Emil S Morelli", "992"],
  ["a9c5b01d-9b11-5bf9-9e84-1c32bbc9bf10", "Ettore Morelli", "999"],
  ["ad03d7fa-5ea0-5daf-8961-f2f26bcd30fa", "Courtland C Morelock", "586"],
  ["1372ab39-0237-5991-8759-4f952a72209a", "Cesare A Moretti", "627"],
  ["34c7f795-525c-5be1-8a98-340d05d3d826", "Benjamin T Morgan", "999"],
  ["45e51449-9a45-57b2-8291-2eaf7324ed1f", "Elliot W Morgan", "120"],
  ["6132aa89-ccf5-5f06-a19c-1e7b0d7c427c", "Elwyn W Morgan", "736"],
] as const;

const unresolved = [
  ["73c016fb-f962-5a4e-9cd4-62a773066a5b", "Obel Moreira Jr."],
  ["04deb36c-72fd-558c-a427-4e82796a7675", "Gerard Moreli"],
  ["96a30605-69c7-5653-9083-1449e4ab5104", "Betty Morelli"],
  ["07d16650-f9c8-52f2-a18d-47f56c486194", "Robert C Moreno"],
  ["702707b1-d944-5652-9c0f-de762f271dd3", "John T Morey"],
  ["4234cd66-9852-5071-9e10-ebd0f3b5715b", "Anna P Morgan"],
  ["4a532ed7-0f12-5ff2-9e21-06cfb2034e2d", "Charles P Morgan"],
  ["5c667566-e44e-5d04-a1ea-4eb25398f71a", "Forrest A Morgan"],
  ["7513e5f6-f9d7-5982-9d70-fa1195a0446e", "Gabriel W Morgan"],
  ["2765a28d-42ab-5d48-84d1-e28a05d4bb55", "George M Morgan"],
  ["93cb2bc3-f15d-5665-acf3-be9a31f4fdb1", "Glen Morgan"],
  ["290e2ee9-ab5f-58c6-bf45-91bfc4e48eb0", "Harry S Morgan"],
  ["3c41b7ee-ab55-5b8e-97b3-9964110dd196", "Helen E Morgan"],
] as const;

test("Batch 677 publishes all 24 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 329");
    await expect(page.locator("main")).toContainText("Archive box537");
  }
});

test("Batch 677 publishes nine Army identity matches without employer inference", async ({ page }) => {
  for (const [id, name, privateOccupationCode] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(`occupation code ${privateOccupationCode}`);
    await expect(main).not.toContainText(`civilian_occupation_code=${privateOccupationCode}`);
  }
});

test("Batch 677 preserves printed spelling while exposing reviewed variants", async ({ page }) => {
  await page.goto("./people/c1ed6da3-3b64-5ed5-ba92-4cdf18638f3b/");
  await expect(page.getByRole("heading", { name: "Raymound O Morehouse", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Raymond O Morehouse");

  await page.goto("./people/028f4423-3632-5eed-b3d5-ac5ce4159acf/");
  await expect(page.getByRole("heading", { name: "Emil S Morelli", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("MOR LLI EMIL S");

  await page.goto("./people/a9c5b01d-9b11-5bf9-9e84-1c32bbc9bf10/");
  await expect(page.getByRole("heading", { name: "Ettore Morelli", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("MORELL ETTORE R");
});

test("Batch 677 identifies Irby Moree without turning OSS duties into pre-OSS employment", async ({ page }) => {
  await page.goto("./people/f9e78b94-4f1c-522e-8a96-858fd04dc896/");
  const main = page.locator("main");
  await expect(main).toContainText("Detachment 101");
  await expect(main).toContainText("Area B");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 677 publishes Morère's last civilian employer without calling it immediate", async ({ page }) => {
  await page.goto("./people/e87eba5a-b3ad-52ec-ac07-d2c5d198709f/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Jean Morere", level: 1 })).toBeVisible();
  await expect(main).toContainText("Jean-Marie Morère");
  await expect(main).toContainText("Marseille Police");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("1 May 1921");
  await expect(main).toContainText("not labeled immediate");
  await expect(main).toContainText("GR 28 P 4 396 / 143");
});

test("Batch 677 gives all 13 unresolved people terminal research pages", async ({ page }) => {
  for (const [id, name] of unresolved) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Archival-review priorityhigh");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 677 publishes exact coverage and keeps the oil-company category strict", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,626");
  await expect(page.locator("body")).toContainText("36.03%");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil companies");
  await expect(category).not.toContainText("Wesley C Morck");

  await page.goto("./people/");
  const directoryCategory = page.locator(".featured-directory-category");
  await expect(directoryCategory.locator("li")).toHaveCount(8);
  await expect(directoryCategory).not.toContainText("Wesley C Morck");
});
