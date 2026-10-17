import { expect, test } from "@playwright/test";

const profiles = [
  ["cae43044-a42a-58a1-9c1b-93ca0ffcff95", "George Shaskan"],
  ["1d656791-ba1b-52c8-bc1a-54484fd9e2f1", "J P Shatto"],
  ["02e35fee-2439-5b0e-97c0-3a1cc7bfb009", "Betty T Shattuck"],
  ["23b1b518-38ee-54a7-8d13-fe9ebc39ba76", "Victor C Shattuck"],
  ["22e88dab-70a4-54b4-b3bc-c3cd769a7d0e", "James F Shaughnessy"],
  ["4ff773fd-a30c-5cfb-a4a8-d547ce99d7ad", "Michael Q Shaughnessy"],
  ["f2d1aa07-15a6-5a01-bedb-461608820e23", "Nathan Shaul"],
  ["a6928b2b-b0b5-5f4e-a6a0-da705a944761", "Robert S Shaul"],
  ["48e08cb7-9350-5cb0-a6f3-c41c7f29eda5", "William H Shaul"],
  ["dcdeab11-47b7-5a6a-bfbb-28f8f8d4e416", "William H Shaul"],
  ["fe7bcaa3-9190-5d57-9aaa-3e911cec95f4", "George R Shaver"],
  ["932832b3-0fc7-5def-afe3-b9c50607e318", "Talmage C Shaver"],
  ["a8835691-c4e7-5367-907c-0864b8b13d0b", "Wanda Shaver"],
  ["38f509ac-ab7c-552b-94ed-5f65907afc26", "Cautley N Shaw"],
  ["9da865a8-4d0e-539b-85df-e5d5af74db33", "Constance C Shaw"],
  ["ef5fb5b9-1595-513f-80a6-534c42957fec", "David C Shaw"],
  ["39255270-4900-5402-96ec-9951281c177a", "Earl B Shaw"],
  ["be3a1960-ebfb-5813-a316-5f8e00e5baab", "Ernest B Shaw"],
  ["642cbbf3-b6f3-5464-a9d5-ff0a3a92feb2", "Gustavus W Shaw"],
  ["52d3f9e1-d439-5635-96e2-2625602d51b7", "Lyman A Shaw"],
  ["cc2dfa22-5df8-5f17-bdf4-17b336ac4c7a", "Phyllis Shaw"],
  ["04e2bebb-7a11-5a52-ac1a-5ba253fa84f0", "Richard H Shaw"],
  ["39327f4a-b965-551f-8616-a11525a6d358", "Robert J Shaw"],
] as const;

test("Batch 864 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Cautley Shaw publishes a prewar RAF assignment without calling it civilian employment", async ({ page }) => {
  await page.goto("./people/38f509ac-ab7c-552b-94ed-5f65907afc26/");
  const main = page.locator("main");
  await expect(main).toContainText("Cautley Nasmyth Shaw");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Royal Air Force Special Reserve");
  await expect(main).toContainText("Pilot Officer; honorary Flying Officer");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("not a civilian employer");
  await expect(main).not.toContainText("Last civilian employer before serviceRoyal Air Force Special Reserve");
});

test("Lyman Shaw is confirmed by a protected-number bridge without publishing the number", async ({ page }) => {
  await page.goto("./people/52d3f9e1-d439-5635-96e2-2625602d51b7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Appointment Number 94");
  await expect(main).toContainText("postwar identity evidence only");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("0141123");
  await expect(main).not.toContainText("141123");
});

test("the two William H Shaul rows remain separate and visibly unresolved", async ({ page }) => {
  await page.goto("./people/48e08cb7-9350-5cb0-a6f3-c41c7f29eda5/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Kline William H");
  await expect(main).toContainText("Compare both William H. Shaul files");

  await page.goto("./people/dcdeab11-47b7-5a6a-bfbb-28f8f8d4e416/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("spacing defect");
  await expect(main).toContainText("Distinct protected identifiers");
});

test("Batch 864 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 576,
    research_attempted_people: 12_840,
    verified_affiliation_people: 933,
    verified_employer_people: 423,
    archival_review_assessed_people: 11_307,
    published_claims: 7_764,
    public_sources: 5_303,
  });
});
