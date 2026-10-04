import { expect, test } from "@playwright/test";

const profiles = [
  ["6fbad49a-53e4-5d14-aed9-758a47d822da", "Laura M Norris"],
  ["7ad07c6f-6450-537b-b252-10c269a5c026", "Leonard E Norris"],
  ["1323fda9-7315-5d91-99c1-1927c238b51d", "Marshall G Norris"],
  ["4be5195f-e2d8-5640-8b66-2f47212ef215", "Mary T Norris"],
  ["aa4b133b-9956-5bde-8e37-0b8194528ba0", "Steve F Norsic Jr."],
  ["16415eb2-bb53-592d-9476-1aea8bcf76f7", "Henry R North"],
  ["001ce3f6-c322-5afc-bbb9-185266e56087", "Robert G North"],
  ["be4fc838-d317-5967-b1f4-c1ed50175fe5", "David T Northault"],
  ["cedbe6da-94e6-53bd-8978-e6e46410bf10", "Robert P Northup"],
  ["1182a15d-d230-569c-b3bc-4b6199a2bf52", "Clara H Norton"],
  ["1f894653-a29c-5fe9-808b-c227d96b4d16", "Edna V Norton"],
  ["f22258ab-8cdf-5294-aa89-86e4f6ac825c", "Irving M Norton"],
  ["6325ef4b-f8d0-5a95-b953-24663e295a43", "James E Norton"],
  ["b9371607-e7ae-5347-9129-290ce99914f6", "William A Norton"],
  ["41b68919-d03d-5d57-88ca-be1bc5b6dacc", "Wilson K Norton"],
  ["72bbf8a7-58bd-5693-ab3f-097a5536bc0c", "William A Norwood"],
  ["e379e1ee-bfdc-5a14-b342-b8f498511033", "William A Notbohm"],
  ["44f61989-07da-5a7b-86ac-b59f2f5bf6b6", "Rudolf S Nothmann"],
  ["ea689f2d-719a-5158-9de9-de027ca15c52", "Theodore Notides"],
  ["ab12ff88-de43-5a0f-ab42-375cbf91e891", "Barbara A Notman"],
  ["090efe49-9e60-5ebd-8139-178e862d22e9", "Genevieve M Noto"],
  ["f1caaad5-1498-59a3-beb9-8bc0234e686f", "Leroi G Nottoli"],
  ["2805e6d1-cab3-5a2f-9668-f06389fc89ad", "Charles J Novak"],
] as const;

test("Batch 709 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 709 classifies Robert Northup's Cornell record as education, not employment", async ({ page }) => {
  await page.goto("./people/cedbe6da-94e6-53bd-8978-e6e46410bf10/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Cornell University");
  await expect(main).toContainText("Mechanical Engineering student");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Cornell University was his employer");
});

test("Batch 709 publishes Theodore Notides's dated banking chronology", async ({ page }) => {
  await page.goto("./people/ea689f2d-719a-5158-9de9-de027ca15c52/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Manufacturers Trust Company");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Corn Exchange Bank & Trust Company");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
});

test("Batch 709 preserves surname conflicts and the adjacent shared-identifier pair", async ({ page }) => {
  await page.goto("./people/be4fc838-d317-5967-b1f4-c1ed50175fe5/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("David T Northcutt");

  await page.goto("./people/44f61989-07da-5a7b-86ac-b59f2f5bf6b6/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("Rudolf Nothman");

  for (const id of ["41b68919-d03d-5d57-88ca-be1bc5b6dacc", "72bbf8a7-58bd-5693-ab3f-097a5536bc0c"]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Identity statusprobable");
    await expect(page.locator("main")).toContainText("Duplicate groupduplicate-");
  }
});

test("Batch 709 preserves visually confirmed index anomalies without exposing full identifiers", async ({ page }) => {
  await page.goto("./people/7ad07c6f-6450-537b-b252-10c269a5c026/");
  const leonard = page.locator("main");
  await expect(leonard).toContainText("requires archival review");
  await expect(leonard).toContainText("Serial••••5633");
  await expect(leonard).not.toContainText("Serial5633");

  await page.goto("./people/4be5195f-e2d8-5640-8b66-2f47212ef215/");
  await expect(page.locator("main")).toContainText("folders s");

  await page.goto("./people/090efe49-9e60-5ebd-8139-178e862d22e9/");
  await expect(page.locator("main")).toContainText("possible");
});

test("Batch 709 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,346");
  await expect(main).toContainText("39.04%");
  await expect(main).toContainText("323");
  await expect(main).toContainText("14,588");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
