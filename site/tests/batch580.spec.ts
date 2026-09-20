import { expect, test } from "@playwright/test";

const cohort = [
  ["bb2f7687-e088-5ab7-9bb8-6b74a5899f4f", "John E Deyoung"],
  ["e3f6b1ff-70df-51f9-b771-c60b55c6d9b8", "Louis A Dezman"],
  ["322aa2f1-ff7d-566d-b961-ed2126809a4c", "Serge A Diab"],
  ["91c597f7-5760-527d-9995-f29749e13b3b", "John G Dial Jr."],
  ["b3b06374-696f-596d-82fc-ac7161ebaab1", "Spyros Dialismas"],
  ["577cd1dd-ed29-546c-bcd3-14bd7f303752", "Paul Diamantoukos"],
  ["88b7db00-ec3c-5822-ab44-ba858591e816", "Pavlos Diamantoukos"],
  ["47d9cccc-5ca5-58fd-a893-04ffeeee54be", "Goodhue Diament"],
  ["330b0c5e-6c4a-5f75-8a64-4720405e59db", "Melvin Diamond"],
  ["eadd095b-3044-5a40-9c61-9f7b6ef1e45c", "Damon Diamondes"],
] as const;

test("batch 580 preserves ten separate, terminal archival-review profiles", async ({ page }) => {
  for (const [id, name] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("Box 185", { exact: false }).first()).toBeVisible();
    await expect(page.getByText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
      { exact: true },
    ).first()).toBeVisible();
  }
});

test("official identity bridges do not become invented employers", async ({ page }) => {
  for (const id of [cohort[2][0], cohort[4][0], cohort[7][0]]) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" }).first()).toBeVisible();
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  }
  await page.goto(`./people/${cohort[7][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByRole("link", { name: "Office of Strategic Services Mission to France: Award of Unit Certificate of Merit" })).toBeVisible();
});

test("John de Young candidate stays qualified and student status stays private", async ({ page }) => {
  await page.goto(`./people/${cohort[0][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByText(/plausible but unconfirmed match/)).toBeVisible();
  await expect(page.getByRole("link", { name: "John E. de Young" })).toBeVisible();
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate.getByText("No reviewed claim currently meets the publication threshold.")).toBeVisible();
  await expect(immediate.locator(".affiliation-card")).toHaveCount(0);
});

test("Paul and Pavlos remain distinct with visible conflict", async ({ page }) => {
  await page.goto(`./people/${cohort[5][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByText(/Army entry shares the indexed Paul Diamantoukos identifier but names Pavlos/)).toBeVisible();
  await expect(page.getByText("conflicting", { exact: true }).first()).toBeVisible();
  await page.goto(`./people/${cohort[6][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.getByText(/distinct unnumbered index row adjacent to Paul/)).toBeVisible();
});
