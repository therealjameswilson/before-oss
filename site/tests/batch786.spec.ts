import { expect, test } from "@playwright/test";

const profiles = [
  ["4b1af7ee-d7ff-5225-b1e1-6079853e41c8", "Peter Rago"],
  ["768e3ee8-c08d-5704-b3ee-8e1ba1de9ff1", "Maurice T Ragsdale"],
  ["38b1ec58-c8d5-52aa-bc02-a7fa8294f22b", "Charles E Rahn"],
  ["8cc496d1-c999-5b8b-87e2-392a8930510c", "Joseph L Raichle"],
  ["0a78a4e8-195f-56fa-9df1-9317ff165972", "Milton E Raichle"],
  ["97d73e65-0ce9-5534-afc3-c2294ee09ca9", "Renato Raimondi"],
  ["f05a8ab2-21b5-5dab-8881-952356ff59c3", "Alice L Raine"],
  ["cf7f3bc4-f9b1-578d-9c33-8d70cd56b5bd", "Richard F Rainer"],
  ["5a62773e-c17b-593b-b5cb-70a6ac621a58", "Archie B Rainey"],
  ["ded086e3-ba8c-59cb-a423-8e4bba8300bc", "John Raiss"],
  ["0ffccbb5-8496-5d9c-b5ba-02a72a21f8d2", "James B Raiter"],
  ["ccd3f40d-2c5d-5d27-ae36-44b18adf99aa", "Matti Raivio"],
  ["880836ae-f6f2-59a4-ad01-b27c1af18580", "Joe Rajacic"],
  ["8501b5ca-81a8-55eb-b7cc-2fb990ea0446", "Michael Rajacich"],
  ["8192bd50-45e2-5e96-8534-bc8651df1e93", "Robert Rajacich"],
  ["d6be728a-be08-5fa9-bee2-ab2dd6c7a6cc", "Hardy L Raley"],
  ["a617ac7e-ebf1-50b5-9192-8e139acba093", "Mary S Raley"],
  ["87d74908-03e5-5fb2-8046-49ddf182154c", "Vincent P Ralph"],
  ["9fba784c-5938-5b7e-9082-94d4e0c88f3f", "William F. W. Ram"],
  ["715aa774-2008-5dcb-9c2c-40787605b067", "Waitman M Ramage"],
  ["53bfb7c1-3487-5aba-93b3-545cffb3e59b", "Ralph L Ramberg"],
  ["851f3a78-78ab-5f47-bbca-99ef2dddb3e5", "Floyd B Rambin"],
  ["a2ed27f6-b4af-5b46-abe6-d04fc66074fe", "Emile D Ramel"],
  ["30979b38-d4f9-577c-80ad-60cae16d3da6", "Angelo Ramirez"],
] as const;

test("Batch 786 publishes all 24 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 786 publishes Rajacich's official identity evidence without an employer claim", async ({ page }) => {
  await page.goto("./people/8501b5ca-81a8-55eb-b7cc-2fb990ea0446/");
  const main = page.locator("main");
  await expect(main).toContainText("Operation Halyard");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Dossier of Zvonimir Vuckovic");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 786 preserves literal clipped notes without expansion", async ({ page }) => {
  for (const [id, note] of [
    ["97d73e65-0ce9-5534-afc3-c2294ee09ca9", "Polish Ar"],
    ["cf7f3bc4-f9b1-578d-9c33-8d70cd56b5bd", "Also Ann"],
    ["87d74908-03e5-5fb2-8046-49ddf182154c", "French"],
    ["9fba784c-5938-5b7e-9082-94d4e0c88f3f", "Also Par"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText(note);
  }
});

test("home page exposes the rebuilt Batch 786 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,078");
  await expect(home).toContainText("46.28%");
  await expect(home).toContainText("12,856");
  await expect(home).toContainText("803");
  await expect(home).toContainText("358");
  await expect(home).toContainText("9,537");
});
