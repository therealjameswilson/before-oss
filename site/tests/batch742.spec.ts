import { expect, test } from "@playwright/test";

const profiles = [
  ["696d108d-2ede-5c1c-a356-44003b26fd0f", "Franklin H Pearson"],
  ["11e67d65-f7e2-5893-a19e-5c5cfaf5f942", "Helen E Pearson"],
  ["9881df31-435b-52a0-a071-834c36386ceb", "James G Pearson"],
  ["1f428f15-c6a5-51a5-a662-4f1b419c98a7", "Joan H Pearson"],
  ["4f9c1791-2595-5664-8168-08b7e4bdbae6", "John W Pearson"],
  ["623dc110-764f-5f73-af83-c3be5c8fc3ce", "Kathleen Pearson"],
  ["9e161c56-f13d-52f7-bc8c-778fe6ff8677", "Norman H Pearson"],
  ["ac298139-fded-5910-b2b2-82108992002a", "William C Pearson"],
  ["f791093e-9259-5519-8169-2c31ce633a26", "Burl E Pease"],
  ["addccbb4-1372-5bfd-b53f-d6f6203f4ff4", "Patricia Pease"],
  ["000e27c1-d058-5965-873b-4dd8fd5d29d8", "Amos J Peaslee"],
  ["900d5768-4821-5f9f-b861-2c98c546c5ad", "Al Peavey"],
  ["9267cbe2-94a1-5bd5-883a-3ddfa987880e", "Paul D Peay"],
  ["dd7d247a-5572-5dba-abc4-4c9205a34da7", "Charles K Peck Jr."],
  ["dd07d875-d0e9-5810-aadd-9be06f8f74a7", "Edward T Peck Jr."],
  ["0d5c6d25-c76d-55e4-b880-8dc2d256f813", "George T Peck"],
  ["c03d91dd-21ad-5e17-9e9d-86f927272dbe", "Helen B Peck"],
  ["47961094-e255-54f9-b8c0-e6deac8aa9ce", "Herbert M Peck Jr."],
  ["b6ef8c8b-77af-5ed0-8466-df12be4d82ba", "Lea Peck"],
  ["a77b7ee6-bbcd-56de-846b-58b1e1026cc9", "Lyle V Peck"],
  ["cb2756c7-c976-5839-9826-14d6b660fde1", "Marion H Peck"],
  ["c713ad99-cbc1-5a3e-8b27-81e603fc345c", "Rea Peck"],
  ["f2a8eb53-07f2-59c7-bd5a-48ce47f621c2", "Walter H Peck"],
] as const;

test("Batch 742 publishes all 23 page-361 profiles with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\d{4,8}$/);
  }
});

test("five exact Army matches publish identity evidence without invented employers", async ({ page }) => {
  for (const id of [
    "696d108d-2ede-5c1c-a356-44003b26fd0f",
    "9881df31-435b-52a0-a071-834c36386ceb",
    "f791093e-9259-5519-8169-2c31ce633a26",
    "9267cbe2-94a1-5bd5-883a-3ddfa987880e",
    "47961094-e255-54f9-b8c0-e6deac8aa9ce",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Walter Peck has direct NARA OSS identity evidence without a pre-OSS inference", async ({ page }) => {
  await page.goto("./people/f2a8eb53-07f2-59c7-bd5a-48ce47f621c2/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Special Orders No. 9");
  await expect(main).toContainText("Company B, Special Reconnaissance Battalion");
  await expect(main).toContainText("internal OSS assignment");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main).not.toContainText(/39[ -]?303[ -]?203/);
});

test("unresolved distinctive-name candidates remain qualified", async ({ page }) => {
  await page.goto("./people/000e27c1-d058-5965-873b-4dd8fd5d29d8/");
  let main = page.locator("main");
  await expect(main).toContainText("Amos Jenkins Peaslee II");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("none directly links");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/a77b7ee6-bbcd-56de-846b-58b1e1026cc9/");
  main = page.locator("main");
  await expect(main).toContainText("Lyle Vern Peck");
  await expect(main).toContainText("ambiguous");
  await expect(main).toContainText("discovery-only genealogy record");
});

test("source punctuation, officer ranks, and filing notes remain visible", async ({ page }) => {
  await page.goto("./people/dd7d247a-5572-5dba-abc4-4c9205a34da7/");
  await expect(page.locator("main")).toContainText("1st Lt");
  await expect(page.locator("main")).toContainText("Charles, Jr.");

  await page.goto("./people/dd07d875-d0e9-5810-aadd-9be06f8f74a7/");
  await expect(page.locator("main")).toContainText("Edward, Jr.");

  await page.goto("./people/0d5c6d25-c76d-55e4-b880-8dc2d256f813/");
  await expect(page.locator("main")).toContainText("ENSIGN");

  await page.goto("./people/c713ad99-cbc1-5a3e-8b27-81e603fc345c/");
  await expect(page.locator("main")).toContainText("One fold");
  await expect(page.locator("main")).toContainText("filing note");
});

test("Norman Pearson retains cited Yale employment and the rebuilt coverage", async ({ page }) => {
  await page.goto("./people/9e161c56-f13d-52f7-bc8c-778fe6ff8677/");
  const profile = page.locator("main");
  await expect(profile).toContainText("Yale University");
  await expect(profile).toContainText("English faculty member");
  await expect(profile).toContainText("Last civilian employer");

  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,097");
  await expect(home).toContainText("42.18%");
  await expect(home).toContainText("13,837");
  await expect(home).toContainText("751");
  await expect(home).toContainText("335");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
