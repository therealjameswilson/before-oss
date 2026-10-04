import { expect, test } from "@playwright/test";

const profiles = [
  ["bea99f29-37b5-5ad9-b8bc-9c90aec97f20", "Mary J Odgers"],
  ["dbc5892b-135b-5d95-8109-824ad6306e58", "Clifford K Odom"],
  ["149a7513-2e53-5ea0-bba8-4dc4ec4eab9c", "John C Odonnell"],
  ["a76d4948-7ae8-598f-9e18-e94640e52c23", "Justin E Odonnell"],
  ["3e587fb1-5ad6-5d82-82de-c1a79f9c6020", "M G Odonnell"],
  ["347fc453-2231-5915-809e-5931116bc289", "Marian G Odonnell"],
  ["767ee661-5128-598d-bec5-f08273d564de", "Myrl K Odonnell"],
  ["5fa33be5-9ef6-5cb1-9df1-1f3920530a31", "Robert N Odonnell"],
  ["06410ab9-f2aa-5d36-beb3-e1d6b92de417", "William G Odonnell"],
  ["3211979d-bdca-5d47-8e2c-9b2999038519", "William H Odonnell"],
  ["04baf7c4-a7ee-5dc4-bd7d-61f2c257400b", "Dorothea E Odonnoghue"],
  ["98d6f28e-7e5b-5bc7-a1c5-e387db8a75be", "Elsie E Odunne"],
  ["9498e359-beed-5d64-ad40-040e9df5337e", "Francis Oechsner"],
  ["30103234-1eb3-5e50-810b-44313d87042b", "Cecil f Oelker"],
  ["c0288700-9675-5cfa-a5fe-61b7ccf74bda", "Herbert W Oelschlaeger"],
  ["8419a2a1-53b0-55d3-8844-0344d75cd068", "Bjarne Oen"],
  ["d797152b-4ca7-5bed-86c8-76dec1be57b1", "Frederick C Oesh"],
  ["6ca311d0-b60f-53e4-a414-d364287e2978", "Jack Oestreich"],
  ["8de81714-121f-55a3-b7b6-fa407675f927", "Edward W Oexner"],
  ["257cec9d-1a0f-5870-b176-95eeacfe64ab", "John L Ofax"],
  ["851199d0-2d25-5e3a-aa31-07736e60126e", "Evelyn K Offers"],
  ["d083e695-b714-52b9-9d80-0d7d5f8fab4d", "Charles Z Offin"],
  ["062ae9fc-cfe4-5b4a-8728-597a62d4747e", "Wilma B Offut"],
] as const;

test("Batch 714 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 714 publishes Bjarne Oen's Norwegian military pathway", async ({ page }) => {
  await page.goto("./people/8419a2a1-53b0-55d3-8844-0344d75cd068/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Bjarne Øen");
  await expect(main).toContainText("Norwegian Armed Forces High Command, Fourth Office (FO IV)");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Store norske leksikon");
});

test("Batch 714 qualifies Charles Z Offin's documented prewar publishing role", async ({ page }) => {
  await page.goto("./people/d083e695-b714-52b9-9d80-0d7d5f8fab4d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Pictures on Exhibit");
  await expect(main).toContainText("Editor and publisher");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("medium B authoritative institutional");
  await expect(main).toContainText("not as a verified immediate employer");
});

test("Batch 714 visibly qualifies Edward W Oexner's probable identity", async ({ page }) => {
  await page.goto("./people/8de81714-121f-55a3-b7b6-fa407675f927/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("probably the World War II Army master sergeant");
  await expect(main).toContainText("medium D correlative or secondary");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 714 preserves the Ofax and OFAK identity conflict", async ({ page }) => {
  await page.goto("./people/257cec9d-1a0f-5870-b176-95eeacfe64ab/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("OFAK JOHN L");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("do not merge");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 714 publishes the accepted Army identity without inventing employment", async ({ page }) => {
  await page.goto("./people/3211979d-bdca-5d47-8e2c-9b2999038519/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Electronic Army Serial Number Merged File");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 714 publishes exact rebuilt coverage and preserves the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,460");
  await expect(main).toContainText("39.52%");
  await expect(main).toContainText("14,474");
  await expect(main).toContainText("721");
  await expect(main).toContainText("325");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
