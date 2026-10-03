import { expect, test } from "@playwright/test";

const profiles = [
  ["4e138276-9338-583d-b498-571536a8f5e8", "Ralph A Minton"],
  ["31f6ebd2-443a-59c0-ad8a-af3ba158f1bc", "George Mintz"],
  ["a19af16c-f851-58c5-94df-7d23d64e548d", "Harry C Minutillo"],
  ["883ddddb-2868-581a-8ac0-3ef3307ca6ce", "Louis A Mion"],
  ["04c1f2f6-439d-5a63-9742-b88bfc4cd26f", "Paul J Miramont"],
  ["4d97ccbc-5dab-59ce-b51e-2cb135679956", "Felix A Mirando"],
  ["bae35893-fb80-5e5a-8b90-fc925f78289c", "Samuel Mirasole"],
  ["42442c07-efbd-5d5f-b9bb-7e374c5eca37", "Walter J Mirbach"],
  ["82b71620-81d3-550c-8a01-d9d125e3f869", "Peter G Mirkine"],
  ["a2269e9f-6745-59e7-becb-bac2797e3c11", "Nicholas Mirkovich"],
  ["2986fc02-64a9-5b62-9f1e-f604de69c629", "Miguel A Miro"],
  ["abd43721-2a28-5124-8111-fc81fc50f575", "Bohus Miroslav"],
  ["0e5f39d2-9b8c-577a-ae34-cbbe24fa76d2", "Edward F Mischler"],
  ["81291414-d10e-511d-8d35-5fe375668928", "Walter P Mischuk"],
  ["db125755-a752-5e9c-8d23-327bb39b3641", "Harvey N Misenheimer"],
  ["d13e3e3a-2946-50c0-ae88-29e8422d7d53", "Bernard Mishkin"],
  ["e8165e89-3754-52a0-aa51-fee93715d41a", "Harold Mishkin"],
  ["9cbe983f-80a4-591c-8cfb-4c6f795d35cb", "Peter M Mishopoulos"],
  ["571a4df1-8679-5cbf-90af-850893f7586d", "Sylvester C Missal"],
  ["cc0ce485-96f7-5f20-a49d-2cae971cf87e", "Joseph W Missenda"],
  ["aeb8485b-7027-591a-bf65-bf3ab0754475", "Andrew S Mitchell II"],
  ["ae1773d9-f552-5d42-831a-0ca7d10b41ff", "Barbara B Mitchell"],
] as const;

test("Batch 665 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 665 qualifies Nicholas Mirkovich's last civilian government affiliation", async ({ page }) => {
  await page.goto("./people/a2269e9f-6745-59e7-becb-bac2797e3c11/");
  const main = page.locator("main");

  await expect(main).toContainText("Yugoslav Government Office of Reconstruction");
  await expect(main).toContainText("Technical editor and reconstruction economist");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("medium strongly date bounded");
  await expect(main).not.toContainText("explicit immediate");
});

test("Batch 665 keeps Bernard Mishkin's contracting employer distinct from his museum role", async ({ page }) => {
  await page.goto("./people/d13e3e3a-2946-50c0-ae88-29e8422d7d53/");
  const main = page.locator("main");

  await expect(main).toContainText("Committee for Inter-American Artistic and Intellectual Relations");
  await expect(main).toContainText("Museo Nacional del Perú");
  await expect(main).toContainText("Visiting Curator");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("one-year contract");
});

test("Batch 665 resolves Bohus Miroslav's cover name without inventing an immediate employer", async ({ page }) => {
  await page.goto("./people/abd43721-2a28-5124-8111-fc81fc50f575/");
  const main = page.locator("main");

  await expect(main).toContainText("Bedřich Neumann");
  await expect(main).toContainText("Bohuš Miroslav");
  await expect(main).toContainText("career Czechoslovak military officer and general");
  await expect(main).not.toContainText("agrarian bank");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 665 publishes Sylvester Missal's occupation but no guessed medical employer", async ({ page }) => {
  await page.goto("./people/571a4df1-8679-5cbf-90af-850893f7586d/");
  const main = page.locator("main");

  await expect(main).toContainText("otolaryngologist");
  await expect(main).toContainText("May 1942");
  await expect(main).toContainText("first OSS chief surgeon");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 665 preserves all three identifier conflicts", async ({ page }) => {
  const conflicts = [
    ["4e138276-9338-583d-b498-571536a8f5e8", "Ralph A. Monton"],
    ["a19af16c-f851-58c5-94df-7d23d64e548d", "Harry C. Menutile"],
    ["9cbe983f-80a4-591c-8cfb-4c6f795d35cb", "Peter M. Moshopoulos"],
  ] as const;

  for (const [id, conflictingName] of conflicts) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Evidence conflicts");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 665 excludes Samuel Mirasole's postwar brewery work from pre-OSS employment", async ({ page }) => {
  await page.goto("./people/bae35893-fb80-5e5a-8b90-fc925f78289c/");
  const main = page.locator("main");

  await expect(main).toContainText("Salvatore Mirasole");
  await expect(main).toContainText("Sam Mirasole");
  await expect(main).toContainText("Eighth Army Detachment");
  await expect(main).not.toContainText("Pittsburgh Brewing");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 665 updates exact coverage and retains the oil-company category at the top", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,380");
  await expect(page.locator("body")).toContainText("35.01%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(category).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
