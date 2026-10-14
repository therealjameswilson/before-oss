import { expect, test } from "@playwright/test";

const profiles = [
  ["31195a09-7e84-57fe-bf00-ab0888dbc5af", "Maurice H Rapf"],
  ["f76514ea-6bb9-5fd9-abda-8cd35aa65da3", "Erwin E Raphael"],
  ["f3865880-7729-5333-aa4c-4d8fedf71b2d", "Andre L Rapicault"],
  ["85acd027-7030-558d-b00b-085e6f7c75da", "Anastas D Rapoff"],
  ["2bec1157-57e7-5536-af40-57d9f2265341", "Robert N Rapoport"],
  ["85915b4f-be7f-534d-b316-de90f7a4e2a0", "Milton J Raport"],
  ["00fde3b6-0829-5395-91c9-fefdded91513", "Manuel C Raposa"],
  ["bb45ddfb-4138-5809-84c2-8d6c72cca13e", "Arthur F Rapp"],
  ["1105144a-1f16-581a-b420-39d9fe575620", "Milton A Rapp"],
  ["da09ace6-f204-5103-a1aa-7444f0c6c6e6", "Alfred M Rasero"],
  ["5b32cb57-45c6-5e24-bf07-d925fc1ce0a5", "Lee Rashall"],
  ["df16618a-fcbd-5f52-9d2a-92c9af2a9100", "Dale M Raska"],
  ["85218c2f-c141-5f48-b693-39e154fdddf1", "George P Rasmussen"],
  ["9dc8c96b-b03b-5930-bffe-697b197935e9", "Wilton M Rasmussen"],
  ["ffc6389f-d99e-5491-943a-9895f5fbbf0f", "Charles Rata"],
  ["cdd7844d-2e52-53dc-88e3-8dcc3c4a5a5f", "Charles B Ratchford"],
  ["5bec7833-ed18-5e99-b6b6-e72f26fc384f", "Edward G Ratcliffe"],
  ["e04f251a-30e5-5a79-927b-0f46ea841720", "William H Rath"],
  ["45440588-5c05-5ed1-b1f9-dda58b5adbae", "Virginia Rathbun"],
  ["b6f96b15-470b-5833-ba07-ed8c06e9a68d", "Seymour A Rattenberg"],
  ["90072d44-985d-5904-8661-90ffe10beece", "Eleanor M Rattigan"],
  ["43caee00-93f6-5914-8404-4a7e93020e19", "Joan L Rattner"],
  ["29abdc48-6e58-5960-a696-16cce602107b", "Michael Ratushni"],
] as const;

test("Batch 789 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 789 qualifies Rapf's freelance work and does not invent a studio employer", async ({ page }) => {
  await page.goto("./people/31195a09-7e84-57fe-bf00-ab0888dbc5af/");
  const main = page.locator("main");
  await expect(main).toContainText("Maurice Harry Rapf");
  await expect(main).toContainText("freelance screenwriter in Hollywood");
  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("Dartmouth Libraries");
  await expect(main).toContainText("No studio employer is inferred");
});

test("Batch 789 presents Skidmore as Rathbun's student affiliation, not an employer", async ({ page }) => {
  await page.goto("./people/45440588-5c05-5ed1-b1f9-dda58b5adbae/");
  const main = page.locator("main");
  await expect(main).toContainText("Virginia Rathbun Stuart");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("Skidmore College");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("Student; English major");
  await expect(main).toContainText("strongly date bounded");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("Skidmore College");
  await expect(main).toContainText("Skidmore is recorded as a student affiliation, not an employer");
});

test("Batch 789 exposes the Rattenberg and Rottenberg conflict without merging or exposing the identifier", async ({ page }) => {
  const ids = [
    "b6f96b15-470b-5833-ba07-ed8c06e9a68d",
    "2b490178-2fd8-557d-9a74-08a8d8d2cd0f",
  ] as const;
  const groups: string[] = [];
  for (const id of ids) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Duplicate group");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
    const text = await main.textContent();
    const match = text?.match(/duplicate-[0-9a-f]+/);
    expect(match).toBeTruthy();
    groups.push(match![0]);
  }
  expect(groups[0]).toBe(groups[1]);
  await page.goto("./people/b6f96b15-470b-5833-ba07-ed8c06e9a68d/");
  await expect(page.locator("main")).toContainText("Saymour A Rottenberg");
  await expect(page.locator("main")).toContainText("conflicting");
});

test("Batch 789 preserves clipped notes and masks the printed scientific-notation identifier", async ({ page }) => {
  for (const [id, note] of [
    ["bb45ddfb-4138-5809-84c2-8d6c72cca13e", "see file"],
    ["1105144a-1f16-581a-b420-39d9fe575620", "Record"],
    ["85218c2f-c141-5f48-b693-39e154fdddf1", "photogra"],
    ["e04f251a-30e5-5a79-927b-0f46ea841720", "Record"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText(note);
  }
  await page.goto("./people/5bec7833-ed18-5e99-b6b6-e72f26fc384f/");
  const main = page.locator("main");
  await expect(main).toContainText("••••82E0");
  const serials = await main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]").allTextContents();
  for (const value of serials) expect(value).not.toMatch(/^\d(?:\.\d+)?e[+-]?\d+$/i);
});

test("home page exposes the rebuilt Batch 789 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,145");
  await expect(home).toContainText("46.56%");
  await expect(home).toContainText("12,789");
  await expect(home).toContainText("806");
  await expect(home).toContainText("360");
  await expect(home).toContainText("9,604");
});
