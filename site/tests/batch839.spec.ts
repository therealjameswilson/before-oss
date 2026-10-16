import { expect, test } from "@playwright/test";

const profiles = [
  ["c9f76929-cf52-573a-a464-41148eda08ea", "Joseph F Sartiano"],
  ["d7e00713-8e36-5ace-abcb-6ce9e318b83b", "Francis J Sartorio"],
  ["12a7b69f-89e3-5048-9f2b-94c37a5c2210", "Dwight G Sartwell"],
  ["dd3c47cf-e59e-5feb-bae2-8b49ac4778cd", "Charles L Sarver"],
  ["3f39b1a3-b47e-54c0-bd11-1a9ef2416aa2", "Byron C Sarvis"],
  ["3b383dda-6380-571a-a0ed-9db053918a38", "Joseph J Sascavitz"],
  ["1b2cc918-dad1-59be-979d-0dee6dcee5be", "Michael F Sasko"],
  ["32ab199b-4226-5566-b7e0-078083063563", "Samuel K Saslaw"],
  ["d0a70f62-9ba6-5f9b-b386-55f0f52cb7ad", "Frankie W Sass"],
  ["acc74166-5d54-50c1-96f9-3c8f28b089f1", "Agnes L Sassoer"],
  ["d1342f43-0948-5c2f-839b-534a3a08c003", "Earl Satagofiel"],
  ["bbff6a92-aac1-5885-bf96-1fbafdee74fc", "James H Satcher"],
  ["a6ad86d6-8780-514a-9e6c-0bcc1f9d49a0", "Earl Saterfield"],
  ["7598a315-5856-55c8-b6d4-041244f19663", "Eve Satner"],
  ["23681031-4f23-574d-87ad-bd932a87655c", "Tom Satner"],
  ["52b8472a-870a-50ca-ab5d-a6294a026f50", "Robert Y P Sato"],
  ["914c7272-9aab-5716-a2cf-12775cc91e7d", "Takashi T Sato"],
  ["f0fb6249-ba23-54ae-b2d8-efda432b8580", "Elizabeth W Sauer"],
  ["8fc94009-045e-5386-8582-98c1725b2589", "Francis W Saul"],
  ["7987e57b-abc9-57c7-8385-2e926b655ed7", "Edith J Saull"],
  ["f4dba175-31ea-59d4-97c9-cc8eb553cbf4", "Bruce E Saunders"],
  ["c3359fd1-4122-57aa-a1bd-015cdabc4ef2", "Edward R Saunders"],
  ["b8e66bcf-b420-5bf4-8fa2-4f45d5258a03", "G C Saunders"],
] as const;

test("Batch 839 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
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

test("Joseph Sartiano separates the immediate Army pathway from civilian music work", async ({ page }) => {
  await page.goto("./people/c9f76929-cf52-573a-a464-41148eda08ea/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("accordion instructor and bandleader");
  await expect(main).toContainText("The Silver Strings");
  await expect(main).toContainText("Last civilian employer before service");
});

test("Byron Sarvis publishes a qualified University of Kansas employer claim", async ({ page }) => {
  await page.goto("./people/3f39b1a3-b47e-54c0-bd11-1a9ef2416aa2/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("University of Kansas");
  await expect(main).toContainText("assistant professor of psychology");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("not an unqualified claim that KU immediately preceded OSS");
  await expect(main).toContainText("E middle initial and Bryon spelling");
});

test("Francis Saul remains a qualified probable West Point match, not an employer", async ({ page }) => {
  await page.goto("./people/8fc94009-045e-5386-8582-98c1725b2589/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("United States Military Academy");
  await expect(main).toContainText("cadet");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("Student status remains analytically separate from employment");
  await expect(main.getByRole("heading", { name: "Last civilian employer before service" })
    .locator("xpath=following-sibling::p[1]")).toContainText("No reliable pre-OSS employer");
});

test("accepted Batch 839 Army crosswalks publish identity but no coded occupation", async ({ page }) => {
  for (const id of [
    "dd3c47cf-e59e-5feb-bae2-8b49ac4778cd",
    "12a7b69f-89e3-5048-9f2b-94c37a5c2210",
    "d7e00713-8e36-5ace-abcb-6ce9e318b83b",
    "d0a70f62-9ba6-5f9b-b386-55f0f52cb7ad",
    "1b2cc918-dad1-59be-979d-0dee6dcee5be",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("Sascavitz conflict is visible without leaking the alternate candidate", async ({ page }) => {
  await page.goto("./people/3b383dda-6380-571a-a0ed-9db053918a38/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("materially different name");
  await expect(main).toContainText("Alternate identity and coded fields are withheld");
  await expect(main).not.toContainText("Army occupation code");
});

test("Satagofiel and Saterfield stay separate while the possible duplicate remains visible", async ({ page }) => {
  for (const [id, name] of [
    ["d1342f43-0948-5c2f-839b-534a3a08c003", "Earl Satagofiel"],
    ["a6ad86d6-8780-514a-9e6c-0bcc1f9d49a0", "Earl Saterfield"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("Identity statusambiguous");
    await expect(main).toContainText("Duplicate groupduplicate-");
    await expect(main).toContainText("index duplication");
    await expect(main).toContainText("Review both Box 678 personnel jackets side by side");
  }
});

test("Samuel Saslaw preserves competing namesakes instead of selecting one", async ({ page }) => {
  await page.goto("./people/32ab199b-4226-5566-b7e0-078083063563/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("court reporter and a physician");
  await expect(main).toContainText("distinguish the indexed Samuel K Saslaw");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("initials-only G C Saunders gets critical archival guidance without a namesake employer", async ({ page }) => {
  await page.goto("./people/b8e66bcf-b420-5bf4-8fa2-4f45d5258a03/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("critical");
  await expect(main).toContainText("initials alone are insufficient");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("unresolved Batch 839 profiles retain dignified archival guidance", async ({ page }) => {
  for (const id of [
    "acc74166-5d54-50c1-96f9-3c8f28b089f1",
    "bbff6a92-aac1-5885-bf96-1fbafdee74fc",
    "7598a315-5856-55c8-b6d4-041244f19663",
    "23681031-4f23-574d-87ad-bd932a87655c",
    "52b8472a-870a-50ca-ab5d-a6294a026f50",
    "914c7272-9aab-5716-a2cf-12775cc91e7d",
    "f0fb6249-ba23-54ae-b2d8-efda432b8580",
    "7987e57b-abc9-57c7-8385-2e926b655ed7",
    "f4dba175-31ea-59d4-97c9-cc8eb553cbf4",
    "c3359fd1-4122-57aa-a1bd-015cdabc4ef2",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Review Box");
  }
});
