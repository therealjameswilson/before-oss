import { expect, test } from "@playwright/test";

const profiles = [
  ["f64473e1-4d95-5380-9981-c15ac3a58e7d", "Walter Sereda"],
  ["2f815af4-c7db-522d-bd5a-9d9f8c2dd161", "Anthony J Serelis"],
  ["e52fa6b3-1f56-5ff1-97b2-81f51af4a580", "William Seremitis"],
  ["ef0c87a7-c820-5071-adce-2a859f9ac59f", "Renzo Sereno"],
  ["72cffa14-7c38-586d-a02c-833e417a81bd", "Boris Sergievsky"],
  ["ddcf45b7-3436-5985-9a92-5baba0331322", "Edwin P Serian"],
  ["2b7775a0-cec5-5ba1-aad4-54cd47466678", "Alexander Serigos"],
  ["1c0361fa-6c10-52e8-b4ba-7da7a9676264", "Robert L Seriven"],
  ["6b1642a6-503e-568d-8837-a57050b1c659", "Albert Serkes"],
  ["92af53a2-0fe3-5673-a7a9-1a0369528dd2", "Edna D Serlick"],
  ["7fdebec2-a1fd-58cc-8e38-527373550cd0", "Edison C Serna"],
  ["1e49ce8b-9f99-5f9b-bc4f-2a694d0da393", "Andre Serot"],
  ["429deab6-09b7-572b-b6ce-1e54bef6b29d", "Michael Serotko"],
  ["c1298832-a511-5815-b211-cc9319e28421", "John J Sersen"],
  ["f53edf3f-c393-5b75-853c-f2c5f3da3399", "Donald P Serton"],
  ["f046ad43-c5c0-5fb5-9c2f-3ce38da14c64", "Beurt R SerVaas"],
  ["0d43d0bd-1cf6-5c6f-8a47-865b5cb193ba", "Jean A Servais"],
  ["5d4332a7-1b18-5f1a-9974-256aa42e1f30", "Harry M Servis"],
  ["8efff180-1d4a-5454-bba2-ddc2ac561540", "Raymond P Sessions"],
  ["0fea00ec-7cc8-577f-96e7-efe65877d340", "Robert D Sethian"],
  ["6ae0ebbb-1e94-5f41-b4d4-a4bfe872c833", "Frank Settipani"],
  ["797e7284-4fca-5ac7-89b0-2d0e9578f903", "Joseph J Setton"],
  ["132ec1cd-cbfe-5c34-9533-83d57d8c8bf0", "Paul D Sevcik"],
] as const;

test("Batch 860 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Renzo Sereno remains a qualified probable identity with prewar Chicago research employment", async ({ page }) => {
  await page.goto("./people/ef0c87a7-c820-5071-adce-2a859f9ac59f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("University of Chicago");
  await expect(main).toContainText("Research assistant in political science");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationUniversity of Chicago");
});

test("Boris Sergievsky keeps two employers chronological but neither immediate", async ({ page }) => {
  await page.goto("./people/72cffa14-7c38-586d-a02c-833e417a81bd/");
  const main = page.locator("main");
  await expect(main).toContainText("Sikorsky Aircraft");
  await expect(main).toContainText("Chief test pilot");
  await expect(main).toContainText("Helicopter Corporation of America");
  await expect(main).toContainText("Vice-president");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationSikorsky Aircraft");
});

test("Andre Serot is classified as an Allied officer and his French assignments stay military", async ({ page }) => {
  await page.goto("./people/1e49ce8b-9f99-5f9b-bc4f-2a694d0da393/");
  const main = page.locator("main");
  await expect(main).toContainText("André Sérot");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("French Military Intelligence Service");
  await expect(main).toContainText("French Air Force Security Service");
  await expect(main).toContainText("military assignment");
  await expect(main).not.toContainText("Last civilian employer before serviceFrench Air Force Security Service");
});

test("Beurt SerVaas publishes Shortridge as both immediate and last civilian employer", async ({ page }) => {
  await page.goto("./people/f046ad43-c5c0-5fb5-9c2f-3ce38da14c64/");
  const main = page.locator("main");
  await expect(main).toContainText("Immediate pre-OSS affiliationShortridge High School");
  await expect(main).toContainText("Last civilian employer before serviceShortridge High School");
  await expect(main).toContainText("Chemistry and Spanish teacher");
  await expect(main).toContainText("explicit immediate");
  await expect(main).not.toContainText("Last civilian employer before servicePurdue University");
});

test("Army identity bridges preserve variants and enlisted evidence without inventing employers", async ({ page }) => {
  await page.goto("./people/e52fa6b3-1f56-5ff1-97b2-81f51af4a580/");
  const seremitis = page.locator("main");
  await expect(seremitis).toContainText("William G. Seremetis");
  await expect(seremitis).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/2f815af4-c7db-522d-bd5a-9d9f8c2dd161/");
  const serelis = page.locator("main");
  await expect(serelis).toContainText("Greek-American OSS Operational Group");
  await expect(serelis).toContainText("enlisted army personnel");
  await expect(serelis).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/c1298832-a511-5815-b211-cc9319e28421/");
  const sersen = page.locator("main");
  await expect(sersen).toContainText("T/5 John J. Sersen");
  await expect(sersen).toContainText("enlisted army personnel");
  await expect(sersen).toContainText("No reliable pre-OSS employer has yet been identified");
});
