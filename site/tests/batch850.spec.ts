import { expect, test } from "@playwright/test";

const profiles = [
  ["abcd6e26-368f-5e45-a550-8e62e44b2673", "Joseph Schreiber"],
  ["f4ae00d5-90e3-5c97-9a85-e7f9916ee16e", "Morris Schreibman"],
  ["3e907636-bfc6-5d46-b634-e6ad9541ba54", "Henry T Schreier"],
  ["756cbb3c-6648-5d37-8d91-9908f2894d6d", "Samuel A Schreiner"],
  ["e63578b0-398a-5694-9f37-7a67243248a8", "Samuel A Schreiner"],
  ["113c5579-0dc0-58f0-b2a5-97dad08d3287", "Samuel A Schreiner"],
  ["200cedcd-ab12-5d44-a352-e76be3ff2cf8", "George A Schriever"],
  ["ce8a5b6c-7281-5c6d-a26f-131661791dc5", "Beryl H Schroeder"],
  ["202f80f4-1ae4-5acd-87ba-abbc7f6a5e41", "Louis W Schroeder"],
  ["89c6f5f4-3dd1-5a7e-ba0e-2fbabee6724c", "Gustave A Schroer"],
  ["c3686019-5ca8-5409-b082-0dacbd996699", "Clarice C Schrott"],
  ["6e581218-6adc-5465-a1fd-6ff48d3a5450", "Willy Schrott"],
  ["6d7f72ae-9e11-5a5f-a528-b5afd05e3f89", "Richard E Schrunk"],
  ["be91d383-3d5f-5a0f-9696-62317b26ca2a", "Elliott W Schryver"],
  ["41c0a1b2-0ad7-5070-a311-1eb8455d1ad9", "Robert H Schubel"],
  ["8bdbc6ef-c8ac-5395-bc0a-9ed61a1bb24c", "Adella H Schubert"],
  ["3ceefe77-877f-580b-9a60-595c0bab373a", "Arthur J Schubert"],
  ["941fa7a4-3109-56e7-995d-1f00962e8f2a", "Evelyn V Schubert"],
  ["ea2111c0-5bce-5c4b-9b4a-e4cfa631146a", "Richard L Schubert"],
  ["3ae7eec2-4bbb-5c96-952d-ad4767b74b6f", "Edward C Schuberth"],
  ["3b03ea1a-8f28-5663-91a4-eb3c8021ff0b", "Kenneth D Schuckers"],
  ["59d12013-954d-5833-b1c5-a1b95681d471", "Helen J Schudlik"],
  ["34eac593-ea42-5758-9ac1-5aaf432d1a02", "Gloria M Schuette"],
] as const;

test("Batch 850 publishes all 23 reviewed profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("George Schriever publishes an explicit Army-school pathway without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/200cedcd-ab12-5d44-a352-e76be3ff2cf8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Immediate pre-OSS affiliationU.S. Army Infantry School");
  await expect(main).toContainText("Officer Candidate School at Ft. Benning, GA");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("University of Missouri");
  await expect(main).toContainText("B.S. student in Political Science");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed");
  await expect(main).not.toContainText("Last civilian employer before serviceU.S. Army Infantry School");
});

test("Elliott Schryver publishes student status but not undated publishing employment", async ({ page }) => {
  await page.goto("./people/be91d383-3d5f-5a0f-9696-62317b26ca2a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("University of Chicago");
  await expect(main).toContainText("PhB student");
  await expect(main).toContainText("student");
  await expect(main).toContainText("does not date publishing employment before OSS");
  await expect(main).not.toContainText("Last civilian employer before serviceDoubleday");
});

test("three Samuel Schreiner rows remain separate and share only a possible-duplicate flag", async ({ page }) => {
  for (const id of [
    "756cbb3c-6648-5d37-8d91-9908f2894d6d",
    "e63578b0-398a-5694-9f37-7a67243248a8",
    "113c5579-0dc0-58f0-b2a5-97dad08d3287",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("duplicate-00d664d3f5a6");
    await expect(main).toContainText("Box 687");
  }
});

test("Kenneth Schuckers keeps the shared-identifier conflict qualified and unmerged", async ({ page }) => {
  await page.goto("./people/3b03ea1a-8f28-5663-91a4-eb3c8021ff0b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("duplicate-b293daa256b6");
  await expect(main).toContainText("Kenneth D. Shuckers");
  await expect(main).toContainText("remain separate person entities");
  await expect(main).not.toContainText("civilian occupation code");
});

test("unfamiliar rank text is preserved without expansion", async ({ page }) => {
  await page.goto("./people/6d7f72ae-9e11-5a5f-a528-b5afd05e3f89/");
  const main = page.locator("main");
  await expect(main).toContainText("1ST ST");
  await expect(main).toContainText("evidence justifying expansion of the unfamiliar abbreviation");
  await expect(main).toContainText("Personnel categoryunknown or indeterminate");
});

test("Army-only Batch 850 identities do not publish coded occupations as employers", async ({ page }) => {
  for (const id of [
    "abcd6e26-368f-5e45-a550-8e62e44b2673",
    "3e907636-bfc6-5d46-b634-e6ad9541ba54",
    "113c5579-0dc0-58f0-b2a5-97dad08d3287",
    "41c0a1b2-0ad7-5070-a311-1eb8455d1ad9",
    "3ceefe77-877f-580b-9a60-595c0bab373a",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});
