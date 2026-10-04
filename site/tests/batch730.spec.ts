import { expect, test } from "@playwright/test";

const profiles = [
  ["c46fa8c6-9a31-5c11-b5b6-66fef601fe06", "Leonard M Pallen"],
  ["ac561d5a-8d8a-5639-b6ea-cbfec243675f", "Mitchell D Palles"],
  ["93c92a2e-fd4c-5c2d-a852-8cc54713d29e", "Peter D Pallescki"],
  ["8d657093-f603-555d-9da7-14b4a4e7b951", "George Palley"],
  ["7fee759f-d62e-5025-ac94-c33070724dab", "James L Pallord"],
  ["9da295cb-9cdb-5be5-9e23-58842d51d02f", "Augustine N Palluccio"],
  ["074fed85-700b-556d-8784-864278366cc1", "* Palmbaum"],
  ["fb512fa5-dd73-55fa-82fd-d0a91d8a9335", "Arthur E Palmer"],
  ["9b08433f-62e5-5337-8211-6a788b56c6fc", "Carter Palmer"],
  ["4c22c3a2-447c-5102-a2ef-8f746b1e87e5", "Constance B Palmer"],
  ["61217254-0088-587f-9e03-4311e41cccc3", "Dixie S Palmer"],
  ["70768090-d654-5b2e-aed0-f296cb7cb68d", "Donald D Palmer"],
  ["2bdd20a7-2a6d-5c1a-9bf6-24d5d7cf2133", "Glenn E Palmer"],
  ["d8d3f950-78c4-5b87-889c-721bdc583a6c", "Hazel Palmer"],
  ["226acb7b-b882-57f1-b297-3b5d6c94fa45", "Henry J Palmer"],
  ["c2cd8138-9237-5c51-881e-db9965bc30d0", "Howard V Palmer"],
  ["6fd18e93-f218-5670-9ced-83ac0257a799", "Howard M Palmer"],
  ["32d548c9-e4db-518b-892f-a0f0acbd1478", "James W Palmer"],
  ["c652bf6f-9979-5fdb-80f6-8bdd4604cfc7", "Jenny Palmer"],
  ["95782bbb-493e-5b46-a1aa-1d50057c5d97", "Luther R Palmer Jr."],
  ["16c3c9f2-fc9a-586c-84c8-6c33ebcae15b", "Norman R Palmer"],
  ["eb9a2868-9542-56d0-b32d-9463d8fcfc94", "Pauline Palmer"],
  ["80b519cd-e52b-557d-927b-d60d7f284504", "Quentin S Palmer"],
] as const;

test("Batch 730 publishes all 23 direct profile routes with reviewed outcomes", async ({ page }) => {
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

test("Batch 730 presents Mitchell Palles's university link as qualified student status", async ({ page }) => {
  await page.goto("./people/ac561d5a-8d8a-5639-b6ea-cbfec243675f/");
  const main = page.locator("main");
  await expect(main).toContainText("University of South Carolina");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("probable");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationUniversity of South Carolina");
  await expect(main).not.toContainText("Last civilian employerUniversity of South Carolina");
});

test("Batch 730 qualifies Hazel Palmer and excludes her postwar museum role", async ({ page }) => {
  await page.goto("./people/d8d3f950-78c4-5b87-889c-721bdc583a6c/");
  const main = page.locator("main");
  await expect(main).toContainText("Radcliffe College");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("1941");
  await expect(main).toContainText("recruited by the OSS");
  await expect(main).toContainText("probable");
  await expect(main.locator('section[aria-labelledby="earlier-affiliations"]')).not.toContainText(
    "Museum of Fine Arts",
  );
  await expect(main).not.toContainText("Last civilian employerRadcliffe College");
});

test("Batch 730 preserves Carter Palmer's official identifier conflict", async ({ page }) => {
  await page.goto("./people/9b08433f-62e5-5337-8211-6a788b56c6fc/");
  const main = page.locator("main");
  await expect(main).toContainText("Howard R Krampitz");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(main).not.toContainText("Last civilian employer before serviceArmy");
});

test("Batch 730 rebuilds exact coverage without changing verified-employer totals", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,826");
  await expect(main).toContainText("41.05%");
  await expect(main).toContainText("14,108");
  await expect(main).toContainText("741");
  await expect(main).toContainText("332");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
