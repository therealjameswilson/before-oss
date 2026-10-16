import { expect, test } from "@playwright/test";

const profiles = [
  ["0269169c-187b-5c88-9300-e686736d97a2", "Charles A Sanchez"],
  ["bd26f2dd-1c58-5ee8-8233-b83a16833939", "Erie Y Sanchiomi"],
  ["61632266-2fe7-5c30-9cf8-60ba519916a0", "Robert J Sander"],
  ["7960001e-a6d2-53c6-80ac-dea560886991", "Ann P Sanders"],
  ["808debd3-bd4c-5cee-bbff-de1eec54cf6d", "Dale Sanders"],
  ["79a1e6e7-ad15-5939-a898-30ea59536924", "Emily D Sanders"],
  ["5eba0412-f37c-58c1-b6d5-c06db6cf1087", "John L Sanders"],
  ["78fad053-306a-5fed-abdb-3ca3aad6e255", "Joseph J Sanders Jr."],
  ["8818ff9a-4aeb-53ca-853c-49656ebd29f4", "Leo Sanders"],
  ["6ecfca62-4188-5535-b621-fcc8b7b927ae", "Robert H Sanders"],
  ["375e5eb1-e052-51c8-a2c7-2c7d42f40af4", "David E Sanderson"],
  ["d8fe0655-d9f1-5e7b-a88a-5dacbdaf767d", "Elizabeth D Sanderson"],
  ["78285d97-7c32-50d7-bfe9-d3cf4b5171f2", "Fred M Sanderson"],
  ["30503700-fc7a-5eb2-a1c3-99bca185265a", "Kenneth D Sandmire"],
  ["9582770b-b66a-541b-b5f1-4b39f14de879", "Nichol M Sandoe Jr."],
  ["3e7c1490-b788-5b0e-a0e1-c0d7d85a7111", "Ralph W Sandoz"],
  ["8b9ea5f9-8585-5365-91c0-bcb385544476", "Clemens M Sandresky"],
  ["0ee2acbe-8511-5ef1-a71a-35434b7bc46a", "C Sands"],
  ["73d98a8d-53c8-554b-b18d-2dd68761e669", "Oliver J Sands Jr."],
  ["39fb321c-1602-5623-9a51-5e6743a04c00", "John H Sandstrom"],
  ["50a4493d-6872-581d-960f-7c0dd4c2b614", "Ole B Sandtory"],
  ["b8af8923-5852-51c3-9e7d-0fb9cff22650", "Arthur A Sandusky"],
  ["ab12c454-0bf1-5730-a4bd-c4b03b690a69", "Elizabeth R Sanford"],
] as const;

test("Batch 836 publishes all 23 profiles with reviewed outcomes and masked identifiers", async ({ page }) => {
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

test("Nichol Sandoe publishes Dartmouth student status as immediate affiliation, not employment", async ({ page }) => {
  await page.goto("./people/9582770b-b66a-541b-b5f1-4b39f14de879/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("Dartmouth College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("explicit immediate");
  await expect(main).not.toContainText("Dartmouth College employed");
});

test("Clemens Sandresky preserves the initial conflict and publishes the Army training pathway", async ({ page }) => {
  await page.goto("./people/8b9ea5f9-8585-5365-91c0-bcb385544476/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Clemens Harold Sandresky");
  await expect(main).toContainText("middle initial M");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("Fort Bragg");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("Princeton University");
  await expect(main).toContainText("military assignment");
  await expect(main).not.toContainText("Princeton University employed");
});

test("accepted Army crosswalks publish identity only and keep protected fields private", async ({ page }) => {
  for (const id of [
    "61632266-2fe7-5c30-9cf8-60ba519916a0",
    "6ecfca62-4188-5535-b621-fcc8b7b927ae",
    "50a4493d-6872-581d-960f-7c0dd4c2b614",
  ]) {
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
    "8818ff9a-4aeb-53ca-853c-49656ebd29f4",
    "39fb321c-1602-5623-9a51-5e6743a04c00",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("Oliver Sands remains ambiguous and receives no bank or railroad employer", async ({ page }) => {
  await page.goto("./people/73d98a8d-53c8-554b-b18d-2dd68761e669/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("candidate biography is not assigned");
  await expect(main).not.toContainText(/American National Bank|Richmond-Ashland Railway/);
});
