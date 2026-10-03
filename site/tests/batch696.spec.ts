import { expect, test } from "@playwright/test";

const profiles = [
  ["f2a52e16-1d6e-54a6-8fa2-eb96e5e20b4a", "Glenn R Naylor"],
  ["a7776225-998d-5b9d-b633-0218225a6f45", "Herman E Naylor Jr."],
  ["615be030-45cb-5e4e-bd05-384eb6be6a72", "Jack R Naylor"],
  ["953e0b72-a366-5e9b-a522-e2358ebad297", "Josephine Naymark"],
  ["19f8bb65-757b-5e1b-a770-cfbc692d26da", "John Nazzarro"],
  ["4f4039a7-98bc-5827-9717-29df82ec42b1", "John Neague"],
  ["09dce15a-18b4-5be1-af85-af76283ab03d", "Frederick W Neal"],
  ["bbcd511a-8abc-5bd3-90d7-499aa78d4f80", "Gerald M Neal"],
  ["6cc606fd-59f0-5cd4-b768-df4bdd843c40", "Robert L Neal"],
  ["09656fd2-7b61-5012-9937-3e0d4aea9d4d", "Rosamond F Neale"],
  ["b833f3e8-61cb-57b6-8454-7c95abf2e666", "Robert D Neasse"],
  ["43bdd995-7dc6-5f86-93e7-b00aa021a5af", "Charles F Neave"],
  ["2d48c61a-a90c-5162-b128-fb9bb1aa634f", "Harry M Neben"],
  ["86dabb55-2802-50e0-b757-15e0c2449b2b", "Paul Nebenzahl"],
  ["3e9e5d4e-ebf5-5a72-bb31-9cc6113075aa", "N L Necci"],
  ["5aab8322-ad5f-549c-8b2c-635594d5632c", "Joseph Nechunskas"],
  ["0870df1c-b52c-57a0-8a41-74cfae8f517a", "William F Necker"],
  ["831717c4-a725-5e6e-a8ae-52f3d22b1d8a", "Martin E Nedell"],
  ["68f546e8-b27c-58dc-8cfe-63175faafe20", "William F Nee"],
  ["dd00b616-c69b-5de4-8d30-01cca2f2ed2c", "Dean B Needham"],
  ["bca3667c-9b5d-5863-81c3-6fd049970294", "Adam M Neely"],
  ["04571977-7055-5dce-ac46-d26cc1e15fad", "Anna R Neely"],
  ["7515c24f-0dbd-5374-9891-7b30bdfff58a", "Charles R Neff"],
] as const;

test("Batch 696 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 696 separates Robert Neasse's Army pathway from student status", async ({ page }) => {
  await page.goto("./people/b833f3e8-61cb-57b6-8454-7c95abf2e666/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Robert Dunham Neasse");

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("Enlisted soldier; later on detached service with OSS");
  await expect(immediate).toContainText("explicit immediate");

  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier).toContainText("Ohio Wesleyan University");
  await expect(earlier).toContainText("Student");
  await expect(earlier).toContainText("student");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 696 publishes Charles Neave's 1916 post only as earlier military service", async ({ page }) => {
  await page.goto("./people/43bdd995-7dc6-5f86-93e7-b00aa021a5af/");
  const main = page.locator("main");
  await expect(main).toContainText("Battery B, Yale University");
  await expect(main).toContainText("First lieutenant");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("earlier context only");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 696 publishes Harry Neben as occupation-only without inventing an employer", async ({ page }) => {
  await page.goto("./people/2d48c61a-a90c-5162-b128-fb9bb1aa634f/");
  const main = page.locator("main");
  await expect(main).toContainText("amateur radio operator");
  await expect(main).toContainText("W9QB");
  await expect(main).toContainText("occupation only found");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 696 preserves qualified and conflicting identities", async ({ page }) => {
  await page.goto("./people/831717c4-a725-5e6e-a8ae-52f3d22b1d8a/");
  await expect(page.locator("main")).toContainText("Identity statusprobable");
  await expect(page.locator("main")).toContainText("probable match");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/bca3667c-9b5d-5863-81c3-6fd049970294/");
  const conflict = page.locator("main");
  await expect(conflict).toContainText("Identity statusconflicting");
  await expect(conflict).toContainText("Evidence conflict");
  await expect(conflict).toContainText("surname and Private grade conflict");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 696 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("9,052");
  await expect(body).toContainText("37.81%");
  await expect(body).toContainText("317");
  await expect(body).toContainText("14,882");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
