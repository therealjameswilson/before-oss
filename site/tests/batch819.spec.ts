import { expect, test } from "@playwright/test";

const profiles = [
  ["6aad5298-2d26-58d4-9351-760a406ae906", "James F Roosevelt"],
  ["221b804d-039b-5da1-ad65-c62ea650a63b", "Kermit Roosevelt Jr."],
  ["e0a1d831-be98-53a5-85b4-5df26f0625f2", "Quentin Roosevelt"],
  ["3b81d781-de7c-535f-a75f-12a4adac0cf1", "Elmo Roper"],
  ["fb2dce26-7f86-5ef2-8c52-9760824fc54f", "Eugene A Roper Jr."],
  ["6773c749-5282-5020-85f8-e2d381d80f7c", "Mack A Roper"],
  ["17a8f2cd-1c27-5342-a669-dd2ce398161e", "Mary L Roper"],
  ["3bdc1005-cf1c-5850-b947-383ee76fe196", "Robert V Rosa"],
  ["3a4a16db-5348-5641-856b-dde2cf0cf08e", "Francesco Rosapepe"],
  ["66bad083-cc49-551a-b60c-b8a779ad4971", "Albert Rose"],
  ["b6384cce-f2d0-5359-93cc-541f0da8fdcc", "Alma E Rose"],
  ["301e232d-ec86-58ac-bebc-f8665d6011f1", "Cornelia B Rose"],
  ["a61359ac-ac23-58b0-8c71-910b88fb46a2", "George F Rose"],
  ["f0f3776c-3fc4-5067-b7a2-5fb1c97ea021", "Howard A Rose"],
  ["0df1e608-38e8-5080-9614-541d261ba5b0", "James F Rose"],
  ["946a39b0-f3a4-52bd-bdd7-bbcaf1b3e09d", "Krisanthe Rose"],
  ["86de095d-03c9-53bd-a1b2-b6f10cc2a658", "Mario Rose"],
  ["c501e9b3-d19d-50e3-a707-a75fbc1b0a79", "Robert R Rose Jr."],
  ["e24e3f45-c7b6-5183-a3de-b1e701cde5e9", "Telphi Rose"],
  ["306a703a-d637-5639-894f-61929747d4c3", "Robert S Roseberry"],
  ["3307b8f5-9776-554e-920d-34f6a52b59dd", "Fred E Rosell Jr."],
  ["1b06cd75-491f-5089-9d44-06d270679836", "Louis F Rosemire"],
  ["7682bd86-92a3-52ca-bfee-23589d594c93", "David V Rosen"],
] as const;

test("Batch 819 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("James Roosevelt profile separates Marine assignment from the last civilian employer", async ({ page }) => {
  await page.goto("./people/6aad5298-2d26-58d4-9351-760a406ae906/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Immediate pre-OSS affiliation", level: 2 })).toBeVisible();
  await expect(main).toContainText("United States Marine Corps");
  await expect(main).toContainText("temporary detachment");
  await expect(page.getByRole("heading", { name: "Last civilian employer before service", level: 2 })).toBeVisible();
  await expect(main).toContainText("Samuel Goldwyn, Inc.");
  await expect(main).toContainText("vice president");
});

test("Quentin Roosevelt profile models Harvard as student status and preserves the Army-to-OSS uncertainty", async ({ page }) => {
  await page.goto("./people/e0a1d831-be98-53a5-85b4-5df26f0625f2/");
  const main = page.locator("main");
  await expect(main).toContainText("Harvard College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("do not establish the exact unit or transfer sequence");
  await expect(main).toContainText("WN#18751");
});

test("Elmo Roper profile qualifies the probable immediate company and publishes named earlier work", async ({ page }) => {
  await page.goto("./people/3b81d781-de7c-535f-a75f-12a4adac0cf1/");
  const main = page.locator("main");
  await expect(main).toContainText("Roper Organization");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("Cherington, Wood, and Roper");
  await expect(main).toContainText("Traub Company");
});

test("Direct Cairo interviews support Krisanthe and Telphi Rose without hiding the spelling variant", async ({ page }) => {
  await page.goto("./people/946a39b0-f3a4-52bd-bdd7-bbcaf1b3e09d/");
  await expect(page.locator("main")).toContainText("War Department, Ordnance");
  await expect(page.locator("main")).toContainText("Detroit");

  await page.goto("./people/e24e3f45-c7b6-5183-a3de-b1e701cde5e9/");
  const main = page.locator("main");
  await expect(main).toContainText("Telpi Rose");
  await expect(main).toContainText("Gotham Hotel");
  await expect(main).toContainText("finance work");
});

test("The printed 1/SGT variant is enlisted and excluded from commissioned-officer results", async ({ page }) => {
  await page.goto("./people/a61359ac-ac23-58b0-8c71-910b88fb46a2/");
  const main = page.locator("main");
  await expect(main).toContainText("1/SGT");
  await expect(main).toContainText(/enlisted army personnel/i);
  await page.goto("./people/?commissioned=true&q=George%20F%20Rose");
  await expect(page.locator("main")).not.toContainText("George F Rose");
});
