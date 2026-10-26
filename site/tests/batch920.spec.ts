import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page450-isabel-stokes-to-franklin-stone-review_batch-920_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["bf4437e8-a3fb-5387-b289-c9e27e117b4e", "Isabel Stokes"],
  ["12343f77-a18b-559d-864b-71cc57d115c4", "James W Stokes"],
  ["33413cb8-c61e-56e2-81e7-5e2e8a613240", "James K Stokes"],
  ["1d94cda6-a735-5a4a-9047-27a27013cc61", "James R Stokes"],
  ["3e179fd6-e6a9-5bf2-b1ca-5997e5df0300", "Robert Stokes"],
  ["b98dfab5-e0d0-51d7-b9ce-3696abcc8827", "Alice O Stolb"],
  ["041c3b88-ce0b-5a7c-bbac-bfbc68000c0a", "Robert F Stolb"],
  ["f47a9347-c428-512a-8421-04b72a6e8fc2", "John A Stolba"],
  ["3f95a78f-89c6-59d5-8120-f97cef7d50c2", "Samuel J Stolin"],
  ["1e2adc0f-26d5-5033-992f-828b60315c18", "Carrol J Stoll"],
  ["fd99bf74-21d1-5158-87bf-5f1f007d2ac1", "Carl Stolle"],
  ["ef6b0129-32d4-5866-90f7-0758bc48a640", "Norman E Stoller"],
  ["b97f6b08-7810-5cd3-b4e3-b6c0138ac4c6", "Edwin R Stolp"],
  ["67c66b5e-b4f4-59cd-bab9-62be1163b616", "George W Stolte"],
  ["3988ba42-de0b-58ed-9d67-87122d344b2d", "William J Stolte"],
  ["acf22eae-f5a0-50fd-b211-edbcccb657f7", "Thomas Stonborough"],
  ["5dc90dbe-8b7b-5fa5-8a11-96e0f50480b3", "Bruce D Stone"],
  ["f3851d6e-3d61-5083-9420-e249e5569012", "Charlotte B Stone"],
  ["92e75949-e907-5931-b0c7-1dfe8c5141cc", "Edward A Stone"],
  ["c1173b12-5447-565c-b347-429b4d680b14", "Everett L Stone"],
  ["ae7a9be2-be83-544b-853c-7e8b43b6272e", "Frank D Stone"],
  ["368971b6-e196-56dc-be2d-d22ae72978a6", "Frank D Stone"],
  ["18c19532-d243-5e0a-982e-6a79be33cce2", "Franklin M Stone"],
] as const;

test("Batch 920 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Thomas Stonborough separates the immediate OPA assignment from prior self-employment", async ({ page }) => {
  await page.goto("./people/acf22eae-f5a0-50fd-b211-edbcccb657f7/");
  const main = page.locator("main");
  await expect(main).toContainText("Research Director, Cleveland area");
  await expect(main).toContainText("Office of Price Administration");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("his own market research business");
  await expect(main).toContainText("last documented civilian work");
  await expect(main).toContainText("government assignment");
});

test("Samuel Stolin publishes the direct OSS identity evidence without inventing an employer", async ({ page }) => {
  await page.goto("./people/3f95a78f-89c6-59d5-8120-f97cef7d50c2/");
  const main = page.locator("main");
  await expect(main).toContainText("M/Sgt Samuel J. Stolin — Approved");
  await expect(main).toContainText("Stock clerks");
  await expect(main).toContainText("no employer is identified");
  await expect(main).toContainText("occupation only found");
});

test("James K Stokes keeps the middle-initial conflict visible and transfers no Army occupation", async ({ page }) => {
  await page.goto("./people/33413cb8-c61e-56e2-81e7-5e2e8a613240/");
  const main = page.locator("main");
  await expect(main).toContainText("James E Stokes");
  await expect(main).toContainText("middle-initial conflict");
  await expect(main).toContainText("conflicting sources");
  await expect(main).not.toContainText("Actors and actresses");
});

test("the two Frank D Stone rows remain separate and the undefined code is withheld", async ({ page }) => {
  await page.goto("./people/ae7a9be2-be83-544b-853c-7e8b43b6272e/");
  await expect(page.locator("main")).toContainText("first of two adjacent");
  await expect(page.locator("main")).toContainText("different protected identifier");

  await page.goto("./people/368971b6-e196-56dc-be2d-d22ae72978a6/");
  const second = page.locator("main");
  await expect(second).toContainText("second indexed Frank D Stone row");
  await expect(second).toContainText("remains separate");
  await expect(second).toContainText("occupation code 993 is undefined");
  await expect(second).toContainText("is not interpreted");
});

test("Batch 920 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 920 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 618,
    research_attempted_people: 14_109,
    verified_affiliation_people: 1_004,
    verified_employer_people: 452,
    archival_review_assessed_people: 12_582,
    published_claims: 8_646,
    public_sources: 5_742,
  });
});
