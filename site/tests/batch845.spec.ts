import { expect, test } from "@playwright/test";

const profiles = [
  ["49e5cc7b-2445-5559-afe9-92636212076a", "Marcus A Schillace"],
  ["fbec618c-1471-53cb-a3a1-b69469bc5ac5", "Marian M Schillinger"],
  ["a6feb4e2-f139-55df-9ba4-0dac0fa9a14f", "Hollis R Schilt"],
  ["335d4855-21cb-5088-95b0-b11833a4ae41", "Stuart B Schimmel"],
  ["b90c27e8-f865-540c-9359-19ae5ab520dc", "Charles J Schimpf"],
  ["3f1cf07b-c1c5-5798-be83-a4d9342a7240", "B P Schinchirimini"],
  ["745bcc8f-e823-5ee9-b10c-a189e64c6596", "Peter F Schinchirimini"],
  ["ac61e02f-2e7d-5359-b0a3-1fdab0134f61", "James C Schindler"],
  ["d4e2ee7a-8d50-5e78-9fe9-0d6a0eee6d62", "Harold H Schiowitz"],
  ["5c3ea8a0-f94b-585e-8b5b-35d6ef90c123", "Charles N Schirone"],
  ["584856d4-71c7-51c1-a1a9-e0dd1aa6ce44", "Francis J Schlack"],
  ["42f4688e-a1ab-5ecd-a7a4-35e11dce4c6c", "Louis A Schlafani"],
  ["bc18d8a4-a651-5a89-bf67-c6c04ca1e500", "Adrian A Schlaht"],
  ["d4dcd64c-80c4-5004-b48b-f9984fdaf48a", "Kermit F Schlamb"],
  ["ba63cec6-967a-5539-8d31-314b46b2740a", "Robert Schlangen"],
  ["6f2d4d43-bd2b-5c2c-a259-0dddc752028f", "Frederick C Schlein"],
  ["7f111cc6-d046-5eac-93ab-63f6387c204b", "Arthur M Schlesinger"],
  ["62efddb6-4cb5-566b-8141-1af088bf3041", "Edmond Schlesinger"],
  ["3a26cde1-e749-53d5-98c1-0c6acf60c267", "Aline B Schletter"],
  ["96f4df4d-2b15-54c6-a423-69683cefa21c", "Reeve Schley"],
  ["b1685556-2f90-53f4-bff3-bde745f8dd47", "Herbert W Schlickenmaie"],
  ["6232e29f-d11d-5d9e-a459-7d8af28d2395", "Frederick C Schlien"],
  ["8eb9c90a-0c92-5bb2-a6fe-17144b49774d", "Claymer Schluter"],
] as const;

test("Batch 845 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Robert Schlangen publishes State Department as an immediate government assignment", async ({ page }) => {
  await page.goto("./people/ba63cec6-967a-5539-8d31-314b46b2740a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("United States Department of State");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Advanced OSS Special Operations class");
  await expect(main).toContainText("not a private employer or last civilian-employer finding");
});

test("Reeve Schley keeps Cavalry evidence qualified and excludes his father's bank career", async ({ page }) => {
  await page.goto("./people/96f4df4d-2b15-54c6-a423-69683cefa21c/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Reeve Schley Jr");
  await expect(main).toContainText("US Cavalry");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("senior Reeve Schley's banking career is not assigned");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Arthur Schlesinger separates OWI, the Society of Fellows, and occupation context", async ({ page }) => {
  await page.goto("./people/7f111cc6-d046-5eac-93ab-63f6387c204b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("United States Office of War Information");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("Harvard Society of Fellows");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("young Harvard scholar and author");
  await expect(main).toContainText("Harvard is not converted into an employer");
});

test("Edmond Schlesinger remains a qualified probable identity without an employer", async ({ page }) => {
  await page.goto("./people/62efddb6-4cb5-566b-8141-1af088bf3041/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Edmond Robert Schlesinger");
  await expect(main).toContainText("wartime soldier and journalist");
  await expect(main).toContainText("qualified identity context and is excluded from default employer analytics");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Claymer Schluter publishes identity continuity but no pre-OSS employer", async ({ page }) => {
  await page.goto("./people/8eb9c90a-0c92-5bb2-a6fe-17144b49774d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("CIC Germany and SSU");
  await expect(main).toContainText("post-OSS continuity");
  await expect(main).toContainText("No pre-OSS affiliation is inferred");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 845 protected-identifier conflicts expose no alternate identity", async ({ page }) => {
  for (const id of [
    "745bcc8f-e823-5ee9-b10c-a189e64c6596",
    "6232e29f-d11d-5d9e-a459-7d8af28d2395",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("materially different name");
    await expect(main).toContainText("alternate identity remains private");
    await expect(main).not.toContainText("Alternate identity:");
  }
});

test("Batch 845 spelling variants preserve the indexed display form", async ({ page }) => {
  await page.goto("./people/b1685556-2f90-53f4-bff3-bde745f8dd47/");
  let main = page.locator("main");
  await expect(main).toContainText("Herbert W Schlickenmaie");
  await expect(main).toContainText("Herbert W Schlickenmaier");
  await expect(main).toContainText("documented variant rather than a silent correction");

  await page.goto("./people/42f4688e-a1ab-5ecd-a7a4-35e11dce4c6c/");
  main = page.locator("main");
  await expect(main).toContainText("Louis A Schlafani");
  await expect(main).toContainText("Louis A Sclafani");
  await expect(main).toContainText("documented source variant rather than a silent correction");
});
