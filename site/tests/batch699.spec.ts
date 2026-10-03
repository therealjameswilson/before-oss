import { expect, test } from "@playwright/test";

const profiles = [
  ["262e397a-9490-547f-bdf6-dea50bd04c58", "James A Nelson"],
  ["aea51292-dbab-5509-a109-5368d239c6f0", "John T Nelson"],
  ["7c19abc8-5933-5d8b-9e45-925190394edd", "Leonard A Nelson"],
  ["88e588f6-5c9a-53c3-bf5b-b0f3932a33f6", "M A Nelson"],
  ["fffe1351-0f64-5638-ae9d-b860f0c7d386", "Marian L Nelson"],
  ["40867c66-a36f-5a3b-a8b4-80df7851c94e", "Orval D Nelson"],
  ["584ef9b3-4139-5834-8338-e47413f3c99c", "Oscar K Nelson Jr."],
  ["390bb8d7-6c00-534e-b0ab-6c9b23a3fc3d", "Paul B Nelson"],
  ["184420ff-ea96-5ba7-8d52-336bca79bc2c", "Ralph L Nelson Jr."],
  ["e3300a50-50c2-552f-808b-832224983c29", "Raymond A Nelson"],
  ["137f57d6-bfa4-59b6-8606-8ed686fd3d10", "Robert A Nelson"],
  ["0fce5f7e-d13f-5bf3-aa6a-b0e2488d585f", "Robert C Nelson"],
  ["e4ff92f6-d35d-5fb7-99b8-df201edf564b", "Ronald H Nelson"],
  ["5b8c6f30-a26b-5562-8eab-b87786d5a6d6", "Vern W Nelson"],
  ["f779ea27-b42a-5921-893c-4a480472cc5e", "Walter W Nelson"],
  ["15c108b1-3187-5a2b-8203-eaa6a8d5ed12", "James M Nelson. III"],
  ["8a5207a4-b5d9-5ee9-9565-9e34fc03beee", "Charles M Nemec"],
  ["0a09b94c-55d6-5c44-9aa6-821ed75eeb5f", "John A Nemecz"],
  ["d36b57d2-07e2-5be6-8b2d-fb3b2b18eee8", "Peter Nemekofsky"],
  ["f08461ef-d84c-5af0-948e-20841dd2ad37", "Conrad R Nemeth"],
  ["5b959f12-6f20-51b7-8260-11fa878a8e9f", "Peter N Nemeth"],
  ["4f783983-7b1e-5b86-b7bf-dc775fd5737a", "Walter C Nemetz"],
  ["a3d65e4f-84da-5472-99b3-6fbff6cdd201", "Lubitsa Nenadovich"],
] as const;

test("Batch 699 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{7,8}$/);
  }
});

test("Batch 699 publishes identity-only decisions without inventing affiliations", async ({ page }) => {
  for (const id of [
    "aea51292-dbab-5509-a109-5368d239c6f0",
    "40867c66-a36f-5a3b-a8b4-80df7851c94e",
    "584ef9b3-4139-5834-8338-e47413f3c99c",
    "e3300a50-50c2-552f-808b-832224983c29",
    "5b8c6f30-a26b-5562-8eab-b87786d5a6d6",
    "5b959f12-6f20-51b7-8260-11fa878a8e9f",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Batch 699 keeps both protected-identifier conflicts visible", async ({ page }) => {
  await page.goto("./people/7c19abc8-5933-5d8b-9e45-925190394edd/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflict");
  await expect(main).toContainText("FELLOWS ROBERT R");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/0a09b94c-55d6-5c44-9aa6-821ed75eeb5f/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflict");
  await expect(main).toContainText("RAY ROBERT");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 699 preserves difficult names and explains archival next steps", async ({ page }) => {
  await page.goto("./people/15c108b1-3187-5a2b-8203-eaa6a8d5ed12/");
  let main = page.locator("main");
  await expect(main).toContainText("James M Nelson. III");
  await expect(main).toContainText("source literally prints the surname as Nelson. III");
  await expect(main).toContainText("Archive box555");
  await expect(main).toContainText("Archival-review priorityhigh");

  await page.goto("./people/a3d65e4f-84da-5472-99b3-6fbff6cdd201/");
  main = page.locator("main");
  await expect(main).toContainText("Lubitsa Nenadovich");
  await expect(main).toContainText("lack a direct OSS bridge");
  await expect(main).toContainText("Archive box556");
  await expect(main).toContainText("Archival-review priorityhigh");
});

test("Batch 699 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("9,121");
  await expect(body).toContainText("38.10%");
  await expect(body).toContainText("317");
  await expect(body).toContainText("14,813");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
