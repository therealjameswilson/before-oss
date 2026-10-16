import { expect, test } from "@playwright/test";

const profiles = [
  ["8b00a8bf-06e8-5d13-bfb3-5e503155f05e", "William W Selvig"],
  ["a3f4d0d6-d47f-5c05-9534-a161d6edae5e", "Peter H Selz"],
  ["1ad7c019-7110-572b-be27-61b077db5e6b", "Mary Semack"],
  ["287d7392-923f-5771-9313-322ba7ae9601", "Hercules J Sembrakis"],
  ["6644490c-c6cc-5a0c-b9a7-648708dc9940", "Amato A Semenza"],
  ["ea91f7b4-6ab5-5fc9-82ab-87d349e929ae", "Agnes T Semin"],
  ["ef76ba64-93f1-54e9-a07c-00c6f37f4b01", "Antonino J Seminara"],
  ["b19e86ea-78c0-5a49-85b6-b90266f818fd", "Mario V Semolich"],
  ["75fa7167-7df8-5652-944f-28adcbb41447", "Alfonso A Senatore"],
  ["9b037098-2111-54a1-a760-140777af3727", "Frank J Senft"],
  ["4952675d-3a32-51c5-b277-2625b1424f39", "Lester L Seng"],
  ["bf499088-fd5b-5477-89f1-c89b6d45c2e8", "Frederick A Senger"],
  ["23053618-2802-5aea-919d-f880c541a495", "Helen L Senger"],
  ["1d5fc83d-1efa-53c8-a422-8294b3f81ebc", "Royal F Sengstacken"],
  ["4a0f3a90-594a-54ad-b985-54b84837552d", "Edward Senior"],
  ["54721347-6e74-5d58-8cd5-4819096220fc", "Faith A Senior"],
  ["a3360a71-3c34-5b98-9537-352a5ee63d4d", "Louis P Senser"],
  ["43af9a53-69eb-56e0-8c94-f23a249d1016", "John W Senter"],
  ["95eadc40-348c-5c56-843f-7faf55ac57f6", "Amos E Sentman"],
  ["e2235ca9-9c0f-56b3-9632-879090812f40", "Sylvester J Sepanski"],
  ["91e9885d-1c34-5ebb-b2ac-301874767c87", "August V Sepetauc"],
  ["35064936-f3ed-5d82-82e4-964a2f5aca50", "Toshiye A Sera"],
  ["33e639b5-6c5c-5dc2-a464-7785c6688be3", "Anthony Serao"],
] as const;

test("Batch 859 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Peter Selz's Columbia record remains student status, not employment", async ({ page }) => {
  await page.goto("./people/a3f4d0d6-d47f-5c05-9534-a161d6edae5e/");
  const main = page.locator("main");
  await expect(main).toContainText("Peter Howard Selz");
  await expect(main).toContainText("Columbia University");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Last civilian employer before serviceColumbia University");
});

test("Mario Semolich publishes Palmer House only as the last civilian employer", async ({ page }) => {
  await page.goto("./people/b19e86ea-78c0-5a49-85b6-b90266f818fd/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Last civilian employer before servicePalmer House");
  await expect(main).toContainText("Cook");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("OSS board of officers report on arrival at Naples");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationPalmer House");
});

test("Amos Sentman keeps Regular Army service distinct from civilian employment", async ({ page }) => {
  await page.goto("./people/95eadc40-348c-5c56-843f-7faf55ac57f6/");
  const main = page.locator("main");
  await expect(main).toContainText("Immediate pre-OSS affiliationUnited States Army");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceUnited States Army");
});

test("Semenza and Sembrakis publish service context without invented employers", async ({ page }) => {
  await page.goto("./people/6644490c-c6cc-5a0c-b9a7-648708dc9940/");
  const semenza = page.locator("main");
  await expect(semenza).toContainText("32d Signal Center Team");
  await expect(semenza).toContainText("Psychological Warfare Branch");
  await expect(semenza).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/287d7392-923f-5771-9313-322ba7ae9601/");
  const sembrakis = page.locator("main");
  await expect(sembrakis).toContainText("Greek Operational Group II");
  await expect(sembrakis).toContainText("enlisted army personnel");
  await expect(sembrakis).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Army crosswalk variants remain transparent and identity-only", async ({ page }) => {
  await page.goto("./people/9b037098-2111-54a1-a760-140777af3727/");
  const senft = page.locator("main");
  await expect(senft).toContainText("Frank J. Senfft");
  await expect(senft).toContainText("Identity statushigh confidence");
  await expect(senft).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/1d5fc83d-1efa-53c8-a422-8294b3f81ebc/");
  const sengstacken = page.locator("main");
  await expect(sengstacken).toContainText("Royal F. Sengstacken, Jr.");
  await expect(sengstacken).toContainText("Electronic Army Serial Number Merged File");
  await expect(sengstacken).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("The unfamiliar Senter rank stays verbatim and indeterminate", async ({ page }) => {
  await page.goto("./people/43af9a53-69eb-56e0-8c94-f23a249d1016/");
  const main = page.locator("main");
  await expect(main).toContainText("Rank or gradeCAMDR");
  await expect(main).toContainText("unknown or indeterminate");
  await expect(main).toContainText("without forced normalization");
});
