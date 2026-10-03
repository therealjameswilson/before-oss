import { expect, test } from "@playwright/test";

const profiles = [
  ["8d2a5d03-1fee-56b6-ac65-7b37fc2ad4a9", "Ira F Moyer"],
  ["097505ab-f9bf-5b6e-b46e-70b4f762e85c", "Jean S Moyer"],
  ["2cde4c85-fdfb-51e3-952b-3e41936b7e82", "Robert E Moyers"],
  ["4c6c9226-ee23-5495-86b7-a243d0f7c0af", "Carl J Moyes"],
  ["4112ee89-4033-5796-ae89-fbfde292160c", "Dorothy M Moyingan"],
  ["3b57a04f-be7a-5ef5-8c6d-60b520279b21", "James F Moyles"],
  ["ce3d5638-dd08-52ff-9aed-ccb0df456f61", "John F Moynahan"],
  ["63d07db5-bb39-5fb1-8896-b68368dd1f9c", "Mary A Moynihan"],
  ["86cdc1f7-8192-57de-bca4-646d304e6e53", "Harold Mrazik"],
  ["6fcd9148-101e-50d1-9e52-bd0e923d7c50", "Ante Mrgudic"],
  ["fe57effa-33fe-5580-94bc-1629480b3ea0", "Edmund A Mroz"],
  ["8bc523c2-4398-540a-80e7-c3b2b9f6214a", "Edward J Mroziz"],
  ["5b5bc21d-663b-5d5d-aa4a-92515f7ea052", "Frank F Mucciolo"],
  ["04fa92bc-c768-5cc6-9e30-1f9cb602e187", "Gordon M Muchow"],
  ["3580a495-bbf3-5d2e-b944-3f9919f9a98c", "William L Mudge"],
  ["6a5e2362-2735-5827-bb05-c260ee3811f7", "Nick Mudrick"],
  ["25f368d5-5c3d-557b-8232-ed273228bb77", "Rudolph Mudrick"],
  ["77a91f87-d964-5b36-8551-8485a4abe22e", "Daniel Mudrinich"],
  ["7676dc93-1f36-53d3-a933-75a780af4a22", "Charles A Mueke"],
  ["0fcf7ed2-ff6e-5fbf-a726-91994f1827a1", "Arnold W Mueller"],
  ["1be1d747-0174-50cf-8d82-0ed3cdbca465", "Charles K Mueller"],
  ["524c5bcf-977d-5be4-968d-00414525479b", "Elizabeth Mueller"],
  ["2ba38dd8-0464-5835-84ee-4726f563e8ad", "Erna L Mueller"],
] as const;

test("Batch 685 publishes all 23 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 333");
    await expect(page.locator("main")).toContainText("Archive box");
  }
});

test("Batch 685 publishes Robert Moyers's Army Dental Corps pathway without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/2cde4c85-fdfb-51e3-952b-3e41936b7e82/");
  const main = page.locator("main");
  await expect(main).toContainText("Robert Edison Moyers");
  await expect(main).toContainText("United States Army Dental Corps");
  await expect(main).toContainText("Army dentist assigned to Cairo");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("University of Iowa");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 685 keeps John Moynahan's student history separate from his unresolved wartime sequence", async ({ page }) => {
  await page.goto("./people/ce3d5638-dd08-52ff-9aed-ccb0df456f61/");
  const main = page.locator("main");
  await expect(main).toContainText("John Francis Moynahan");
  await expect(main).toContainText("Boston College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Army Air Forces");
});

test("Batch 685 publishes Daniel Mudrinich's explicit Camp Roberts pathway", async ({ page }) => {
  await page.goto("./people/77a91f87-d964-5b36-8551-8485a4abe22e/");
  const main = page.locator("main");
  await expect(main).toContainText("Infantry Replacement Training Center, Camp Roberts");
  await expect(main).toContainText("Second lieutenant");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 685 preserves both identifier-name conflicts without exposing full identifiers", async ({ page }) => {
  const conflicts = [
    ["8d2a5d03-1fee-56b6-ac65-7b37fc2ad4a9", "Ira F Moyer", "Edward M Malachowski"],
    ["25f368d5-5c3d-557b-8232-ed273228bb77", "Rudolph Mudrick", "Rudolph Murdirk"],
  ] as const;

  for (const [id, indexed, variant] of conflicts) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(indexed);
    await expect(main).toContainText(variant);
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 685 publishes six bounded Army identities without employer claims", async ({ page }) => {
  for (const id of [
    "4c6c9226-ee23-5495-86b7-a243d0f7c0af",
    "5b5bc21d-663b-5d5d-aa4a-92515f7ea052",
    "04fa92bc-c768-5cc6-9e30-1f9cb602e187",
    "6a5e2362-2735-5827-bb05-c260ee3811f7",
    "0fcf7ed2-ff6e-5fbf-a726-91994f1827a1",
    "1be1d747-0174-50cf-8d82-0ed3cdbca465",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 685 keeps the oil-company category at nine cited people", async ({ page }) => {
  await page.goto("./");
  const homeCategory = page.locator("#oil-companies");
  await expect(homeCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(homeCategory).toContainText("11 historically named oil companies");
  await expect(homeCategory).toContainText("John A Mowinckel");
});

test("Batch 685 updates exact coverage counts", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,804");
  await expect(body).toContainText("36.78%");
  await expect(body).toContainText("308");
  await expect(body).toContainText("15,130");
});
