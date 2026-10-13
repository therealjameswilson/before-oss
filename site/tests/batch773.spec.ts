import { expect, test } from "@playwright/test";

const profiles = [
  ["0979793f-7178-5ed1-970c-0ba293d749e2", "Philip P Pratt"],
  ["9430d6a0-3184-5344-b259-50b6db22f112", "Richard G Pratt"],
  ["dfdc66ed-75f4-518c-b845-2fa7deda8879", "Barbara S Preble"],
  ["601d766c-241d-5c3d-bc0a-825f74ac504e", "Thomas M Preen"],
  ["981d15f1-7978-5030-bc9d-12c05e27a589", "William B Prendergast"],
  ["fe155e2e-489c-50f3-a87b-7911e56b96d4", "Ruth S Prengel"],
  ["fcd7d6a5-927a-55a5-a665-3ac2c3f539ab", "George Prentice"],
  ["b8900509-93c0-5b7a-8c8c-13a9adc2609d", "Howard V Prenzel"],
  ["18187186-422f-596c-8ec0-c1a634cfe758", "Ethel M Prescott"],
  ["0240fd0d-65bb-53c1-ba04-3a8146465efc", "Henry S Prescott"],
  ["040f3fb8-dc67-5bfe-8b99-0f383fc9533f", "Oscar L Presnell"],
  ["4aa440c6-75d7-5736-a5d3-6fa232e75c53", "Sylvia Press"],
  ["83d1a7f2-474e-5d8d-96d2-d545d63ccc68", "Theodore R Press"],
  ["66df1496-1c22-5076-ab97-a7172c2f24ab", "Van W Pressley"],
  ["5a7da261-0bf2-5f60-9e13-0cc646653eed", "Margaret W Pressly"],
  ["d2ad812b-7536-50cb-b10e-6cc7a19d3a74", "Corinne Pressman"],
  ["3ea5dd8b-fa27-57b2-b916-9f9c0f5b1421", "Julio Prester"],
  ["3d4678fb-cf18-5715-a88a-23f4624b57a9", "Doris W Preston"],
  ["7c7cf8d6-dc89-50f6-aee3-c0ff992b46fa", "Howard J Preston"],
  ["4e305a11-a73e-5e0c-99b4-3854134bb3b2", "James R Preston"],
  ["eab90aa9-e8ed-504e-b8a2-fc08202b4442", "John E Preston"],
  ["f2eaa80b-41c6-5fae-b2dc-6a2b7cba0cfa", "Julia J Preston"],
] as const;

test("Batch 773 publishes all 22 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 773 exposes the Howard V Prenzel identifier-name conflict without adopting the Army name", async ({ page }) => {
  await page.goto("./people/b8900509-93c0-5b7a-8c8c-13a9adc2609d/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("RE E HOWARD V");
  await expect(main).toContainText("surname conflict");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 773 publishes John E Preston's Army identity without converting occupation code 992 into an employer", async ({ page }) => {
  await page.goto("./people/eab90aa9-e8ed-504e-b8a2-fc08202b4442/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("PRESTON JOHN E");
  await expect(main).toContainText("enlisted army personnel");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
  await expect(main).toContainText("coded occupation is not employer evidence");
});

test("Batch 773 does not publish the rejected Howard K Preston newspaper namesake", async ({ page }) => {
  await page.goto("./people/7c7cf8d6-dc89-50f6-aee3-c0ff992b46fa/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("Howard K Preston, not Howard J Preston");
  await expect(main).not.toContainText("Milford chronicle");
});

test("Batch 773 withholds the discovery-only Julio Prester finding-aid lead from public facts", async ({ page }) => {
  await page.goto("./people/3ea5dd8b-fa27-57b2-b916-9f9c0f5b1421/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Persico");
  await expect(main).not.toContainText("Claim-level evidence");
});

test("Batch 773 preserves the indexed commissioned and civilian classifications", async ({ page }) => {
  for (const id of [
    "fcd7d6a5-927a-55a5-a665-3ac2c3f539ab",
    "4e305a11-a73e-5e0c-99b4-3854134bb3b2",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("commissioned army officer");
  }
  for (const id of [
    "18187186-422f-596c-8ec0-c1a634cfe758",
    "5a7da261-0bf2-5f60-9e13-0cc646653eed",
    "d2ad812b-7536-50cb-b10e-6cc7a19d3a74",
    "f2eaa80b-41c6-5fae-b2dc-6a2b7cba0cfa",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("civilian professional or administrative grade");
  }
});

test("Batch 773 masks Thomas M Preen's unusual printed serial value", async ({ page }) => {
  await page.goto("./people/601d766c-241d-5c3d-bc0a-825f74ac504e/");
  await expect(page.locator("main")).not.toContainText("1.31765e+0");
});

test("home page exposes the rebuilt Batch 773 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,781");
  await expect(home).toContainText("45.04%");
  await expect(home).toContainText("13,153");
  await expect(home).toContainText("791");
  await expect(home).toContainText("352");
  await expect(home).toContainText("9,239");
});
