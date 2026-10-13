import { expect, test } from "@playwright/test";

const profiles = [
  ["df3a0aee-4a10-50c6-a1d5-7a7e7283470d", "Peppino Puleo"],
  ["3df37b1c-ca06-5aad-a3e4-ae5fd569a04c", "Peppino Puleo"],
  ["b76e1207-47fa-5279-9cf1-2a5a5c8b807f", "Harley N Pulling"],
  ["13212e25-96c2-5a0e-ae21-20642903d9a2", "Harry J Pulos"],
  ["34b0cfde-d25e-5225-9a80-3261a72d760d", "Jerry Pulpan"],
  ["563e3645-5d21-544a-9e3a-cdf339b93e3e", "Grace W Pulver"],
  ["13b3a05f-4415-529f-be5e-891e7e874a0b", "Alan E Pumphrey"],
  ["79a12961-6a25-571d-bba5-0e0d4c03fb13", "Edmund J Pung"],
  ["901250ed-9cd2-5cca-a94d-5d1ec9cc75df", "Chalong Pungtragul"],
  ["56539540-5a55-5173-b2e7-bb760ff50f39", "Antoon N. A. Puntman"],
  ["c47ff9ba-8b67-5aa4-8615-0f5380eed462", "John M Punzirudu"],
  ["c503b140-7663-5d07-96d1-0c7ffb6c18aa", "Louis A Punzirudu"],
  ["da8cab9f-1f81-5a89-87cf-b8746b23ab28", "Udom Pupadhana"],
  ["dcb95492-21dd-57b6-8886-d5d9061885e6", "Donald H Purcell"],
  ["6420f149-1ce6-5d70-8778-a0745d073021", "Doris Purcell"],
  ["e7d353e5-04f9-5ba4-85e5-983c7335239f", "Francis R Purcell"],
  ["3b94c6af-3d39-5536-b807-28ede829cccc", "Robert Purcell"],
  ["bea24905-748b-5225-a473-e6594d3fab0e", "William L Purcell"],
  ["b9c1f24a-c8d2-58db-84f4-9e6de9c5175f", "Maude E Purdue"],
  ["0f83c991-969d-5152-baf5-0979c8ff3897", "James S Purdum"],
  ["44f283ab-8531-587d-a60f-e9fb1a5a479d", "Elizabeth J Purdy"],
  ["cd1c39f1-eb47-5b81-a1eb-446b520699fa", "John M Purdy"],
  ["a1931a93-001c-5699-a9f7-e145b12e13c5", "Mary C Purdy"],
] as const;

test("Batch 780 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 780 keeps the two Peppino Puleo rows separate and visibly qualified", async ({ page }) => {
  for (const id of [
    "df3a0aee-4a10-50c6-a1d5-7a7e7283470d",
    "3df37b1c-ca06-5aad-a3e4-ae5fd569a04c",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("one or both same-name Box 624 index rows");
    await expect(main).toContainText("Duplicate group");
    await expect(main).toContainText("the two rows remain separate");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
  }
});

test("Batch 780 publishes Pulos OSS evidence without the postwar business as an affiliation", async ({ page }) => {
  await page.goto("./people/13212e25-96c2-5a0e-ae21-20642903d9a2/");
  const main = page.locator("main");
  await expect(main).toContainText("document his OSS service in Europe");
  await expect(main).toContainText("AHEPA");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toHaveCount(0);
});

test("Batch 780 keeps postwar Chalong evidence out of pre-OSS affiliations", async ({ page }) => {
  await page.goto("./people/901250ed-9cd2-5cca-a94d-5d1ec9cc75df/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Wisconsin alumni publication");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toHaveCount(0);
});

test("Batch 780 preserves duplicate safeguards for Pupadhana and Purdum", async ({ page }) => {
  await page.goto("./people/da8cab9f-1f81-5a89-87cf-b8746b23ab28/");
  let main = page.locator("main");
  await expect(main).toContainText("may be a spelling variant");
  await expect(main).toContainText("remain separate pending archival comparison");
  await expect(main).toContainText("is not reassigned to Pupadhana");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toHaveCount(0);

  await page.goto("./people/0f83c991-969d-5152-baf5-0979c8ff3897/");
  main = page.locator("main");
  await expect(main).toContainText("separately indexed James S Perdum and James S Purdum rows remain unmerged");
});

test("Batch 780 preserves literal clipped index notes", async ({ page }) => {
  const examples = [
    ["563e3645-5d21-544a-9e3a-cdf339b93e3e", "Also Gre"],
    ["c47ff9ba-8b67-5aa4-8615-0f5380eed462", "Extract fr"],
    ["dcb95492-21dd-57b6-8886-d5d9061885e6", "One fold"],
    ["44f283ab-8531-587d-a60f-e9fb1a5a479d", "Also in B"],
  ] as const;
  for (const [id, note] of examples) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText(note);
  }
});

test("home page exposes the rebuilt Batch 780 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,940");
  await expect(home).toContainText("45.70%");
  await expect(home).toContainText("12,994");
  await expect(home).toContainText("799");
  await expect(home).toContainText("356");
  await expect(home).toContainText("9,399");
});
