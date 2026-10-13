import { expect, test } from "@playwright/test";

const profiles = [
  ["8df57701-4baa-5052-87e1-3c74af989025", "Albert V Pilone"],
  ["fade327b-5162-5805-921f-5ac2294349ef", "Alwyn C Pinder"],
  ["955e4af3-f2bf-5449-8f48-f00cd9a6d0a8", "David Pinkney"],
  ["5c308447-027b-5717-95ca-1bb1f6c19c34", "Donald R Pipin"],
  ["d6c276df-c282-52e9-8794-d4c5d93f872c", "Dora B Pinkney"],
  ["9f85ef13-ec3d-5232-8605-7e95dc466cde", "Eleftherios Pipinias"],
  ["c5ffdbd5-3131-5e62-bb08-e79d171886c8", "Ernest M Pinson"],
  ["a944066a-7018-50ca-94f4-042952e40924", "Frank B Pinkerton"],
  ["5fd19abe-4b18-5a44-b848-6bf04fec7aba", "Frederick D Pingree"],
  ["d08b7583-eb82-5227-98d9-072e6810f8b3", "George T Pinson"],
  ["204e85b3-d6b0-51a9-88a0-5c5fe585005b", "Gero K Piper"],
  ["f16b69c7-f65d-56e5-9d2f-2cc9b13f6038", "Herbert S Piper"],
  ["edca8612-ad0e-5993-9a09-e1a6b39c2c25", "Irwin N Pincus"],
  ["337e7248-628f-53f4-8ef8-a90b68f0e363", "John Pintar"],
  ["8bbbe4a9-cbe7-593e-89f2-20969fe6af37", "John S Pinover"],
  ["085062bf-62b7-5d7c-bf9c-08394a76c72c", "Mildred I Pinkney"],
  ["4f98c0ae-2fc1-5846-a59a-63b4cd880c6f", "Roberta H Pinkney"],
  ["5227a5e9-bf74-5fbf-8bf5-dc7c9eba66c6", "Wladyslaw Piotrowski"],
] as const;

test("Batch 759 publishes all 18 page-370 profiles with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 759 publishes Pincus's immediate BEW assignment without calling it a civilian employer", async ({
  page,
}) => {
  await page.goto("./people/edca8612-ad0e-5993-9a09-e1a6b39c2c25/");
  const main = page.locator("main");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("Board of Economic Warfare");
  await expect(immediate).toContainText("government assignment");
  await expect(immediate).toContainText("explicit immediate");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "Board of Economic Warfare",
  );
  await expect(main).toContainText("The Secrets War: The Office of Strategic Services in World War II");
});

test("Batch 759 qualifies Pinkney's Harvard student affiliation and probable identity", async ({
  page,
}) => {
  await page.goto("./people/955e4af3-f2bf-5449-8f48-f00cd9a6d0a8/");
  const main = page.locator("main");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Harvard University");
  await expect(earlier).toContainText("doctoral student");
  await expect(earlier).toContainText("medium");
  await expect(main).toContainText("probable");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "Harvard University",
  );
  await expect(main).toContainText("Guide to the Sherman Kent Papers");
});

test("Batch 759 preserves Pipinias's uncertain Army-to-OSS chronology", async ({ page }) => {
  await page.goto("./people/9f85ef13-ec3d-5232-8605-7e95dc466cde/");
  const main = page.locator("main");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Company C, 87th Infantry Regiment");
  await expect(earlier).toContainText("military assignment");
  await expect(earlier).toContainText("temporal relation uncertain");
  await expect(main).toContainText("needs temporal review");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "87th Infantry",
  );
  await expect(main).toContainText("OSS Missions, SOE, Train Sabotage, Katerini, Tsirmulas");
});

test("home page exposes the rebuilt Batch 759 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,480");
  await expect(home).toContainText("43.78%");
  await expect(home).toContainText("13,454");
  await expect(home).toContainText("779");
  await expect(home).toContainText("345");
  await expect(home).toContainText("8,939");
});
