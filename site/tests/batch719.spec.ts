import { expect, test } from "@playwright/test";

const profiles = [
  ["e6923b45-d6bf-5554-89a4-4d4ab7c76e8a", "Curtis Olson"],
  ["c1faf882-2367-578a-90d9-f5339dd2d83b", "Donald E Olson"],
  ["6aaf2a6f-13bb-589c-a53d-fe0f5c31391b", "Ernest Olson"],
  ["f4b22c9a-2407-578a-8372-f23f8bc82daa", "Evald B Olson"],
  ["b7fe99b0-7541-52e4-9a8e-14254cdd0b1b", "Greta G Olson"],
  ["fb67cca2-3aac-5d36-b4f6-87f0e94dae42", "Harlan R Olson"],
  ["e26cfe0a-e761-583f-97bd-83164835c4ea", "Herbert W Olson"],
  ["af1d4a68-3906-5380-bf3e-f7a17a941598", "Howard J Olson"],
  ["98f1a000-4190-5be8-93c6-3908627d492a", "John E Olson"],
  ["8d283571-88b9-598a-b9c6-7e223f653b51", "John P Olson"],
  ["7a560371-c590-560a-824e-45a30c6ec7fb", "Lois Olson"],
  ["3abac725-5dc7-57c7-a171-7ccc8941f0a6", "Lynn H Olson"],
  ["2416f3d9-6634-5e37-b852-644c33d982f2", "Mable E Olson"],
  ["698b025d-9833-5ce0-aa9a-7f75ec9f052d", "Oliver A Olson"],
  ["9a483fdc-7de7-53cb-899f-deb5154756aa", "Robert A Olson"],
  ["c748b549-a655-50ee-aa3e-8dc137096842", "Mary L Olsson"],
  ["2f07c879-0403-5aef-836a-6c149b664d2c", "Harry A Olwell"],
  ["0fc4329d-c242-54e3-91a6-7582ed49751a", "Frank P Omalley"],
  ["9e5948f4-e4e2-5c62-ad4b-9fc90cbffef2", "John M Omalley"],
  ["58457817-f912-5082-8852-a15b077caf93", "Joseph H Omalley"],
  ["79c6cb4a-c741-5da9-9ab5-5935905eeb96", "Robert C Omalley"],
  ["a6575633-9097-5b3d-9176-41cf72deb7eb", "Carla A Oman"],
  ["49032d8d-c62b-5447-bcc5-055eadee8817", "Donn M Omeara"],
] as const;

test("Batch 719 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 719 publishes Joseph H Omalley's pre-OSS military pathway without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/58457817-f912-5082-8852-a15b077caf93/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Joseph Henry O'Malley");
  await expect(main).toContainText("United States Military Academy");
  await expect(main).toContainText("Cadet");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Cavalry officer");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("Official Army Register for 1945");
});

test("Batch 719 keeps John E Olson and John E Olsen separate despite the shared identifier", async ({ page }) => {
  await page.goto("./people/98f1a000-4190-5be8-93c6-3908627d492a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Duplicate group");
  await expect(main).toContainText("John E Olsen");
  await expect(main).not.toContainText("13175112");
});

test("Batch 719 preserves the Carla A Oman and Donn M Omeara identity conflicts", async ({ page }) => {
  await page.goto("./people/a6575633-9097-5b3d-9176-41cf72deb7eb/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("cannot yet be equated with the Army record for Carl A Oman");

  await page.goto("./people/49032d8d-c62b-5447-bcc5-055eadee8817/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("cannot be equated with the Army record for Albert L Monett");
});

test("Batch 719 publishes accepted Army identities without inventing employment", async ({ page }) => {
  for (const id of [
    "e6923b45-d6bf-5554-89a4-4d4ab7c76e8a",
    "8d283571-88b9-598a-b9c6-7e223f653b51",
    "9a483fdc-7de7-53cb-899f-deb5154756aa",
    "2f07c879-0403-5aef-836a-6c149b664d2c",
    "9e5948f4-e4e2-5c62-ad4b-9fc90cbffef2",
    "79c6cb4a-c741-5da9-9ab5-5935905eeb96",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("nonshared protected identifier agree with Army bulk ordinal");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 719 publishes exact rebuilt coverage and preserves the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,575");
  await expect(main).toContainText("40.00%");
  await expect(main).toContainText("14,359");
  await expect(main).toContainText("726");
  await expect(main).toContainText("326");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Joseph H Omalley");
});
