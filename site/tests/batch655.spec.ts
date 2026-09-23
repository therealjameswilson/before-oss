import { expect, test } from "@playwright/test";

const profiles = [
  ["1cfb19b2-3838-5331-8f79-d2c49818b29e", "Jack L Meyer"],
  ["49781ae5-8cc5-5579-9b26-2cf0631cc02e", "Milton W Meyer"],
  ["1f6f9224-4542-5b96-9177-e2f96d69029d", "Nancy Meyer"],
  ["7654d384-115e-5cb2-ac21-79731739a0f7", "Orville Meyer"],
  ["3ee4b1b6-07f2-5547-a264-ccb0d7ec9726", "Paul W Meyer"],
  ["305afbd3-a0cc-511c-a28d-af5fd9135d1a", "Ralph H Meyer"],
  ["509bd146-6970-55cc-a4ee-0ed9f7a265e7", "Roberta J Meyer"],
  ["ff09fdc9-ac8a-5d87-b497-fc23addef505", "Walter J Meyer"],
  ["b5e5c8ce-6f16-5307-8e35-dd0d95776baf", "Walter M Meyer"],
  ["528642a1-c20d-503f-920b-f3ae01a8ff41", "Hans Meyerhoff"],
  ["3084dc84-0ed4-599c-86ca-0d29ae0c5390", "Hans Meyerhoff"],
  ["20429821-fa18-532f-8406-d549721679d8", "Albert C Meyers"],
  ["9951dba6-c525-50ae-be8e-35e5ef17b735", "Gerry P Meyers"],
  ["ed74ba42-7cbd-5f6c-9788-32721a9dcd5e", "Mason G Meyers"],
  ["6183293f-c0ef-5931-8df1-02bedd45f9dc", "Norbert Meyers"],
  ["540693d9-8582-5ab3-ab67-4b9713ab5792", "Norman H Meyers"],
  ["8b06f75a-6119-54d1-a13d-71e1221d0465", "Russell H Meyers"],
  ["daa19225-7597-50d4-b61e-33f736947de3", "Thomas D Meyers"],
  ["d17beea7-7b01-53c5-ae79-1c0220a83bbc", "Faye Meyerson"],
  ["074578a3-6509-59cf-8eac-7665d68b49bf", "Winifred A Meyerson"],
  ["d1d9176d-01d1-5421-9221-43975f5c024b", "Emile Meyran"],
  ["a1bc5e98-c7ae-5a00-a319-14a479df8457", "C P Meysereav"],
] as const;

test("Batch 655 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 655 separates Hans Meyerhoff's military, employment, and student relationships", async ({ page }) => {
  await page.goto("./people/3084dc84-0ed4-599c-86ca-0d29ae0c5390/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Army of the United States");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("University of California at Los Angeles");
  await expect(main).toContainText("Teaching Assistant for Visiting Professor Bertrand Russell");
  await expect(main).toContainText("Undergraduate and graduate student");
});

test("Batch 655 publishes Emile Meyran's qualified oil-company chronology", async ({ page }) => {
  await page.goto("./people/d1d9176d-01d1-5421-9221-43975f5c024b/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Compagnie Française de Raffinage");
  await expect(main).toContainText("Engineer");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("Compagnie des Eaux de Paris");
  await expect(main).toContainText("611e compagnie du PMA");
  await expect(main).toContainText("1 August 1910");
  await expect(main).toContainText("1 April 1910");
});

test("Batch 655 leaves the Hans, Norman, and Meysereav clusters visibly conflicting", async ({ page }) => {
  for (const [id, evidence] of [
    ["528642a1-c20d-503f-920b-f3ae01a8ff41", "different ranks and protected identifiers"],
    ["540693d9-8582-5ab3-ab67-4b9713ab5792", "Norman M. Myers"],
    ["a1bc5e98-c7ae-5a00-a319-14a479df8457", "Charles P. Mersereau"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(evidence);
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 655 updates coverage and the top oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,162");
  await expect(page.locator("body")).toContainText("34.09%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil, petroleum, refining, or exploration companies");
  await expect(category).toContainText("Emile Meyran");
  await expect(category).toContainText("Compagnie Française de Raffinage");
  const categoryPrecedesFilters = await category.evaluate((node) => {
    const filters = document.querySelector("#az-nav");
    return Boolean(filters && (node.compareDocumentPosition(filters) & Node.DOCUMENT_POSITION_FOLLOWING));
  });
  expect(categoryPrecedesFilters).toBe(true);

  await page.goto("./oil-companies/");
  const list = page.getByRole("region", { name: "Oil company work list" });
  await expect(list.locator(".oil-directory__person")).toHaveCount(8);
  await expect(list).toContainText("Emile Meyran");
  await expect(list).toContainText("Qualified medium-confidence work claim");
});
