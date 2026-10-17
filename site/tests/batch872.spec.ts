import { expect, test } from "@playwright/test";

const profiles = [
  ["d94cc593-2154-595e-b939-33b06f1ee71b", "Myron Shpur"],
  ["76502f71-26c1-5afa-bf5f-010d6f757ab1", "Henry J Shrader"],
  ["3d7cdd63-e1ba-566a-b15b-c2f3987eb960", "Frederick C Shrady"],
  ["c4636740-da61-551e-b57c-2020d1048d27", "Ernest H Shrenzel"],
  ["59e6508e-5a17-5e60-871b-35a40f4b6a5b", "Robert F Shreves"],
  ["dd655b84-698a-5cff-ab89-b766c7168597", "Charles E Shrewsbury"],
  ["ab919846-91fc-56c4-8e4c-a45066bf3941", "Kathleen Shrier"],
  ["ef9b03ae-d7b0-5bd6-b6aa-ed49f36200b3", "Glenn K Shriver"],
  ["44042f84-7e9f-5143-a90f-b7c47ab6ac22", "Shirley Shropshire"],
  ["5136263b-da54-519d-b557-b5e004507132", "Marshall E Shroyer"],
  ["cae19dea-0baf-5a94-b18e-3d356a8660fa", "Mortimer Shuart"],
  ["2df620fd-960f-5d0e-a37f-ff11f8cd6862", "Elizabeth C Shub"],
  ["16d49415-f780-5074-844b-a6bffa4a95e9", "Louise K Shuberg"],
  ["5d734df4-3035-58cd-af85-740cb77148e2", "Richard T Shubert"],
  ["3e4c5958-fb47-54d0-a18d-494872be0efa", "Kenneth D Shuckers"],
  ["3b62852e-8b34-52eb-9b82-35f8de7e387a", "Marcia V Shufelt"],
  ["4510f2cf-be9a-5c37-b97e-0c1b0ad51ccd", "Rachel M Shugars"],
  ["4ed0f9b0-2373-5fba-b093-843c99546301", "Herman Shukovsky"],
  ["32b61688-473e-5ef2-a5a2-2046a9a1cccb", "W G Shuling"],
  ["0c3c2dd6-6200-594c-b2bc-4f4688cef09a", "Harvey B Shulman"],
  ["bef73d2d-b504-51ba-87db-fc56ce9cc130", "Helen Shulman"],
  ["3ed5a242-aae0-51f7-a311-5619aa2dfb3a", "Ralph C Shultz"],
  ["f4c0a17b-2176-52eb-b30d-20b2486afa17", "Marshall J Shumate"],
] as const;

test("Batch 872 publishes all 23 profiles with reviewed outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 872 separates Myron Shpur's last civilian War Department role from the Army-to-OSS transition", async ({ page }) => {
  await page.goto("./people/d94cc593-2154-595e-b939-33b06f1ee71b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("United States War Department");
  await expect(main).toContainText("civilian employee");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Army service between the civilian job and OSS");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 872 models Frederick Shrady as a self-employed artist before Army and OSS service", async ({ page }) => {
  await page.goto("./people/3d7cdd63-e1ba-566a-b15b-c2f3987eb960/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("career as an artist");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("No employing organization is invented");
});

test("Batch 872 publishes the Shuling-Suhling identity bridge and keeps the company role qualified", async ({ page }) => {
  await page.goto("./people/32b61688-473e-5ef2-a5a2-2046a9a1cccb/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("William G Suhling Jr");
  await expect(main).toContainText("Suhling & Company, Inc.");
  await expect(main).toContainText("president");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("not shown to be the immediate predecessor");
});

test("Batch 872 preserves the two Kenneth Schuckers-Shuckers jackets without merging them", async ({ page }) => {
  await page.goto("./people/3e4c5958-fb47-54d0-a18d-494872be0efa/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("needs identity review");
  await expect(main).toContainText("separate Box 688 Kenneth D Schuckers row");
  await expect(main).toContainText("prohibit an automatic merge");
  await expect(main).not.toContainText("33769117");

  await page.goto("./people/3b03ea1a-8f28-5663-91a4-eb3c8021ff0b/");
  main = page.locator("main");
  await expect(main).toContainText("Kenneth D Schuckers");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Archive box688");
  await expect(main).not.toContainText("33769117");
});

test("Batch 872 retains accepted Army matches as identity evidence, not employer claims", async ({ page }) => {
  for (const id of [
    "59e6508e-5a17-5e60-871b-35a40f4b6a5b",
    "5136263b-da54-519d-b557-b5e004507132",
    "0c3c2dd6-6200-594c-b2bc-4f4688cef09a",
    "f4c0a17b-2176-52eb-b30d-20b2486afa17",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 872 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 581,
    research_attempted_people: 13_021,
    verified_affiliation_people: 948,
    verified_employer_people: 431,
    archival_review_assessed_people: 11_488,
    published_claims: 7_864,
    public_sources: 5_359,
  });
});
