import { expect, test } from "@playwright/test";

const profiles = [
  ["803e1207-e821-5763-bbfd-bd42d4c14a00", "Camden L Rogers"],
  ["a4a96717-274c-53f3-887e-8269857e4902", "Carl Rogers"],
  ["1c9f5b63-0960-55a2-8307-28a511fbc61e", "Dana Rogers"],
  ["52a60154-9acd-503f-821d-c219bc8980c3", "Fanny G Rogers"],
  ["3756048a-4918-5033-b869-40c972e117b6", "Fred S Rogers"],
  ["3199ce2e-72db-501e-a5d4-88962fdc0aa9", "George A Rogers Jr."],
  ["d996947e-596f-5045-98ab-0a8e80541f7e", "Harold Rogers"],
  ["3e50e062-e22f-5353-b42c-019128514eb0", "J A Rogers"],
  ["91063597-f7a0-5a21-a8bc-9179ec67fa25", "James G Rogers"],
  ["c1514f70-ea17-5fbb-8f01-59bc711b7944", "Joanne Rogers"],
  ["613aa412-25d4-512a-bad1-04cd6f5052f5", "John R Rogers"],
  ["9d9190c4-cff4-5667-baca-43c1d1273efb", "John Albert A Rogers"],
  ["dd3a60d5-c31a-5e67-83fd-e09a0cf9f8c1", "Lyman E Rogers"],
  ["53d4f8bd-68d9-5f6c-8645-74852e9d574b", "Margaret E Rogers"],
  ["1cbfd7d2-a9db-53dc-86fe-da56c7a81a20", "Martin R Rogers"],
  ["6ef870bd-f02d-5b6b-b92f-cd36e195b601", "Martin R Rogers"],
  ["0b75565e-7fbc-5636-abcd-335791c7647e", "Pauline W Rogers"],
  ["055ca8c5-a03c-5850-99fe-2bd7a51a4cb5", "Preston Rogers"],
  ["f1360bd0-4865-5582-921b-2aa30ec327d3", "Ralph T Rogers"],
  ["44e9edf1-c49c-5c1c-9b84-74a81c01d84c", "Robert M Rogers"],
  ["818d8e5e-49c4-513e-9221-434079038304", "Stanwood N Rogers"],
  ["9dbbf83d-95cc-5dee-ae85-a63a798793a3", "William W Rogers"],
  ["1b62e9a5-19c2-5ae9-9f10-1287217110cc", "William G Rogers"],
] as const;

test("Batch 816 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("accepted Army identities do not become inferred employers", async ({ page }) => {
  for (const id of [
    "613aa412-25d4-512a-bad1-04cd6f5052f5",
    "9d9190c4-cff4-5667-baca-43c1d1273efb",
    "055ca8c5-a03c-5850-99fe-2bd7a51a4cb5",
    "1b62e9a5-19c2-5ae9-9f10-1287217110cc",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("confirmed");
    await expect(main).toContainText("official Army");
    await expect(main).toContainText("No reliable pre-OSS employer");
  }
});

test("George and Robert Rogers expose identifier conflicts without merging namesakes", async ({ page }) => {
  await page.goto("./people/3199ce2e-72db-501e-a5d4-88962fdc0aa9/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("KORETSKY HARRY");
  await expect(main).toContainText("No merge is made");

  await page.goto("./people/44e9edf1-c49c-5c1c-9b84-74a81c01d84c/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("ROJAS RUTIN M");
  await expect(main).toContainText("No merge is made");
});

test("the two Martin R Rogers rows remain distinct people", async ({ page }) => {
  await page.goto("./people/1cbfd7d2-a9db-53dc-86fe-da56c7a81a20/");
  let main = page.locator("main");
  await expect(main).toContainText("P-5");
  await expect(main).toContainText("Page 398");

  await page.goto("./people/6ef870bd-f02d-5b6b-b92f-cd36e195b601/");
  main = page.locator("main");
  await expect(main).toContainText("2D LT");
  await expect(main).toContainText("Page 398");
});

test("unassigned employment leads remain qualified and routed to archival review", async ({ page }) => {
  await page.goto("./people/818d8e5e-49c4-513e-9221-434079038304/");
  let main = page.locator("main");
  await expect(main).toContainText("MGM art-director namesake");
  await expect(main).toContainText("remains unassigned");
  await expect(main).toContainText("No reliable pre-OSS employer");

  await page.goto("./people/9dbbf83d-95cc-5dee-ae85-a63a798793a3/");
  main = page.locator("main");
  await expect(main).toContainText("Rochester technical-school instructor");
  await expect(main).toContainText("remains unassigned");
  await expect(main).toContainText("No reliable pre-OSS employer");
});

test("home page exposes the rebuilt Batch 816 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,751");
  await expect(home).toContainText("49.09%");
  await expect(home).toContainText("12,182");
  await expect(home).toContainText("839");
  await expect(home).toContainText("377");
  await expect(home).toContainText("10,215");
});
