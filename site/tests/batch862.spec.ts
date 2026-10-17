import { expect, test } from "@playwright/test";

const profiles = [
  ["784a1c62-71df-5afc-94b3-b81addd310ef", "Eugene Shaffer"],
  ["0df81f04-2ef6-5723-b1da-7f786cf0d170", "Robert B Shaffer"],
  ["e8093cf6-4291-5ba6-be14-b4902a9b57c9", "Theodore F Shaffer"],
  ["0b309106-37b8-5ede-9fe2-c3d756d7b8f3", "Paula Shaffran"],
  ["b6417ee7-eb7e-594a-a1e2-f4d54205020f", "Janet D Shafroth"],
  ["c8ed2783-9177-526e-969c-33b714aff89f", "John M Shaheen"],
  ["45493348-dec8-5369-a1f0-fccdab47b9f2", "Clara K Shaina"],
  ["e2bd3b59-fadb-5c82-818b-8efad3647345", "Joseph S Shalett"],
  ["31437b87-a645-5618-9b6f-e18a2831d029", "Lawrence B Shallcross"],
  ["64d3cdba-67bc-5ab5-8aab-7ed2bdaaef6c", "Robert B Shallenberger"],
  ["611d1247-25fe-5f2a-a750-6808cbfccda2", "Donald D Shallow"],
  ["30ff4d70-e345-5910-82d9-ee648278fe5f", "George H Shambos"],
  ["d443d3fe-4959-55ee-8cdf-d8b8d58c53c6", "Muddassir A Shamsee"],
  ["1a9d14b5-41d0-5967-93a0-7d924fdcadf8", "Alice Shanahan"],
  ["85e8fc30-b1f0-5d42-917e-6dd555b897a3", "John J Shanahan"],
  ["2a3560b3-bd56-5fe6-8c2b-4399366223a1", "Robert J Shane"],
  ["80a07897-7004-51d9-97a0-794782756bad", "Murray Shanfeld"],
  ["525b3570-6305-59d4-8e17-70a1c50356ee", "Julius L Shanker"],
  ["ecd8c0dd-c004-54b5-8aab-2ed6c7622dea", "Julius A Shanker"],
  ["e140a8ad-6e89-5530-b9cb-cfa8f20c84fe", "Bascom M Shanks"],
  ["d8febdf1-a0ec-5f07-9a0f-52d6b514a5fb", "Sam Shanley"],
  ["4ba5072f-f292-5093-8858-b2deee248d2c", "Jack T Shannon"],
  ["4265680b-f798-5829-9c46-f39442b54a74", "John A Shannon"],
] as const;

test("Batch 862 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("John Shaheen publishes the prewar publicity affiliation without recasting postwar oil work", async ({ page }) => {
  await page.goto("./people/c8ed2783-9177-526e-969c-33b714aff89f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Illinois Republican Party");
  await expect(main).toContainText("publicity director");
  await expect(main).toContainText("not as a government job or oil-company role");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Lawrence Shallcross uses the official mission record only for identity", async ({ page }) => {
  await page.goto("./people/31437b87-a645-5618-9b6f-e18a2831d029/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("OSS Mission to France");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceCentral Intelligence Agency");
});

test("Muddassir Shamsee keeps the postwar UN record as qualified identity context", async ({ page }) => {
  await page.goto("./people/d443d3fe-4959-55ee-8cdf-d8b8d58c53c6/");
  const main = page.locator("main");
  await expect(main).toContainText("Muddassir Ali Shamsee");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("postwar identity context only");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationUnited Nations");
});

test("Jack Shannon displays only a qualified Army-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/4ba5072f-f292-5093-8858-b2deee248d2c/");
  const main = page.locator("main");
  await expect(main).toContainText("Jack T. 'Black Jack' Shannon");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Immediate pre-OSS affiliationUnited States Army");
  await expect(main).toContainText("Lieutenant");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Army identity bridges preserve discrepancies and do not merge adjacent Shanker rows", async ({ page }) => {
  await page.goto("./people/85e8fc30-b1f0-5d42-917e-6dd555b897a3/");
  const shanahan = page.locator("main");
  await expect(shanahan).toContainText("Shanhan John J");
  await expect(shanahan).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/525b3570-6305-59d4-8e17-70a1c50356ee/");
  const juliusL = page.locator("main");
  await expect(juliusL).toContainText("Identity statushigh confidence");

  await page.goto("./people/ecd8c0dd-c004-54b5-8aab-2ed6c7622dea/");
  const juliusA = page.locator("main");
  await expect(juliusA).toContainText("Identity statusunresolved");
  await expect(juliusA).toContainText(
    "initials and identifiers differ; no evidence supports merging Julius A. Shanker",
  );
});
