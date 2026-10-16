import { expect, test } from "@playwright/test";

const profiles = [
  ["2e362dbe-f337-51c2-973c-17879fb8f4aa", "Norman B Schofield"],
  ["fc91f776-b9a8-5630-ab6f-c5a971b58587", "Thurman R Scholl"],
  ["0fa972cd-015b-5020-8c58-6ab197768909", "Dewayne F Scholtz"],
  ["b9d27a1a-a80f-5f4a-90af-c2a8289cb851", "Herman F Scholtz"],
  ["6c1d089e-e250-5ef0-8764-8c9de0c1c2e3", "Silverius W Schon"],
  ["9bf89119-e6c5-5645-9604-f19313b879bc", "Marcel H Schonaers"],
  ["5e5b69ae-0db7-5832-bf83-908fa04f679d", "Otto P Schonfield"],
  ["92df19ec-cafc-5b13-b121-1afbf0926186", "Otto P Schonfield"],
  ["6195aa54-b793-59de-a9c6-f616ad1c4e6e", "Francis A Schooley"],
  ["f870eeb7-2f90-5575-8a93-fe5ee59c0e4b", "Frank Schoonmaker"],
  ["2e4e393e-3475-5a79-897a-62d7c3b817ca", "William C Schor"],
  ["d086f590-f86d-5535-8411-aa60aa252f01", "Carl E Schorske"],
  ["4e6e2103-9aae-5f74-b399-993a5a614ee3", "Elizabeth P-I Schorske"],
  ["8c0af45d-f26b-525e-952e-7a72ef4d7f24", "Lawrence S Schottenham"],
  ["7ab58709-5abd-532e-a8a9-a161580a5865", "Henri Schouler"],
  ["fa5ef0fb-8a54-5380-965d-55f78cc4db83", "Peter Schouvaloff"],
  ["f230e8cd-f9c3-57b1-b6c3-c39b0ae2db58", "Emile Schouwer"],
  ["9189438a-d1ca-510c-8633-bbcdf19d1d49", "Marcel H Schovaers"],
  ["b42ecfc9-b170-5ca9-a1c0-e0dd0e3f45c6", "Anton B Schrader"],
  ["e706a118-d204-5d8c-b6fa-15eaf189b3c8", "Robert C Schrader"],
  ["70a83461-c727-5409-95f1-c449568fc64a", "Jack H Schramm"],
  ["482e36f3-7d33-5978-a8e5-09f7b3a9bcba", "William J Schreck"],
  ["3d15f1a8-89ab-5ca6-b83e-c36ec1cabad8", "Dale F Schreckengost"],
] as const;

test("Batch 849 publishes all 23 reviewed profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Herman Scholtz keeps civilian internment between his company and OSS visible", async ({ page }) => {
  await page.goto("./people/b9d27a1a-a80f-5f4a-90af-c2a8289cb851/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Last civilian employer before serviceInternational Engineering Company");
  await expect(main).toContainText("civilian internment intervened");
  await expect(main).toContainText("not labeled the immediate pre-OSS affiliation");
  await expect(main).toContainText("Question AImmediate pre-OSS affiliation");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Frank Schoonmaker publishes the same self-employed business in both required chronology fields", async ({ page }) => {
  await page.goto("./people/f870eeb7-2f90-5575-8a93-fe5ee59c0e4b/");
  const main = page.locator("main");
  await expect(main).toContainText("Immediate pre-OSS affiliationFrank Schoonmaker Selections");
  await expect(main).toContainText("Last civilian employer before serviceFrank Schoonmaker Selections");
  await expect(main).toContainText("Founder and wine importer");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("self employment");
});

test("Anton Schrader publishes Dutch government employment without inventing Royal Engineers service", async ({ page }) => {
  await page.goto("./people/b42ecfc9-b170-5ca9-a1c0-e0dd0e3f45c6/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Rijksbureau voor de Voedselvoorziening in Oorlogstijd");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("not labeled immediate pre-OSS");
  await expect(main).toContainText("authorization for Royal Engineers service is not treated as proof");
});

test("Elizabeth Schorske remains a qualified probable identity with the printed P-I ambiguity", async ({ page }) => {
  await page.goto("./people/4e6e2103-9aae-5f74-b399-993a5a614ee3/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Elizabeth Rorke Schorske");
  await expect(main).toContainText("printed P-I value remains unexplained");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("does not document her pre-OSS employment");
});

test("Henri Schouler and Emile Schouwer publish wartime identities without employer invention", async ({ page }) => {
  await page.goto("./people/7ab58709-5abd-532e-a8a9-a161580a5865/");
  let main = page.locator("main");
  await expect(main).toContainText("André Beignet");
  await expect(main).toContainText("Plutarque");
  await expect(main).toContainText("documents wartime OSS/Sussex service, not a pre-OSS employer");

  await page.goto("./people/f230e8cd-f9c3-57b1-b6c3-c39b0ae2db58/");
  main = page.locator("main");
  await expect(main).toContainText("SHD GR 16 P 541191");
  await expect(main).toContainText("OSS award-list entries");
  await expect(main).toContainText("establishes wartime identity but not a pre-OSS employer or assignment chronology");
});

test("possible duplicate pairs remain separate and visibly flagged", async ({ page }) => {
  for (const [id, group] of [
    ["9bf89119-e6c5-5645-9604-f19313b879bc", "duplicate-1aa095d84383"],
    ["9189438a-d1ca-510c-8633-bbcdf19d1d49", "duplicate-1aa095d84383"],
    ["5e5b69ae-0db7-5832-bf83-908fa04f679d", "duplicate-35bb89ecce92"],
    ["92df19ec-cafc-5b13-b121-1afbf0926186", "duplicate-35bb89ecce92"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText(group);
  }
});

test("Army-only Batch 849 identities do not expose occupation codes or invent employers", async ({ page }) => {
  for (const id of [
    "2e362dbe-f337-51c2-973c-17879fb8f4aa",
    "0fa972cd-015b-5020-8c58-6ab197768909",
    "2e4e393e-3475-5a79-897a-62d7c3b817ca",
    "e706a118-d204-5d8c-b6fa-15eaf189b3c8",
    "70a83461-c727-5409-95f1-c449568fc64a",
    "482e36f3-7d33-5978-a8e5-09f7b3a9bcba",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});
