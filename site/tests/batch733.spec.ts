import { expect, test } from "@playwright/test";

const profiles = [
  ["b56adc90-31ed-54fc-8183-e0a71c1bcbb7", "Charles A Papouschek"],
  ["dc88a935-db79-5e2b-b38a-79936682efb7", "Charles S Pappageorge"],
  ["47aa016e-343b-5fc2-9c96-7bfa2f31cb75", "George L Pappageorge"],
  ["da80029d-8d84-505d-b3fd-e0113b276a51", "Lazar Pappapostoli"],
  ["956dcebc-4bcd-5515-9af8-64f419282839", "Angelo Pappas"],
  ["3d1df980-a0b8-5357-a738-0a075219107e", "Anthony G Pappas"],
  ["454e193b-d221-53fe-8680-6fbe12c0dd9a", "George J Pappas"],
  ["63986759-1000-5747-849c-bceafe0c8262", "Nicholas G Pappas"],
  ["4baabb08-9065-51f1-8eb8-3b8a6b38c2ea", "Sallie Pappas"],
  ["7cba064b-ea8c-5caf-b620-f4fce4ce8834", "Spiro V Pappas"],
  ["8e506640-20e4-5b9c-aecf-0660bc1d3bee", "Zeff Pappas"],
  ["1a35569e-6795-5b67-abba-cd6ef2e8f355", "Frixos P Pappitsas"],
  ["4d01f2a7-7ee9-55a8-8459-a9c9cf0a1ea8", "Roland A Papucci"],
  ["29d31886-9a65-59aa-9ac0-962025abd028", "Stephen F Papula"],
  ["88de4be2-b6c6-5025-836a-0297f16642d9", "Maxwell J Papurt"],
  ["4b78ea5c-88c9-5267-aef3-ae9c230532f7", "Georgia K Papworth"],
  ["eec203c0-aac5-5375-b59c-2bd9b5a17f04", "Alice T Paquette"],
  ["dfd0689a-204e-583a-bfa8-de72896fb728", "Gaston J Paquette"],
  ["be621a4d-8360-5f87-85e1-d1bc4ab98d5e", "Joseph R Paquette"],
  ["2f9e6403-eef7-5475-92b3-8ea6d4bfd558", "Jean L Pardimene"],
  ["2d7f7afa-cc8d-55c6-93dd-c04ec24eaecd", "Gastone Pardo"],
  ["401f4fbf-3495-5820-a409-a53862d5c2ee", "Joseph A Pare"],
  ["4e45762e-bf38-51f4-b77d-15548af0f11c", "Jean P Parent"],
] as const;

test("Batch 733 publishes all 23 page-357 profiles with terminal dispositions", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 733 qualifies the Pappas 122nd Battalion pathways as military assignments", async ({ page }) => {
  for (const [id, name] of [
    ["454e193b-d221-53fe-8680-6fbe12c0dd9a", "George J Pappas"],
    ["63986759-1000-5747-849c-bceafe0c8262", "Nicholas G Pappas"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const immediate = page.locator("section[aria-labelledby='immediate-affiliation']");
    await expect(immediate).toContainText("122nd Infantry Battalion (Separate)");
    await expect(immediate).toContainText("military assignment");
    await expect(immediate).toContainText("probable immediate");
    await expect(immediate).toContainText("medium");
    const civilian = page.locator("section[aria-labelledby='civilian-employer']");
    await expect(civilian).not.toContainText("122nd Infantry Battalion");
  }
});

test("Batch 733 separates Papurt's documented prewar jobs from both predecessor questions", async ({ page }) => {
  await page.goto("./people/88de4be2-b6c6-5025-836a-0297f16642d9/");
  await expect(page.getByRole("heading", { name: "Maxwell J Papurt", level: 1 })).toBeVisible();

  const immediate = page.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(immediate).not.toContainText("Pride of Judea");

  const civilian = page.locator("section[aria-labelledby='civilian-employer']");
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(civilian).toContainText("earlier documented employment appears below");
  await expect(civilian).not.toContainText("New York State Department of Correction");

  const earlier = page.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Pride of Judea Children's Home");
  await expect(earlier).toContainText("Executive director");
  await expect(earlier).toContainText("New York State Department of Correction");
  await expect(earlier).toContainText("Chief psychologist");
  await expect(earlier).toContainText("documented pre-OSS");
  await expect(page.locator("main")).toContainText("The Jewish Herald, December 26, 1941");
});

test("Batch 733 preserves the Pappageorge identifier conflict without merging", async ({ page }) => {
  for (const [id, name, other] of [
    ["dc88a935-db79-5e2b-b38a-79936682efb7", "Charles S Pappageorge", "George L Pappageorge"],
    ["47aa016e-343b-5fc2-9c96-7bfa2f31cb75", "George L Pappageorge", "Charles S Pappageorge"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(other);
    await expect(main).toContainText("remain separate");
    await expect(main).toContainText("Box 584");
  }
});

test("Batch 733 keeps Pardimene and Pardo as qualified identity leads without affiliations", async ({ page }) => {
  for (const [id, name, clue] of [
    ["2f9e6403-eef7-5475-92b3-8ea6d4bfd558", "Jean L Pardimene", "Jean Lucien Pardimene"],
    ["2d7f7afa-cc8d-55c6-93dd-c04ec24eaecd", "Gastone Pardo", "Italian archival and naval sources"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("probable");
    await expect(main).toContainText(clue);
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
    await expect(page.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator("section[aria-labelledby='earlier-affiliations']")).toHaveCount(0);
  }
});

test("Batch 733 rebuilds exact coverage and adds one verified employer and affiliation", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,895");
  await expect(main).toContainText("41.33%");
  await expect(main).toContainText("14,039");
  await expect(main).toContainText("744");
  await expect(main).toContainText("334");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
