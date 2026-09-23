import { expect, test } from "@playwright/test";

const profiles = [
  ["e5a2229d-343f-558d-bbb2-d07afafbdcfd", "Eleanor E Mezoff"],
  ["892ad4bf-b660-5415-96bb-30881c91d866", "Jerry G Mican"],
  ["83d4f45d-a2ff-57d8-8618-b398e43f3145", "Charles A Micaud"],
  ["d6c7933c-eb44-5e74-bddc-a85292ab4cbd", "Roman Michalowski"],
  ["454e1a4d-923d-5332-a01d-cb54b1b7129a", "Charles G Micharlis"],
  ["cb79fc4c-3334-54c0-8042-46ce003efa9c", "Stevens S Micheals"],
  ["01e60caa-2990-5cad-bd94-cb65ea7e6501", "Edith F Michel"],
  ["b86c5538-04dd-5f8a-bd3f-1695bacd09d4", "I Michel"],
  ["ff9d2305-b5cf-53af-9afc-015a2617753b", "John D Michel"],
  ["0f8704ad-b193-53d6-99cd-da1ae803ee2f", "Peter R Michel"],
  ["f77e4f38-0b36-509f-bd81-5671aac641f4", "Raoul Michel"],
  ["01a039fd-80db-5d59-8311-14149cc31a74", "Werner J Michel"],
  ["b02dcb6c-af02-552d-b455-e3b59a0821a6", "Alfredo Michelagnoli"],
  ["bb14d547-4139-50d8-8b01-2cc18ba05489", "Gimino Michelangelo"],
  ["ed398425-6a36-57f7-9dc1-9638d15488f7", "Louis Michielini"],
  ["caabbbba-aeb4-554b-a4d8-06b9788de214", "William G Mickey"],
  ["c1b8eaaa-e84f-5e89-b899-6d852b4421b8", "William R Mickey"],
  ["2e716752-8875-55e7-b145-fa2c4ef343b9", "Anthony G Mickus"],
  ["b36d2c53-4eb6-55bd-b3bb-a44a61ea6668", "Ruth R Midkiff"],
  ["95472968-ba8c-55ea-9170-6195539b3b0c", "Charles E Miechle"],
  ["49eaf098-1bb4-59ca-9458-62b683e2bea5", "Wendelin H Miedaner"],
  ["a9f34ccf-4b45-5d62-9dab-47cc1ea07f00", "Jo Mielziner"],
] as const;

test("Batch 656 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 656 separates Mican occupation from his Army pathway", async ({ page }) => {
  await page.goto("./people/892ad4bf-b660-5415-96bb-30881c91d866/");
  const main = page.locator("main");

  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("taught foreign languages at an unidentified Chicago high school");
  await expect(main).not.toContainText("Farragut High School");
});

test("Batch 656 publishes Michalowski's layered institutional chronology", async ({ page }) => {
  await page.goto("./people/d6c7933c-eb44-5e74-bddc-a85292ab4cbd/");
  const main = page.locator("main");

  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Interallied Information Center");
  await expect(main).toContainText("Deputy Director, Research and Reference Division");
  await expect(main).toContainText("New Europe");
});

test("Batch 656 preserves qualified Micaud, Michelagnoli, and Mielziner findings", async ({ page }) => {
  await page.goto("./people/83d4f45d-a2ff-57d8-8618-b398e43f3145/");
  await expect(page.locator("main")).toContainText("Bowdoin College");
  await expect(page.locator("main")).toContainText("Fellow and teaching fellow in French");

  await page.goto("./people/b02dcb6c-af02-552d-b455-e3b59a0821a6/");
  await expect(page.locator("main")).toContainText("Allied troops");
  await expect(page.locator("main")).toContainText("English-language teacher, writer, and film actor");
  await expect(page.locator("main")).toContainText("medium");

  await page.goto("./people/a9f34ccf-4b45-5d62-9dab-47cc1ea07f00/");
  await expect(page.locator("main")).toContainText("Army Air Forces");
  await expect(page.locator("main")).toContainText("Camouflage specialist");
  await expect(page.locator("main")).toContainText("theatrical set and lighting designer");
});

test("Batch 656 leaves both protected-identifier conflicts visible", async ({ page }) => {
  await page.goto("./people/bb14d547-4139-50d8-8b01-2cc18ba05489/");
  await expect(page.locator("main")).toContainText("Lancaster Wade T");
  await expect(page.locator("main")).toContainText("conflicting");

  await page.goto("./people/b86c5538-04dd-5f8a-bd3f-1695bacd09d4/");
  await expect(page.locator("main")).toContainText("Michel M. Ivy");
  await expect(page.locator("main")).toContainText("Box 365");
  await expect(page.locator("main")).toContainText("conflicting");
});

test("Batch 656 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,184");
  await expect(page.locator("body")).toContainText("34.19%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil, petroleum, refining, or exploration companies");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
