import { expect, test } from "@playwright/test";

const profiles = [
  ["b4e4aef1-383c-525b-88e9-0d84530fe068", "Edgar Salinger"],
  ["d6b4ea1b-ca67-51cb-8827-86eb98b5c787", "Peter F Salisbury"],
  ["87ee683e-4818-5ad8-9b16-2b16ef9b204b", "Herbert J Salisman"],
  ["995e348b-0de4-525f-81f0-392c682b9472", "Paul D Sallee"],
  ["2ed0e6af-feca-5ba8-9c88-4e0809dfe9d6", "Albert J Salmon Jr."],
  ["a8a06481-addb-54f2-813f-b7e981531afc", "Eileen D Salmonson"],
  ["78600cc6-1d7a-514c-a19d-7afcce26d8a9", "John Salmonson"],
  ["aeacc9c3-1079-5083-9224-5c71b25783bf", "Dagmar F Salo"],
  ["4c90348c-1a18-5e13-9fd3-7db395cfdbe8", "D G Salomon"],
  ["7f39bd25-1be6-5f10-b07b-9fdad6b3df7f", "Richard G Salomon"],
  ["a32f720f-e4ce-5dce-962b-a8470c838449", "Einar A Salonnen"],
  ["225e5bd2-5ab8-5afa-8d2f-00673f876117", "Neattie Salowitz"],
  ["a5dd0e6b-f8e0-59be-8cbc-1d5b4f426ff5", "Tillie Salowitz"],
  ["5d70cabe-916a-5b3a-a4db-aacf1edaeb3d", "Edward M Salter"],
  ["23379e95-55c1-576c-8fbd-9c102d7c065a", "Edwin L Salter"],
  ["4743bc08-0a71-5ae0-aa3f-afce72404b4b", "Robert A Saltzstein"],
  ["9ae95c99-0ca8-5830-b97e-39b7c9ef530a", "Joseph W Salvage Jr."],
  ["95a1764c-5f04-50ee-b8f3-bde8c4d23d2e", "Angelo Salvaggio"],
  ["5135c99b-1499-5290-8a4f-44659b851b43", "Steve Salvaggio"],
  ["6be36a33-ee64-56d7-899b-632850e6cd45", "Daniel Salvatore"],
  ["a185c56d-2977-50ae-a42c-146735d20660", "Joseph C Salvatore"],
  ["c4d43b04-a1bd-55f0-849d-d07da55b7020", "Arlotta Salvatre"],
  ["f0ac1de0-6ef1-5616-b890-5ee918f342f9", "Faling K Salvesek"],
] as const;

test("Batch 834 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Edgar Salinger keeps civic and translation evidence separate from an immediate employer", async ({ page }) => {
  await page.goto("./people/b4e4aef1-383c-525b-88e9-0d84530fe068/");
  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("Naval Secret Service, Information Office");
  await expect(earlier).toContainText("Japanese-language translator");
  await expect(earlier).toContainText("Good Neighbor Committee");
  await expect(earlier).toContainText("sponsor");
  await expect(earlier).toContainText("medium");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("No reviewed claim currently meets the publication threshold");
});

test("Richard Salomon publishes both 1939 professorships without choosing an immediate predecessor", async ({ page }) => {
  await page.goto("./people/7f39bd25-1be6-5f10-b07b-9fdad6b3df7f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("Kenyon College");
  await expect(earlier).toContainText("professor of medieval history");
  await expect(earlier).toContainText("Bexley Hall Seminary");
  await expect(earlier).toContainText("professor of church history");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("No reviewed claim currently meets the publication threshold");
});

test("Saltzstein and Salvage show evidence-bounded wartime identities", async ({ page }) => {
  await page.goto("./people/4743bc08-0a71-5ae0-aa3f-afce72404b4b/");
  let main = page.locator("main");
  await expect(main).toContainText("Detachment 101");
  await expect(main).toContainText("Markoto Iwamatsu");
  await expect(main).not.toContainText("American Business Press", { useInnerText: true });

  await page.goto("./people/9ae95c99-0ca8-5830-b97e-39b7c9ef530a/");
  main = page.locator("main");
  await expect(main).toContainText("258th Field Artillery");
  await expect(main).toContainText("temporal relation uncertain");
  const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
    .locator("xpath=following-sibling::dd[1]").allTextContents();
  for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
});

test("Army name conflicts stay visible without publishing candidate biographies", async ({ page }) => {
  const conflicts = [
    "95a1764c-5f04-50ee-b8f3-bde8c4d23d2e",
    "5135c99b-1499-5290-8a4f-44659b851b43",
    "a185c56d-2977-50ae-a42c-146735d20660",
    "f0ac1de0-6ef1-5616-b890-5ee918f342f9",
  ];
  for (const id of conflicts) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("materially different name");
    await expect(main).toContainText("Box 673");
    await expect(main).not.toContainText(/PIRGA JOHN|GRADOWSKI CHESTER|LORER ROBERT|SALVESEN ERLING/);
  }
});
