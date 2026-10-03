import { expect, test } from "@playwright/test";

const profiles = [
  ["827ffc3e-a442-53c8-bf68-f9a146b96f50", "Christo Nicholas"],
  ["9501e8ef-e6cc-5348-924c-0a6211c856b4", "Edna B Nicholas"],
  ["bd3c2c04-e39d-57a9-b1ed-6e01285235e3", "Edward E Nicholas Jr."],
  ["3dcd7e3e-31a1-5e56-8b1d-ab92f1990334", "Paul B Nicholas"],
  ["e3153393-04d5-5793-92d3-cea46680e1bd", "Richard Nicholas"],
  ["5f46caf3-82c8-533a-b899-3c479ec83f01", "Robert C Nicholas"],
  ["ce773c68-1223-51e5-997b-ae302dc03ede", "Robert Nicholas"],
  ["48e61523-be66-5f16-92ed-15ee9c6c7cd9", "John M Nicholich"],
  ["7d8a0a78-20a9-5189-9da2-96d42d54d1be", "John N Nicholich"],
  ["bee40827-db33-5114-b31c-5b027c029d9a", "Frederick W Nicholls"],
  ["a34c8df8-be0b-5bf2-b85b-005964e9f35e", "Ann R Nichols"],
  ["3eb3e492-94f0-551f-9276-94dcb25f52d1", "Calvin J Nichols"],
  ["83f4a034-098d-57d6-b011-497efdb2fe77", "Delia F Nichols"],
  ["278d6a2a-63df-5758-af3b-c5bd19b070ca", "Elizabeth G Nichols"],
  ["464123d8-6a18-5ced-9a3f-0a868564aa08", "Frank B Nichols"],
  ["72026b46-fb17-5749-922c-28f57e576e65", "Lewis H Nichols"],
  ["49b3f759-c330-570c-9a97-fd5c4e557ae0", "Osgood M Nichols"],
  ["75300d04-92e3-5b70-9ac1-4ee256ecd987", "Raymond A Nichols"],
  ["213e3d09-9de7-57a1-b314-89bd1fd64962", "Richard L Nichols"],
  ["fc0ce059-f65d-53d9-8716-da87ed0d0230", "Robert B Nichols"],
  ["c994e51e-c78e-52b8-bd45-cfad5f915eeb", "Virginia J Nichols"],
  ["bcd8918c-c602-5724-98f4-43561d998a90", "Warren Nichols"],
  ["dffe808f-dfa0-5186-b42a-19e6cf469134", "Willard A Nichols"],
] as const;

test("Batch 703 publishes all 23 direct profile routes with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 703 publishes Nicholls as an Allied War Office-to-SOE pathway", async ({ page }) => {
  await page.goto("./people/bee40827-db33-5114-b31c-5b027c029d9a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("British War Office");
  await expect(main).toContainText("General Staff Officer, 1st grade");
  await expect(main).toContainText("Special Operations Executive");
  await expect(main).toContainText("SOE and OSS remain distinct");
});

test("Batch 703 qualifies Osgood Nichols's two federal information assignments", async ({ page }) => {
  await page.goto("./people/49b3f759-c330-570c-9a97-fd5c4e557ae0/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Wage and Hour Division");
  await expect(main).toContainText("National Defense Mediation Board");
  await expect(main).toContainText("Director of Information");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("transition to OSS is not documented");
});

test("Batch 703 leaves the Nicholich and Nicolich conflict visible and unmerged", async ({ page }) => {
  await page.goto("./people/48e61523-be66-5f16-92ed-15ee9c6c7cd9/");
  await expect(page.locator("main")).toContainText("Identity statusambiguous");
  await expect(page.locator("main")).toContainText("John M Nicolich");
  await expect(page.locator("main")).toContainText("must not be silently merged");

  await page.goto("./people/7d8a0a78-20a9-5189-9da2-96d42d54d1be/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("middle initial conflicts");
  await expect(page.locator("main")).toContainText("remain visible and unmerged");
});

test("Batch 703 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,208");
  await expect(main).toContainText("38.46%");
  await expect(main).toContainText("319");
  await expect(main).toContainText("14,726");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
