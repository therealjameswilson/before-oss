import { expect, test } from "@playwright/test";

const profiles = [
  ["deef3e5e-5f05-5da2-a3fb-9867944ffb75", "Eli Shapiro"],
  ["aaa5012c-e786-51ed-a913-72b3393527b4", "Herbert Shapiro"],
  ["9ff49469-302b-5a5c-8601-d36b076affd5", "I D Shapiro"],
  ["058bcf30-30b6-5ff3-9b32-920b5f92a9ce", "Karl J Shapiro"],
  ["f636af7d-6053-556a-8f62-0d3c11a90fc4", "Marjorie F Shapiro"],
  ["fa1bdcfc-ab5a-5cc7-8e93-25f51b8f81c0", "Nathan Shapiro"],
  ["895616db-3298-59a0-81ed-ab0863964aa4", "Sidney Shapiro"],
  ["5c95f685-8086-5cae-9a77-9c8a9c9820b8", "Sol Shapiro"],
  ["6216f6a5-bebb-54da-9960-4cb41d8bd02d", "Harold E Sharber"],
  ["1fc6d1b1-ef4b-53d1-99b1-c77da34784be", "Louis J Sharlip"],
  ["e0d89e8d-0bf6-582a-9190-e7caeea6fd4b", "George C Sharp"],
  ["0d2be377-a8b8-5fa3-b886-da01b7d74dca", "Irving J Sharp"],
  ["34d052f9-72f6-5699-a897-92ab37c5d706", "John B Sharp"],
  ["bd591492-651e-50e3-872a-b652322f8361", "John B Sharp"],
  ["f2c6ad50-f5ef-5d47-b27a-007b0734052e", "John E Sharp"],
  ["98f67c1b-4866-546e-ae5b-1a0ebc1d1936", "Samuel L Sharp"],
  ["276b9a1c-e59d-5650-9a10-ed7ee43b9c52", "Samuel L Sharp"],
  ["8dcf3bc8-52a2-547d-8338-d5d76b3fc54e", "Tom C Sharp"],
  ["c3aac600-400a-5e7d-a145-5a7b399eb6ce", "Walter R Sharp"],
  ["6d77fa68-50f6-506a-a04c-5d9e46e04692", "Preston C Sharpe"],
  ["5b30d3f4-0627-581a-830c-09c34c96fc7c", "Doris Sharrai"],
  ["6cf300e3-bf39-5847-a2ab-50c7320d26cd", "Doris A Sharrar"],
  ["ca8ef372-f24e-56ae-8b8e-8f5571ff73fe", "Lee M Sharrar"],
] as const;

test("Batch 863 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Karl Shapiro publishes student status without recasting the school as an employer", async ({ page }) => {
  await page.goto("./people/058bcf30-30b6-5ff3-9b32-920b5f92a9ce/");
  const main = page.locator("main");
  await expect(main).toContainText("Karl Jay Shapiro");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Enoch Pratt Library School");
  await expect(main).toContainText("student");
  await expect(main).toContainText("student affiliation, not an employer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceEnoch Pratt Library School");
});

test("Lee Sharrar publishes a qualified oil-company employer and earlier Rice employment", async ({ page }) => {
  await page.goto("./people/ca8ef372-f24e-56ae-8b8e-8f5571ff73fe/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Last civilian employer before serviceHumble Oil and Refining Company");
  await expect(main).toContainText("attorney, Legal Department");
  await expect(main).toContainText("Rice Institute");
  await expect(main).toContainText("instructor of economics");
  await expect(main).toContainText("latest identifiable civilian employer");
  await expect(main).toContainText("no source proves a direct Humble-to-Army or Humble-to-OSS transition");
});

test("same-name and near-name rows remain separate pending archival comparison", async ({ page }) => {
  await page.goto("./people/34d052f9-72f6-5699-a897-92ab37c5d706/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Corporal");
  await expect(main).toContainText("Distinct protected identifiers");

  await page.goto("./people/bd591492-651e-50e3-872a-b652322f8361/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Bletz Fred R");
  await expect(main).toContainText("Do not merge the rankless row with the Corporal row");

  await page.goto("./people/5b30d3f4-0627-581a-830c-09c34c96fc7c/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("possible transcription or duplicate relationship");

  await page.goto("./people/6cf300e3-bf39-5847-a2ab-50c7320d26cd/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Doris Sharrar Bohrer");
  await expect(main).toContainText("adjacent Sharrai row remains a separate possible duplicate");
});

test("Lee Sharrar appears in the evidence-qualified oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main.getByRole("link", { name: "Lee M Sharrar" })).toBeVisible();
  await expect(main.getByRole("link", { name: "Humble Oil and Refining Company" }).last()).toBeVisible();
  await expect(main).toContainText("attorney, Legal Department");
  await expect(main).toContainText("high confidence work claim");
});

test("Batch 863 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 575,
    research_attempted_people: 12_817,
    verified_affiliation_people: 932,
    verified_employer_people: 423,
    archival_review_assessed_people: 11_284,
    published_claims: 7_754,
    public_sources: 5_298,
  });
});
