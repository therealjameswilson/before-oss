import { expect, test } from "@playwright/test";

const profiles = [
  ["139e37ef-3801-5024-aa12-6e55b1e8185c", "Joseph Percic"],
  ["2e44220f-5acc-5828-842e-e8695603f32b", "Thomas E Percival"],
  ["d0a9ffd4-06a2-569d-8dbd-3f3c53b29aa0", "Bonnie L Perdue"],
  ["aafb88b1-4a2b-5bd6-8c53-bc1ffd49cdd2", "James S Perdum"],
  ["032795ea-6f85-54e5-80a3-ced37cf4e990", "Albert Perez"],
  ["5c33c6f2-db6c-58aa-9344-2058c0f1e7c1", "Francisco A Perez"],
  ["b84b11f2-0173-50c3-8f20-8ff09b515637", "Richard M Perez"],
  ["17417f80-69d2-5ac9-a709-a9fc201d3606", "Ivan Peric"],
  ["68c2aeba-1dac-538c-a603-b6fc3820df37", "Nick Perica"],
  ["d5b68495-deb6-5afa-81ae-83c8456c98b4", "John Perich"],
  ["891a4b84-cc96-5af4-953d-ecb494006f3a", "Nick Pericha"],
  ["c35b4b79-2026-5228-9814-73e303034181", "Anne W Perin"],
  ["96f01490-65d5-5428-9712-14d0de232397", "Nancy S Perin"],
  ["bdc1e956-972e-58bd-980a-a50dd81d2337", "A Flore Perino"],
  ["1c2ebdc3-c646-5aee-9908-ce6f70bab25f", "Constantine G Peristianis"],
  ["2e441881-e0a3-5727-8d42-95671b61fce6", "David N Perkins"],
  ["ee209c65-818a-5331-9942-9d086ba4dd2c", "Edward R Perkins"],
  ["2388b53d-fbad-5b9b-8079-746b02168512", "Georgia H Perkins"],
  ["52d7ffe9-a981-589a-bddf-207ce27e8f84", "John D Perkins"],
  ["c0b12ae2-a977-50f3-8e0c-4d6a0ba698ea", "John D Perkins"],
  ["ff3e294c-e6d3-5c00-acef-a91d0a0da241", "Mahlon F Perkins"],
  ["2a1c7bc6-6080-5276-8afb-40ee7f5f3fa0", "Nancy M Perkins"],
  ["044f31d3-aa4b-5cb3-8240-2e9b492ed6b3", "Robert W Perkins"],
] as const;

test("Batch 746 publishes all 23 page-363 profiles with reviewed outcomes", async ({ page }) => {
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

test("Nick Perica publishes Standard Oil as last civilian employer and enters the oil category", async ({ page }) => {
  await page.goto("./people/68c2aeba-1dac-538c-a603-b6fc3820df37/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Standard Oil Barge Line",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).toContainText("Nick Perica");

  await page.goto("./oil-companies/");
  const category = page.getByRole("region", { name: "Oil company work list" });
  await expect(category).toContainText("Nick Perica");
  await expect(category.locator(".oil-directory__person")).toHaveCount(10);
  await expect(page.locator("main")).toContainText("12 historically named oil");
});

test("Mahlon Perkins publishes student status without inventing an employer", async ({ page }) => {
  await page.goto("./people/ff3e294c-e6d3-5c00-acef-a91d0a0da241/");
  const main = page.locator("main");
  await expect(main).toContainText("Mahlon Fay Perkins Jr.");
  await expect(main).toContainText("New York School of Social Work");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Operation MAGPIE");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("variant and duplicate risks remain visibly qualified", async ({ page }) => {
  await page.goto("./people/aafb88b1-4a2b-5bd6-8c53-bc1ffd49cdd2/");
  await expect(page.locator("main")).toContainText("James S. Purdum");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/17417f80-69d2-5ac9-a709-a9fc201d3606/");
  await expect(page.locator("main")).toContainText("Ivan Peric");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/891a4b84-cc96-5af4-953d-ecb494006f3a/");
  await expect(page.locator("main")).toContainText("••••");
  await expect(page.locator("main")).not.toContainText("Standard Oil Barge Line");

  await page.goto("./people/52d7ffe9-a981-589a-bddf-207ce27e8f84/");
  await expect(page.locator("main")).toContainText("John H Perkins");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/c0b12ae2-a977-50f3-8e0c-4d6a0ba698ea/");
  await expect(page.locator("main")).toContainText("RM2c");
  await expect(page.locator("main")).not.toContainText("John H Perkins");
});

test("home page exposes the rebuilt Batch 746 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,188");
  await expect(home).toContainText("42.56%");
  await expect(home).toContainText("13,746");
  await expect(home).toContainText("762");
  await expect(home).toContainText("340");
  await expect(home).toContainText("8,647");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(10);
});
