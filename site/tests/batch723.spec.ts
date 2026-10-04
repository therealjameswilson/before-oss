import { expect, test } from "@playwright/test";

const profiles = [
  ["0fca882d-3df1-5283-a99a-362c64c2e010", "Leo J Ortego"],
  ["1b242dc6-9515-5df2-bc84-2793dfff72ed", "William E Orser"],
  ["2322be14-370b-5e70-b460-0466017b79fd", "Theodore P Orth"],
  ["29e293cf-2f94-5394-a356-4f4b4f842341", "Emma L Orschiedt"],
  ["50aa46c3-5950-5219-8aea-6d8f72bb5bf8", "Lucien J Orsoni"],
  ["54ccb76b-229e-543d-a4b6-e936e50d25bb", "Livio M Orsi"],
  ["66590645-fc4b-594a-931e-360ff3e986ea", "Louis Oros"],
  ["81ce2a60-22b1-59f8-b4d0-eaef518925db", "Clifford Orourke"],
  ["87c69f62-a544-5643-add4-1b7111c7a6ea", "Paul E Orr"],
  ["92c7f3e7-39ea-535e-bfd5-283031a64b91", "Harold R Orr"],
  ["95b512b8-7f8c-5a82-95ff-1cdca3525843", "Jacob Ornstein"],
  ["96bea666-a7ea-5750-ab84-ffff87ec9fa3", "Teresa L Ortega"],
  ["986853d4-f9f3-50ed-b3ce-35d15f5ca1b8", "Theresa A Orroch"],
  ["a875ecf6-bce0-5780-b857-f910396a46d9", "Betsy S Orr"],
  ["acb7f824-2a0a-5483-848e-df5677535efa", "Dorothy Ormsby"],
  ["af581bee-549e-56da-9bf9-e6456e87e77b", "Robert L Ort"],
  ["b3abd463-1ab9-5ced-95df-d212efd0afd3", "Theresa Orocchi"],
  ["bc3a06a1-cc1b-54bb-97d4-4eef90f32534", "Ralph Ormond"],
  ["cb051fc3-f0b0-5ca5-946d-ce1f4de89424", "Roman X Ortega"],
  ["cc01bc34-aee0-57ca-9bb9-9aec5c92a3d7", "R D Orr"],
  ["de7968a6-d074-5f0c-b975-6457203781e1", "Regenia A Orr"],
  ["e546b7d7-b758-56b5-8db7-39f01f22838d", "Ray C Orndorff"],
  ["e6b83ea8-7753-5288-98ec-8285952ada68", "Laszlo Ormos"],
] as const;

test("Batch 723 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 723 publishes Jacob Ornstein's date-bounded Washington University employment", async ({ page }) => {
  await page.goto("./people/95b512b8-7f8c-5a82-95ff-1cdca3525843/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Washington University in St. Louis");
  await expect(main).toContainText("Instructor in Spanish and Portuguese");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("verified employer found");
  await expect(main).toContainText("Congressional Record");
});

test("Batch 723 publishes Clifford O'Rourke's immediate Cairo military assignment", async ({ page }) => {
  await page.goto("./people/81ce2a60-22b1-59f8-b4d0-eaef518925db/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Clifford H O'Rourke");
  await expect(main).toContainText("Replacement Center in Cairo");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("requires archival review");
});

test("Batch 723 keeps Laszlo Ormos's occupation qualified and employer-free", async ({ page }) => {
  await page.goto("./people/e6b83ea8-7753-5288-98ec-8285952ada68/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("documentary-film director");
  await expect(main).toContainText("If the probable identity match is correct");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 723 preserves identifier and cross-row conflicts", async ({ page }) => {
  for (const id of [
    "b3abd463-1ab9-5ced-95df-d212efd0afd3",
    "986853d4-f9f3-50ed-b3ce-35d15f5ca1b8",
    "87c69f62-a544-5643-add4-1b7111c7a6ea",
    "0fca882d-3df1-5283-a99a-362c64c2e010",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Identity statusconflicting");
  }

  await page.goto("./people/b3abd463-1ab9-5ced-95df-d212efd0afd3/");
  await expect(page.locator("main")).toContainText("Theresa A Orroch");
  await page.goto("./people/87c69f62-a544-5643-add4-1b7111c7a6ea/");
  await expect(page.locator("main")).toContainText("Rossi Guido J");
  await page.goto("./people/0fca882d-3df1-5283-a99a-362c64c2e010/");
  await expect(page.locator("main")).toContainText("Waltman Frank E Jr");
});

test("Batch 723 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,667");
  await expect(main).toContainText("40.38%");
  await expect(main).toContainText("14,267");
  await expect(main).toContainText("734");
  await expect(main).toContainText("329");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Jacob Ornstein");
});
