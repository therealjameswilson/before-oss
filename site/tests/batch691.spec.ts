import { expect, test } from "@playwright/test";

const profiles = [
  ["d5f49bbc-d427-5d06-ad69-4c9edceeb21c", "William T Mussaeus"],
  ["dad49528-c090-5336-9cbd-6355e1ac5a00", "Mario Mussi"],
  ["fe270e4a-68a8-5acc-a218-3dbdfd62930e", "Victor E Musso"],
  ["e1f1695d-814c-56a6-9bfe-f1057e50380d", "Derrecalde J Muthular"],
  ["de11daf5-4332-57e9-857e-090c5a3dfee3", "Louis Muti"],
  ["cfd56154-1a46-5efc-8e44-fc849a87b4f9", "Luigi Muti"],
  ["a3585859-2060-5f73-bc36-999f9f50cb83", "Robert H Mutrux"],
  ["4a077049-1a03-5c0e-91b3-025f92a8d9c3", "Lawrence Muurphy"],
  ["8f27f82c-90c9-5020-a84b-0c71ecf4c515", "Nicholas J Muza"],
  ["8fe05aee-396c-53e4-8c6d-070f472c1297", "Alex Muzard"],
  ["f39a144e-c60a-5ef4-a484-b6a3f4b95162", "Anthony J Muzukauskas"],
  ["214fa0cf-cbd2-53ca-b446-252e2249be94", "Alexander A Muzzey"],
  ["66bb7cc8-8111-5c50-ba6c-86506fae437b", "John C Myer"],
  ["96970f24-d37b-503f-b6eb-cf58b1b7aaf5", "Ernestine J Myerchin"],
  ["ad354250-d642-5a7a-825a-3a2881ce3523", "Chester L Myers"],
  ["69a02ee4-e5a8-59a7-b186-5a528029ceda", "Earl A Myers"],
  ["a5bb7a03-5f4e-5971-bf94-753023b91b9b", "Edwin G Myers"],
  ["725b9b7d-694f-5d0d-833b-74c833d13378", "Emily G Myers"],
  ["974cce47-ab4b-54b5-9e7a-3eeba29c97a2", "Emily L Myers"],
  ["aa216d67-68e3-5bef-9d3f-325052646b2e", "Frank G Myers"],
  ["c73915f0-17f8-522e-9d22-fd5cc8b558df", "Gerry R Myers"],
  ["4004d8c5-6b44-5b10-90fc-b9190c5d31b7", "Harry Myers"],
  ["b84e9ab8-b8ca-5699-bd1f-49cf9284c19e", "Hugh H Myers"],
] as const;

test("Batch 691 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText(/Page 335|Page 336/);
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 691 publishes Louis Muti's explicit Army-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/de11daf5-4332-57e9-857e-090c5a3dfee3/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("United States Army");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("Corporal");
  await expect(main).toContainText("volunteered for OSS special-operations work");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(main.locator('a[href="https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full"]')).toHaveCount(2);
  await expect(main).not.toContainText(/\b\d{8}\b/);
});

test("Batch 691 preserves Louis and Luigi Muti as a visible unresolved pair", async ({ page }) => {
  for (const id of [
    "de11daf5-4332-57e9-857e-090c5a3dfee3",
    "cfd56154-1a46-5efc-8e44-fc849a87b4f9",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText(/possible duplicate|duplicate/i);
  }
  await expect(page.getByRole("heading", { name: "Luigi Muti", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("ambiguous");
});

test("Batch 691 publishes Muthular d'Errecalde without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/e1f1695d-814c-56a6-9bfe-f1057e50380d/");
  const main = page.locator("main");
  await expect(main).toContainText("Jean-Maurice Muthular d'Errecalde");
  await expect(main).toContainText("Lucas");
  await expect(main).toContainText("file conta");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("United States Army");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("First Lieutenant, Infantry");
  await expect(main).toContainText("director of litigation or legal affairs");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(main.locator('a[href="https://www.archives.gov/files/research/jfk/releases/104-10165-10128.pdf"]')).toHaveCount(2);
  await expect(main).not.toContainText(/\b\d{8}\b/);
});

test("Batch 691 qualifies Alexander Muzzey's FBI service as earlier prewar work", async ({ page }) => {
  await page.goto("./people/214fa0cf-cbd2-53ca-b446-252e2249be94/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Federal Bureau of Investigation");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Special Agent");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(main).toContainText("does not establish an immediate transfer");
});

test("Batch 691 exposes Frank Myers's conflict and preserves literal index evidence", async ({ page }) => {
  await page.goto("./people/aa216d67-68e3-5bef-9d3f-325052646b2e/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("malformed");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(main).not.toContainText(/\b\d{8}\b/);

  await page.goto("./people/4a077049-1a03-5c0e-91b3-025f92a8d9c3/");
  await expect(page.getByRole("heading", { name: "Lawrence Muurphy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Lawrence Murphy");
  await expect(page.locator("main")).not.toContainText("Rank as indexed\nRA");
});

test("Batch 691 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,938");
  await expect(body).toContainText("37.34%");
  await expect(body).toContainText("312");
  await expect(body).toContainText("14,996");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
