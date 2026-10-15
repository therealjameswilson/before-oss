import { expect, test } from "@playwright/test";

const profiles = [
  ["3bc18b83-7c01-5dbf-85ff-64a77c2910ff", "Henry B Roberts"],
  ["0951b750-448b-5ebe-86bd-75701bd220be", "Henry L Roberts"],
  ["04576404-88b6-5725-924e-e514fe1a6de7", "Irving Roberts"],
  ["222acf85-9c67-5cc0-aebf-9863a5908653", "Joe B Roberts"],
  ["86412600-10f0-5bef-a7f2-0cec030bb374", "John R Roberts"],
  ["5addc99c-e64f-5693-9f31-eda43736613a", "Joseph B Roberts"],
  ["23e9c556-d873-5362-8064-d44e0d44b877", "Kenneth A Roberts"],
  ["8652e321-a4df-52fc-b281-eb54c4e4fbe1", "Lucille T Roberts"],
  ["b878a233-b64d-50b5-828c-bbd9d6d23998", "Marcus Roberts"],
  ["207d82ce-c701-5e78-8f67-026d6f9c7c51", "Martha L Roberts"],
  ["79cdcca0-1058-5fe1-bd91-9fe9e07dad34", "Martin M Roberts"],
  ["cc3af525-1396-5994-9dad-87eabeb5cecd", "Mary E Roberts"],
  ["113a123b-7eee-5329-8b75-e847094a7075", "Odie G Roberts Jr."],
  ["c86b9316-5938-5ad0-966a-09311e4d78db", "Paul Roberts"],
  ["ede598dc-c658-5ad4-8002-a5f19ce4aba6", "Ralph G Roberts Jr."],
  ["8ff41a2f-ba7a-51dd-953c-d0e285d78dd5", "Roberta J Roberts"],
  ["8cd05fb6-04c4-5eeb-85b7-aa067e927e71", "Walter Roberts"],
  ["a5aa676e-d19d-5bc7-bbbe-eef880dadaeb", "William A Roberts"],
  ["8ad5f510-2ed6-5361-9b99-87039572d92d", "William A Roberts"],
  ["b52a63d2-85c6-5f70-8d3c-a716ce03b12f", "William B Roberts"],
  ["11c17691-483c-5d5b-8d3d-adec8dbece9e", "Arthur C Robertson"],
  ["8404ba79-3e85-5045-8b55-62c513e2f05c", "Arthur R Robertson"],
  ["a3b2ef20-e7f7-5353-949c-8262376b1adb", "Charles W Robertson Jr."],
] as const;

test("Batch 810 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("650");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("secure Army matches publish identity evidence without employer inference", async ({ page }) => {
  for (const id of [
    "3bc18b83-7c01-5dbf-85ff-64a77c2910ff",
    "222acf85-9c67-5cc0-aebf-9863a5908653",
    "b878a233-b64d-50b5-828c-bbd9d6d23998",
    "113a123b-7eee-5329-8b75-e847094a7075",
    "ede598dc-c658-5ad4-8002-a5f19ce4aba6",
    "a5aa676e-d19d-5bc7-bbbe-eef880dadaeb",
    "a3b2ef20-e7f7-5353-949c-8262376b1adb",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("protected identifier");
    await expect(main).toContainText("requires archival review");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Arthur C Robertson exposes the official identifier conflict", async ({ page }) => {
  await page.goto("./people/11c17691-483c-5d5b-8d3d-adec8dbece9e/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("John J. Perazza");
  await expect(main).toContainText("No employer or identity details are transferred");
});

test("the two William A Roberts rows remain distinct", async ({ page }) => {
  await page.goto("./people/a5aa676e-d19d-5bc7-bbbe-eef880dadaeb/");
  let main = page.locator("main");
  await expect(main).toContainText("Pvt");
  await expect(main).toContainText("docume");
  await expect(main).toContainText("not transferred to the separate Chief Boatswain's Mate");

  await page.goto("./people/8ad5f510-2ed6-5361-9b99-87039572d92d/");
  main = page.locator("main");
  await expect(main).toContainText("CBM");
  await expect(main).toContainText("ranks and protected identifiers differ");
});

test("Walter Roberts keeps the unbridged Walter R Roberts biography out of identity facts", async ({ page }) => {
  await page.goto("./people/8cd05fb6-04c4-5eeb-85b7-aa067e927e71/");
  const main = page.locator("main");
  await expect(main).toContainText("Walter R. Roberts");
  await expect(main).toContainText("cannot safely be assigned");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("home page exposes the rebuilt Batch 810 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,617");
  await expect(home).toContainText("48.53%");
  await expect(home).toContainText("12,316");
  await expect(home).toContainText("831");
  await expect(home).toContainText("374");
  await expect(home).toContainText("10,080");
});
