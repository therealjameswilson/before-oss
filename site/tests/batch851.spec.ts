import { expect, test } from "@playwright/test";

const profiles = [
  ["2c3a7f23-5a24-587a-8b96-9445a7b19575", "Ann M Schuetz"],
  ["6311b1e5-dcf9-58df-8f12-2a69a2a7515b", "John G Schuetz"],
  ["b1934483-f9fb-5d1c-b401-dab96d48bdcc", "Ellsworth F Schug"],
  ["14276c8d-2681-5443-9655-c0c160fc3cda", "Robert E Schukraft"],
  ["b7a8a36f-3f0e-54c1-a0ff-23c840498501", "Seymour W Schulberg"],
  ["63d92813-94cd-578e-942a-c2bdc37a92d8", "Stuart H Schulberg"],
  ["dd816399-3cdf-5218-b783-52be66bf8380", "Charles J Schuler"],
  ["503bcd27-ba09-59dd-8244-5aa75a3d26c7", "Eric T Schuler"],
  ["5873cfb2-69e9-5d78-80a1-02fa4f7f422c", "Preston R Schuler"],
  ["75f1164c-ce8a-57c6-852b-ccf5ae535ac5", "Beatrice B Schulman"],
  ["c35ebe23-f76b-5f74-a5f1-183ecb1361a1", "Ira J Schulman"],
  ["85b1bce4-11ca-57b0-ba6f-3d8885f6efb3", "Walter F. L. Schulte"],
  ["6babdb66-f05b-5acb-bfdc-6ddaff49238b", "Audrey B Schultz"],
  ["a7aa6b6b-2f7a-504c-a4e8-41e0c060b77c", "Carl W Schultz"],
  ["0222b518-60e4-59b3-b3f5-5aed76819510", "Curtis C Schultz"],
  ["b41af879-a52d-58c4-83e8-9b3cb24dc972", "Curtis C Schultz"],
  ["e87090bc-7fac-5a3b-845b-5fbbd9fc5a85", "Ignac G Schultz"],
  ["7688537f-5bfa-5999-8e0c-02f057c3663a", "John W Schultz"],
  ["69ecbdb8-0662-5599-86c7-9104c752e4ce", "Robert A Schultz"],
  ["599b91f4-7d2a-5b1c-a845-4965b80096da", "Thelma C Schultz"],
  ["35c9d96c-52c7-51ad-98fc-1005f48974b0", "William J Schultz"],
  ["df1ecaf7-2b09-564b-9b8c-35436b547003", "Audrey B Schulz"],
  ["7977e41c-7967-5085-83c6-43aadc2a2ba6", "Bernard G Schulz"],
] as const;

test("Batch 851 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Robert Schukraft publishes the documented Army assignment without upgrading it to immediate or civilian employment", async ({ page }) => {
  await page.goto("./people/14276c8d-2681-5443-9655-c0c160fc3cda/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("U.S. Army Signal Intelligence Service");
  await expect(main).toContainText("Signal Intelligence Service, War Department");
  await expect(main).toContainText("Officer in charge of radio intercepts");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationU.S. Army Signal Intelligence Service");
  await expect(main).not.toContainText("Last civilian employer before serviceU.S. Army Signal Intelligence Service");
  await expect(main).toContainText("Pearl Harbor Attack: Hearings Before the Joint Committee");
});

test("Army-only Batch 851 identities do not publish coded occupations as employers", async ({ page }) => {
  for (const id of [
    "6311b1e5-dcf9-58df-8f12-2a69a2a7515b",
    "5873cfb2-69e9-5d78-80a1-02fa4f7f422c",
    "c35ebe23-f76b-5f74-a5f1-183ecb1361a1",
    "0222b518-60e4-59b3-b3f5-5aed76819510",
    "69ecbdb8-0662-5599-86c7-9104c752e4ce",
    "35c9d96c-52c7-51ad-98fc-1005f48974b0",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("two Curtis Schultz rows remain separate and expose the name conflict without inventing employment", async ({ page }) => {
  await page.goto("./people/0222b518-60e4-59b3-b3f5-5aed76819510/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("duplicate-c94da1da02de");
  await expect(main).toContainText("T/4");

  await page.goto("./people/b41af879-a52d-58c4-83e8-9b3cb24dc972/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("duplicate-c94da1da02de");
  await expect(main).toContainText("T/5");
  await expect(main).toContainText("materially conflicting name Kenneth C. Nelson");
  await expect(main).not.toContainText("Last civilian employer before serviceKenneth C. Nelson");
});

test("Audrey Schultz and Audrey Schulz remain separate spelling-variant records", async ({ page }) => {
  for (const [id, name] of [
    ["6babdb66-f05b-5acb-bfdc-6ddaff49238b", "Audrey B Schultz"],
    ["df1ecaf7-2b09-564b-9b8c-35436b547003", "Audrey B Schulz"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("duplicate-239411000406");
    await expect(main).toContainText("insufficient for a merge");
    await expect(main).toContainText("Box 689");
  }
});

test("rejected namesakes remain qualified research notes rather than facts", async ({ page }) => {
  await page.goto("./people/85b1bce4-11ca-57b0-ba6f-3d8885f6efb3/");
  const main = page.locator("main");
  await expect(main).toContainText("chronologically incompatible");
  await expect(main).toContainText("likely namesake");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});
