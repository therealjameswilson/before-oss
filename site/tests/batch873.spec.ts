import { expect, test } from "@playwright/test";

const profiles = [
  ["55f9eace-4406-54ea-8d1f-d10ad7ff40a1", "Leon E Shurman"],
  ["40417539-a1e3-5e79-9c1a-2eaaa232daa3", "Bertha Shurtok"],
  ["343ca227-19ef-566e-b1f9-e34e4d0db5a6", "Merle R Shuster"],
  ["94a3e9b9-448d-5412-a99b-64b561e9823a", "Robert L Shutt"],
  ["0a4c7ed4-0213-5544-a49d-8c39486fc13c", "Michael Shuwarger"],
  ["ad438211-9b83-5907-9413-2d3342879c4a", "Emily L Shwetzer"],
  ["095eae2e-b340-5c04-a97b-15bd878cb87e", "Doosik Shynn"],
  ["9280576d-2eb9-5f81-b2a9-c714835ad07c", "Helen K Shynn"],
  ["1553ad62-4660-5b0a-9d07-d0c336f0e821", "Victor J Siaholm"],
  ["de72b8c7-4fa7-592a-864f-dd75747a37e9", "Paul Siapicas"],
  ["0ce5959d-bdc4-5956-b56b-fe5fe46e5760", "Leona L Siberman"],
  ["442c3d73-8804-5796-a788-91adb4fc15bf", "Bruce E Sibley"],
  ["0ebaabab-a3a9-5edc-8253-c0a24e1eabea", "Mina L Sibley"],
  ["b9de9338-295f-58e8-ba04-227a63b9a465", "Virginia M Sibley"],
  ["ad48969c-0be5-5b1f-bdbb-8de63119e0ae", "Geraldine P Sica"],
  ["3c1a474f-e159-5e1d-9cd6-23ee4050e3d7", "Frank Siccone"],
  ["a2d66764-90d0-5d8d-8102-30c2e0b03ba1", "Peter M F Sichel"],
  ["1bf7bd5e-a790-51d0-9a46-e6046cab07f2", "Peter M Sichel"],
  ["eec0579c-9a6b-5255-90a2-628b4663ea96", "Michael J Sicilian"],
  ["e2c2a68f-b353-5669-8aec-ea4b0eafad7f", "Richard C Sickler"],
  ["ced8fa0d-1189-5608-9ad2-a6fa80529f1b", "Richard C Sickler"],
  ["0f7f7f13-91fa-5026-bdb8-4d6779d7002f", "Paul H Sickor"],
  ["eca2ffac-b714-541b-9e70-8679e58dae1b", "James P Sicuranza"],
] as const;

test("Batch 873 publishes all 23 source-row profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 873 publishes Doosik Shynn's 1938 newspaper work only as a qualified earlier role", async ({ page }) => {
  await page.goto("./people/095eae2e-b340-5c04-a97b-15bd878cb87e/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("The New Korea");
  await expect(main).toContainText("editor in chief");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("not shown to be the immediate pre-OSS affiliation or last civilian employer");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 873 confirms Paul Siapicas from the OSS roster without inventing an employer", async ({ page }) => {
  await page.goto("./people/de72b8c7-4fa7-592a-864f-dd75747a37e9/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Greek operational-group roster");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("The full identifier remains private");
});

test("Batch 873 keeps the Emily-Emil Shwetzer disagreement visible", async ({ page }) => {
  await page.goto("./people/ad438211-9b83-5907-9413-2d3342879c4a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("Emil L Shwetzer");
  await expect(main).toContainText("Emily L Shwetzer");
  await expect(main).toContainText("cannot be silently corrected");
});

test("Batch 873 keeps the two Richard Sickler rows separate and the X-2 record unassigned", async ({ page }) => {
  await page.goto("./people/e2c2a68f-b353-5669-8aec-ea4b0eafad7f/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("two index rows have that name and distinct protected identifiers");
  await expect(main).toContainText("cannot yet be assigned to this same-name index row");

  await page.goto("./people/ced8fa0d-1189-5608-9ad2-a6fa80529f1b/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("separate high-confidence Army identity");
  await expect(main).toContainText("cannot be distinguished between the two same-name rows");
});

test("Batch 873 retains Sicuranza-Securanza as a possible duplicate instead of merging", async ({ page }) => {
  await page.goto("./people/eca2ffac-b714-541b-9e70-8679e58dae1b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("separate James Securanza row remains a possible duplicate");
  await expect(main).toContainText("Box 694 and Box 709 entities remain separate");
  await expect(main).toContainText("no employer evidence is transferred between them");
});

test("Batch 873 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 582,
    research_attempted_people: 13_042,
    verified_affiliation_people: 948,
    verified_employer_people: 431,
    archival_review_assessed_people: 11_509,
    published_claims: 7_876,
    public_sources: 5_364,
  });
});
