import { expect, test } from "@playwright/test";

const profiles = [
  ["d630b25d-c7ab-5600-8f22-dcbf3ff32694", "Adolf Schwartz"],
  ["cf2008c6-45ca-512d-a71f-20d5d5971741", "Bert D Schwartz"],
  ["92c27ba7-53a8-51b4-af2c-192db0da8f46", "Charlotte H Schwartz"],
  ["0f6ef492-f759-586d-8746-e665c1e8e081", "Edward Schwartz"],
  ["762321fc-7031-561f-acc1-98b5dc5cd790", "Evelyn Schwartz"],
  ["e77c8954-8cbd-5e9f-ab19-4ed56b79a9af", "Gare Schwartz"],
  ["d13d2214-2135-5e5c-89c3-c56b5289f777", "George Schwartz"],
  ["82395afc-fdfa-57a3-b1a9-d75b8f3368cb", "Harry Schwartz"],
  ["0bb7195f-21ce-5420-8215-d22e51e3f323", "Harry Schwartz"],
  ["60d2b1f2-c4ae-5194-ad59-b2db06fe23c7", "Irving S Schwartz"],
  ["43a85e68-95ee-53cc-a4d4-c3ff0ebfef8a", "John Schwartz"],
  ["b0300104-093e-527e-a5f6-179bdfebc689", "Joseph K Schwartz"],
  ["f02f0c65-70c5-5b5a-9188-704a406a3f6c", "Martin V Schwartz"],
  ["05a0c398-ff7a-5078-bf66-ead7196c351a", "Myrtil Schwartz"],
  ["7daf9a7d-c613-5832-8e3e-3f88d5c3fdf9", "Stanley C Schwartz"],
  ["bc5a9959-386b-57e5-a380-7e671d8c4e2a", "Nathan Schwartzapfel"],
  ["b0c187ac-a4e1-55ec-8060-3dfb377c8bba", "Dorothy Schwarz"],
  ["a9a10897-8506-56a8-9318-88bfaf75f8c3", "Sanford Schwarz"],
  ["60a0953e-0221-56dc-80f9-e4d2f8bcd69b", "Anthon F Schweer"],
  ["74b2fc0a-e4a6-54bd-a750-da9f10805c58", "Bernard R Schweid"],
  ["02c24c70-6f63-5c90-9fdd-8050129d7554", "Raymond G Schweiker"],
  ["9ed31d6b-9826-5a52-a21e-e85b6b7c02a7", "Murray Schweitzer"],
  ["ee6b746a-616b-586e-9f33-a0b868e0d5a8", "Ruth M Schwenn"],
] as const;

test("Batch 853 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Bert Schwartz and Bernard Schweid publish confirmed assessment-staff identities without inventing employers", async ({ page }) => {
  for (const [id, name] of [
    ["cf2008c6-45ca-512d-a71f-20d5d5971741", "Bert D. Schwartz"],
    ["74b2fc0a-e4a6-54bd-a750-da9f10805c58", "Bernard R. Schweid"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconfirmed");
    await expect(main).toContainText("Assessment of Men: Selection of Personnel for the Office of Strategic Services");
    await expect(main).toContainText(name);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Last civilian employer before serviceAssessment of Men");
  }
});

test("the two Harry Schwartz rows remain separate and do not share career evidence", async ({ page }) => {
  await page.goto("./people/82395afc-fdfa-57a3-b1a9-d75b8f3368cb/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("duplicate-1bd1c838ca98");
  await expect(main).toContainText("New York Times");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/0bb7195f-21ce-5420-8215-d22e51e3f323/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("duplicate-1bd1c838ca98");
  await expect(main).toContainText("No career evidence for the commissioned namesake is assigned to this enlisted row");
  await expect(main).not.toContainText("New York Times");
  await expect(main).not.toContainText("Weizmann Institute");
});

test("John Schwartz publishes the HOUSEBOAT identity bridge but no employer", async ({ page }) => {
  await page.goto("./people/43a85e68-95ee-53cc-a4d4-c3ff0ebfef8a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("HOUSEBOAT");
  await expect(main).toContainText("Nation's Memory Institute");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceHOUSEBOAT");
});

test("Martin Schwartz exposes the protected-identifier conflict and no employer", async ({ page }) => {
  await page.goto("./people/f02f0c65-70c5-5b5a-9188-704a406a3f6c/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("materially different Army transcription");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Myrtil Schwartz keeps qualified occupations separate from an employer", async ({ page }) => {
  await page.goto("./people/05a0c398-ff7a-5078-bf66-ead7196c351a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("prewar mountaineering author and active alpinist");
  await expect(main).toContainText("government official");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before servicegovernment official");
});

test("Sanford Schwarz publishes qualified institutions without copying the adjacent obituary", async ({ page }) => {
  await page.goto("./people/a9a10897-8506-56a8-9318-88bfaf75f8c3/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("duplicate-ba920f5354c9");
  await expect(main).toContainText("United States-Mexican Claims Commission");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("Carnegie Endowment for International Peace");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("People in Political Science: Sanford Schwarz");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("University of Kentucky");
  await expect(main).not.toContainText("Transylvania University");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationCarnegie Endowment");
  await expect(main).not.toContainText("Last civilian employer before serviceCarnegie Endowment");

  await page.goto("./people/ba02d5d6-531c-5d07-95e2-5c68c926bee8/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("duplicate-ba920f5354c9");
  await expect(main).not.toContainText("Carnegie Endowment for International Peace");
});
