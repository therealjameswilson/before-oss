import { expect, test } from "@playwright/test";

const profiles = [
  ["c8ecdcd8-f5d8-5d47-9165-9a4c583e5a5b", "John S Molster"],
  ["243cb3b3-3f8f-56ec-aba2-7fa7e976ab23", "Joseph T Molyson"],
  ["0c9e7644-515a-552f-b884-44af93cbb05d", "George F Monahan"],
  ["bcd1704e-9710-5136-8e4c-365756b48c3d", "Raymond D Monahan"],
  ["f268d933-e929-59c1-9cba-119c8bd490fb", "Leonie A Moncla"],
  ["9d1ed0c7-d5ce-563b-9c45-48410f89dd4e", "Earl M Moncrief"],
  ["6fcabe28-1ea4-5652-8e98-da731b28916a", "John J Mondale"],
  ["0fde19b4-5c3c-50b8-91c1-edf8622bd744", "Bertha C Mondoux"],
  ["52050d2a-7a35-5645-9280-6b702892d6d5", "Lucille H Mondoux"],
  ["8fb929cc-ad45-58ca-b4cd-26ee62b1e211", "Negley C Monett"],
  ["d451e5f1-6df9-52f7-a567-a93dd07799fd", "Mario Monfardini"],
  ["bbbeaed0-dfbd-5908-9a05-448d5c625e41", "Natalene Mongello"],
  ["e8c35b90-8366-50c1-9ad5-fe245cba95df", "Carmine Mongelluzzo"],
  ["dd848c6c-63e4-5507-8a6f-bada1e1c2048", "Pasquale Mongelluzzo"],
  ["eda77222-89bb-54ce-aed5-5e19afc85798", "Paul J Mongrain"],
  ["4baa7687-b843-5b57-badc-5ccdd8d776d2", "Marcel P Monier"],
  ["f2d70507-f85e-539b-94e9-bee48b5fbbd7", "John J Monigan"],
  ["ab2a07c9-cb7b-5a39-9368-21c91aa15fc8", "Billy B Monk"],
  ["a09f1be0-73d6-5700-988b-e484360b223d", "Ursula L Monks"],
  ["101c7710-99bb-5f4c-9581-6b014fc92788", "Robert P Monlvx"],
  ["a3767902-406b-5931-97d4-0e8426410cf0", "Cecil S Monnin"],
  ["70bfdfd3-627f-559d-a1d2-77454622e499", "Avary C Monroe"],
] as const;

test("Batch 669 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 669 qualifies Negley Monett's documented newspaper employment", async ({ page }) => {
  await page.goto("./people/8fb929cc-ad45-58ca-b4cd-26ee62b1e211/");
  const main = page.locator("main");

  await expect(main).toContainText("San Francisco News");
  await expect(main).toContainText("1938");
  await expect(main).toContainText("1941");
  await expect(main).toContainText("medium documented pre-OSS");
  await expect(main).toContainText("probably worked");
  await expect(main).toContainText("Polk's Crocker-Langley San Francisco City Directory");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("San Francisco News");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("San Francisco News");
});

test("Batch 669 publishes reviewed Army identities without inventing employers", async ({ page }) => {
  const armyMatches = [
    ["243cb3b3-3f8f-56ec-aba2-7fa7e976ab23", "Joseph T Molyson"],
    ["0c9e7644-515a-552f-b884-44af93cbb05d", "George F Monahan"],
    ["bcd1704e-9710-5136-8e4c-365756b48c3d", "Raymond D Monahan"],
    ["9d1ed0c7-d5ce-563b-9c45-48410f89dd4e", "Earl M Moncrief"],
    ["6fcabe28-1ea4-5652-8e98-da731b28916a", "John J Mondale"],
    ["e8c35b90-8366-50c1-9ad5-fe245cba95df", "Carmine Mongelluzzo"],
    ["eda77222-89bb-54ce-aed5-5e19afc85798", "Paul J Mongrain"],
    ["a3767902-406b-5931-97d4-0e8426410cf0", "Cecil S Monnin"],
  ] as const;

  for (const [id, name] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("Batch 669 preserves suffix variants and the Monlvx index spelling", async ({ page }) => {
  await page.goto("./people/0c9e7644-515a-552f-b884-44af93cbb05d/");
  await expect(page.locator("main")).toContainText("George F Monahan Jr");

  await page.goto("./people/6fcabe28-1ea4-5652-8e98-da731b28916a/");
  await expect(page.locator("main")).toContainText("John J Mondale Jr");

  await page.goto("./people/f2d70507-f85e-539b-94e9-bee48b5fbbd7/");
  await expect(page.locator("main")).toContainText("John J Monigan Jr");
  await expect(page.locator("main")).toContainText("Harvard Law School Library Nuremberg Trials Project");
  await expect(page.locator("main")).not.toContainText("Stryker, Tams");

  await page.goto("./people/101c7710-99bb-5f4c-9581-6b014fc92788/");
  await expect(page.getByRole("heading", { name: "Robert P Monlvx", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Robert P Monlux");
});

test("Batch 669 keeps identifier conflicts and duplicate clusters visible", async ({ page }) => {
  await page.goto("./people/ab2a07c9-cb7b-5a39-9368-21c91aa15fc8/");
  await expect(page.locator("main")).toContainText("Billy D. Monk");
  await expect(page.locator("main")).toContainText("needs identity review");
  await expect(page.locator("main")).not.toContainText("Verified employer");

  await page.goto("./people/4baa7687-b843-5b57-badc-5ccdd8d776d2/");
  await expect(page.locator("main")).toContainText("source or column-shift conflict");
  await expect(page.locator("main")).not.toContainText("Clarence J. La Ferriere");

  await page.goto("./people/bbbeaed0-dfbd-5908-9a05-448d5c625e41/");
  await expect(page.locator("main")).toContainText("Natelene Mengello");
  await expect(page.locator("main")).toContainText("not auto-merged");

  await page.goto("./people/70bfdfd3-627f-559d-a1d2-77454622e499/");
  await expect(page.locator("main")).toContainText("Avary C. Munroe");
  await expect(page.locator("main")).toContainText("not auto-merged");
});

test("Batch 669 updates exact coverage and preserves the oil category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,467");
  await expect(page.locator("body")).toContainText("35.37%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  await expect(oilList).not.toContainText("Negley C Monett");
});
