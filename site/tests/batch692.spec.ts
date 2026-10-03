import { expect, test } from "@playwright/test";

const profiles = [
  ["e48bf7cc-955d-5a35-a4e4-0b96603e4ad4", "Jack M Myers"],
  ["7a2a86ca-3630-5ff5-8db0-6b2aa251e65a", "Julian G Myers"],
  ["7a9371fe-778f-5513-a716-12130e4f1455", "Nicholas J Myers"],
  ["4040244a-e4a1-51a6-b27e-c2e82626a995", "Norman M Myers"],
  ["9f1715bc-f710-5ae8-b8d5-1d72af5b108e", "Richard E Myers"],
  ["be7de223-953f-58e9-9a67-c01398a64f7e", "Robert J Myers"],
  ["be9fb6c6-9121-576e-acd3-4ed0228fe14b", "Thomas E Myers"],
  ["8a8723f6-cc8f-555a-8064-dc43ffa00012", "Thomas L Myers"],
  ["8c6e126d-080a-535e-8980-1ad618db0478", "Walter R Myers"],
  ["52cd7903-c869-5065-8c7f-bc67a25a07ca", "William L Myers"],
  ["005a567b-aa84-5edf-80ea-a3a2f8f27543", "Kenneth Mygatt"],
  ["e8d024a1-e3d2-52a8-9bc7-c8ae1a49ff79", "Charles P Myhra"],
  ["9eed15b0-ad5c-55a4-b9df-1dc9f7928b96", "Gunnar G Mykland"],
  ["d7b18fb1-fbef-5af9-ad53-aef62274a13f", "Cecilia F Mynatt"],
  ["252cd8ad-a5e8-5076-803c-af26da7ac566", "Richard Myrick"],
  ["5c1004be-dfa1-5b8d-b395-d4b1c9ed8e7d", "Marinus D Myrland"],
  ["b3640022-9c4c-5b0d-b62f-9db4382aa9cf", "Cecil F Myrott"],
  ["a5c42cc0-5bf7-5610-a2e9-435701be9209", "James H Mysberch"],
  ["746b64fa-158f-5c27-9673-7612ee24ed1a", "Frederick Myskill"],
  ["77f6dc38-00d5-5b9a-b9bc-a442ef6514e0", "John E Mysza"],
  ["1d425af9-24c7-592b-bebc-74922141cd83", "Joseph E Nadeau"],
  ["56b958d3-1917-5a6f-a9dc-06cd80136dbe", "Jacqueline I Nadelhoffer"],
  ["50cb7e28-f12b-57e6-b55a-943517bb3f95", "Thomas G Nader"],
] as const;

test("Batch 692 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Page 336");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 692 publishes Gunnar Mykland's documented 1939 municipal-housing employment", async ({ page }) => {
  await page.goto("./people/9eed15b0-ad5c-55a4-b9df-1dc9f7928b96/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier).toContainText("Housing Authority of Austin");
  await expect(earlier).toContainText("Assistant Director");
  await expect(earlier).toContainText("documented pre-OSS");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(main).toContainText("does not establish exact employment dates");
  await expect(main.locator('a[href^="https://www.govinfo.gov/content/pkg/GOVPUB-GP3-"]')).toHaveCount(2);
});

test("Batch 692 publishes Myrland's occupation without inventing a shipping employer", async ({ page }) => {
  await page.goto("./people/5c1004be-dfa1-5b8d-b395-d4b1c9ed8e7d/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("ship's engineer");
  await expect(main).toContainText("No employer is inferred");
  await expect(main).toContainText("retained");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 692 preserves the Mysberch and Mysbergh spellings", async ({ page }) => {
  await page.goto("./people/a5c42cc0-5bf7-5610-a2e9-435701be9209/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "James H Mysberch", level: 1 })).toBeVisible();
  await expect(main).toContainText("James H Mysbergh");
  await expect(main).toContainText("Detachment 101");
  await expect(main).toContainText("high confidence");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 692 exposes four identity conflicts without merging records", async ({ page }) => {
  for (const id of [
    "e48bf7cc-955d-5a35-a4e4-0b96603e4ad4",
    "4040244a-e4a1-51a6-b27e-c2e82626a995",
    "d7b18fb1-fbef-5af9-ad53-aef62274a13f",
    "b3640022-9c4c-5b0d-b62f-9db4382aa9cf",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  }

  await page.goto("./people/d7b18fb1-fbef-5af9-ad53-aef62274a13f/");
  await expect(page.locator("main")).toContainText("Cecil F Myrott");
  await page.goto("./people/b3640022-9c4c-5b0d-b62f-9db4382aa9cf/");
  await expect(page.locator("main")).toContainText("Cecilia F Mynatt");
});

test("Batch 692 masks Thomas Nader's numeric rank-column value", async ({ page }) => {
  await page.goto("./people/50cb7e28-f12b-57e6-b55a-943517bb3f95/");
  const main = page.locator("main");
  await expect(main).toContainText("Numeric identifier printed in rank column (masked)");
  await expect(main).toContainText("••••2453");
  await expect(main).not.toContainText(/\b\d{7,8}\b/);
});

test("Batch 692 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,961");
  await expect(body).toContainText("37.43%");
  await expect(body).toContainText("313");
  await expect(body).toContainText("14,973");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
