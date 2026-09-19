import { expect, test } from "@playwright/test";

const reviewedPeople = [
  ["a5ecef68-b8c1-5727-a4c5-0fcb9d233aea", "John B Deull"],
  ["827318f1-fe04-5175-a8f1-9d055c52c5b5", "Sol nmi Deull"],
  ["086eb6e9-de8d-5e24-a899-44f7d1b17c95", "Edna Deut"],
  ["09679737-4509-5894-b52d-0f0d53fcdb43", "Dorothea J Deuth"],
  ["e37c4af1-356b-5f33-b85d-a419024d1ba1", "Janet M Deutsch"],
  ["1965da78-0a8c-57d9-bc43-94e5ea174c08", "William C Deutsch"],
  ["5367ee17-f511-5aae-9b9a-bbeb3619ac21", "Catherine DeVaney"],
  ["932d3a12-6d03-5ae9-88c3-a4cd4ae18b12", "Francis A Devautor"],
  ["6dc15970-6935-57bf-8086-351c4c9ba10e", "Hector F DeVega"],
] as const;

test("batch 575 profiles preserve separate files and unresolved employers", async ({ page }) => {
  for (const [personId, name] of reviewedPeople) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.getByText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
      { exact: true },
    ).first()).toBeVisible();
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  }
});

test("Catherine DeVaney lead is qualified and does not publish undated jobs", async ({ page }) => {
  await page.goto("./people/5367ee17-f511-5aae-9b9a-bbeb3619ac21/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText(/may be Catherine Devaney Wallace/).first()).toBeVisible();
  await expect(page.getByRole("link", { name: /Catherine Devaney Wallace, 87/i }).first()).toHaveAttribute(
    "href",
    "https://dailyvoice.com/article/catherine-devaney-wallace-87-longtime-fairfield-resident/",
  );
  await expect(page.getByText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.", { exact: true }).first()).toBeVisible();
});

test("Army identity links do not become employer claims", async ({ page }) => {
  for (const personId of [
    "1965da78-0a8c-57d9-bc43-94e5ea174c08",
    "6dc15970-6935-57bf-8086-351c4c9ba10e",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" }).first()).toHaveAttribute(
      "href",
      "https://catalog.archives.gov/id/1263923",
    );
    await expect(page.getByText("No reviewed claim currently meets the publication threshold.").first()).toBeVisible();
  }
});
