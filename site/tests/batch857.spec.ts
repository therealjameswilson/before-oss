import { expect, test } from "@playwright/test";

const profiles = [
  ["295d5ae0-cdc3-508d-a42f-341f5d12968c", "Catherine C Seerley"],
  ["5a4dccbe-4f04-5fbf-aacf-2fcc29c92afe", "Manuel Segal"],
  ["31028dc8-5d0a-5c84-9409-2578c00d239b", "Maurice J Segal"],
  ["540db647-18ac-5dc8-a616-75b789195347", "Philip Segal"],
  ["935fbceb-c069-5a03-8fd4-9c0f61aebe3c", "Herman Segall"],
  ["e98c7cf5-db89-5a51-ac64-6ba8bc7a5a37", "Fumiko Segawa"],
  ["acb8445d-8235-5076-b5ce-f5ea01e1091b", "Harry Segen"],
  ["9b1b6453-00f3-531e-8726-16e833e8edd5", "Gerhart Seger"],
  ["814b3401-7774-5f4c-bc35-7b5164162d6d", "Steven F Segeti"],
  ["9e3ec489-4edd-58ad-8a15-fcbcd693fbdd", "Guy E Seiber"],
  ["f42cee60-189e-5211-b960-f8908e5ebad2", "Karl G Seibold"],
  ["b7a74fed-7bf7-5263-b026-f71d91c9478d", "Kuragi Seida"],
  ["4f3c6a0a-538a-59da-933a-282044004755", "Herbert H Seidell"],
  ["630791cf-7325-5125-8f74-165bdcd2f31c", "Joseph H Seidl"],
  ["0a0e60a5-9fdc-5aee-b8e9-70dcfadbd70b", "Francis Seidler"],
  ["b34d7db9-5ced-5822-9291-0dc224adba7a", "Elvin A Seidner"],
  ["5aabfd31-fd0e-50b5-9ce1-4e5dd492c573", "Alf Seierstad"],
  ["a119a443-2e06-52f2-9b14-07cf9fd39d5c", "David Seiferheld"],
  ["6ae55d2f-f22c-585c-ae89-d4cb70b6cceb", "Allen J Seilheimer"],
  ["ce3008ce-9292-506b-9537-f28a68c5c4fc", "Robert N Seiple"],
  ["c36ad91d-bbea-5e65-99a9-d5020f6368d5", "Robert N Seiple"],
  ["520b13f2-66dd-5e68-9df5-61878dee460b", "Melita U Seipp"],
  ["4830f92a-578d-518e-83d1-0c4ffb69115a", "Max Seitelman"],
] as const;

test("Batch 857 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Manuel Segal publishes NBC as the last civilian employer, not the immediate affiliation", async ({ page }) => {
  await page.goto("./people/5a4dccbe-4f04-5fbf-aacf-2fcc29c92afe/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main.getByRole("heading", { name: "Last civilian employer before service" })).toBeVisible();
  await expect(main).toContainText("National Broadcasting Company");
  await expect(main).toContainText("Sound effects engineer");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Radio Warfare: OSS and CIA Subversive Propaganda");
  await expect(main).toContainText("Sound Effects");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationNational Broadcasting Company");
});

test("Fumiko Segawa publishes an explicit WAAC military pathway without inventing an employer", async ({ page }) => {
  await page.goto("./people/e98c7cf5-db89-5a51-ac64-6ba8bc7a5a37/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Immediate pre-OSS affiliationWomen's Army Auxiliary Corps");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Third Training Center");
  await expect(main).toContainText("Private");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Gerhart Seger's newspaper work remains documented prewar rather than immediate", async ({ page }) => {
  await page.goto("./people/9b1b6453-00f3-531e-8726-16e833e8edd5/");
  const main = page.locator("main");
  await expect(main).toContainText("Neue Volkszeitung");
  await expect(main).toContainText("employment");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationNeue Volkszeitung");
});

test("Francis Seidler separates his Army pathway from earlier Austrian government service", async ({ page }) => {
  await page.goto("./people/0a0e60a5-9fdc-5aee-b8e9-70dcfadbd70b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Immediate pre-OSS affiliation7th Photographic Intelligence Detachment");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Austrian Federal Chancellery");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("David Seiferheld keeps nonprofit roles and a generic occupation separate from employment", async ({ page }) => {
  await page.goto("./people/a119a443-2e06-52f2-9b14-07cf9fd39d5c/");
  const main = page.locator("main");
  await expect(main).toContainText("American Friends of German Freedom");
  await expect(main).toContainText("Emergency Rescue Committee");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("textile executive");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceAmerican Friends of German Freedom");
  await expect(main).not.toContainText("Last civilian employer before serviceEmergency Rescue Committee");
});

test("official Army crosswalks publish identity evidence only", async ({ page }) => {
  for (const id of [
    "31028dc8-5d0a-5c84-9409-2578c00d239b",
    "acb8445d-8235-5076-b5ce-f5ea01e1091b",
    "9e3ec489-4edd-58ad-8a15-fcbcd693fbdd",
    "4f3c6a0a-538a-59da-933a-282044004755",
    "5aabfd31-fd0e-50b5-9ce1-4e5dd492c573",
    "6ae55d2f-f22c-585c-ae89-d4cb70b6cceb",
    "ce3008ce-9292-506b-9537-f28a68c5c4fc",
    "4830f92a-578d-518e-83d1-0c4ffb69115a",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }

  await page.goto("./people/814b3401-7774-5f4c-bc35-7b5164162d6d/");
  const main = page.locator("main");
  await expect(main).toContainText("Steven F. Segeti, Jr.");
  await expect(main).toContainText("Greek Group VII");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("the two Robert Seiple source rows remain separate with one opaque duplicate label", async ({ page }) => {
  for (const id of [
    "ce3008ce-9292-506b-9537-f28a68c5c4fc",
    "c36ad91d-bbea-5e65-99a9-d5020f6368d5",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Duplicate groupduplicate-21fba3b6d113");
    await expect(main).not.toContainText("page418-robert-seiple-pair");
  }
});
