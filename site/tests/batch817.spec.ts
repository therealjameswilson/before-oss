import { expect, test } from "@playwright/test";

const profiles = [
  ["6283f997-3523-5df8-b80c-0ee736c4bfc8", "Howard B Rogers Jr."],
  ["38bc7d1f-4110-5109-a9aa-a9069025ed11", "Sverre B Rogne"],
  ["1a741e4c-e657-5939-978c-8545a3f0c6e4", "Anthony J Rogowski"],
  ["3bbe2717-af08-54b0-b1a9-348bd99af2d8", "Karl Rohe"],
  ["86c8f3a8-da30-5af4-bb73-d513347fd7d5", "William S Rohleder"],
  ["ff3ee78c-e099-5da5-93ff-a403d8dffd71", "Harry L Rohlfing"],
  ["6ddcb3a3-ab0d-5946-b361-639fe6951032", "Gladys F Rohloff"],
  ["f72f64fe-1ee6-5636-b1b1-0baac7e655f0", "John A Rohr"],
  ["aa484cd2-f694-5d17-8d3c-835cbac42347", "Emmett E Rohrbaugh"],
  ["27567410-3b56-529f-ab01-79a604234a22", "George F Rohrlich"],
  ["f9040982-e2f8-5ffc-9467-533ee6ce494f", "Charlene Roland"],
  ["d05bb2e0-0645-5a2d-b321-19b7c31b237a", "James V Roland"],
  ["18a997c6-deee-5437-8b1f-e457bfa45c23", "Joseph M Roland"],
  ["a4884170-1850-58d0-860a-56c6263d07ea", "Mary O Rolater"],
  ["ab4ee08c-ddd2-5257-9f2b-4fc2009f8c53", "Edward J Rolka"],
  ["20c32590-f0e6-5d87-9774-ca396a16d5b4", "Hendrik B Roll"],
  ["f01b9a3b-7b89-5127-afe7-a65bcc57aaa3", "Loma E Roll"],
  ["f9e31312-0509-5b29-aa94-114d89550365", "John S Roller"],
  ["2db02d81-a7c1-5fd0-9c9a-f032a703a7b8", "Lawrence A Rollins"],
  ["07741b86-895d-5be1-a283-aaff7668d21a", "Joseph A Rollo"],
  ["179f9290-b017-5c15-af89-811bdfb0af5c", "Thomas A Rollo"],
  ["9fcbad88-611d-585f-b566-9f9efb38aced", "Cecil B Rollow"],
  ["ee0fa566-36e2-50be-8820-d74f694d8849", "Albert G Roloff"],
] as const;

test("Batch 817 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Sverre Rogne profile separates merchant work from military assignment", async ({ page }) => {
  await page.goto("./people/38bc7d1f-4110-5109-a9aa-a9069025ed11/");
  const main = page.locator("main");
  await expect(main).toContainText("M/S Pleasantville");
  await expect(main).toContainText("Able seaman");
  await expect(main).toContainText("99th Infantry Battalion");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("not proven to be the immediate pre-OSS role");
});

test("George Rohrlich profile publishes qualified Brookings and Sweet Briar chronology", async ({ page }) => {
  await page.goto("./people/27567410-3b56-529f-ab01-79a604234a22/");
  const main = page.locator("main");
  await expect(main).toContainText("Sweet Briar College");
  await expect(main).toContainText("Instructor, Division of Social Studies");
  await expect(main).toContainText("Brookings Institution");
  await expect(main).toContainText("neither source establishes that the job immediately preceded OSS service");
});

test("Army identity records do not become inferred employers", async ({ page }) => {
  for (const id of [
    "6283f997-3523-5df8-b80c-0ee736c4bfc8",
    "1a741e4c-e657-5939-978c-8545a3f0c6e4",
    "3bbe2717-af08-54b0-b1a9-348bd99af2d8",
    "f72f64fe-1ee6-5636-b1b1-0baac7e655f0",
    "aa484cd2-f694-5d17-8d3c-835cbac42347",
    "d05bb2e0-0645-5a2d-b321-19b7c31b237a",
    "ab4ee08c-ddd2-5257-9f2b-4fc2009f8c53",
    "20c32590-f0e6-5d87-9774-ca396a16d5b4",
    "2db02d81-a7c1-5fd0-9c9a-f032a703a7b8",
    "07741b86-895d-5be1-a283-aaff7668d21a",
    "179f9290-b017-5c15-af89-811bdfb0af5c",
    "ee0fa566-36e2-50be-8820-d74f694d8849",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("confirmed");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer");
  }
});

test("Charlene Roland retains the printed P-3 grade", async ({ page }) => {
  await page.goto("./people/f9040982-e2f8-5ffc-9467-533ee6ce494f/");
  const main = page.locator("main");
  await expect(main).toContainText("P-3");
  await expect(main).toContainText("Page 398");
});
