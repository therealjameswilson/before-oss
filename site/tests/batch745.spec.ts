import { expect, test } from "@playwright/test";

const profiles = [
  ["b7b520f4-7dc9-5bdb-95d8-70a25419f4fc", "Kathryn M Pendleton"],
  ["e53d3e0b-cfed-5f09-bc64-4a1dd019fc71", "William H Pendleton"],
  ["6da75180-7c7e-5823-b7f0-f08f0465334f", "Michael P Penetar"],
  ["075a69a7-f251-533b-9dcf-b4a300c9eeca", "Helen L Penland"],
  ["005b2636-9273-5ccc-b6e0-2549a666cf74", "Morris Penn"],
  ["2dd160c7-d7bf-5e5e-9c26-60954c239975", "Rylie L Penn"],
  ["cacd0937-2515-5b81-8f83-3cfb3f249f22", "Anial E Pennell"],
  ["5ad550db-2ae5-5e08-83b2-f961da3d5732", "Thomas F Penney"],
  ["6a06a530-92ba-535f-9993-3b2958d641b0", "Leroy Pennington"],
  ["942bcdbe-1bc8-54d4-b97b-effae5c4e709", "William Pennington"],
  ["f813fbd8-8492-5b00-9268-b40aa362de18", "John P Pennsovecchi"],
  ["a00492b7-4054-5866-8815-6e8ac005303e", "Herbert L Penny"],
  ["319dfc16-dd2f-5362-9e30-c5b4c77da362", "Clement B Penrose"],
  ["33b20906-139b-5667-8feb-2be7ac982735", "Stephen B. L. Penrose"],
  ["4b39dfec-4547-51e7-a740-2281ef2e1895", "Billie S Pentecost"],
  ["8dfb1222-0744-5f05-8c05-19a8851a151d", "Anthony Pepe"],
  ["b5d1c051-188c-5b4f-bc66-734805d8241d", "Frank Pepe"],
  ["740d63c6-1e44-51aa-8e4f-5068395da19f", "Stanley J Pepera"],
  ["f5cbd14b-001e-5009-a388-b6c60d447170", "Louis J Pepin"],
  ["26dc7dc9-0ec0-51ec-9855-60789310f94e", "Nelson A Pepin"],
  ["25907cb4-bc3b-5d91-9e86-d784ca5a2885", "Elias Pepper"],
  ["e2bd8505-1e60-5ca1-9dae-e49352463614", "William Peratino"],
  ["ab99da51-a18a-54ba-b2ed-e6a234d71c25", "William Peratino"],
] as const;

test("Batch 745 publishes all 23 page-363 profiles with terminal reviewed outcomes", async ({ page }) => {
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

test("Stephen Penrose publishes a separated immediate employer and earlier teaching chronology", async ({ page }) => {
  await page.goto("./people/33b20906-139b-5667-8feb-2be7ac982735/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Near East College Association",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Assistant Director",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Near East College Association",
  );
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("American University of Beirut");
  await expect(earlier).toContainText("Whitman College");
  await expect(earlier).toContainText("Rockford College");
  await expect(main).toContainText("OSS Board interviews, Cairo, May-June 1944");
  await expect(main).toContainText("Guide to the Stephen B. L. Penrose, Jr. Papers");
});

test("Michael Penetar publishes student status without inventing a university employer", async ({ page }) => {
  await page.goto("./people/6da75180-7c7e-5823-b7f0-f08f0465334f/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Scranton");
  await expect(main).toContainText("student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main).toContainText("The Aquinas");
});

test("Elias Pepper publishes Panama Railroad employment and Hunter student status separately", async ({ page }) => {
  await page.goto("./people/25907cb4-bc3b-5d91-9e86-d784ca5a2885/");
  const main = page.locator("main");
  await expect(main).toContainText("Elias John Papachristos");
  await expect(main).toContainText("Panama Railroad Company");
  await expect(main).toContainText("Hunter College");
  await expect(main).toContainText("court stenography student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "A single last civilian employer",
  );
  await expect(main).toContainText("President's Secretary, Shorthand Champ, Once A Spy");
});

test("the two William Peratino rows remain separate and only the corporal receives occupation evidence", async ({ page }) => {
  await page.goto("./people/e2bd8505-1e60-5ca1-9dae-e49352463614/");
  let main = page.locator("main");
  await expect(main).toContainText("1st Lt");
  await expect(main).toContainText("••••4228");
  await expect(main).toContainText("needs identity review");
  await expect(main).not.toContainText("Accounting and auditing");
  await expect(main).not.toContainText("Benjamin Franklin University");

  await page.goto("./people/ab99da51-a18a-54ba-b2ed-e6a234d71c25/");
  main = page.locator("main");
  await expect(main).toContainText("Cpl");
  await expect(main).toContainText("••••1664");
  await expect(main).toContainText("Accounting and auditing");
  await expect(main).toContainText("Benjamin Franklin University");
  await expect(main).toContainText("OSS Board interviews, Cairo, May-June 1944");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("suffix and surname conflicts remain visibly qualified", async ({ page }) => {
  await page.goto("./people/319dfc16-dd2f-5362-9e30-c5b4c77da362/");
  await expect(page.locator("main")).toContainText("Clement B Penrose Jr.");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/f813fbd8-8492-5b00-9268-b40aa362de18/");
  await expect(page.locator("main")).toContainText("John P Pensovecchio");
  await expect(page.locator("main")).toContainText("probable");
});

test("home page exposes the rebuilt Batch 745 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,165");
  await expect(home).toContainText("42.46%");
  await expect(home).toContainText("13,769");
  await expect(home).toContainText("760");
  await expect(home).toContainText("339");
  await expect(home).toContainText("8,624");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
