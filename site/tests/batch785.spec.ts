import { expect, test } from "@playwright/test";

const profiles = [
  ["5c457ec6-3e86-5710-ad28-9591210776dc", "Edwin R Raddatz"],
  ["f7cbb4b9-f928-5324-8465-a96de802ca93", "Leo A Radell"],
  ["329ff642-8d79-56d0-89a1-1b78f3b68a52", "Clarence T Rader"],
  ["3747599e-a32c-5c54-90cd-9a7f4b310174", "William J Rader"],
  ["51c2c732-7c98-5b10-88fa-895a17e20386", "Vjekoslav Radic"],
  ["50e0291b-04a6-54b7-a4a6-8d1f7419736c", "Harold L Radies"],
  ["1a3e31f4-e635-5801-8b76-27ccdb14420f", "Michael Radigan"],
  ["8c0653de-5d11-5fd7-b6ab-f93c788e83aa", "Robert Radke"],
  ["1bfcb59c-6a82-5133-9fdd-0c1186896b5a", "Edward Z Radlo"],
  ["f6e23542-a8ae-5588-abb0-a61eb8a50db1", "Alan R Rado"],
  ["08f58581-e9ce-5097-9e00-86a6d9de2da6", "Emmy C Rado"],
  ["5e659ef7-a684-520a-8f92-d6e27cf0896d", "Joseph A Radsivilovky"],
  ["cd082742-6454-52d4-aa8e-efa2898f44d1", "Eugene Radzikowski"],
  ["393dc833-9faa-5c34-913d-28172a88218d", "Harold R Raemer"],
  ["7b54f5a0-37af-52a3-acac-a55be7e11c04", "Nathan Raenoff"],
  ["ee0a1623-f060-5e4d-8473-135b2935b915", "Aldo L Raffa"],
  ["6e2461cf-2bd0-5d0f-b43a-7c9e12832387", "Everett M Raffel"],
  ["ed23a7ff-000c-534a-850d-426089b90c87", "Donald J Rafferty"],
  ["230bc9d5-aef1-58e8-98ce-4fb7a5febb9f", "Louis L Rafferty"],
  ["d5d771f0-ed24-573c-b113-0c9bdb286809", "Charles C Raftell"],
  ["019f4e88-d150-5dfd-9c8a-cdb66e76e5f5", "Anna F Ragan"],
  ["ee856ee4-cc12-5828-a9c8-51bafcf906ce", "Philip E Ragan"],
] as const;

test("Batch 785 publishes all 22 person profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 785 publishes Raffa's qualified Georgetown employer evidence", async ({ page }) => {
  await page.goto("./people/ee0a1623-f060-5e4d-8473-135b2935b915/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Georgetown University",
  );
  await expect(main).toContainText("political science instructor");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Docume");
  await expect(main).toContainText("Everyday Denazification in Postwar Germany");
});

test("Batch 785 keeps identity uncertainty and conflicts visible", async ({ page }) => {
  await page.goto("./people/5c457ec6-3e86-5710-ad28-9591210776dc/");
  await expect(page.locator("main")).toContainText("RADDARZ EDWIN R");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/cd082742-6454-52d4-aa8e-efa2898f44d1/");
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("four incompatible");

  await page.goto("./people/7b54f5a0-37af-52a3-acac-a55be7e11c04/");
  await expect(page.locator("main")).toContainText("LOMAX JAMES E JR");
  await expect(page.locator("main")).toContainText("conflicting");
});

test("Batch 785 preserves literal notes without expansion", async ({ page }) => {
  await page.goto("./people/ed23a7ff-000c-534a-850d-426089b90c87/");
  await expect(page.locator("main")).toContainText("file retai");

  await page.goto("./people/019f4e88-d150-5dfd-9c8a-cdb66e76e5f5/");
  await expect(page.locator("main")).toContainText("French");
});

test("home page exposes the rebuilt Batch 785 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,054");
  await expect(home).toContainText("46.18%");
  await expect(home).toContainText("12,880");
  await expect(home).toContainText("803");
  await expect(home).toContainText("358");
  await expect(home).toContainText("9,513");
});
