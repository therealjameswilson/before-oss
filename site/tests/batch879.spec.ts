import { expect, test } from "@playwright/test";

const profiles = [
  ["6d2fb252-3737-561e-ab60-b7a216f2dce4", "Rose A Simons"],
  ["6876d538-e5fc-57ce-907e-3f4fde4b5000", "Serena A Simons"],
  ["1d2a84f7-7973-5a7e-8d36-3772dce3c796", "Erik Simonsen"],
  ["1b4ca170-9496-507a-bd81-aca67c348ba0", "Richard M Simonsen"],
  ["26043056-c09d-57e7-b939-317010499744", "Lee Simonson"],
  ["9104d7f2-cbdc-5536-ab82-d0ae84e946f5", "Collins Simpson"],
  ["9c9040bd-33a9-5fd5-9243-46f6d4f4ce5d", "Collis Simpson"],
  ["9f30dace-e129-5747-b0e9-44e4f0dac838", "Deurell C Simpson"],
  ["5c0096a5-ba5a-511c-acae-10bb4a2f5712", "Elliot H Simpson"],
  ["db986519-0d95-5af0-8977-99460edbae03", "Maurice W Simpson"],
  ["b23766b1-9282-50da-97ec-fd82df86eda8", "Robert C Simpson"],
  ["64f47d6e-59da-5209-9d23-ae88d8e28616", "Robert I Simpson"],
  ["d5a40215-5e2b-5e58-a44e-1c88afd1a2ab", "Roger E Simpson"],
  ["46c4071e-393f-5689-816d-8ae8c29bbf31", "Ronald S Simpson"],
  ["cf7296c7-7a3c-5962-b7f6-b2974381215f", "Stephen H Simpson"],
  ["55453f61-485f-5348-bbb2-26ce0fc81cc4", "Vivian V Simpson"],
  ["a24bab42-d9b3-57e0-a0bc-3e947cbcda67", "Wendel K. Simpson"],
  ["0c68defb-0ace-5562-86e3-9d0c1e5b2c2f", "Albert T Sims"],
  ["68b772a9-990d-52d1-b7ec-1057a6f66475", "Percy E Sims"],
  ["cc79ac97-86d8-5551-8025-7c56f22dae58", "Ralph Y Sims"],
  ["fccd7dda-93a9-5710-834e-13bbda8af9f6", "William P Sims"],
  ["ebd08356-80fe-57d3-b7c2-dd7d8d1a33d1", "Marie L Sinaguglia"],
  ["ad79da97-bd5f-5ee2-9adb-3b1f7be9e9a5", "Nathan Sinai"],
] as const;

test("Batch 879 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 879 documents Nathan Sinai's Michigan employment without overstating recruitment", async ({ page }) => {
  await page.goto("./people/ad79da97-bd5f-5ee2-9adb-3b1f7be9e9a5/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("University of Michigan");
  await expect(main).toContainText("Professor of Hygiene and Public Health");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("not an explicit recruited-from statement");
  await expect(main).toContainText("Last civilian employer before serviceUniversity of Michigan");
});

test("Batch 879 keeps Lee Simonson's Theatre Guild role professional rather than an employer claim", async ({ page }) => {
  await page.goto("./people/26043056-c09d-57e7-b939-317010499744/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Theatre Guild");
  await expect(main).toContainText("Founding member and theatrical designer");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText(/documented prewar/i);
  await expect(main).toContainText("not proven to be his immediate employer before OSS");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 879 qualifies Ronald Simpson's 101st Cavalry service", async ({ page }) => {
  await page.goto("./people/46c4071e-393f-5689-816d-8ae8c29bbf31/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("101st Cavalry, New York National Guard");
  await expect(main).toContainText("Troop E serviceman");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("does not establish the transfer date into OSS");
  await expect(main).toContainText("Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified");
});

test("Batch 879 preserves Deurell and Wendel source disagreements", async ({ page }) => {
  await page.goto("./people/9f30dace-e129-5747-b0e9-44e4f0dac838/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("disagree on the middle initial");
  await expect(main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]"))
    .toContainText(/^••••\d{4}$/);

  await page.goto("./people/a24bab42-d9b3-57e0-a0bc-3e947cbcda67/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("spells the first name Wendell");
  await expect(main).toContainText("obituary is not transferred");
  await expect(main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]"))
    .toContainText(/^••••\d{4}$/);
});

test("Batch 879 retains Stephen Simpson's indexed commissioned naval classification", async ({ page }) => {
  await page.goto("./people/cf7296c7-7a3c-5962-b7f6-b2974381215f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Rank or gradeLT CMD");
  await expect(main).toContainText("Personnel categorycommissioned naval officer");
  await expect(main).toContainText("Commissioned officerYes");
});

test("Batch 879 does not publish rejected namesake occupations or employers", async ({ page }) => {
  await page.goto("./people/a24bab42-d9b3-57e0-a0bc-3e947cbcda67/");
  let main = page.locator("main");
  await expect(main).not.toContainText("American Life Convention");
  await expect(main).not.toContainText("DePauw University");

  await page.goto("./people/ebd08356-80fe-57d3-b7c2-dd7d8d1a33d1/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).not.toContainText("Secretary");
});

test("Batch 879 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 584,
    research_attempted_people: 13_180,
    verified_affiliation_people: 954,
    verified_employer_people: 433,
    archival_review_assessed_people: 11_647,
    published_claims: 7_952,
    public_sources: 5_399,
  });
});
