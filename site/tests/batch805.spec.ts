import { expect, test } from "@playwright/test";

const profiles = [
  ["3371dba6-d74a-5c54-ab0a-013b6937153e", "Ivan B Rigby"],
  ["be13f981-ee54-5bab-8d8b-146c014f7ea5", "Horace A Rigg"],
  ["288a215b-85ca-54a9-9ca3-3b0f6422c3ba", "Elizabeth S Riggin"],
  ["01067f2b-5ec0-552d-b183-d85c4eca8578", "George B Riggin"],
  ["d50118c9-bfda-51e0-b663-d320fb90d699", "Jewell W Riggin"],
  ["3aab60d7-ff5e-53ee-80bd-37fbe20bcebf", "Elizabeth P Riggs"],
  ["3c92b33e-da9b-5970-ad6b-b0014fc52360", "Lawrence S Riggs"],
  ["70932905-062f-57f4-b85b-95121a9e920e", "Walter M Riggs Jr."],
  ["f6a1b183-9afd-59e7-918d-8ebb311dd9b0", "Andre Rigot"],
  ["5d874ace-7c03-554d-8772-e9baba464833", "Catherine Rigsbee"],
  ["bfac956b-637e-5d42-a400-8d11467877e5", "Edward F Rijos"],
  ["b8ae6cb1-a993-529b-ab0e-2b0eaf398a1b", "Alvin F Riley"],
  ["536ef296-40cc-5404-80c9-332655403514", "Anne J Riley"],
  ["0ec48c03-c28a-5f2b-8f50-3f596418db97", "Elizabeth A Riley"],
  ["57359d60-29e0-5171-8aed-95b59750892c", "Henry D Riley"],
  ["e88e52a8-d928-50f6-ab56-4c1aa1f948b6", "Horace B Riley"],
  ["edc281c7-f01a-5135-9727-a1990e5237b8", "James A Riley"],
  ["d32914ba-ab78-57ad-b165-26e9946d9785", "James L Riley"],
  ["107f1b74-8dad-5d18-b3d6-9078a85e02b1", "John E Riley"],
  ["cf31c546-63a2-5077-867b-3fc8250e9f7a", "John E Riley"],
  ["1fc69565-d515-5696-8077-172fb082c198", "Leonard C Riley"],
  ["01ad5a5d-5edd-5288-a7dc-a82d13488462", "Lois A Riley"],
  ["6e16e728-7c48-5704-a292-a0d38d7cdd99", "Margaret R Riley"],
] as const;

test("Batch 805 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("645");
    await expect(main).not.toContainText("not started");
    await expect(main).toContainText("requires archival review");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Andre Rigot publishes Team FILAN identity but no invented employer", async ({ page }) => {
  await page.goto("./people/f6a1b183-9afd-59e7-918d-8ebb311dd9b0/");
  const main = page.locator("main");
  await expect(main).toContainText("André Rigot");
  await expect(main).toContainText("Team FILAN");
  await expect(main).toContainText("observer");
  await expect(main).toContainText("does not establish a pre-OSS employer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Catherine Rigsbee presents the 1946 voucher only as a probable identity bridge", async ({ page }) => {
  await page.goto("./people/5d874ace-7c03-554d-8772-e9baba464833/");
  const main = page.locator("main");
  await expect(main).toContainText("F. Catherine Rigsbee");
  await expect(main).toContainText("Admin. Asst.");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("postwar identity evidence only");
  await expect(main).toContainText("does not document the person's pre-OSS employment");
});

test("the two John E Riley rows remain distinct people", async ({ page }) => {
  await page.goto("./people/107f1b74-8dad-5d18-b3d6-9078a85e02b1/");
  const t5 = page.locator("main");
  await expect(t5).toContainText("T-5");
  await expect(t5).toContainText("also AS");
  await expect(t5).toContainText("separately printed Pfc row");

  await page.goto("./people/cf31c546-63a2-5077-867b-3fc8250e9f7a/");
  const pfc = page.locator("main");
  await expect(pfc).toContainText("Pfc");
  await expect(pfc).toContainText("separately printed T-5 row");
  await expect(pfc).not.toContainText("also AS");
});

test("Batch 805 preserves clipped notes without silent expansion", async ({ page }) => {
  await page.goto("./people/be13f981-ee54-5bab-8d8b-146c014f7ea5/");
  await expect(page.locator("main")).toContainText("photogra");

  await page.goto("./people/d50118c9-bfda-51e0-b663-d320fb90d699/");
  await expect(page.locator("main")).toContainText("Honorab");

  await page.goto("./people/3c92b33e-da9b-5970-ad6b-b0014fc52360/");
  await expect(page.locator("main")).toContainText("Record");
});

test("home page exposes the rebuilt Batch 805 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,502");
  await expect(home).toContainText("48.05%");
  await expect(home).toContainText("12,431");
  await expect(home).toContainText("824");
  await expect(home).toContainText("372");
  await expect(home).toContainText("9,965");
});
