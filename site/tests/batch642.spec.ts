import { expect, test } from "@playwright/test";

test("Batch 642 publishes five high-confidence identity outcomes without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["116fc97e-96d1-5f5c-b97d-6e282c1e01d8", "James A McLaughlin"],
    ["c3e47113-2f34-5958-8f4f-2915a2e0ee16", "John J McLaughlin"],
    ["0f00812f-801f-5820-bc02-a7ca47e9931f", "Ellis R McLuckie"],
    ["f69ec40e-d619-5c5d-bb6e-ec35e0240443", "James A McLuskey"],
    ["151f290a-b097-5a8f-b7cf-c7faf214b293", "Robert F McMahon"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("protected identifier");
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("Batch 642 exposes the Gene J McLaughlin first-name conflict", async ({ page }) => {
  await page.goto("./people/169b969d-d244-5b28-bf73-4452b6bc2b35/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Gene J McLaughlin", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Jean J. McLaughlin");
  await expect(main).toContainText("Box 510");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(
    page.locator(".index-record dl > div").filter({ hasText: "Serial" }).locator("dd"),
  ).toHaveText(/^••••\w{4}$/);
  await expect(main).toContainText("the number is withheld from public output");
});

test("Batch 642 qualifies the probable Francis B McLeod identity", async ({ page }) => {
  await page.goto("./people/4f1b0b55-f38c-5dd0-a0d1-4ad44a3b2268/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Francis B McLeod", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("unexplained trailing text");
  await expect(main).toContainText("Box 510");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 642 preserves two John J McLaughlin source rows and rejects namesake occupations", async ({
  page,
}) => {
  await page.goto("./people/c3e47113-2f34-5958-8f4f-2915a2e0ee16/");
  await expect(page.locator(".index-record")).toHaveCount(2);
  await expect(page.locator("main")).toContainText("two printed John J. McLaughlin rows");

  const excludedProfiles = [
    ["116fc97e-96d1-5f5c-b97d-6e282c1e01d8", ["Harvard Law professor", "Major James F"]],
    ["c3e47113-2f34-5958-8f4f-2915a2e0ee16", ["Chicago political", "John R. McLaughlin"]],
  ];
  for (const [personId, excludedTerms] of excludedProfiles) {
    await page.goto(`./people/${personId}/`);
    const body = await page.locator("main").innerText();
    for (const term of excludedTerms) expect(body).not.toContain(term);
  }
});

test("Batch 642 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,876");
  await expect(page.locator("body")).toContainText("32.90%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".page-hero .lede")).toContainText("9 historically named oil");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McLaughlin");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McLeod");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McMahon");
});
