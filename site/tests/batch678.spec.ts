import { expect, test } from "@playwright/test";

const profiles = [
  ["be9ff307-e61a-51c8-a87c-864b03eacf70", "Horace F Morgan"],
  ["6c876dcb-3bd1-52ac-9bc4-52aa3a4b16b7", "James D Morgan"],
  ["81fefcad-b4bc-5af9-8ce3-c0919ab4bc01", "John T/J Morgan"],
  ["3ded1a1a-bebb-555c-b3da-d951a8b640a7", "Joseph E Morgan"],
  ["aaa83b52-5ab0-5c86-9146-db6dc477dd9e", "Junius S Morgan"],
  ["499ddff2-f339-549e-bd53-9cbc89e0bd42", "Leon Morgan"],
  ["6791356f-8552-5660-a72d-1bbd90ee782c", "Melvin Morgan"],
  ["3689017c-093f-559b-9913-9fca90d4b302", "Morgan H Morgan"],
  ["95a85bed-369b-50d8-be24-1a9e22cd9417", "Ralph D Morgan"],
  ["f59008bd-9fb8-51df-a711-31c787dd359e", "Raymond F Morgan"],
  ["a43c2070-0ffc-5822-96e3-13b827e851ff", "Roy M Morgan"],
  ["82848f9e-7b39-5053-8be5-89fc8d616703", "Russell K Morgan"],
  ["fcf39fc7-6cf7-5f1a-a1d8-172342fa275a", "Shepard Morgan"],
  ["bfccc6e3-ec5b-5345-8a75-6bca70b8bce8", "Sylvia Morgan"],
  ["9c46afa9-cc87-5967-8fd7-b5731d09d598", "Thelma Morgan"],
  ["2bcc0178-9b2d-5ca6-8e20-07943c9b9533", "Thomas B Morgan"],
  ["232b3c0e-0988-59b0-a34c-9984cc3170c8", "William J Morgan"],
  ["6876b7ae-3d5f-5ef1-be7f-bea987ffbeaa", "Willis F Morgan"],
  ["b103f936-8713-53ae-ab14-15b94df853e2", "Melvin Morgen"],
  ["ff57f99c-f0ec-5553-a0dc-69f0272c7311", "Stern S Morgen"],
  ["354a3252-95e3-5c20-94b3-af2887af9589", "Andrew Morguest"],
  ["0a5ee8da-66c1-501d-8f4e-a0ee0f29abc2", "Charles Y Mori"],
] as const;

const highConfidenceArmyMatches = [
  ["be9ff307-e61a-51c8-a87c-864b03eacf70", "Horace F Morgan", "155"],
  ["3ded1a1a-bebb-555c-b3da-d951a8b640a7", "Joseph E Morgan", "999"],
  ["3689017c-093f-559b-9913-9fca90d4b302", "Morgan H Morgan", "773"],
  ["95a85bed-369b-50d8-be24-1a9e22cd9417", "Ralph D Morgan", "736"],
  ["f59008bd-9fb8-51df-a711-31c787dd359e", "Raymond F Morgan", "101"],
  ["2bcc0178-9b2d-5ca6-8e20-07943c9b9533", "Thomas B Morgan", "306"],
] as const;

test("Batch 678 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 329");
    await expect(page.locator("main")).toContainText(/Archive box(537|538)/);
  }
});

test("Batch 678 publishes six high-confidence Army identities without employer inference", async ({ page }) => {
  for (const [id, name, privateOccupationCode] of highConfidenceArmyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(`occupation code ${privateOccupationCode}`);
    await expect(main).not.toContainText(`civilian_occupation_code=${privateOccupationCode}`);
  }
});

test("Batch 678 keeps the Melvin Morgan and Melvin Morgen rows separate", async ({ page }) => {
  await page.goto("./people/6791356f-8552-5660-a72d-1bbd90ee782c/");
  let main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Melvin Morgan", level: 1 })).toBeVisible();
  await expect(main).toContainText("needs identity review");
  await expect(main).toContainText("Melvin Morgen");
  await expect(main).toContainText("shared");

  await page.goto("./people/b103f936-8713-53ae-ab14-15b94df853e2/");
  main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Melvin Morgen", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Melvin Morgan");
  await expect(main).toContainText("Box 538");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 678 rejects the Army namesake mismatch for Stern Morgen", async ({ page }) => {
  await page.goto("./people/ff57f99c-f0ec-5553-a0dc-69f0272c7311/");
  const main = page.locator("main");
  await expect(main).toContainText("MORGENSTEM SAMUEL");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("civilian_occupation_code=580");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 678 publishes Shepard Morgan's Chase employment with bounded chronology", async ({ page }) => {
  await page.goto("./people/fcf39fc7-6cf7-5f1a-a1d8-172342fa275a/");
  const main = page.locator("main");
  const immediateAffiliation = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilianEmployer = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(page.getByRole("heading", { name: "Shepard Morgan", level: 1 })).toBeVisible();
  await expect(main).toContainText("Chase National Bank");
  await expect(main).toContainText("Vice-President");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("R&A/London");
  await expect(immediateAffiliation).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(immediateAffiliation).not.toContainText("Chase National Bank");
  await expect(civilianEmployer).toContainText("Chase National Bank");
});

test("Batch 678 qualifies Thelma Morgan's official commendation lead", async ({ page }) => {
  await page.goto("./people/9c46afa9-cc87-5967-8fd7-b5731d09d598/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Thelma Morgan", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Unit Commander's Certificate of Merit");
  await expect(main).toContainText("104-10165-10120");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("administrative assistant");
});

test("Batch 678 preserves the earlier Junius and William Morgan findings", async ({ page }) => {
  await page.goto("./people/aaa83b52-5ab0-5c86-9146-db6dc477dd9e/");
  await expect(page.locator("main")).toContainText("J.P. Morgan & Co.");
  await expect(page.locator("main")).toContainText("Last civilian employer");

  await page.goto("./people/232b3c0e-0988-59b0-a34c-9984cc3170c8/");
  const main = page.locator("main");
  await expect(main).toContainText("school psychologist");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 678 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,646");
  await expect(page.locator("body")).toContainText("36.12%");
  await expect(page.locator("body")).toContainText("305");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil companies");
  await expect(category).not.toContainText("Shepard Morgan");

  await page.goto("./people/");
  const directoryCategory = page.locator(".featured-directory-category");
  await expect(directoryCategory.locator("li")).toHaveCount(8);
  await expect(directoryCategory).not.toContainText("Shepard Morgan");
});
