import { expect, test } from "@playwright/test";

const profiles = [
  ["ebee0a8b-370c-5c43-94f2-f01b611a98b9", "John E Quintrell"],
  ["45157eed-1d81-5193-814f-83318748a7bd", "Leanio M Quirino"],
  ["7c9b297c-88cd-5586-a4bd-5a945dbec4e5", "Akeley P Quirk"],
  ["ed0d75bd-1b4e-531d-882a-521dd0c4cd38", "Maurice A Quirk"],
  ["32b2fded-c1dd-59be-b62e-5ca8b4e7f49f", "Frank D Quisenberry"],
  ["7de28278-ed6c-5163-8490-0f4f03f02c53", "Carl H Raab"],
  ["912eb966-28ae-5575-a51d-4bd8771c69ec", "Gregory L Rabassa"],
  ["29e14ae0-6aac-5148-974c-cc998daf63c4", "Stuart W Rabb"],
  ["4b05ab17-1f3d-5a90-9add-4431a823bb7e", "James A Rabbit"],
  ["402b10a6-f1c1-5d22-bc45-da2bc12958a5", "Gale W Rablin"],
  ["3385c324-4180-5889-867c-961f039640b3", "Orah A Rabon"],
  ["c5ffd104-97d9-5f27-8c3d-76ef26c264c5", "Carlo A Racano"],
  ["84741b5f-5e4b-598c-bb3b-b3949b0aacea", "Janice V Race"],
  ["bafc9d58-cb99-5460-b1f6-26b21e328f9c", "Norman E Rachel"],
  ["52a3a1d6-da37-582e-bdbc-10a14540f799", "Melbourne L Rackett"],
  ["29a76884-0325-5002-a04c-e901b2caf41e", "Benjamin M Racusin"],
  ["93c7c822-3196-59cb-a875-d1e29d5e0ed4", "John W Raczkiewicz"],
  ["e0319140-99f0-503e-9e26-f536f9fa677a", "Simon Rad"],
  ["48d98450-146a-5629-8aa0-cf68172893f1", "Edward J Rada"],
  ["465b60a4-847c-5f5a-9c1f-40553e7e1f8f", "Alex Radak"],
  ["4b4150cf-2bed-54e7-b0e8-4ee280077d26", "Robert Radakovich"],
  ["977d9046-dc38-5ad5-bfd6-e484ec779b11", "David Radam"],
  ["09d4744e-7bc4-50da-9706-b4965ff089f1", "John M Radaszewski"],
] as const;

test("Batch 784 publishes all 23 person profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 784 publishes Rabassa's military pathway and keeps Dartmouth separate from employment", async ({ page }) => {
  await page.goto("./people/912eb966-28ae-5575-a51d-4bd8771c69ec/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "United States Army",
  );
  await expect(main).toContainText("Dartmouth College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("cryptographer");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 784 publishes Quirk's prewar attorney status without inventing a firm", async ({ page }) => {
  await page.goto("./people/7c9b297c-88cd-5586-a4bd-5a945dbec4e5/");
  const main = page.locator("main");
  await expect(main).toContainText("Akeley Park Quirk");
  await expect(main).toContainText("State Bar of California");
  await expect(main).toContainText("attorney");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 784 publishes Rackett's documented OSS context but no unsupported employer", async ({ page }) => {
  await page.goto("./people/52a3a1d6-da37-582e-bdbc-10a14540f799/");
  const main = page.locator("main");
  await expect(main).toContainText("OSS Detachment 101");
  await expect(main).toContainText("somewhere in Burma, early 1944");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 784 preserves the two John Radaszewski rows and literal clipped notes", async ({ page }) => {
  await page.goto("./people/09d4744e-7bc4-50da-9706-b4965ff089f1/");
  const main = page.locator("main");
  await expect(main).toContainText("629");
  await expect(main).toContainText("630");
  await expect(main).toContainText("Extract fr");
  await expect(main).toContainText("RADASZE SKI JOHN M");

  await page.goto("./people/29a76884-0325-5002-a04c-e901b2caf41e/");
  await expect(page.locator("main")).toContainText("No first n");

  await page.goto("./people/ebee0a8b-370c-5c43-94f2-f01b611a98b9/");
  await expect(page.locator("main")).toContainText("Extract fr");
});

test("home page exposes the rebuilt Batch 784 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,032");
  await expect(home).toContainText("46.08%");
  await expect(home).toContainText("12,902");
  await expect(home).toContainText("803");
  await expect(home).toContainText("358");
  await expect(home).toContainText("9,491");
});
