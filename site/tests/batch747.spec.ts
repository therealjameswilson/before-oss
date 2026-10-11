import { expect, test } from "@playwright/test";

const profiles = [
  ["deae4c7e-2c7f-5be1-b126-ea4a5637102d", "Roy Perkins"],
  ["aa0961f4-c604-5863-8a04-224c5d1e7d43", "Willie B Perkins"],
  ["bef029a1-bff4-5d76-b314-6a7bb6827027", "John Perkovich"],
  ["f5da9ccd-2b92-5931-b5dd-90a87af88df0", "Finis H Perky"],
  ["59ce9cbf-ca27-5e02-bbac-8b7ff754cab9", "Abraham I Perl"],
  ["9edd797e-5d25-596b-881a-21b91f4e6916", "Henry G Perley"],
  ["fb7b413e-ea0f-5006-8616-9f18e21db654", "Joshua Perlmutter"],
  ["ebe4b6f9-2cbd-5f63-97d9-e137dae50595", "Walter S Perlmutter"],
  ["bef50317-9225-5250-81da-1ad68ead72c1", "Albino J Perna"],
  ["8565e060-b485-5bdb-bf3d-d28854c0dd45", "John Perna"],
  ["a62e657d-0929-51df-b566-b71a39963559", "Nicholas L Pernice"],
  ["a81baefd-4304-571c-9f42-91588dcfb790", "Herbert J Pero"],
  ["34351a6a-c92f-5b9d-a3ca-8f41ea3224f6", "Greta Perreau de La"],
  ["fd54b302-47a5-59e7-95e7-c4a93e48e43d", "Michael S Perri"],
  ["a25116e2-c4a8-539b-92ff-ef5afa673edf", "Doyle C Perrigin"],
  ["c31dc947-0164-5bab-ae3a-25f21b1e45c1", "Anita C Perrin"],
  ["0130af69-ff04-5f95-a370-40c2632e2369", "Vincenzo J Perruccio"],
  ["bf186258-1a82-572b-922c-9096049cc3cc", "Anne R Perry"],
  ["af4f91bd-a4c7-5d4e-9df0-428c3dd7f4d1", "Charles R Perry"],
  ["395ac2e1-37d7-5384-847c-a05aa23d4a7a", "Charles S Perry"],
  ["455006e6-46ca-5c04-bd0b-c2683f516ffa", "Dolly Perry"],
  ["b132a744-cbb5-5084-b2ee-f52239318484", "Erma G Perry"],
  ["34907310-30ed-55da-a894-d39fb806320f", "Francis Perry"],
] as const;

test("Batch 747 publishes all 23 page-364 profiles with terminal reviewed outcomes", async ({ page }) => {
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

test("Henry Perley publishes Dartmouth as student status, never as an employer", async ({ page }) => {
  await page.goto("./people/9edd797e-5d25-596b-881a-21b91f4e6916/");
  const main = page.locator("main");
  await expect(main).toContainText("Henry Gabriel (Eagle) Perley");
  await expect(main).toContainText("Dartmouth College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("high documented pre-OSS");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "Dartmouth College",
  );
  await expect(main).toContainText("104-10219-10000");
});

test("Francis Perry publishes qualified occupations without inventing a named employer", async ({ page }) => {
  await page.goto("./people/34907310-30ed-55da-a894-d39fb806320f/");
  const main = page.locator("main");
  await expect(main).toContainText("2677th Regiment");
  await expect(main).toContainText("manufacture of knit goods");
  await expect(main).toContainText("journalist in Austria");
  await expect(main).toContainText("medium D correlative or secondary");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).toContainText("French");
});

test("identity-only evidence remains separate from employer evidence", async ({ page }) => {
  await page.goto("./people/a62e657d-0929-51df-b566-b71a39963559/");
  const nicholas = page.locator("main");
  await expect(nicholas).toContainText("high confidence");
  await expect(nicholas.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "Taylor-Winfield",
  );

  await page.goto("./people/0130af69-ff04-5f95-a370-40c2632e2369/");
  const vincenzo = page.locator("main");
  await expect(vincenzo).toContainText("high confidence");
  await expect(vincenzo.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "used-car",
  );

  await page.goto("./people/a25116e2-c4a8-539b-92ff-ef5afa673edf/");
  await expect(page.locator("main")).toContainText("Also in B");
  await expect(page.locator("main")).toContainText("archival review");
});

test("home page exposes the rebuilt Batch 747 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,211");
  await expect(home).toContainText("42.65%");
  await expect(home).toContainText("13,723");
  await expect(home).toContainText("763");
  await expect(home).toContainText("340");
  await expect(home).toContainText("8,670");
});
