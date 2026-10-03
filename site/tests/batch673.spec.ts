import { expect, test } from "@playwright/test";

const profiles = [
  ["dda0cb1c-4208-5812-8cda-0901352235e3", "Edward O Mooney"],
  ["ee554e32-3260-5c8f-8db5-13b4ef146c27", "Frank E Mooney"],
  ["de8819f1-5165-51cb-b877-7b0d4d2178c9", "Mary B Mooney"],
  ["74196584-aa24-50d4-8b2c-2481002d9b93", "Regina Mooney"],
  ["62e55e7a-2acc-56d2-b128-37fe165258b3", "Thomas F Mooney"],
  ["0ea044d8-f3d5-50de-b72e-ffaaf89cfba9", "Alex Moore"],
  ["d633583e-637d-519b-a417-0eeb7ee8305b", "Barrington Moore"],
  ["72bc62b3-a44e-5cff-83dd-6dac38b73d83", "Benjamin Moore"],
  ["8846ebb3-d0b5-5d91-be99-e80fa752456c", "Benjamin T Moore"],
  ["838fdb30-9f9f-5596-8c12-8a197426bd4b", "Bernice V Moore"],
  ["34449b8e-1495-5d88-b170-d998caa556d3", "Billy G Moore"],
  ["07a4d0e9-cf25-563d-9af0-82645c907674", "Dan T Moore"],
  ["2f63e1a1-3d58-5855-9db9-4131b60ff692", "Daniel E Moore"],
  ["03fac92b-c504-5fb0-bc63-10c3597ffb54", "Dorothy A Moore"],
  ["50ccb8f7-1f6c-5cd2-856b-e8b9039e5591", "Douglas S Moore"],
  ["d5e3661a-dda8-553c-af82-8695eba5b416", "Elizabeth S Moore"],
  ["5e1d052f-c850-5f5d-9e3e-aee2704e973e", "Elizabeth C Moore"],
  ["53cf5481-33d4-5ca9-b3ac-f6b05b641053", "Emmett E Moore"],
  ["826bda4c-5fc3-5d1d-82c7-fd0bb95a77a7", "Ernestine M Moore"],
  ["2c6339ee-40d8-5050-a399-d64878072bcb", "Eugene W Moore"],
  ["8dd59a40-775b-5d7d-9414-db4cdd22de5d", "Frank J Moore"],
  ["07b755b0-2d44-5875-9eb1-264c1274fded", "Frank W Moore"],
] as const;

test("Batch 673 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 327");
    await expect(page.locator("main")).toContainText("Archive box534");
  }
});

test("Batch 673 publishes Alex Moore's Army transfer and qualified Red Cross relationship", async ({ page }) => {
  await page.goto("./people/0ea044d8-f3d5-50de-b72e-ffaaf89cfba9/");
  const main = page.locator("main");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');

  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("Military intelligence interrogation-team officer");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("explicit immediate");
  await expect(main).toContainText("American Red Cross");
  await expect(main).toContainText("relationship remains unknown");
  await expect(main).toContainText("January 1945");
  await expect(main).toContainText("On the Trail of Nazi Counterfeiters");
  await expect(lastCivilian).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(lastCivilian).not.toContainText("American Red Cross");
});

test("Batch 673 keeps Dan Moore's overlapping federal assignments distinct", async ({ page }) => {
  await page.goto("./people/07a4d0e9-cf25-563d-9af0-82645c907674/");
  const main = page.locator("main");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');

  await expect(main).toContainText("Dan Tyler Moore Jr.");
  await expect(immediate.locator(".affiliation-card")).toHaveCount(2);
  await expect(immediate).toContainText("U.S. Securities and Exchange Commission");
  await expect(immediate).toContainText("Office of Civilian Defense");
  await expect(immediate).toContainText("government assignment");
  await expect(lastCivilian).toContainText("U.S. Securities and Exchange Commission");
  await expect(lastCivilian).toContainText("Cleveland regional administrator");
  await expect(main).toContainText("does not establish whether this or the SEC assignment ended last");
  await expect(main).toContainText("Moore, Dan Tyler, Jr.");
  await expect(main).toContainText("not a private-sector employer");
});

test("Batch 673 publishes seven protected-identifier identities without employer inference", async ({ page }) => {
  const armyMatches = [
    ["dda0cb1c-4208-5812-8cda-0901352235e3", "Edward O Mooney"],
    ["72bc62b3-a44e-5cff-83dd-6dac38b73d83", "Benjamin Moore"],
    ["8846ebb3-d0b5-5d91-be99-e80fa752456c", "Benjamin T Moore"],
    ["34449b8e-1495-5d88-b170-d998caa556d3", "Billy G Moore"],
    ["2f63e1a1-3d58-5855-9db9-4131b60ff692", "Daniel E Moore"],
    ["8dd59a40-775b-5d7d-9414-db4cdd22de5d", "Frank J Moore"],
    ["07b755b0-2d44-5875-9eb1-264c1274fded", "Frank W Moore"],
  ] as const;

  for (const [id, name] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText("occupation code 602");
    await expect(main).not.toContainText("occupation code 123");
  }
});

test("Batch 673 gives all twelve unresolved people terminal research pages", async ({ page }) => {
  const unresolved = [
    ["ee554e32-3260-5c8f-8db5-13b4ef146c27", "Frank E Mooney"],
    ["de8819f1-5165-51cb-b877-7b0d4d2178c9", "Mary B Mooney"],
    ["74196584-aa24-50d4-8b2c-2481002d9b93", "Regina Mooney"],
    ["62e55e7a-2acc-56d2-b128-37fe165258b3", "Thomas F Mooney"],
    ["838fdb30-9f9f-5596-8c12-8a197426bd4b", "Bernice V Moore"],
    ["03fac92b-c504-5fb0-bc63-10c3597ffb54", "Dorothy A Moore"],
    ["50ccb8f7-1f6c-5cd2-856b-e8b9039e5591", "Douglas S Moore"],
    ["d5e3661a-dda8-553c-af82-8695eba5b416", "Elizabeth S Moore"],
    ["5e1d052f-c850-5f5d-9e3e-aee2704e973e", "Elizabeth C Moore"],
    ["53cf5481-33d4-5ca9-b3ac-f6b05b641053", "Emmett E Moore"],
    ["826bda4c-5fc3-5d1d-82c7-fd0bb95a77a7", "Ernestine M Moore"],
    ["2c6339ee-40d8-5050-a399-d64878072bcb", "Eugene W Moore"],
  ] as const;

  for (const [id, name] of unresolved) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Archival-review priorityhigh");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 673 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,532");
  await expect(page.locator("body")).toContainText("35.64%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  for (const [, name] of profiles) {
    await expect(oilList).not.toContainText(name);
  }
});
