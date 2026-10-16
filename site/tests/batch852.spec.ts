import { expect, test } from "@playwright/test";

const profiles = [
  ["d0f5c183-e2cd-555d-ab7e-8d297f3b74ab", "Ernest C Schulz"],
  ["621e1624-a829-534c-b0ac-da3c101d8e56", "Marjorie M Schulz"],
  ["450c8291-12dd-58a3-82bb-b522b663c431", "Gordon Schulze"],
  ["7e52a7f7-67b2-5007-88e9-8e7fde9c0f2c", "Eileen Schumaker"],
  ["f9f893a6-c4cd-59d5-a901-aab63b0de762", "Mary H Schupp"],
  ["01e93ce3-14d8-55cc-a76f-e37f8860b867", "Joseph R Schurman"],
  ["443575d2-8f57-54ce-a7fe-a7b7a6b23fc2", "Sam H Schurr"],
  ["d644ca01-1045-5458-ac8d-3373d7a2ca4b", "Walter Schuschnigg"],
  ["988e5fc2-a081-5c85-b3ca-d442478ff56e", "Albert H Schuster"],
  ["7ddd8ae8-79e5-5d68-a1f1-95bf571c1cf4", "Albert H Schuster"],
  ["dceb8a9a-1d83-5ce5-917f-b0cc41ccdfd0", "Carl Schuster"],
  ["92c273a5-0bfc-5b71-aa48-67ec3d001803", "Louis J Schutty"],
  ["f9834b32-435e-5903-baef-a44c1e3cb6c1", "Helen M Schuyler"],
  ["acba71d8-90b3-5d58-a17c-e74d5172c7c5", "Jerome C Schuyler"],
  ["3f38a5fa-471d-5571-8753-1fa60a366e3e", "William M Schuyler"],
  ["8c556884-bc99-5ee2-a547-9bd86e459c27", "Hermann C Schwab"],
  ["632bb4f0-a8b8-55ae-82f6-852d01efc8e0", "Walter H Schwab"],
  ["1a8bf061-2053-5a2b-bda0-5a92ad5d6717", "John Schwabauer"],
  ["d15e0ca9-e451-5d37-9b76-0be92622166a", "Charles Schwanda"],
  ["4c20bdef-18bb-55f8-a221-820e19b016da", "Frank Schwaner"],
  ["ba02d5d6-531c-5d07-95e2-5c68c926bee8", "Sanford Schwars"],
  ["62745da7-0c09-58fa-be20-99a797c8d9aa", "Leopold Schwarsschild"],
  ["9739ed19-e030-5d94-bd91-2593dfacc0de", "Esther A Schwarts"],
] as const;

test("Batch 852 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Sam Schurr publishes NBER as both immediate affiliation and last civilian employer", async ({ page }) => {
  await page.goto("./people/443575d2-8f57-54ce-a7fe-a7b7a6b23fc2/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("National Bureau of Economic Research");
  await expect(main).toContainText("research economist");
  await expect(main).toContainText("The Washington Post");
  await expect(main).toContainText("The Mining Industries, 1899-1939");
});

test("Joseph Schurman keeps Cornell student status separate from employment", async ({ page }) => {
  await page.goto("./people/01e93ce3-14d8-55cc-a76f-e37f8860b867/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Cornell University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).toContainText("The Washington Post");
  await expect(main).toContainText("Harvard Law School");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceCornell University");
});

test("Army-only Batch 852 identities do not publish coded occupations as employers", async ({ page }) => {
  for (const id of [
    "d0f5c183-e2cd-555d-ab7e-8d297f3b74ab",
    "7ddd8ae8-79e5-5d68-a1f1-95bf571c1cf4",
    "acba71d8-90b3-5d58-a17c-e74d5172c7c5",
    "632bb4f0-a8b8-55ae-82f6-852d01efc8e0",
    "1a8bf061-2053-5a2b-bda0-5a92ad5d6717",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("the two Albert Schuster rows remain separate and expose the material conflict", async ({ page }) => {
  await page.goto("./people/988e5fc2-a081-5c85-b3ca-d442478ff56e/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("duplicate-3f642397c88d");
  await expect(main).toContainText("Ralph E. Davis");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceRalph E. Davis");

  await page.goto("./people/7ddd8ae8-79e5-5d68-a1f1-95bf571c1cf4/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("duplicate-3f642397c88d");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("qualified student affiliations remain students rather than employers", async ({ page }) => {
  for (const [id, institution] of [
    ["8c556884-bc99-5ee2-a547-9bd86e459c27", "Yale University"],
    ["d15e0ca9-e451-5d37-9b76-0be92622166a", "Wesleyan University"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusprobable");
    await expect(main).toContainText(institution);
    await expect(main).toContainText("student");
    await expect(main).toContainText("medium documented pre-OSS");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(`Last civilian employer before service${institution}`);
  }
});

test("Leopold Schwarsschild publishes qualified editorship dates and source disagreement", async ({ page }) => {
  await page.goto("./people/62745da7-0c09-58fa-be20-99a797c8d9aa/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Das Neue Tage-Buch");
  await expect(main).toContainText("1933");
  await expect(main).toContainText("1940");
  await expect(main).toContainText("Deutsche Biographie");
  await expect(main).toContainText("Leo Baeck Institute");
  await expect(main).toContainText("discrepancy");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationDas Neue Tage-Buch");
  await expect(main).not.toContainText("Last civilian employer before serviceDas Neue Tage-Buch");
});
