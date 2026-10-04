import { expect, test } from "@playwright/test";

const profiles = [
  ["7dbfb86e-161a-5410-b181-a39c004c0355", "Lewis C Paterson"],
  ["898ac3fb-3a7a-5ca4-bcb5-55b92ba2126f", "Lewis C Paterson"],
  ["17d184fe-d445-5d05-b5a8-09f1abfc7662", "Alexander F Pathy"],
  ["876117f5-f6df-5e75-9d99-8ad08f2792f7", "Henry A Patin"],
  ["094ef662-c09b-5087-bb2a-522fb2926498", "Erwin M Patlak"],
  ["ea5394ce-2882-5f93-be6a-a47fb7ff5a9c", "John F Patoch Jr."],
  ["8a2e0f3c-7dab-5641-b623-a7092ff748d7", "Gustav G Paton"],
  ["ffb188b7-7cd4-5534-b4e4-4b3bd1e72dfc", "Larissa Patrekeyeva"],
  ["416844e7-c4d5-59d8-ba01-f82be5056ddd", "Flay R Patrick"],
  ["985b354a-0030-5103-8df9-04d22bd70162", "Fred F Patrone"],
  ["d73b8cc0-e2b7-56c9-a836-1e5f68cab678", "Paul Patsoros"],
  ["1c9b9153-2216-5e2c-9587-a197107b6829", "Pises Pattaborgse"],
  ["19cbec33-b76e-5f48-bb2a-1969eb8aafba", "Paul B Pattee"],
  ["209cb8fb-609e-5f61-a0cf-7290705fb167", "Carl E Patten"],
  ["040c2591-ed93-5837-8527-23a9994e0e28", "Alexander R Patterson"],
  ["3f0c035d-f54c-526e-a3ef-3d0cf352598e", "Analee F Patterson"],
  ["79a99f12-559c-5036-a0b0-624063963786", "Benjamin F Patterson"],
  ["952afbad-9eec-5ce2-b900-7573ef7cdc17", "Gardner Patterson"],
  ["bdbd09a2-a84a-5742-8bcd-8729068cf6ba", "Harry M Patterson"],
  ["2f37ce6f-0ab2-5770-a0c8-3f1387ebe033", "James L Patterson"],
  ["3163ae69-a99c-5ffe-8a99-8c0a3f3ae474", "James P Patterson"],
  ["31d07208-430d-5e41-87a1-2a2acda7d3d6", "James T Patterson"],
  ["e4cdc7ec-89e6-584c-9dad-c9537689e80e", "Jere W Patterson"],
] as const;

test("Batch 738 publishes all 23 page-359 profiles with terminal dispositions", async ({ page }) => {
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

test("Batch 738 keeps the two Lewis C Paterson rows separate and qualified", async ({ page }) => {
  await page.goto("./people/7dbfb86e-161a-5410-b181-a39c004c0355/");
  let main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("compatible enlisted-to-officer sequence");
  await expect(main).toContainText("duplicate-b0be7f8d431c");

  await page.goto("./people/898ac3fb-3a7a-5ca4-bcb5-55b92ba2126f/");
  main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("enlisted army personnel");
  await expect(main).toContainText("duplicate-b0be7f8d431c");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 738 publishes Pises's Cornell relationship as student evidence, not employment", async ({ page }) => {
  await page.goto("./people/1c9b9153-2216-5e2c-9587-a197107b6829/");
  const main = page.locator("main");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("Pises Pattabongse");
  await expect(main).toContainText("Phiset Pattaphong");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Cornell University");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Mechanical engineering student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 738 keeps Larissa's postwar identity evidence qualified", async ({ page }) => {
  await page.goto("./people/ffb188b7-7cd4-5534-b4e4-4b3bd1e72dfc/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("postwar Library of Congress analyst");
  await expect(main).toContainText("cannot establish pre-OSS employment");
});

test("Batch 738 rejects the Gardner Patterson economist namesake", async ({ page }) => {
  await page.goto("./people/952afbad-9eec-5ce2-b900-7573ef7cdc17/");
  const main = page.locator("main");
  await expect(main).toContainText("not to the prominent economist and Navy namesake");
  await expect(main).toContainText("incompatible Navy and Treasury chronology");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 738 keeps official identity evidence separate from employer evidence", async ({ page }) => {
  for (const id of [
    "ea5394ce-2882-5f93-be6a-a47fb7ff5a9c",
    "985b354a-0030-5103-8df9-04d22bd70162",
    "d73b8cc0-e2b7-56c9-a836-1e5f68cab678",
    "19cbec33-b76e-5f48-bb2a-1969eb8aafba",
    "040c2591-ed93-5837-8527-23a9994e0e28",
    "2f37ce6f-0ab2-5770-a0c8-3f1387ebe033",
    "3163ae69-a99c-5ffe-8a99-8c0a3f3ae474",
    "e4cdc7ec-89e6-584c-9dad-c9537689e80e",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 738 rebuilds exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("10,008");
  await expect(main).toContainText("41.81%");
  await expect(main).toContainText("13,926");
  await expect(main).toContainText("748");
  await expect(main).toContainText("334");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
