import { expect, test } from "@playwright/test";

const profiles = [
  ["bd914014-0c43-5334-b0c9-9829d2b011de", "Helen J Murray"],
  ["039ff924-7560-5963-be0d-3e15c917d9d2", "Henry A Murray"],
  ["0aaf22dd-dbd3-5aa5-bab8-4eb4204b485e", "James W Murray"],
  ["22865a72-286f-548f-8062-7fd92e3281c7", "John M Murray"],
  ["d5d9e162-c732-5bba-941a-649804fff2b1", "John W Murray"],
  ["bc301e52-f53e-5b17-86d2-7cee63c45b7c", "Joseph L Murray"],
  ["05b83ea7-f45b-54b7-89f1-9ac9acf88176", "Morris F Murray"],
  ["55661b71-496a-5e0d-8b82-793220b7acb5", "Olga Murray"],
  ["4dc5ab89-2299-5976-a887-15100eaeca44", "Robert M Murray"],
  ["5e8db3c8-a0e5-5fba-998a-f2f2dd77824f", "Robert A Murray"],
  ["1d8b6067-3e81-55c9-96e6-f0660095cbb3", "Shady Murray"],
  ["22b9092f-cbc0-5941-8f76-1cf763d1e6cd", "Sherwood C Murray"],
  ["f876729e-05ff-57b9-8349-1b9034237def", "William S Murray"],
  ["0b23c00f-9002-57ad-bc12-1a8aac17b39a", "Rubye Murrell"],
  ["344f32a9-5a6d-58d7-8825-f715a5cd0d8b", "Percy L Muschamp"],
  ["e2b1a895-4a09-517b-8c12-b8d190b35781", "Walter W Muselin"],
  ["05e4eae6-d5e0-5f9e-a237-8c53517919a9", "Lawrence A Musella"],
  ["b405abfd-d43f-5f32-8e13-11428e304390", "Lirving D Musgrove"],
  ["d168797d-2686-5d72-bb74-0fa6f90b41b5", "Margaret J Musgrove"],
  ["62fd5c71-9913-51eb-b4d9-c7dd27d429a1", "Casimer P Musial"],
  ["6df71376-3491-5715-91af-53606a60d0fd", "George S Musolin"],
] as const;

test("Batch 690 publishes all 21 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Page 335");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 690 keeps six Army matches as identities without inventing employers", async ({ page }) => {
  for (const id of [
    "0aaf22dd-dbd3-5aa5-bab8-4eb4204b485e",
    "22865a72-286f-548f-8062-7fd92e3281c7",
    "5e8db3c8-a0e5-5fba-998a-f2f2dd77824f",
    "1d8b6067-3e81-55c9-96e6-f0660095cbb3",
    "e2b1a895-4a09-517b-8c12-b8d190b35781",
    "05e4eae6-d5e0-5f9e-a237-8c53517919a9",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 690 qualifies Percy Muschamp's earlier Halifax Academy work", async ({ page }) => {
  await page.goto("./people/344f32a9-5a6d-58d7-8825-f715a5cd0d8b/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Percy Lawrence Herbert Muschamp");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Halifax Academy");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("medium");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(main).not.toContainText("Yale University");
});

test("Batch 690 publishes Casimer Musial's grocery only as last civilian self-employment", async ({ page }) => {
  await page.goto("./people/62fd5c71-9913-51eb-b4d9-c7dd27d429a1/");
  const main = page.locator("main");
  await expect(main).toContainText("Casimir P. Musial");
  await expect(main).toContainText("high confidence");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Self-employed");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Grocery proprietor");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("1943");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(main).not.toContainText("1946 supermarket");
  await expect(main).not.toContainText(/\b\d{8}\b/);
});

test("Batch 690 preserves duplicate and literal index evidence", async ({ page }) => {
  await page.goto("./people/e2b1a895-4a09-517b-8c12-b8d190b35781/");
  await expect(page.locator(".index-record")).toHaveCount(2);
  await expect(page.locator("main")).toContainText("Both identical Walter W Muselin index rows");

  await page.goto("./people/f876729e-05ff-57b9-8349-1b9034237def/");
  await expect(page.locator("main")).toContainText("possibly");

  await page.goto("./people/b405abfd-d43f-5f32-8e13-11428e304390/");
  await expect(page.getByRole("heading", { name: "Lirving D Musgrove", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Irving D Musgrove (search alias only)");
});

test("Batch 690 preserves Henry Murray and George Musolin's reviewed evidence", async ({ page }) => {
  await page.goto("./people/039ff924-7560-5963-be0d-3e15c917d9d2/");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("United States Army");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Harvard Psychological Clinic");

  await page.goto("./people/6df71376-3491-5715-91af-53606a60d0fd/");
  const main = page.locator("main");
  await expect(main).toContainText("George S. Musulin");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("115th Infantry Regiment");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("University of Pittsburgh");
});

test("Batch 690 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,915");
  await expect(body).toContainText("37.24%");
  await expect(body).toContainText("312");
  await expect(body).toContainText("15,019");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
