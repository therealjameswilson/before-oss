import { expect, test } from "@playwright/test";

const profiles = [
  ["a57f5d23-394c-55b0-a72d-9c71a40e5cf4", "Warren E Nash"],
  ["2952dd85-0890-5a46-bd28-44e368baa1cc", "John Nasht"],
  ["6bc9829d-e9a7-5caa-8f8f-39f7c91973e8", "Albert Nasi"],
  ["4b502024-57a5-5436-af34-d6e151c26653", "Leonard H Nason"],
  ["4ef2a8d0-a247-5caf-8b0d-60a8dd840f38", "Thomas N Nassoor"],
  ["29b90326-fb38-578d-880a-a8a16647cc96", "Angeline R Nastri"],
  ["61935eb4-7590-58ca-8ab7-e4f517ccbf3b", "Orlando P Nastri"],
  ["fb3aee64-7cdb-5ffa-98f7-f54d03a3ee63", "Richard Natali"],
  ["32939645-0f3e-5f5a-bc8d-47196b611f85", "Dora C Natalie"],
  ["70b422fe-e186-5174-a8dd-974376d6b5ed", "Jean M Nater"],
  ["546d96f6-a6bf-5cf2-b2c7-78c4e28bf06d", "Robert R Nathan"],
  ["790de038-6517-5258-ac2f-1369ee1d6832", "Irwin M Nathanson"],
  ["cd2f2921-f2db-587d-a227-3a67d0330d1f", "Arthur R Natho"],
  ["9a6b2139-8a25-58a5-81b6-5d11775e0253", "Blanche L Nations"],
  ["73bffb53-ed69-5fff-8c4a-528f69a8db44", "Malia G Natirbov"],
  ["ab892b0e-f69f-59c1-ac63-68bac3cf8572", "Anthony E Natoli"],
  ["cd8d3271-842a-56d8-bbf5-99fe1417a6eb", "James K Naughan"],
  ["2456e76e-12d5-5b5f-a401-4e5343b5dbff", "Lambro J Naumoff"],
  ["14dedda5-0981-5e15-85ac-0b963ca0b3a3", "Charles J Naura"],
  ["2bb10033-1c66-53cc-8c22-f465a0085b9d", "John F Navarro"],
  ["ff4946de-eb63-544b-bdb1-6f1dc34ce6ee", "Santos C Navarro"],
  ["8017c448-fd40-53d7-8219-2db12234443e", "Frank Navellou"],
  ["83126492-c5c5-5c71-8a34-ff794a770143", "Walter T Nawrocki"],
] as const;

test("Batch 695 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{7,8}$/);
  }
});

test("Batch 695 separates Robert Nathan's Army pathway from his last civilian government assignment", async ({ page }) => {
  await page.goto("./people/546d96f6-a6bf-5cf2-b2c7-78c4e28bf06d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Robert R. Nathan");

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("Enlisted soldier assigned to OSS");
  await expect(immediate).toContainText("explicit immediate");

  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(lastCivilian).toContainText("U.S. War Production Board");
  await expect(lastCivilian).toContainText("Chairman, Planning Committee");
  await expect(lastCivilian).toContainText("strongly date bounded");
  await expect(main.locator('a[href="https://www.trumanlibrary.gov/library/oral-histories/nathanrr"]')).toHaveCount(3);
});

test("Batch 695 publishes Leonard Nason's Mutual Broadcasting work only as documented prewar employment", async ({ page }) => {
  await page.goto("./people/4b502024-57a5-5436-af34-d6e151c26653/");
  const main = page.locator("main");
  await expect(main).toContainText("Leonard Hastings Nason");
  await expect(main).toContainText("Leonard 'Steamer' Nason");
  await expect(main).toContainText("Mutual Broadcasting System");
  await expect(main).toContainText("Military analyst");
  await expect(main).toContainText("documented prewar");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 695 keeps Malia Natirbov qualified and leaves her employer unresolved", async ({ page }) => {
  await page.goto("./people/73bffb53-ed69-5fff-8c4a-528f69a8db44/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Malia Giurey Natirbov");
  await expect(main).toContainText("probably");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 695 exposes the Naughan and Navellou identity conflicts without assigning employers", async ({ page }) => {
  for (const id of [
    "cd8d3271-842a-56d8-bbf5-99fe1417a6eb",
    "8017c448-fd40-53d7-8219-2db12234443e",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("Evidence conflict");
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Batch 695 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("9,029");
  await expect(body).toContainText("37.72%");
  await expect(body).toContainText("317");
  await expect(body).toContainText("14,905");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
