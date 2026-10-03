import { expect, test } from "@playwright/test";

const profiles = [
  ["828ec324-879e-5e50-9219-c25738902a89", "Harry C Nadler"],
  ["289f8732-2af4-58fe-98cb-bfbfdd78b661", "Martin Nadler"],
  ["8a3cc251-afae-59e4-9ad0-bd2cc38b6c28", "Donald P Naetzker"],
  ["11ecf8c3-7f6c-56c2-ab79-721d97ad0945", "Elayne D Naftalin"],
  ["1c5fd899-894e-5a09-b28a-d4049e7b0282", "Gary H Nagai"],
  ["3257b7aa-bec4-5d0c-9252-d3845f306317", "Calvin H Nagel"],
  ["76eb6dae-f326-5ae5-a319-a34d50cb0b14", "Nicholas J Nagel"],
  ["bf54c55b-b3f3-5ab9-b5a5-950d26077bab", "Finn Nagell"],
  ["85082cbe-41d7-50d4-9e0c-cf54d9debd45", "Catherine G Nagle"],
  ["2826bffc-418a-5520-8a84-0b6783a899df", "Albin L Nagler"],
  ["7431faf9-e899-5d9f-b2af-2d74e9046254", "Henry S Nagler"],
  ["7aac8ad6-0c35-5298-bc42-8e647c63482b", "Charles Nagy"],
  ["5cc06ebe-7d22-5bb0-9df0-ebb516d06f44", "Harold E Nail"],
  ["3328f7c0-e130-5522-b94c-a4c1646b2ad9", "Robert J Naismith"],
  ["2ec4cc09-4a4d-55ee-97c4-93597a5bde48", "Yoshinao Nakada"],
  ["1d81d0e1-eea7-5962-967f-e3b7439ea46b", "Kashumi Nakagawa"],
  ["bae9f49a-c79b-540f-99a3-5d5983f7978c", "Alice K Nakajima"],
  ["7959a500-45f6-5752-b3a0-fbf38d7e0c80", "Albert K Nakamura"],
  ["dd659246-3c61-5241-828c-79614bb55b90", "Charles M Nakamura"],
  ["ccf64dbc-ad05-53d4-b4bc-96a7e4a2cca1", "Chaste Y Nakamura"],
  ["79e7e554-041d-53f5-9693-111814f2d40c", "Chiyeko Nakamura"],
  ["e37eacb3-e3f0-5db6-8bf8-72b80609b8b6", "Edward S Nakamura"],
  ["cbd0aa3d-5c0d-5ee4-8dde-08fef2d8e5cb", "Shingi Nakamura"],
] as const;

test("Batch 693 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 693 publishes Chiyeko Nakamura's immediate and last civilian employment", async ({ page }) => {
  await page.goto("./people/79e7e554-041d-53f5-9693-111814f2d40c/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate).toContainText("Columbia University");
  await expect(immediate).toContainText("Part-time Japanese-language teacher");
  await expect(immediate).toContainText("explicit immediate");
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(lastCivilian).toContainText("Columbia University");
  await expect(main).toContainText("Tokyo Dressmaking Women's Institute");
  await expect(main).toContainText("working part-time for Columbia University");
  await expect(main.locator('a[href^="https://www.konan-u.ac.jp/souken/"]')).toHaveCount(4);
});

test("Batch 693 keeps Finn Nagell's two publishers and wartime assignment qualified", async ({ page }) => {
  await page.goto("./people/bf54c55b-b3f3-5ab9-b5a5-950d26077bab/");
  const main = page.locator("main");
  await expect(main).toContainText("J.W. Cappelens Forlag");
  await expect(main).toContainText("Steenske Forlag");
  await expect(main).toContainText("Norwegian Ministry of Defence Intelligence Office");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 693 keeps Caltech attendance separate from Yoshinao Nakada's employment", async ({ page }) => {
  await page.goto("./people/2ec4cc09-4a4d-55ee-97c4-93597a5bde48/");
  const main = page.locator("main");
  await expect(main).toContainText("California Institute of Technology");
  await expect(main).toContainText("Student, class of 1940");
  await expect(main).toContainText("student");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 693 publishes Shingi Nakamura's community affiliation without inventing an employer", async ({ page }) => {
  await page.goto("./people/cbd0aa3d-5c0d-5ee4-8dde-08fef2d8e5cb/");
  const main = page.locator("main");
  await expect(main).toContainText("Zaibei Okinawan Seinenkai");
  await expect(main).toContainText("Member and first president");
  await expect(main).toContainText("gardening and hotel work");
  await expect(main).toContainText("No employer is inferred");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 693 preserves the Albin and Alvin Nagler conflict", async ({ page }) => {
  await page.goto("./people/2826bffc-418a-5520-8a84-0b6783a899df/");
  const main = page.locator("main");
  await expect(main).toContainText("Albin L Nagler");
  await expect(main).toContainText("Alvin L Nagler");
  await expect(main).toContainText("conflicting");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
});

test("Batch 693 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,984");
  await expect(body).toContainText("37.53%");
  await expect(body).toContainText("315");
  await expect(body).toContainText("14,950");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
