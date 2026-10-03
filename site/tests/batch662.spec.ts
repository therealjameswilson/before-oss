import { expect, test } from "@playwright/test";

const profiles = [
  ["f4bf03d6-1a2f-584d-99fc-314ac4246453", "Robert L Miller"],
  ["77be6fb4-b4ac-5255-886d-2d86aceaeff6", "Robert E Miller"],
  ["b9f5cad6-eac8-5d91-b1a5-dc7a47c0e6f1", "Robert H Miller"],
  ["40e2ceb5-bc18-5c00-9daa-3cc3057f7b7a", "Robert L Miller"],
  ["63b51c67-a80a-58b5-81e2-6f1ef8d26a58", "Roberta Miller"],
  ["8629a9a7-9411-59e7-b68d-ec35c9d6a1e4", "Ruby M Miller"],
  ["8f0ac801-9b52-5612-9612-0414b5263558", "Rudolph Miller"],
  ["d85b0ed0-ec17-58de-aab9-4d3ccc8900e5", "Ruth A Miller"],
  ["9ed442e9-7cfe-5213-94c4-df4ca0ff4149", "Stuart D Miller"],
  ["d0868842-bb87-59b1-8844-9dacec5e8037", "Victor L Miller"],
  ["1fcf51bc-bf06-5a23-a1a2-fe3f6c2c7a18", "Victor T Miller"],
  ["54565812-cef5-5831-a477-3e9cf8bf41c5", "Virgil C Miller"],
  ["143f3cd5-6fc4-5287-9f00-529324408c83", "Walter Miller"],
  ["b75e5e53-f3af-57cf-b3c6-dfd93b9ce12b", "Walter Miller"],
  ["6d14fb0d-8c55-5877-aca5-69475ad1b16e", "Walter H Miller"],
  ["76912f44-64c4-53b2-af23-ae1651007c45", "William R Miller"],
  ["406be370-b7c6-53d6-bfaf-f50b4ee2358d", "William H Miller"],
  ["68dcfed9-fb2f-577a-87ed-2f27571867a1", "William F Miller"],
  ["37c759b2-b776-5eb1-a79b-62537cbf9097", "William B Miller"],
  ["fa8fb556-47e7-57cf-a0ea-7a9cba779054", "William S Miller"],
  ["e7b756b7-e872-5d02-884c-60990065a8c8", "Stephen C Millett"],
] as const;

test("Batch 662 publishes all 21 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 662 publishes Roberta Miller's qualified CBS chronology", async ({ page }) => {
  await page.goto("./people/63b51c67-a80a-58b5-81e2-6f1ef8d26a58/");
  const main = page.locator("main");

  await expect(main).toContainText("Columbia Broadcasting System");
  await expect(main).toContainText("Assistant to Edward R. Murrow");
  await expect(main).toContainText("Explicit immediate");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("probably worked");
  await expect(main).toContainText("Texas Jewish Post");
});

test("Batch 662 keeps the Robert H Miller shared-identifier conflict visible", async ({ page }) => {
  await page.goto("./people/b9f5cad6-eac8-5d91-b1a5-dc7a47c0e6f1/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Robert L. Miller Jr.");
  await expect(main).toContainText("Box 526");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 662 keeps Victor Miller's roster corroboration and Army conflict separate", async ({ page }) => {
  await page.goto("./people/d0868842-bb87-59b1-8844-9dacec5e8037/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Greek Operational Group roster");
  await expect(main).toContainText("William P. Rivers");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 662 preserves both William R Miller source rows", async ({ page }) => {
  await page.goto("./people/76912f44-64c4-53b2-af23-ae1651007c45/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Boxes 526 and 527");
  await expect(main).toContainText("526/527");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 662 publishes high-confidence identity evidence without inventing employment", async ({ page }) => {
  await page.goto("./people/77be6fb4-b4ac-5255-886d-2d86aceaeff6/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("protected identifier");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 662 leaves the inaccessible Stephen Millett lead unpublished", async ({ page }) => {
  await page.goto("./people/e7b756b7-e872-5d02-884c-60990065a8c8/");
  const main = page.locator("main");

  await expect(main).toContainText("unresolved");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("Box 527");
  await expect(main).not.toContainText("practiced law in New York");
});

test("Batch 662 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,314");
  await expect(page.locator("body")).toContainText("34.73%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil, petroleum, refining, or exploration companies");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
