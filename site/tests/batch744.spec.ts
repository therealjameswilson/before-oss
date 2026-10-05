import { expect, test } from "@playwright/test";

const profiles = [
  ["acbe9efe-13d3-502c-9c5a-c4cea072a89b", "Dorothy Pelefsky"],
  ["ec26af35-2cce-534e-8f5b-0e9fe4edadc3", "Reed Pelfray"],
  ["46abdbcf-cc74-5c48-b4bb-c163817fff0d", "Frank J Pellacore"],
  ["9ae53621-cacd-5e9e-b163-7e61cf628380", "Joseph J Pellecchia"],
  ["2026a124-58fc-5a97-9230-430f3970d32a", "Joseph J Pelletier"],
  ["0f6b990a-ede2-5cca-9333-74822aa920d9", "Lucien P Pelletier"],
  ["7d7c83e4-92ed-50ed-a062-4e8e1cfa1505", "Raoul Pelletier"],
  ["2aad2534-e457-5bd7-a78f-b89c583f0704", "Mallby K Pelletreau"],
  ["418b5db6-9cd3-5cee-beca-652c8e6b637a", "Anthony B Pelliccia"],
  ["6e7a4c9c-7e23-58ae-8043-30daccf32fcd", "Joseph M.C. Pellizary"],
  ["a4f0168a-1a90-5279-930a-9341988f97b2", "Francis W Peloquin"],
  ["993dd304-355e-541f-8286-1213d9523e7f", "Cornelius H Pelton"],
  ["876e2701-6e0e-5d52-bd5b-5619a9c83ca1", "Jane B Pelton"],
  ["9a7e63db-6dfa-5a00-8162-5541a93e1b5e", "Anthony Peluso"],
  ["28a399b5-4a61-5ec2-b0c4-9102da128bbd", "John R Pemberton"],
  ["ae3503c6-884b-53a8-a68c-ab10abf20fa1", "Edward F Penak"],
  ["dcfb8286-9cd4-536a-8e78-69eeefa3044c", "William Pencak"],
  ["89a5de53-3cf5-5350-8ccb-cc141a9aec82", "Robert J Pence"],
  ["bdf138fb-c6f0-5168-bd57-3b63debdb180", "Clayton C Pend"],
  ["4042d7e9-f997-5b9b-aaa3-ccf1eb77243d", "Carolyn D Pendar"],
  ["6e85e460-a5b1-5e91-a53c-be15fe60f958", "Kenneth W Pendar"],
  ["dfd6bb52-5646-5695-9c4c-c0d248216751", "James R Pender"],
  ["c9ebdb96-df11-5dc7-9c4b-18074b35a533", "Edward S. H. Pendergast"],
] as const;

test("Batch 744 publishes all 23 page-362 profiles with terminal reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\d{4,9}$/);
  }
});

test("Kenneth Pendar publishes a qualified State Department vice-consular assignment", async ({ page }) => {
  await page.goto("./people/6e85e460-a5b1-5e91-a53c-be15fe60f958/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("United States Department of State");
  await expect(main).toContainText("American Vice Consul");
  await expect(main).toContainText("Casablanca");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("Notes by the President's Special Assistant");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("accepted Army matches publish identity evidence without invented employers", async ({ page }) => {
  for (const id of [
    "9ae53621-cacd-5e9e-b163-7e61cf628380",
    "0f6b990a-ede2-5cca-9333-74822aa920d9",
    "418b5db6-9cd3-5cee-beca-652c8e6b637a",
    "a4f0168a-1a90-5279-930a-9341988f97b2",
    "993dd304-355e-541f-8286-1213d9523e7f",
    "89a5de53-3cf5-5350-8ccb-cc141a9aec82",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("suffix and name conflicts remain visibly qualified", async ({ page }) => {
  await page.goto("./people/2aad2534-e457-5bd7-a78f-b89c583f0704/");
  await expect(page.locator("main")).toContainText("Mallby K Pelletreau");
  await expect(page.locator("main")).toContainText("Maltby K Pelletreau");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/28a399b5-4a61-5ec2-b0c4-9102da128bbd/");
  await expect(page.locator("main")).toContainText("John R Pemberton Jr.");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/c9ebdb96-df11-5dc7-9c4b-18074b35a533/");
  await expect(page.locator("main")).toContainText("Edward S. H. Pendergast Jr.");
  await expect(page.locator("main")).toContainText("probable");
});

test("printed notes and malformed serial renderings remain recoverable but masked", async ({ page }) => {
  await page.goto("./people/9ae53621-cacd-5e9e-b163-7e61cf628380/");
  await expect(page.locator("main")).toContainText("One fold");

  await page.goto("./people/0f6b990a-ede2-5cca-9333-74822aa920d9/");
  await expect(page.locator("main")).toContainText("Also 088");

  await page.goto("./people/6e7a4c9c-7e23-58ae-8043-30daccf32fcd/");
  await expect(page.locator("main")).toContainText("Folder tr");

  await page.goto("./people/bdf138fb-c6f0-5168-bd57-3b63debdb180/");
  await expect(page.locator("main")).toContainText("Folder e");

  await page.goto("./people/7d7c83e4-92ed-50ed-a062-4e8e1cfa1505/");
  await expect(page.locator("main")).toContainText("••••21E0");
  await expect(page.locator("main")).not.toContainText("3.12821e+0");

  await page.goto("./people/9a7e63db-6dfa-5a00-8162-5541a93e1b5e/");
  await expect(page.locator("main")).toContainText("••••92E0");
  await expect(page.locator("main")).not.toContainText("3.26592e+0");
});

test("home page exposes the rebuilt Batch 744 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,142");
  await expect(home).toContainText("42.37%");
  await expect(home).toContainText("13,792");
  await expect(home).toContainText("756");
  await expect(home).toContainText("337");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
