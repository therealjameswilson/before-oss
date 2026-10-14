import { expect, test } from "@playwright/test";

const profiles = [
  ["375a9923-706e-5981-b3a9-78af8d32c946", "Benjamin P Reyes"],
  ["48d3181f-c884-5847-bcae-0010ae8e6ac9", "Allen E Reynold"],
  ["3d1e0765-c35d-5df6-a26e-bce6a0fa36d5", "Bette L Reynolds"],
  ["f25bb1c6-8f93-558f-9428-885203a60271", "Dana Reynolds Jr."],
  ["05ed6212-5d23-5afa-beab-fae60ee4732f", "Emmett A Reynolds"],
  ["6791dfe6-c48e-5732-a9ec-36d878503cc0", "Foster N Reynolds"],
  ["1d230ded-bd5a-5ce1-b477-be82d5937e64", "Frank R Reynolds"],
  ["f49fdb7d-02f3-538b-a173-46d97c41e30c", "Henry D Reynolds"],
  ["895b27fa-371a-5d61-8292-259a776018fa", "Hugh Reynolds"],
  ["33a9ec02-423f-5cff-9935-0a54aaecefea", "Lucy A Reynolds"],
  ["249e9fd7-f039-5c7e-944f-fea6c4cf6ec4", "Mary D Reynolds"],
  ["c0b481de-ea6b-52e7-a4af-7d8b1c50bd12", "Myron P Reynolds"],
  ["087f1bef-dc95-531d-b57b-ab664214dde1", "Raymond E Reynolds"],
  ["4f8c63ce-df5f-5dcd-a7a9-fffb768b296c", "Robert L Reynolds"],
  ["4f5bfc62-19c2-5ef8-aef5-8954a517788f", "Ted R Reynolds"],
  ["2a51d8b3-f58e-5e25-aca7-ad2a318d850e", "Willard G Reynolds"],
  ["a783807a-ab20-5241-9e48-9b383432bce1", "William Reynolds"],
  ["c5998236-d3e8-5892-b4e3-7c478aac1244", "Robert R Rhea"],
  ["0d8bd26c-658c-539c-9825-d86ce1ebba9b", "Eward R Rhead"],
  ["189e689c-e865-5cd4-903f-aa967c5ddcfe", "George L Rheims"],
  ["7cd51ad7-faec-52d3-83b7-4d9c6c920a9f", "Marcella Rhein"],
  ["142a3477-0b11-5195-a9c3-4072bd63fd23", "George D Rheinbold"],
  ["bc4ce795-99df-52a7-af15-52aa649594ee", "Charles E Rhetts"],
] as const;

test("Batch 799 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Hugh Reynolds exposes a qualified Army pathway without inventing an employer", async ({ page }) => {
  await page.goto("./people/895b27fa-371a-5d61-8292-259a776018fa/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("United States Army");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("medium");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Lt. Colonel Hugh Reynolds Obituary");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Eward R Rhead preserves the printed spelling and publishes British Army status only", async ({ page }) => {
  await page.goto("./people/0d8bd26c-658c-539c-9825-d86ce1ebba9b/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Eward R Rhead", level: 1 })).toBeVisible();
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("British Army");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("temporal relation uncertain");
  await expect(main).toContainText("OSS Awards and Decorations Board records");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("George L Rheims remains a qualified identity and does not inherit his father's employer", async ({ page }) => {
  await page.goto("./people/189e689c-e865-5cd4-903f-aa967c5ddcfe/");
  const main = page.locator("main");
  await expect(main).toContainText("George Loring Rheims");
  await expect(main).toContainText("probable");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("United States Army");
  await expect(main).toContainText("The Ritchie Boys: Complete Roster");
  await expect(main).not.toContainText("Leon Rheims Company");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Charles E Rhetts separates dated federal assignments from immediate affiliation", async ({ page }) => {
  await page.goto("./people/bc4ce795-99df-52a7-af15-52aa649594ee/");
  const main = page.locator("main");
  await expect(main).toContainText("Charles Edward Rhetts");
  await expect(main).toContainText("confirmed");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("U.S. War Production Board");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("U.S. Department of Justice");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main).toContainText("P-8 Lt J");
  await expect(main).toContainText("Deaths: Charles Edward Rhetts");
});

test("Batch 799 organization pages expose the four normalized institutions", async ({ page }) => {
  for (const [id, name] of [
    ["865faf71-f9b5-558b-97a3-0b9d4332d29d", "British Army"],
    ["24cec6d5-c3cc-5dc4-b8c9-10ef805535e9", "United States Army"],
    ["b67d5ac8-c53b-5b93-9cff-a0dd715acbfe", "U.S. War Production Board"],
    ["9e3f0482-04d1-5745-ac04-4ed0d5132090", "U.S. Department of Justice"],
  ]) {
    await page.goto("./organizations/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("home page exposes the rebuilt Batch 799 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,366");
  await expect(home).toContainText("47.48%");
  await expect(home).toContainText("12,568");
  await expect(home).toContainText("818");
  await expect(home).toContainText("368");
  await expect(home).toContainText("9,828");
});
