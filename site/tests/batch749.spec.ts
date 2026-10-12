import { expect, test } from "@playwright/test";

const profiles = [
  ["a1befad1-4308-5145-bf6d-568104c3976f", "Edmund Persons"],
  ["acea5a5d-88bb-5e4a-863d-312e75cfefc4", "Claude Perthius"],
  ["71f5577c-26cf-5183-8237-d1c599d939f6", "Lillian Perugia"],
  ["f5aeb18e-e157-5bb2-b532-966bac6b2d64", "Cyril J Perusek"],
  ["0036498b-ef7e-512d-b398-69bca6257edd", "Sam Perusso"],
  ["6610226e-6f74-56a3-a93b-6f3e5121fb50", "Carl S Perutz"],
  ["cdda72eb-0b5a-59aa-8f80-7af56e87647a", "Herman Perveslin"],
  ["2368ce3c-af72-56d3-a52a-3ffa84a1b2ab", "Albert Perz"],
  ["6c720f4e-a9c9-5490-ae80-b1ac6ad97918", "Victor C Petchul"],
  ["f10e5960-545f-5f37-834d-3a38bff7a8ec", "George Petemezas"],
  ["91191cc2-0fc7-5e63-8900-b736eb7749cd", "Jane P Peterkin"],
  ["c9cb0511-d595-5964-86fb-abfc6c3e5684", "Carl B Peters"],
  ["8cac9e3c-3e66-5d38-8c6b-381f4cb25c48", "David L Peters"],
  ["aa5b528c-e67e-5430-86ef-23da35ea021f", "Emerson E Peters"],
  ["d087f8d1-a5be-523d-83bb-cf593e1584c4", "Franklin A Peters"],
  ["388fa769-a40b-5f84-9cd1-2bde67895545", "Fred W Peters"],
  ["7cf591b5-9304-5bdd-b557-d624e7ada8a0", "H Frede Peters"],
  ["b93e2177-6ce6-58ba-bd9c-d8f730569657", "Harry L Peters"],
  ["04231f18-0f2c-5469-8f03-c9c6dc6d8e8e", "Heinz F Peters"],
  ["6e7e51d1-dd0d-5151-bb52-3a8b883bd976", "Horace W Peters"],
  ["7fa8ea95-46a6-5eb9-9814-0e73f2fcf621", "James R Peters"],
  ["16cf8d3e-06dd-59fa-af8e-b9f13b430b72", "John Peters"],
] as const;

test("Batch 749 publishes all 22 page-365 person profiles with reviewed outcomes", async ({ page }) => {
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

test("Victor Petchul publishes Tilden as student status, never as an employer", async ({ page }) => {
  await page.goto("./people/6c720f4e-a9c9-5490-ae80-b1ac6ad97918/");
  const main = page.locator("main");
  await expect(main).toContainText("Tilden Technical High School");
  await expect(main).toContainText("Senior student and Service Club participant");
  await expect(main).toContainText("Victor Petchul — Tilden High");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "Tilden Technical High School",
  );
});

test("George Petemezas publishes a qualified Army-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/f10e5960-545f-5f37-834d-3a38bff7a8ec/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("served honorably as an OSS agent in Yugoslavia");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 749 preserves the Perez-Perz conflict and both Fred Peters rows", async ({ page }) => {
  await page.goto("./people/2368ce3c-af72-56d3-a52a-3ffa84a1b2ab/");
  const perz = page.locator("main");
  await expect(perz).toContainText("Albert Perez");
  await expect(perz).toContainText("conflicting");
  await expect(perz).toContainText("Albert Perez Box 595 and Albert Perz Box 598");

  await page.goto("./people/388fa769-a40b-5f84-9cd1-2bde67895545/");
  const fred = page.locator("main");
  const indexRows = fred.locator("article.index-record");
  await expect(indexRows).toHaveCount(2);
  await expect(indexRows.nth(0)).toContainText("599");
  await expect(indexRows.nth(1)).toContainText("598");
  await expect(fred).toContainText("CSP(X)");
});

test("home page exposes the rebuilt Batch 749 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,256");
  await expect(home).toContainText("42.84%");
  await expect(home).toContainText("13,678");
  await expect(home).toContainText("764");
  await expect(home).toContainText("340");
  await expect(home).toContainText("8,715");
});
