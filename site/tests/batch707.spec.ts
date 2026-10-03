import { expect, test } from "@playwright/test";

const profiles = [
  ["8ba86d4c-00cc-5263-b823-f365799eafe5", "Joseph L Noel"],
  ["f6c1446e-855b-5b62-9a5e-53792995ffea", "Lillian B Noel"],
  ["5218d214-65f2-5607-9bc7-b84a5a92baf7", "Joe P Nogay"],
  ["b0f7f12e-25ad-5da5-9389-3f7c12110f11", "Isamu Noguchi"],
  ["5e01ae2f-2d63-5634-8fb9-f43eda00ae93", "Oscar D Nohowel"],
  ["5005fe20-7b5e-5355-bdc4-cc2890983ed4", "Joseph Noia"],
  ["8920cfe0-702d-51ab-9c6f-53fe44806b9d", "Loren A Nolan"],
  ["5d460def-ae6d-565f-ba3f-9b5c3274e2ea", "Paul F Nolan"],
  ["14be7197-7473-5160-b849-67b57fd33fe9", "Richard G Nolan"],
  ["e5c2afce-3fe5-5bb8-ae19-610e4f2af2c2", "Thomas A Nolan"],
  ["3e272e85-b9e4-5f40-a41b-fc87d9e8dec4", "William F Nolan"],
  ["f42c8170-3cdd-59c3-b0d2-9a6cd55a2bff", "Arta Nolino"],
  ["9db533b1-1af8-57da-9cba-58f9e9f2c09a", "Charles G Nollet"],
  ["56babc37-f23c-5acf-a6d4-41660c2e3566", "Lily T Noma"],
  ["1d3a4e7e-777f-53c2-931b-838c3027ae37", "Orestes M Nomico"],
  ["de852308-ea01-54de-a884-6fda90aeb125", "Yasuichi T Nomura"],
  ["fdfbe47d-e6f2-586f-8531-bc20b919cf6a", "Louis A Nonni"],
  ["36b9cc03-ba69-5bff-84a5-c687afef49b6", "Henry P Nooe"],
  ["530e97e1-5064-5991-9728-e2463facf1e7", "Ruth P Noon"],
  ["6347cc85-a409-5edf-a111-7fb463e038ab", "Sait Noor"],
  ["c570507a-6c15-5375-ae1a-c10d09290ca6", "John N Norback"],
  ["bc89fa80-c0f9-5b1e-907d-51cd4f0bb25a", "Theodore M Norbeck"],
  ["2e0332d5-9e4e-5de9-be57-0432aaddb434", "Charles R Norberg"],
] as const;

test("Batch 707 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{5,8}$/);
  }
});

test("Batch 707 qualifies Isamu Noguchi rather than promoting a famous-name match", async ({ page }) => {
  await page.goto("./people/b0f7f12e-25ad-5da5-9389-3f7c12110f11/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("Sculptor and artist");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("do not establish his OSS accession");
  await expect(main).not.toContainText("confirmed match");
});

test("Batch 707 identifies Joseph Noia without inventing a pre-OSS employer", async ({ page }) => {
  await page.goto("./people/5005fe20-7b5e-5355-bdc4-cc2890983ed4/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Chicago II and Ginny I");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 707 preserves both protected-identifier name conflicts", async ({ page }) => {
  await page.goto("./people/5e01ae2f-2d63-5634-8fb9-f43eda00ae93/");
  await expect(page.locator("main")).toContainText("Oscar D Nohowell");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");

  await page.goto("./people/c570507a-6c15-5375-ae1a-c10d09290ca6/");
  await expect(page.locator("main")).toContainText("John N Morback");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
});

test("Batch 707 publishes Charles Norberg's employer only as a qualified probable match", async ({ page }) => {
  await page.goto("./people/2e0332d5-9e4e-5de9-be57-0432aaddb434/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Charles Robert Norberg");
  await expect(main).toContainText("Hepburn and Norris");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("medium");
});

test("Batch 707 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,300");
  await expect(main).toContainText("38.85%");
  await expect(main).toContainText("320");
  await expect(main).toContainText("14,634");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
