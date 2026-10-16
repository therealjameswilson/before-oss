import { expect, test } from "@playwright/test";

const profiles = [
  ["aaf77cba-1358-573f-aa90-92831573ab8b", "Lily Salz"],
  ["71c17aa9-0f3c-5620-8f71-0b3c93b59d95", "Ronzy N Salza"],
  ["2687df64-7ff6-5980-ba33-985005e420d5", "Rafael L Salzmann"],
  ["76fc732a-5a3b-5c74-a467-000dac06f0af", "Frances F Samagm"],
  ["a4544045-3708-5059-baa2-8f011a975b33", "Terry Samapas"],
  ["09c1fb30-c102-50ee-9b5c-496fe22ddf31", "Chris J Samardzieh"],
  ["9bbc8834-9928-55e6-87d6-9fbb64551f6a", "Stefan U Samek"],
  ["3400ad36-a817-5664-b256-2d1077bdb724", "Michael J Sammarco"],
  ["aeff27e4-b4c7-552b-97da-5fa079bd0ae2", "Sara L Sammon"],
  ["f0031e3a-8ee4-5f1c-b0da-3ac53ec0572a", "William Samolin"],
  ["a6616425-2146-5627-912b-446221892a16", "A G Sampatacacus"],
  ["f18c0b2d-5a2f-589c-8ae2-57aace9682db", "Joseph S Sample"],
  ["28c121b7-e26a-551a-88e9-5273a6a6bdb1", "Bryan T Samples"],
  ["dc6de13a-5d1a-5533-a584-8fa2565509b6", "Herbert A Sampson"],
  ["69db6017-04e8-5bf0-8e10-dc84cd78fbfb", "Paul W Sampson"],
  ["eda0022b-91d2-5cc5-9d11-4146a7292d03", "Alexander Z Samu"],
  ["c29ea6b2-2a11-5ac9-bc82-ad877cf110e2", "Richard M Samuel"],
  ["72016753-133a-5a39-909d-534def2349c5", "Nicholas Sanabria"],
  ["308720be-62f8-5fbf-83e6-4dbaec2434d8", "Albert W Sanborn"],
  ["62c66770-2afa-5349-a607-5818c2a4f3a5", "Arlene Sanborn"],
  ["4bb4e0e8-27d0-54e2-aff8-db45a36889bf", "Forrest J Sanborn"],
  ["812e0fcb-a08f-5792-ba2e-52870a416f79", "Eunice W Sanches"],
  ["b5ffc7e3-6c66-530a-b311-d25096df9c82", "Armando Sanchez"],
] as const;

test("Batch 835 publishes all 23 profiles with reviewed outcomes and masked identifiers", async ({ page }) => {
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

test("Forrest Sanborn separates confirmed identity and occupation from timing-uncertain company leads", async ({ page }) => {
  await page.goto("./people/4bb4e0e8-27d0-54e2-aff8-db45a36889bf/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("chemical engineer");
  await expect(main).toContainText("Factory Mutual");
  await expect(main).toContainText("Improved Risk Mutuals");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("medium");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("No reviewed claim currently meets the publication threshold");
});

test("accepted Army crosswalks publish identity only and keep protected fields private", async ({ page }) => {
  const accepted = [
    "3400ad36-a817-5664-b256-2d1077bdb724",
    "a6616425-2146-5627-912b-446221892a16",
    "28c121b7-e26a-551a-88e9-5273a6a6bdb1",
    "eda0022b-91d2-5cc5-9d11-4146a7292d03",
    "72016753-133a-5a39-909d-534def2349c5",
    "b5ffc7e3-6c66-530a-b311-d25096df9c82",
  ];
  for (const id of accepted) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Army occupation code");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Army name conflicts remain visible without leaking candidate names", async ({ page }) => {
  for (const id of [
    "71c17aa9-0f3c-5620-8f71-0b3c93b59d95",
    "a4544045-3708-5059-baa2-8f011a975b33",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Army occupation code");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("William Samolin's historian namesake remains unassigned", async ({ page }) => {
  await page.goto("./people/f0031e3a-8ee4-5f1c-b0da-3ac53ec0572a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("historian and professor");
  await expect(main).not.toContainText(/Columbia University|University of Hartford/);
});
