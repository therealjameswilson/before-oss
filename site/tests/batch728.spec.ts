import { expect, test } from "@playwright/test";

const profiles = [
  ["58d5b8dd-fbf7-5304-94a5-d0ce242d5b56", "Charles H Padden"],
  ["9e4a04bf-4c6f-52cc-9de0-ca3f41b0a783", "Fred M Padgett"],
  ["dd88d672-eb28-53b4-9d05-24088248e78e", "Harold E Padgett"],
  ["1990c01d-a751-5014-a2cb-a37e7b540a66", "Sosteno Padilla"],
  ["caaea89e-a840-5780-8121-fddff9a32e81", "Vincent A Pado"],
  ["6c04259d-0aaf-5c19-87e9-6fb1d7000112", "Saul K Padover"],
  ["6bc751d1-53ad-5d76-a08c-c71392748fb3", "Joseph Padula"],
  ["b02ffee4-39ee-5f1d-ac26-9d5166780ac6", "Henry M Paechter"],
  ["19ec2a67-0ab2-50dc-a7c5-bda7e75a6300", "Salvatore C Pagand"],
  ["2766b9e4-b2fc-5a24-95f1-ed9476b80fc4", "Joseph M Pagano"],
  ["57c9d8fc-59dc-533f-9652-b2f7f0705b7a", "Andre R Pagatte"],
  ["8f25077d-d682-55d8-a4a0-fdd6c413c59c", "Alicia E Page"],
  ["e3901033-75e4-5ff6-a93a-af997218ef92", "Eloise E Page"],
  ["3f3c3891-8220-560a-8ccd-78c3a0718da5", "Emma J Page"],
  ["86f1278a-d139-5436-8e0d-c1725ad6573f", "George K Page"],
  ["eb6d5855-c956-5ead-88fc-2448c1deb61c", "Henry Page"],
  ["af69675f-6af8-5235-bbfc-8813641c6ad9", "Jean B Page"],
  ["5beee1c2-facd-550b-bc07-5675126780ad", "Jimmie Page"],
  ["b914d48c-035a-5b64-98f1-29f818fcd966", "Keith A Page"],
  ["e693205d-3e8f-5770-9706-f52131bd921e", "Lewis W Page"],
  ["6d6fe81f-257b-5a2d-9abd-968171f89f3e", "Shelby Page"],
  ["decfb5d6-4408-5030-a104-e6b432dc2eb0", "Walter H Page"],
  ["fa0857b9-fa64-5be4-8e56-a368038b1fe3", "Wellman Page"],
] as const;

test("Batch 728 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 728 publishes Paechter-Pachter identity and qualified freelance work", async ({ page }) => {
  await page.goto("./people/b02ffee4-39ee-5f1d-ac26-9d5166780ac6/");
  const main = page.locator("main");
  await expect(main).toContainText("Henry M. Pachter");
  await expect(main).toContainText("Heinz Maximilian Paechter");
  await expect(main).toContainText("Freelance writer and lecturer");
  await expect(main).toContainText("1930");
  await expect(main).toContainText("1933");
  await expect(main).toContainText("University at Albany");
  await expect(main).toContainText("documented prewar employer found");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationSelf-employed");
  await expect(main).not.toContainText("Last civilian employerSelf-employed");
});

test("Batch 728 uses the Simcol roster for Padula identity, not employment", async ({ page }) => {
  await page.goto("./people/6bc751d1-53ad-5d76-a08c-c71392748fb3/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Simcol");
  await expect(main).toContainText("T5 Joseph Padula");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationSimcol");
  await expect(main).not.toContainText("Last civilian employerSimcol");
});

test("Batch 728 preserves both official identity conflicts", async ({ page }) => {
  await page.goto("./people/caaea89e-a840-5780-8121-fddff9a32e81/");
  await expect(page.locator("main")).toContainText("Vincent A Pade Jr");
  await expect(page.locator("main")).toContainText("conflicting sources");

  await page.goto("./people/57c9d8fc-59dc-533f-9652-b2f7f0705b7a/");
  await expect(page.locator("main")).toContainText("Andre R Pacatte");
  await expect(page.locator("main")).toContainText("conflicting sources");
  await expect(page.locator("main")).not.toContainText("Berlitz School of Languages");
});

test("Batch 728 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,780");
  await expect(main).toContainText("40.85%");
  await expect(main).toContainText("14,154");
  await expect(main).toContainText("739");
  await expect(main).toContainText("331");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Henry M Paechter");
});
