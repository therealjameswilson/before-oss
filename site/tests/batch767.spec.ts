import { expect, test } from "@playwright/test";

const profiles = [
  ["a3924d30-9290-525f-8668-f2addbcfde6b", "Charles A Pooler"],
  ["6ddaaef2-ece0-5755-ba2d-e4faa98e402d", "Charles E Pooler"],
  ["7754dea3-144d-5712-8156-b3caa74b5a0a", "Charles G Poore"],
  ["195fed3e-0e88-53bb-9ed5-9db9067fe123", "John Popa"],
  ["a5f9d179-5388-523f-9a32-01bd715ffa9c", "Arthur A Pope"],
  ["432e3687-c285-5856-bf4a-903c71d08fe0", "Charles R Pope"],
  ["3efab07e-3d58-5df3-a97e-313713dc5b00", "Clem L Pope"],
  ["68548731-7017-56af-84f3-0d41c448a6fe", "Fiore Pope"],
  ["88829043-9c69-5a02-af30-9ec0b9283920", "Gordon A Pope"],
  ["edc243d6-0e6d-5512-b06d-4c270dd011d3", "Joseph C Pope"],
  ["9985eacd-32d3-52ab-a4c6-f50150271518", "Leslie R Pope"],
  ["0e338ead-20e4-5479-a887-989ecb8260ff", "Paul B Pope"],
  ["46c07ac8-3ca2-5201-aad7-eef6f2b97849", "Homer W Popoff"],
  ["243f16a0-64f0-52be-96c1-adee7549fb2c", "Radovan Popovic"],
  ["e2681729-9cf2-59dc-88c1-feee241f08fb", "Eli Popovich"],
  ["fb7db99d-7c79-5b25-8c85-7d0e2be34adc", "Eva M Popovich"],
  ["68788085-a069-5b1c-968d-fef2910e2788", "William B Popovich"],
  ["6903a798-b606-5c72-9ff3-83d9e694f51c", "William I Popper"],
  ["265d3352-eecf-566a-886d-11903fc9974a", "Valentina C Poppescu"],
  ["d09701e0-1257-5c6a-9809-4c4cb5b38811", "Robert E Poppie"],
  ["0868b9c5-0501-5278-be82-c0451e5537ec", "Edmund S Porada"],
  ["8f94f7b3-d6bd-5372-8856-db9ee9fc1194", "Edward S Porada"],
  ["1838f39f-f003-5813-9e11-9f41848e8110", "Fred J Poremba"],
  ["49dba747-4503-52bf-8a87-43d97010c1c5", "Armando Poretta"],
] as const;

test("Batch 767 publishes all 24 page profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 767 publishes Eva Popovich's student status without inventing a university employer", async ({ page }) => {
  await page.goto("./people/fb7db99d-7c79-5b25-8c85-7d0e2be34adc/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("university student");
  await expect(main).toContainText("Recruited by OSS while still in university");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 767 qualifies Eli Popovich's Army pathway and keeps occupation separate from employer", async ({ page }) => {
  await page.goto("./people/e2681729-9cf2-59dc-88c1-feee241f08fb/");
  const main = page.locator("main");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("engineer");
  await expect(main).toContainText("steel mills");
  await expect(main).toContainText("Ilija (Eli) Popović");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 767 preserves the Poretta and Porada review cautions", async ({ page }) => {
  await page.goto("./people/49dba747-4503-52bf-8a87-43d97010c1c5/");
  await expect(page.locator("main")).toContainText("PORRETTA");
  await expect(page.locator("main")).toContainText("probable");
  await page.goto("./people/8f94f7b3-d6bd-5372-8856-db9ee9fc1194/");
  await expect(page.locator("main")).toContainText("Compare the two Porada files");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("home page exposes the rebuilt Batch 767 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,643");
  await expect(home).toContainText("44.46%");
  await expect(home).toContainText("13,291");
  await expect(home).toContainText("786");
  await expect(home).toContainText("349");
  await expect(home).toContainText("9,101");
});
