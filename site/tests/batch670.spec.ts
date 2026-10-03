import { expect, test } from "@playwright/test";

const profiles = [
  ["3d7aa2b0-3614-5bc5-9a66-69e8645d76e2", "Barbara R Monroe"],
  ["e0baf64d-9d00-54ec-ad19-b2261ecb1949", "Donald B Monroe"],
  ["f6fbd2d0-f087-5897-8890-9031572ac577", "Donald K Monroe"],
  ["12cb28b4-7531-5a39-ac81-c5318c8ec28e", "John J Monroe"],
  ["c08acd42-5748-5e0b-9514-7a7508d10957", "John N Monroe"],
  ["56e3f06e-4604-5b76-b4a5-dc2693dc47be", "Ralph W Monroe"],
  ["b891418b-1710-5233-9fce-9736e5063ee4", "Anna H Monson"],
  ["f07c28d4-7ca1-58f5-87fe-f250f522584a", "Catello J Montagna"],
  ["8b9d2e94-a29c-5580-a34a-657b76655e80", "Frances V Montague"],
  ["29d7a4a6-0cc2-53d8-ae5d-33bac98d1e58", "Margaret E Montague"],
  ["c25fb0c4-388e-5daf-9774-25d7b5bb6fbb", "Payne D Montague"],
  ["48306801-649b-5578-aed0-b4f8fcc3477a", "Vanni B Montana"],
  ["6d389967-922a-5f5f-a11a-0317fd1ec588", "Charles P Montanard"],
  ["b01357ae-5977-5dda-82fa-ac8de238ffa9", "Dan C Montanell"],
  ["a98d712d-7451-5c55-96bd-8a06597878f8", "James Montante"],
  ["2324a26e-b350-5ff2-a44f-3a4031e280e2", "Hobart C Montee"],
  ["6df21429-4fea-508d-b19d-121a77b59aee", "Ernest M Montefalco"],
  ["801f79ea-fa99-5201-9626-1758829933d9", "Frank Monteleone"],
  ["9a18df77-f73a-5935-86ad-3c27da554689", "Nicholas A Montesano"],
  ["7e8e4319-a3d3-5613-a1c7-5eb97d566d05", "Frederick S Montgomery"],
  ["f3315603-2352-5982-b762-c90381e0eaca", "Henry I Montgomery"],
  ["2dc32dd2-4124-5470-9c31-7fe64bfbb9f7", "Hugh Montgomery"],
] as const;

test("Batch 670 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 670 publishes James Montante's self-employed legal practice without inventing a firm", async ({ page }) => {
  await page.goto("./people/a98d712d-7451-5c55-96bd-8a06597878f8/");
  const main = page.locator("main");
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');

  await expect(lastCivilian).toContainText("Self-employed");
  await expect(lastCivilian).toContainText("his law practice");
  await expect(lastCivilian).toContainText("Attorney in private practice");
  await expect(lastCivilian).toContainText("Detroit");
  await expect(lastCivilian).toContainText("strongly date bounded");
  await expect(main).toContainText("James Montante Seeks Judgeship");
  await expect(main).toContainText("Montante Announced A Circuit Judge Favorite At Election");
  await expect(main).toContainText("no firm is inferred");
  await expect(main).not.toContainText("Montante &");
});

test("Batch 670 qualifies Hobart Montee's United Press work as documented prewar", async ({ page }) => {
  await page.goto("./people/2324a26e-b350-5ff2-a44f-3a4031e280e2/");
  const main = page.locator("main");

  await expect(main).toContainText("United Press");
  await expect(main).toContainText("Staff correspondent");
  await expect(main).toContainText("1939-01-25");
  await expect(main).toContainText("1940-10-06");
  await expect(main).toContainText("documented prewar");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("United Press");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("United Press");
});

test("Batch 670 keeps Frank Monteleone's Navy pathway separate from civilian employment", async ({ page }) => {
  await page.goto("./people/801f79ea-fa99-5201-9626-1758829933d9/");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');

  await expect(immediate).toContainText("United States Navy");
  await expect(immediate).toContainText("Radio operator");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("explicit immediate");
  await expect(lastCivilian).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(lastCivilian).not.toContainText("United States Navy");
  await expect(page.locator("main")).toContainText(
    "The OSS's Eighth Army Detachment in Italy: A Few Men and Their Radio",
  );
});

test("Batch 670 labels Hugh Montgomery's Harvard status as student and preserves the date conflict", async ({ page }) => {
  await page.goto("./people/2dc32dd2-4124-5470-9c31-7fe64bfbb9f7/");
  const main = page.locator("main");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');

  await expect(immediate.locator(".affiliation-card")).toHaveCount(1);
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("Airborne soldier");
  await expect(earlier.locator(".affiliation-card")).toHaveCount(1);
  await expect(earlier).toContainText("Harvard University");
  await expect(earlier).toContainText("Student");
  await expect(earlier).toContainText("1941 or 1942");
  await expect(lastCivilian).not.toContainText("Harvard University");
  await expect(lastCivilian).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main).toContainText("The History-Maker: Remembering Ambassador Montgomery");
});

test("Batch 670 publishes reviewed Army identities without deriving employers from codes", async ({ page }) => {
  const armyMatches = [
    ["f6fbd2d0-f087-5897-8890-9031572ac577", "Donald K Monroe"],
    ["6df21429-4fea-508d-b19d-121a77b59aee", "Ernest M Montefalco"],
    ["f3315603-2352-5982-b762-c90381e0eaca", "Henry I Montgomery"],
  ] as const;

  for (const [id, name] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("Batch 670 keeps identity conflicts and spelling variants visible", async ({ page }) => {
  await page.goto("./people/c08acd42-5748-5e0b-9514-7a7508d10957/");
  await expect(page.locator("main")).toContainText("John Manual");
  await expect(page.locator("main")).toContainText("protected identifier");
  await expect(page.locator("main")).toContainText("neither row is merged");
  await expect(page.locator("main")).not.toContainText("Verified employer");

  await page.goto("./people/6d389967-922a-5f5f-a11a-0317fd1ec588/");
  await expect(page.locator("main")).toContainText("Montanaro");
  await expect(page.locator("main")).toContainText("needs identity review");
  await expect(page.locator("main")).not.toContainText("Verified employer");

  await page.goto("./people/b01357ae-5977-5dda-82fa-ac8de238ffa9/");
  await expect(page.locator("main")).toContainText("Montanelli");
  await expect(page.locator("main")).toContainText("needs identity review");
  await expect(page.locator("main")).not.toContainText("Verified employer");
});

test("Batch 670 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,488");
  await expect(page.locator("body")).toContainText("35.46%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  for (const [, name] of profiles) {
    await expect(oilList).not.toContainText(name);
  }
});
