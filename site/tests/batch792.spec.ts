import { expect, test } from "@playwright/test";

const profiles = [
  ["d562de5c-586e-5e39-8cb2-b3671a5ff2f1", "Margot F Reck"],
  ["b55d8e6a-799b-5438-914e-e3adfded1628", "Ann Reckas"],
  ["61ee9689-08de-519b-aa91-4c956dea5b1a", "Gordon F Reckord"],
  ["b4fdc79a-27eb-5457-9125-3435e6a31f0d", "Olive I Reddick"],
  ["52373229-4853-553b-99c8-9b5732239082", "Willis C Reddick"],
  ["64377e3c-560c-5cd6-8465-14c1ddcf979f", "James J Redding"],
  ["14a4b6a7-db7f-5a1e-a043-322def4db6c2", "Leonard J Redding"],
  ["d0217735-cd5b-5239-9744-c809e523ead3", "William J Redding"],
  ["40698c00-1ef2-5aa4-a914-888c9dd3ead4", "Joseph F Reddish"],
  ["207d4ec8-9232-5bd3-9fed-f4a7496294cb", "Maurice J Reddy"],
  ["ffefd0f0-353c-5940-a23f-a4a5f8028cea", "Ralph H Redford"],
  ["0443c615-5e21-516e-ba8b-f6e42ef8cd5c", "Jack M Redman"],
  ["796ac649-d385-5910-b09e-b7be76b35d55", "Everett S Redmond"],
  ["b614cfd1-042f-5d35-a21f-8eba11ebbee7", "Hugh F Redmond"],
  ["8947c635-8000-59b8-9f91-b8a46c62d31a", "Neil J Redmond"],
  ["18ac6ec8-a801-530f-bac2-dcf888b514ac", "Norris J Redmond"],
  ["5e0e9346-fc6b-5d7c-bd2f-45bd6e83cee9", "Martin Redovian"],
  ["63fd12aa-451a-5233-b0c5-cb3f6a101d0d", "Randall C Redpath"],
  ["b661b510-a4d9-574a-951f-78acb16780f5", "Lenore M Reece"],
  ["ab145b73-11a1-5c14-8c8a-df2f867cc776", "Benjamin W Reed"],
  ["ebdfcb3b-7584-5b8c-abb4-834eccdf9438", "Blanche Reed"],
  ["80c0d945-24d3-5373-8a05-05a67d87f887", "Catherine C Reed"],
] as const;

test("Batch 792 publishes all 22 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 792 qualifies Hood College without calling it Olive Reddick's employer", async ({ page }) => {
  await page.goto("./people/b4fdc79a-27eb-5457-9125-3435e6a31f0d/");
  const main = page.locator("main");
  await expect(main).toContainText("Hood College");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("do not prove immediate pre-OSS status or employment continuity");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("Hood College");
});

test("Batch 792 publishes Reddick's printer occupation without inventing a company", async ({ page }) => {
  await page.goto("./people/52373229-4853-553b-99c8-9b5732239082/");
  const main = page.locator("main");
  await expect(main).toContainText("Willis Calhoun Reddick");
  await expect(main).toContainText("printer from Illinois");
  await expect(main).toContainText("no named employer is established");
  await expect(main).toContainText("Extract fr");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("printer");
});

test("Batch 792 preserves qualified military and duplicate evidence", async ({ page }) => {
  await page.goto("./people/ffefd0f0-353c-5940-a23f-a4a5f8028cea/");
  await expect(page.locator("main")).toContainText("United States Army Coast Artillery Corps");
  await expect(page.locator("main")).toContainText("not shown to be the immediate pre-OSS affiliation");

  await page.goto("./people/796ac649-d385-5910-b09e-b7be76b35d55/");
  const everett = page.locator("main");
  await expect(everett).toContainText("rows 13-14");
  await expect(everett).toContainText("WWII ce");
  await expect(everett.locator("dt").filter({ hasText: /^Serial$/ })).toHaveCount(2);
});

test("home page exposes the rebuilt Batch 792 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,211");
  await expect(home).toContainText("46.83%");
  await expect(home).toContainText("12,723");
  await expect(home).toContainText("808");
  await expect(home).toContainText("362");
  await expect(home).toContainText("9,671");
});
