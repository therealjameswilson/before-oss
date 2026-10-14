import { expect, test } from "@playwright/test";

const profiles = [
  ["7c345fd0-8854-58b0-be02-9abc1820bc68", "Harold J Regan"],
  ["91986635-1332-5303-bdc6-bfa6ac8165be", "John Regan"],
  ["128c4bf3-4a08-50fb-86c3-80722067bc46", "Raymond Regan"],
  ["aaaf3179-6333-576e-bf35-0874adfa4f14", "Thomas J Regan"],
  ["a79994a5-ae78-50e2-873b-385d3cea8aad", "William C Regan"],
  ["ca0d73fb-6dc2-5dbd-ba5b-e5eece9e41d6", "John G Regler"],
  ["f8033812-c8db-5940-adc9-d2dc19aec748", "Lucien J Rego"],
  ["ba2432a5-f9f4-5254-91d4-ba17547db4ff", "Andrew J Regusis"],
  ["3ffd4f7a-6f58-5b59-b56f-236f89b8f396", "Alexander S Rehak"],
  ["7b551401-01da-5756-aa3f-ab02688049a9", "Hans J Rehfisch"],
  ["9589662e-56c9-5786-85d5-95268598d8f7", "Louis S Rehm"],
  ["582c5166-cba9-58cc-89f2-f5a019fef845", "Madison P Rehm"],
  ["fd719ab0-0e3d-56dd-b163-810da257da6e", "William L Rehm"],
  ["77cb05b5-8ee3-539e-8ffa-6ec5f25908d3", "Harry V Rehmann"],
  ["a59ae766-2d28-5dff-947b-6728cf326899", "Mildred F Rehn"],
  ["e0789330-1331-5682-b91c-c946abdd3059", "Edward T Reichelt"],
  ["eed63d2a-26ca-54b8-a29a-23bfef469261", "Jack Reichenstein"],
  ["7f493876-3b11-5f18-aaa1-29b976d98f30", "William L Reichle"],
  ["5a86222d-e75a-574b-8323-29676add395c", "Felix Reichman"],
  ["298ecfb4-2ea0-5a8a-9390-3d986c4f5b6d", "Edward M Reichmuth"],
  ["a13e330f-5f63-585f-b7a1-dd43246c0f0a", "Phoebe L Reichner"],
  ["03c79bc4-7211-5943-9f95-d8ccd7c07739", "Andrew G Reid Jr."],
  ["fa88792b-8d6a-5313-9035-f10758deb2c8", "Gordon S Reid"],
] as const;

const officialIdentityProfiles = [
  "aaaf3179-6333-576e-bf35-0874adfa4f14",
  "f8033812-c8db-5940-adc9-d2dc19aec748",
  "ba2432a5-f9f4-5254-91d4-ba17547db4ff",
  "7f493876-3b11-5f18-aaa1-29b976d98f30",
] as const;

test("Batch 794 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 794 publishes four official identity claims without inventing employers", async ({ page }) => {
  for (const id of officialIdentityProfiles) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Official Army bulk data supports a high-confidence identification");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Rehfisch publishes documented BBC work without overstating immediacy", async ({ page }) => {
  await page.goto("./people/7b551401-01da-5756-aa3f-ab02688049a9/");
  const main = page.locator("main");
  await expect(main).toContainText("Hans José Rehfisch");
  await expect(main).toContainText("British Broadcasting Corporation");
  await expect(main).toContainText("documented prewar");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Reichmann publishes the civilian-to-Army-to-OSS sequence with citations", async ({ page }) => {
  await page.goto("./people/5a86222d-e75a-574b-8323-29676add395c/");
  const main = page.locator("main");
  await expect(main).toContainText("Felix Reichmann");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "United States Army",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Carl Schurz Memorial Foundation",
  );
  await expect(main).toContainText("Landis Valley Museum");
  await expect(main).toContainText("Alois Reichmann Buchhandlung und Antiquariat");
  await expect(main).toContainText("Felix Reichmann (1899-1987)");
  await expect(main).toContainText("The Hobby That Became a Museum");
});

test("Batch 794 keeps Army-name conflicts explicit and employer-free", async ({ page }) => {
  for (const id of [
    "128c4bf3-4a08-50fb-86c3-80722067bc46",
    "eed63d2a-26ca-54b8-a29a-23bfef469261",
    "03c79bc4-7211-5943-9f95-d8ccd7c07739",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("conflict");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("home page exposes the rebuilt Batch 794 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,255");
  await expect(home).toContainText("47.02%");
  await expect(home).toContainText("12,679");
  await expect(home).toContainText("810");
  await expect(home).toContainText("364");
  await expect(home).toContainText("9,716");
});
