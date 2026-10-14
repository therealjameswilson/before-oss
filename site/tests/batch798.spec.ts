import { expect, test } from "@playwright/test";

const profiles = [
  ["0134d0ec-ef71-5682-9f06-d1d755403c13", "John V Rentzeperis"],
  ["0bd3d8a2-612c-503e-a7c5-68a54f93aaf4", "Lawrence E Renzi"],
  ["9c360099-f4ba-5650-b57b-2d1a8801532e", "Robert T Reppenhagen"],
  ["5ddac44a-ce14-5db5-85b6-83880e566f9d", "Robert R Reque"],
  ["0101ab60-2171-5501-9e7e-606430b8afdb", "Carlo Resio"],
  ["2ad8f3f7-f29d-516b-a61c-5d1bb07a4aed", "Joseph V Ress"],
  ["4df87754-b695-511d-bbbc-501c9070eb3a", "Joseph L Ressani"],
  ["abee3674-bf36-50b9-bf28-b28905129288", "Howard C Ressler"],
  ["7e9387c0-e707-5a48-b246-42e3f6083c3d", "Jean Retheret"],
  ["b09deeb5-9efc-5821-9c63-4499bf05e4d0", "Maurice H Rettersmann"],
  ["d5461687-d02c-56e2-890d-0bed8b121aaf", "Robe R Reubell"],
  ["db5fa023-e3d0-531c-9623-8e3da3d6325b", "William Reuff"],
  ["4e41e78b-2980-5fd3-9adf-27ab9dcf096b", "Frederick Reuss"],
  ["472ee2a8-20fa-5d44-86f8-01fce83c8153", "Henry Reuter"],
  ["dfe10bc1-47f9-5e74-a522-d9126d257f37", "Alfred D Reutershan"],
  ["a14a492d-2b19-5710-b03e-36751c2eca94", "Alix Reuther"],
  ["0771cd82-d11e-581e-93ef-0538f45facd9", "Rene Reverett"],
  ["fdd39c21-ff07-5182-b1d7-04c1f995c791", "John Rew"],
  ["e9c93255-cee7-5cd6-8304-505467d6dc65", "John Rexford"],
  ["455d6136-02eb-5684-8918-703f87d86160", "Vorley M Rexroad"],
  ["0549b48b-0677-5e67-88ac-3f10dbfe85fa", "Jean R Rey"],
  ["58df1bb7-7a2c-542c-9c37-596c530c296e", "Anne M Reybaud"],
  ["ac7566ac-c70e-5313-8f23-a4d22c43ee85", "Evelyn Reyer"],
] as const;

const officialArmyIdentityProfiles = [
  "0134d0ec-ef71-5682-9f06-d1d755403c13",
  "0bd3d8a2-612c-503e-a7c5-68a54f93aaf4",
  "9c360099-f4ba-5650-b57b-2d1a8801532e",
  "5ddac44a-ce14-5db5-85b6-83880e566f9d",
  "4df87754-b695-511d-bbbc-501c9070eb3a",
  "abee3674-bf36-50b9-bf28-b28905129288",
  "472ee2a8-20fa-5d44-86f8-01fce83c8153",
  "e9c93255-cee7-5cd6-8304-505467d6dc65",
] as const;

test("Batch 798 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 798 publishes accepted Army identity evidence without inventing employers", async ({ page }) => {
  for (const id of officialArmyIdentityProfiles) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Army/i);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Resio publishes Italian naval intelligence as an immediate military affiliation only", async ({ page }) => {
  await page.goto("./people/0101ab60-2171-5501-9e7e-606430b8afdb/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Italian Naval Intelligence Service",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("military assignment");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main).toContainText("Counterintelligence Reader, Volume 2");
});

test("Reutershan keeps the 27th Division in earlier military affiliations", async ({ page }) => {
  await page.goto("./people/dfe10bc1-47f9-5e74-a522-d9126d257f37/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("27th Division");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Chemical Warfare");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).toContainText("Annual Report of the Adjutant General for the Year 1940");
});

test("Rexford distinguishes Army language training from Dartmouth student status", async ({ page }) => {
  await page.goto("./people/e9c93255-cee7-5cd6-8304-505467d6dc65/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Army Specialized Training Program at Fordham University",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("medium");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Dartmouth College");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Rexroad separates immediate Army assignment from qualified civilian employment", async ({ page }) => {
  await page.goto("./people/455d6136-02eb-5684-8918-703f87d86160/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "U.S. Army Air Corps training center",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Cowen High School");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("medium");
  await expect(main).toContainText("Rexroad Named Alumnus of the Year");
});

test("Reverett preserves the indexed spelling while exposing documented variants", async ({ page }) => {
  await page.goto("./people/0771cd82-d11e-581e-93ef-0538f45facd9/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Rene Reverett", level: 1 })).toBeVisible();
  await expect(main).toContainText("Rene Reveret");
  await expect(main).toContainText("Rene Duvallet");
  await expect(main).toContainText("Ramadier");
  await expect(main).toContainText("Sussex Jeanne");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Rettersmann and Reuff conflicts stay visible and employer-free", async ({ page }) => {
  await page.goto("./people/b09deeb5-9efc-5821-9c63-4499bf05e4d0/");
  let main = page.locator("main");
  await expect(main).toContainText("Maurice H Rottersmann");
  await expect(main).toContainText(/conflict/i);
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/db5fa023-e3d0-531c-9623-8e3da3d6325b/");
  main = page.locator("main");
  await expect(main).toContainText("Richard V Goldie");
  await expect(main).toContainText(/conflict/i);
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 798 organization pages expose all six reviewed affiliations", async ({ page }) => {
  for (const [id, name] of [
    ["0e3c340a-e105-5aa0-a854-1a3b5457258c", "Italian Naval Intelligence Service"],
    ["79b51239-5ef4-5e4a-9c84-edee99206ea2", "27th Division, U.S. Army"],
    ["d3dbf976-0ae8-535a-875a-57329173acb8", "Dartmouth College"],
    ["245815f1-cb74-54b0-b647-e2381b2b3110", "Army Specialized Training Program at Fordham University"],
    ["8630808f-628e-55d1-8639-e5b87a1f4ad6", "U.S. Army Air Corps training center"],
    ["90f0e77c-baa4-5884-ac8e-80e013c5acab", "Cowen High School"],
  ]) {
    await page.goto("./organizations/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("home page exposes the rebuilt Batch 798 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,344");
  await expect(home).toContainText("47.39%");
  await expect(home).toContainText("12,590");
  await expect(home).toContainText("818");
  await expect(home).toContainText("368");
  await expect(home).toContainText("9,805");
});
