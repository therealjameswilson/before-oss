import { expect, test } from "@playwright/test";

const profiles = [
  ["5f29c5d0-6a99-5700-a096-56209fc5f812", "Maida O Oliver"],
  ["6e5c3eee-cf2c-56a2-af6f-c4851aab62a4", "Richard H Oliver"],
  ["3edde251-f5c9-5225-8d7f-01851be5b3ea", "Victor M Oliveria"],
  ["b69ce22a-daf3-505c-98f2-db5b3c904b70", "Jean M Olivier"],
  ["e3cbb54f-4497-5625-915b-63313a7a4d72", "Richard P Ollenburg"],
  ["959fe8b4-331e-5242-8e0c-fcd3b09f51d6", "Bernadine V Ollinger"],
  ["9bb0e60e-a584-5ce9-95d4-9d03643fdff0", "Clarence W Olmstead"],
  ["fa37bfc8-0511-5bc0-801c-4e9677c0b7a1", "John M Olmstead"],
  ["b942ce85-9c99-5f0a-a9cd-41432adae90e", "Martha K Olmstead"],
  ["fd171a98-c923-5b62-ad52-aadd0b2ae19f", "Nicholas V Olos"],
  ["560ffee0-88ad-5f3a-a5ee-9965c5907c09", "Benjamin C Olsen"],
  ["32c1bb2d-8f96-5148-ad72-cd2d9da930f4", "Erik J Olsen"],
  ["f14aef2d-a69b-50be-b65a-a4053b73581b", "Erling M Olsen"],
  ["d3fe53df-6f71-59ca-b230-1a1d10436a23", "Franklin H Olsen"],
  ["fcf6cb1a-1dad-599a-9848-70555fe1a044", "Harvey W Olsen"],
  ["e2c38b76-bbff-5e9b-a08a-0fc3377188bb", "Iver C Olsen"],
  ["e4bb76c8-58b4-5678-bae7-30c446421754", "John E Olsen"],
  ["789f1fd0-9ef1-54fc-bc32-63dea6313e15", "Lynn T Olsen"],
  ["bec6d32e-0149-5404-9fc2-6e319af54a05", "Matthias C Olsen"],
  ["fb662b9c-7090-5254-91c5-f0d3414bd724", "Olaf Olsen"],
  ["ec91021f-dfac-5695-8af0-cc901a41369e", "Oliver A Olsen"],
  ["fc54bc9a-fce8-5e2b-a8cc-001aa5150d71", "Rodney E Olsen"],
  ["d65b9333-c8d3-5fae-ac0d-17e47aeb23a0", "Clinton L Olson"],
] as const;

test("Batch 718 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 718 publishes Clinton L Olson's military pathway without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/d65b9333-c8d3-5fae-ac0d-17e47aeb23a0/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("United States Military Supply Mission to the Soviet Union");
  await expect(main).toContainText("Deputy to the mission chief");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Office of the Chief of Ordnance");
  await expect(main).toContainText("Production Control Officer, Small Arms Division");
  await expect(main).toContainText("Stanford University");
  await expect(main).toContainText("Graduate student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("Clinton L. Olson Oral History");
});

test("Batch 718 preserves Nicholas V Olos and Nicholas V Olds as a name conflict", async ({ page }) => {
  await page.goto("./people/fd171a98-c923-5b62-ad52-aadd0b2ae19f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("cannot yet be equated with the Army record for Nicholas V Olds");
  await expect(main).toContainText("Box 571");
  await expect(main).not.toContainText("13141820");
});

test("Batch 718 keeps John E Olsen and John E Olson separate despite the shared identifier", async ({ page }) => {
  await page.goto("./people/e4bb76c8-58b4-5678-bae7-30c446421754/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Duplicate group");
  await expect(main).toContainText("John E Olson");
  await expect(main).not.toContainText("13175112");
});

test("Batch 718 publishes accepted Army identities without inventing employment", async ({ page }) => {
  for (const id of [
    "3edde251-f5c9-5225-8d7f-01851be5b3ea",
    "e3cbb54f-4497-5625-915b-63313a7a4d72",
    "f14aef2d-a69b-50be-b65a-a4053b73581b",
    "fc54bc9a-fce8-5e2b-a8cc-001aa5150d71",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("nonshared protected identifier agree with Army bulk ordinal");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 718 publishes exact rebuilt coverage and preserves the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,552");
  await expect(main).toContainText("39.90%");
  await expect(main).toContainText("14,382");
  await expect(main).toContainText("725");
  await expect(main).toContainText("326");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Clinton L Olson");
});
