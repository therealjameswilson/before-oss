import { expect, test } from "@playwright/test";

const profiles = [
  ["9b6ebdeb-3d1b-5e18-ad62-84818e61e306", "Earl G Rowell"],
  ["7b25d150-d285-5d30-92f9-9bc46e4aa9ce", "Betty S Rower"],
  ["f5ec02b6-02d3-570f-bd31-d7d4d2ae0f1e", "Diana Rowland"],
  ["3603b522-fde8-5542-9e44-22c03249549b", "Edward J Roy"],
  ["483156b0-e0b4-5380-b2c5-6977bdeb0b88", "Elaine G Roy"],
  ["7b7d07b2-36b8-518b-a56c-c8fe865d132a", "Emile G Roy"],
  ["6a51b632-fd5a-5de0-b01c-dc8987c145c4", "Jean E Roy"],
  ["38281b2b-39e0-52c5-bd32-671aea48e833", "Robert F Roy"],
  ["abb89ac5-094f-57f0-a4db-ffe17ac73eeb", "Wilmo R Roy"],
  ["fe3b30b8-77b6-599a-add3-b6034f7ce288", "Herbert F Roye"],
  ["2b9dcdba-a28c-55e1-8bc1-18c7f8392ab7", "Howard E Roylance"],
  ["7235ed9e-6b23-5081-bcda-78b787ab7bd8", "Morton W Royse"],
  ["04862878-1777-5d5f-bf00-a84f37f347fe", "Alexander M Rozanoff"],
  ["38fb02d5-2bef-514f-a766-19859efff436", "Joseph Rozman"],
  ["7d19a893-a458-5ace-9036-08ee76dd65e9", "Anthony P Rua"],
  ["7c54dd6d-0130-52dc-9b21-4853fc687992", "Ernest Ruben"],
  ["b372409f-ec23-5c84-9ee8-212e8d145227", "Sidney S Rubenstein"],
  ["6265606f-e13b-5b7f-a274-9c7cc25633de", "Hannah Rubin"],
  ["ffed5d7e-8807-5755-b1ad-bde1ceae8b12", "Herbert Rubin"],
  ["c31c6042-10aa-5769-88ae-c8d734676715", "Robert H Rubin"],
  ["581beeca-5acb-5f1c-ae41-4e8aa20f9ede", "Stanley Rubini"],
  ["77732183-1bd6-53ad-a817-3ac8da82359e", "Josip Rubinic"],
  ["3adfc247-b00c-5907-aac4-67b7b3853d09", "Christopher Rubio"],
] as const;

test("Batch 825 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Morton Royse profile separates documented prewar work from the immediate-affiliation question", async ({ page }) => {
  await page.goto("./people/7235ed9e-6b23-5081-bcda-78b787ab7bd8/");
  const main = page.locator("main");
  await expect(main).toContainText("Federal Writers' Project");
  await expect(main).toContainText("social-ethnic studies editor");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("not as an immediate predecessor");
  await expect(main).toContainText("Projects - MO - Royse in Crete");
});

test("Herbert Roye profile publishes identity corroboration without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/fe3b30b8-77b6-599a-add3-b6034f7ce288/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Captain-to-Major-to-Colonel");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("accepted Army identities do not expose coded occupations or invent employers", async ({ page }) => {
  for (const id of [
    "7b7d07b2-36b8-518b-a56c-c8fe865d132a",
    "7d19a893-a458-5ace-9036-08ee76dd65e9",
    "ffed5d7e-8807-5755-b1ad-bde1ceae8b12",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("occupation code");
  }
});

test("rejected Army name conflicts remain visible and unmerged", async ({ page }) => {
  const cases = [
    ["04862878-1777-5d5f-bf00-a84f37f347fe", "Stratton Earl E"],
    ["abb89ac5-094f-57f0-a4db-ffe17ac73eeb", "Herbert W. Kuelling"],
    ["581beeca-5acb-5f1c-ae41-4e8aa20f9ede", "Rubint Stanley"],
  ] as const;
  for (const [id, conflictingName] of cases) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText(/rejected/i);
    await expect(main).toContainText("conflicting sources");
  }
});
