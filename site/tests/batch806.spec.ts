import { expect, test } from "@playwright/test";

const profiles = [
  ["a493431e-d64f-58e5-944d-c1fe56f70c49", "Thomas R Riley", "646"],
  ["31002dfc-9ad4-5b6d-9c15-39fec4d1196d", "Thomas M Riley Jr.", "646"],
  ["d0cc4700-84a8-5b82-9c49-c1fe97adfb51", "Wilma M Riley", "646"],
  ["528a2eb9-e4b8-5e6b-b0c4-bbc337416c74", "Leonard L Rinaldi", "646"],
  ["90b0a0cd-d5d2-5d01-9e61-068277f0eff9", "Louis Rinaldi", "646"],
  ["c3b619e9-85f5-5f69-b8c0-1200f463c864", "Grace L Ring", "646"],
  ["c55a2eeb-39f7-5aa8-a88f-d30a7abcf221", "Harry P Ring", "646"],
  ["3be7bcee-1f3f-53db-8b5f-489682d630d6", "Peter Ringland", "646"],
  ["06e301a9-d500-5ddc-8aea-1ed2afe4f600", "Ralph E Ringwald", "646"],
  ["14dbcffa-9fcb-5458-965b-6fde057b10c9", "Lyman E Rinker", "646"],
  ["192bfbff-9571-515d-b1f7-fc5b5398c6e7", "Andrew Rinko", "646"],
  ["bf06d5e8-a357-576e-bda8-88847a6dddf2", "Janet (Dr.) Rioch", "646"],
  ["8150f59d-49c1-5c26-ab52-4b98b5d82693", "Margaret M Riordan", "646"],
  ["ef1c04a0-4de5-5ce1-85b9-496fa5c8dd37", "Norbert J Rioux", "646"],
  ["46b5940a-2f2e-5069-b41a-2c5121007048", "Raymond J Ripkowski", "646"],
  ["f6e73502-4ee3-53fe-8481-7605997a9153", "William T Ripley", "646"],
  ["b9cad525-1f13-50c1-8e25-1138618cab61", "Sidney (Dr.) D Ripley II", "646"],
  ["855d1fe6-dd0c-5d54-88d2-a9e3bd462692", "Robert H Riplow", "646"],
  ["d0f39a38-64ea-559e-862b-fcd61ddd818f", "Mildred G Ripman", "646"],
  ["fd8a0f2b-ddbb-5c4e-9941-a0ca122e79ef", "Harold B Ripp", "647"],
  ["766b40cc-c419-5d82-be53-8ac9cd55dc83", "Malcolm G Rippeteau", "647"],
  ["2c462d88-6dfb-5b33-bb27-360c2d3fddc1", "Tena L Rips", "647"],
  ["732db2b5-d522-5c5e-933c-4703e1a08972", "Walter F Risdon", "647"],
] as const;

test("Batch 806 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Janet Rioch separates her hospital employment from institute affiliation", async ({ page }) => {
  await page.goto("./people/bf06d5e8-a357-576e-bda8-88847a6dddf2/");
  const main = page.locator("main");
  await expect(main).toContainText("Janet M. Rioch");
  await expect(main).toContainText("Presbyterian Hospital");
  await expect(main).toContainText("Acting director, pediatric psychiatric clinic");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("William Alanson White Institute");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("does not count the institute as an employer");
});

test("Sidney Dillon Ripley has a direct museum-to-OSS employment sequence", async ({ page }) => {
  await page.goto("./people/b9cad525-1f13-50c1-8e25-1138618cab61/");
  const main = page.locator("main");
  await expect(main).toContainText("S. Dillon Ripley");
  await expect(main).toContainText("United States National Museum, Division of Birds");
  await expect(main).toContainText("Assistant curator of birds");
  await expect(main).toContainText("Explicit immediate");
  await expect(main).toContainText("left to volunteer for the Office of Strategic Services");
  await expect(main).toContainText("Confirmed");
});

test("Robert Riplow publishes an Army assignment without inventing an employer", async ({ page }) => {
  await page.goto("./people/855d1fe6-dd0c-5d54-88d2-a9e3bd462692/");
  const main = page.locator("main");
  await expect(main).toContainText("tank destroyer unit");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("detailed to OSS beginning in 1944");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Peter Ringland publishes qualified education and Army evidence only", async ({ page }) => {
  await page.goto("./people/3be7bcee-1f3f-53db-8b5f-489682d630d6/");
  const main = page.locator("main");
  await expect(main).toContainText("St. John's College");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("order-of-battle specialist");
  await expect(main).toContainText("does not explicitly name OSS");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Tena Rips keeps the clipped note and probable identity qualified", async ({ page }) => {
  await page.goto("./people/2c462d88-6dfb-5b33-bb27-360c2d3fddc1/");
  const main = page.locator("main");
  await expect(main).toContainText("Tena Lowe Rips");
  await expect(main).toContainText("Probable");
  await expect(main).toContainText("photogra");
  await expect(main).toContainText("remains unexpanded");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("home page exposes the rebuilt Batch 806 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,525");
  await expect(home).toContainText("48.15%");
  await expect(home).toContainText("12,408");
  await expect(home).toContainText("828");
  await expect(home).toContainText("374");
  await expect(home).toContainText("9,988");
});
