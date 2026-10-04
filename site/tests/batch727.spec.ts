import { expect, test } from "@playwright/test";

const profiles = [
  ["4f938b8a-dc91-5fdc-b3ff-c3607e529ec9", "Eligio P Pacchiodo"],
  ["52de6009-a568-5b57-ba7f-82b9f27c4d06", "Francis X Oxley"],
  ["54b76e37-cde4-5f6c-a27c-e364afe5529f", "Henry S Pachowicz"],
  ["5c892ff7-fb18-509a-ac12-d346da3562b3", "Rose F Pachella"],
  ["69257cb3-3d04-5e12-ba12-2dffe87b4baa", "Sara L Owens"],
  ["70276fc3-38a5-50e0-b5a5-796cf15e21b0", "Louise Owens"],
  ["77e146c1-fdbd-54d1-b557-392257429a41", "Eston W Oyler"],
  ["7b225a72-349f-51fa-81db-e8a90edc38b4", "George W Owings"],
  ["822ee09f-b52b-560e-a55e-0cf75ca65520", "George M Oye"],
  ["8cf28055-0112-51f3-973c-e047ff8c2c2a", "Emily L Owens"],
  ["8fc3e784-2477-5d2c-89b1-c0efcc769a8f", "Joseph A Pacheco"],
  ["96840296-0eb1-525a-9c4f-cd4dfe7c6e5d", "Andre R Pacatte"],
  ["a0036def-733f-5e66-b652-93490fa0abd9", "Margit R Oxholm"],
  ["c3884840-5a32-59e4-b13b-12013b37c40e", "George J Packard Jr."],
  ["c7b2f43d-8f0b-5fb7-89d7-1e8191f7b9e0", "Don S Packer"],
  ["d98a642a-520b-572f-b73e-f61f096c9541", "Isabelle H Pack"],
  ["db5c9aaa-8752-5a5d-ad24-57f030c0085d", "Durant L Pace"],
  ["e1a40fec-cade-5469-a4b7-407883aaf03a", "Ned K Owyang"],
  ["e56c6401-4941-5b8b-8c03-91f269629ad6", "* P"],
  ["f1b6b164-6f27-55c9-9ee4-55803342a68f", "* Pacchiotti"],
  ["f7d3386e-596c-540d-81bc-4691bfa5cae8", "Axel H Oxholm"],
  ["fbbc4320-38d9-53ef-83b1-a338cbf5d8b8", "Richard C Owens"],
  ["462807a1-55f2-5b69-b960-df7d837735cf", "Owen J Owens"],
] as const;

test("Batch 727 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 727 publishes Oxholm's qualified 1942 civilian employer", async ({ page }) => {
  await page.goto("./people/f7d3386e-596c-540d-81bc-4691bfa5cae8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Pacific Forest Industries");
  await expect(main).toContainText("Managing director");
  await expect(main).toContainText("June 1942");
  await expect(main).toContainText("last civilian employer");
  await expect(main).toContainText("American Builder");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationPacific Forest Industries");
});

test("Batch 727 keeps Owyang's college record separate from employment", async ({ page }) => {
  await page.goto("./people/e1a40fec-cade-5469-a4b7-407883aaf03a/");
  const main = page.locator("main");
  await expect(main).toContainText("Ned Ke-Hung Owyang");
  await expect(main).toContainText("Tri-State College");
  await expect(main).toContainText("under radio engineering");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("student");
  await expect(main).not.toContainText("Last civilian employerTri-State College");
});

test("Batch 727 publishes Pacatte's qualified Berlitz record and identifier conflict", async ({ page }) => {
  await page.goto("./people/96840296-0eb1-525a-9c4f-cd4dfe7c6e5d/");
  const main = page.locator("main");
  await expect(main).toContainText("André Pacatte");
  await expect(main).toContainText("Berlitz School of Languages");
  await expect(main).toContainText("Washington");
  await expect(main).toContainText("Cleveland");
  await expect(main).toContainText("Andre R Pagatte");
  await expect(main).toContainText("documented prewar employer found");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationBerlitz School of Languages");
});

test("Batch 727 exposes Pachowicz and Packard conflicts without transferring metadata", async ({ page }) => {
  await page.goto("./people/54b76e37-cde4-5f6c-a27c-e364afe5529f/");
  await expect(page.locator("main")).toContainText("Lewis Randall A");
  await expect(page.locator("main")).toContainText("conflicting sources");
  await expect(page.locator("main")).not.toContainText("Army of the United States");

  await page.goto("./people/c3884840-5a32-59e4-b13b-12013b37c40e/");
  await expect(page.locator("main")).toContainText("Mary A Hawkins");
  await expect(page.locator("main")).toContainText("conflicting sources");
  await expect(page.locator("main")).not.toContainText("Army of the United States");
});

test("Batch 727 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,758");
  await expect(main).toContainText("40.76%");
  await expect(main).toContainText("14,176");
  await expect(main).toContainText("738");
  await expect(main).toContainText("330");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Axel H Oxholm");
});
