import { expect, test } from "@playwright/test";

test("Batch 640 publishes two high-confidence Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["e9ded329-c58c-5637-8bcf-26783ffe2149", "Donald E McInnis"],
    ["cab5a497-9f2c-5f8e-ac99-557fc564d797", "William T McGuire"],
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

test("Batch 640 keeps Loughlin G McHugh visibly conflicting", async ({ page }) => {
  await page.goto("./people/8d673f1d-952a-59df-8197-8404206eb0b8/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Loughlin G McHugh", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("middle initial is G in the index and F in the Army file");
  await expect(main.getByText("critical", { exact: true })).toBeVisible();
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 640 exposes the Thomas F McGuire name conflict without a full identifier", async ({
  page,
}) => {
  await page.goto("./people/74bcb75d-d0b9-54c5-9404-33d108056164/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Thomas F McGuire", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Robert N. Durbin");
  await expect(main).toContainText("Box 507");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(
    page.locator(".index-record dl > div").filter({ hasText: "Serial" }).locator("dd"),
  ).toHaveText(/^••••\d{4}$/);
  await expect(main).toContainText("the number is withheld from public output");
});

test("rejected Batch 640 namesakes and occupations stay out of public profiles", async ({
  page,
}) => {
  const profiles = [
    ["c9a01212-57dd-51e7-a539-0fcd48426344", ["Albany Herald"]],
    ["b3075200-83c5-5e59-995c-e36fcaf8969b", ["religious lecturer", "restaurant owner"]],
    ["348b62ba-10cb-58a3-8862-711b6c6ba7fb", ["stonecutters association", "Marine recruit"]],
    ["74bcb75d-d0b9-54c5-9404-33d108056164", ["Homer Laughlin", "pottery worker"]],
  ];

  for (const [personId, excludedTerms] of profiles) {
    await page.goto(`./people/${personId}/`);
    const body = await page.locator("main").innerText();
    for (const term of excludedTerms) expect(body).not.toContain(term);
  }
});

test("Batch 640 preserves the two adjacent Carolyn McIntosh rows as separate profiles", async ({
  page,
}) => {
  await page.goto("./people/ae5d6a79-fad8-57c1-9076-6d7ba2e0d892/");
  await expect(page.getByRole("heading", { name: "Carolyn S McIntosh", level: 1 })).toBeVisible();
  await expect(
    page.locator(".index-record dl > div").filter({ hasText: /^Box/ }).locator("dd"),
  ).toHaveText("508");

  await page.goto("./people/e440e796-473a-51d5-97a9-fdbcdc42b986/");
  await expect(page.getByRole("heading", { name: "Carolyn McIntosh", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("CAF-2");
  await expect(
    page.locator(".index-record dl > div").filter({ hasText: /^Box/ }).locator("dd"),
  ).toHaveText("507");
});

test("Batch 640 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,832");
  await expect(page.locator("body")).toContainText("32.72%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".page-hero .lede")).toContainText("9 historically named oil");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McGuire");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McHugh");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McInnis");
});
