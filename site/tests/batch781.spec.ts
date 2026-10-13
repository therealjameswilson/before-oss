import { expect, test } from "@playwright/test";

const profiles = [
  ["4b8bf103-e658-53fa-a3e8-ddebcf39620e", "Raymond J Purdy"],
  ["61e6a893-2a50-5661-bcdf-dccf0095baf4", "Irma J Purifoy"],
  ["49f84958-c4f3-5145-93c8-9c3a5ac6cee7", "Betty A Purnell"],
  ["4dcf2c26-666e-5865-863e-4bb8d3e57873", "Jane Purnell"],
  ["cf2c5994-2fda-53f3-81e8-b4dc07e78bf2", "Thomas F Purner"],
  ["13ae78fd-23fd-5cb1-a18d-cfc3e8d71b78", "Minnie K Purvey"],
  ["ba4c97d5-4cca-55de-91b7-9c01d1749964", "Harry A Puryear"],
  ["2f1bc107-50f3-55e8-aa18-49d39c47590b", "John Pusateri"],
  ["b5bd9732-b2c8-50f9-893a-680461f8052a", "Stuart O Pusey"],
  ["d2f041be-3fe5-5ed0-b921-832ac7f94099", "Andrew V Puskas"],
  ["a625b577-82ed-5a50-bb69-29ec71e97da6", "Andrew B Puskas"],
  ["e0c80400-9743-5dd2-93c4-da0c26f7abc9", "August J Pusnik"],
  ["6cfcd3d0-5c4a-5310-8ec2-c21292c0b5e1", "Dante I Putignano"],
  ["217a0aa1-660b-55a3-999f-fb826e9b0e11", "Cecil R Putnam"],
  ["bdd7d5a9-0d94-5e1d-97f1-4f232d8b1971", "Eva B Putnam"],
  ["c5e61cb2-46e4-5269-94c4-249c1aed0f87", "Jane S Putnam"],
  ["97826e1d-4062-57b9-951c-427f0d5d1563", "Leonard R Putnam"],
  ["be6219b0-d0e5-560d-9e47-673d8684ea42", "Thomas N Putnam"],
  ["2b986e9e-676f-59d1-8bad-5dc6b87c3bd3", "Theodore J Putney"],
  ["78ebc639-182e-56a8-8b0e-f4b2680d18d6", "Edward J Putzell"],
  ["2cf427e5-ba8c-54cb-a2c1-f3def4cc18fd", "Edwin J Putzell"],
  ["cfb0bea0-06cd-5edd-b8ae-842049930422", "Louis Puy"],
  ["51d82c31-77a5-532b-8f03-d06b16ae56ef", "Florence E Pyatte"],
] as const;

test("Batch 781 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 781 publishes Putzell's law-firm employment in both defined predecessor categories", async ({ page }) => {
  await page.goto("./people/2cf427e5-ba8c-54cb-a2c1-f3def4cc18fd/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Donovan, Leisure, Newton and Lumbard",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "legal clerk",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Donovan, Leisure, Newton and Lumbard",
  );
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Edwin J. Putzell, Jr. Collection");
  await expect(main).toContainText("Harvard Law School");
  await expect(main).not.toContainText("Monsanto Co. in St.");
});

test("Batch 781 keeps Edward and Edwin Putzell separate pending file comparison", async ({ page }) => {
  await page.goto("./people/78ebc639-182e-56a8-8b0e-f4b2680d18d6/");
  let main = page.locator("main");
  await expect(main).toContainText("Duplicate group");
  await expect(main).toContainText("all reviewed Donovan and OSS evidence names Edwin");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );

  await page.goto("./people/2cf427e5-ba8c-54cb-a2c1-f3def4cc18fd/");
  main = page.locator("main");
  await expect(main).toContainText("The adjacent Edward J Putzell row remains separate and unresolved");
});

test("Batch 781 publishes identity evidence without inventing employers", async ({ page }) => {
  await page.goto("./people/b5bd9732-b2c8-50f9-893a-680461f8052a/");
  let main = page.locator("main");
  await expect(main).toContainText("OSS Special Operations Branch");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );

  for (const id of [
    "4b8bf103-e658-53fa-a3e8-ddebcf39620e",
    "a625b577-82ed-5a50-bb69-29ec71e97da6",
  ]) {
    await page.goto("./people/" + id + "/");
    main = page.locator("main");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
  }
});

test("Batch 781 preserves literal clipped index notes", async ({ page }) => {
  const examples = [
    ["61e6a893-2a50-5661-bcdf-dccf0095baf4", "Also in B"],
    ["a625b577-82ed-5a50-bb69-29ec71e97da6", "Also Ra"],
    ["bdd7d5a9-0d94-5e1d-97f1-4f232d8b1971", "Also 335"],
  ] as const;
  for (const [id, note] of examples) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText(note);
  }
});

test("home page exposes the rebuilt Batch 781 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,963");
  await expect(home).toContainText("45.80%");
  await expect(home).toContainText("12,971");
  await expect(home).toContainText("800");
  await expect(home).toContainText("357");
  await expect(home).toContainText("9,422");
});
