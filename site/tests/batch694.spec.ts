import { expect, test } from "@playwright/test";

const profiles = [
  ["abefd735-686f-5299-a603-cd5774cc824c", "Errol M Nakao"],
  ["12e9c14e-610d-5634-a0b4-5dd8fed5d121", "George K Nakashima"],
  ["2e32b434-26a5-59e3-a010-242c260a4cdc", "Joe H Nakata"],
  ["80a43fb2-8ce6-5c1c-99b4-87404b8f2ed7", "Peter T Namkoong"],
  ["6ff7f117-b55c-5030-b350-01cbb8ad8a2c", "James N Nancarrow"],
  ["fe23d352-1212-5c18-b589-da66133af18b", "Gust Nanos"],
  ["9c5f147c-b070-542a-89bd-6c73e99fd1c1", "Edward J Napieralski"],
  ["b3f1e4af-58b7-58a2-84f4-3f8bd7e1f7b2", "John B Napoles"],
  ["ad8d9214-d43c-5a07-8376-989dfa147118", "Gerard S Napoletano"],
  ["c070d5f3-7f95-5997-a0cf-1138996acf39", "Ralph R Napolitano"],
  ["3c9a0fc5-d63f-5d91-a2f1-d7a2f0b22679", "A Napombejara"],
  ["2ad36f54-8770-5bbb-82eb-4915651be3b3", "Chok Naranong"],
  ["0b51140b-f003-546a-9fe3-b834ed1e332c", "Ralph J Nardella"],
  ["054f3ca9-a079-546c-aaa0-76f3d036714c", "Dino Nardi"],
  ["d1a2e376-cf50-5ea7-b50f-54f59af9f2e3", "Joseph J Nardi"],
  ["b40a932c-5c51-5178-a931-f4cfdc277d8d", "Warren L Nardin"],
  ["8237b13b-0d23-50fe-ba5d-e3851f4b9a38", "Boleslaus V Narewski"],
  ["0c0185bb-2c80-5953-8d3f-def95a8d6fce", "Gilbert R Nary"],
  ["87514e1a-450f-5c0e-87ec-597cc9e43695", "Ann Nash"],
  ["b0486308-3a90-5573-bc01-56f1e51d1bbe", "Charles P Nash"],
  ["e7a01792-5e55-56df-8565-3b9b12e6cdbc", "Herman T Nash"],
  ["ccece99c-337a-5c6a-9e97-9b7ace5d2f94", "John Nash"],
  ["4e52e447-1ff2-5864-8098-02737846119c", "John S Nash"],
] as const;

test("Batch 694 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 694 publishes Ann Nash's Vogue employment with qualified timing", async ({ page }) => {
  await page.goto("./people/87514e1a-450f-5c0e-87ec-597cc9e43695/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("E. Ann Nash");
  await expect(main).toContainText("Ann Nash Bottorff");

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate).toContainText("Vogue");
  await expect(immediate).toContainText("Editorial assistant");
  await expect(immediate).toContainText("strongly date bounded");

  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(lastCivilian).toContainText("Vogue");
  await expect(lastCivilian).toContainText("Editorial assistant");
  await expect(main).toContainText("Federal agency in China");
  await expect(main).toContainText("Office of Strategic services");
  await expect(main.locator('a[href="https://hdl.handle.net/1813/27896"]')).toHaveCount(3);
});

test("Batch 694 retains Gus Nanos as an identity variant without inventing an employer", async ({ page }) => {
  await page.goto("./people/fe23d352-1212-5c18-b589-da66133af18b/");
  const main = page.locator("main");
  await expect(main).toContainText("Gus Nanos");
  await expect(main).toContainText("Greek Operational Group VII");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 694 leaves the unbridged George Nakashima and John Nash profiles unresolved", async ({ page }) => {
  await page.goto("./people/12e9c14e-610d-5634-a0b4-5dd8fed5d121/");
  await expect(page.locator("main")).toContainText("Identity statusunresolved");
  await expect(page.locator("main")).not.toContainText("prominent architect");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/ccece99c-337a-5c6a-9e97-9b7ace5d2f94/");
  await expect(page.locator("main")).toContainText("Identity statusunresolved");
  await expect(page.locator("main")).not.toContainText("mathematician");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 694 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("9,007");
  await expect(body).toContainText("37.62%");
  await expect(body).toContainText("316");
  await expect(body).toContainText("14,927");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
