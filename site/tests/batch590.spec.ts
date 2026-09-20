import { expect, test } from "@playwright/test";

const cohort = [
  ["a8fd203c-5fa1-52bf-808a-f76836bcf93a", "Clarence J Dobretzberger"],
  ["3e0b5de9-77b7-5644-9ca2-282a2899f368", "Otto Dobrovolny"],
  ["e7a2758e-5b82-5afa-abdf-473d11fbb845", "Benjamin C Dobrski"],
  ["dd17d586-7218-519b-a7ac-447ea5caa7b7", "Betty L Dobson"],
  ["0d79b04b-b70b-5be5-8da3-72e7b08e8569", "Hugh H Dobson"],
  ["14e0daf0-e924-57e5-98f7-f8455b006108", "Louise Dobson"],
  ["9fcb14b8-828c-5ac7-8f7d-58ddf0658ee4", "Richard I Dobson"],
  ["7462dcb6-b185-5dd3-8fc7-531d5824878d", "Joseph C Dockendorf"],
  ["ffddaccc-fa76-5883-b85d-2d62d28244fc", "Ellen A Dockery"],
  ["0ba150b9-3d63-54dd-95d2-ab463513821b", "Kenneth C Dockery"],
  ["90b32c86-be18-5345-99d4-886f370e87a5", "Paul G Dodd"],
  ["bd693bbb-498e-5810-87e3-f94b23d3b1bb", "Perry G Dodd"],
  ["29fc2eac-d610-5945-b6ec-7dc9f54a1233", "Edward H Dodd Jr."],
  ["abbc5932-b3a0-5294-973b-b54cf28517be", "Robert R Dodderidge"],
  ["3724fc20-8424-5e64-a7fe-954e4fe5f3e5", "George C Dodds"],
  ["da0ff273-07ab-54bc-bca4-5aa98fe6ee9f", "Vera E Dodds"],
  ["73b2d0e1-30a3-59cc-8c87-af0c9fae24f1", "Chester A Dodge"],
  ["8a1554e5-7d86-5f6d-b775-235d68efa18e", "David S Dodge"],
  ["9ec6cd13-153e-5bed-8b15-eae47d6e6664", "Donald E Dodge"],
  ["42b7f4b0-04cb-51eb-822f-eaa0da8b24bf", "Harvey H Dodge"],
] as const;

test("batch 590 keeps all twenty Box 190 people distinct and does not invent a civilian employer", async ({ page }) => {
  for (const [id, name] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("Box 190", { exact: false }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Dodderidge's White House aide role is qualified earlier work, not immediate affiliation", async ({ page }) => {
  await page.goto("./people/abbc5932-b3a0-5294-973b-b54cf28517be/");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier.getByRole("link", { name: "The White House" })).toBeVisible();
  await expect(earlier.getByText("aide", { exact: true })).toBeVisible();
  await expect(earlier.getByText("medium", { exact: true })).toBeVisible();
  await expect(page.getByText(/whether this was his immediate pre-OSS assignment remains unverified/)).toBeVisible();
});

test("unbridged Dodd Mead candidate and rejected newspaper namesakes stay off profiles", async ({ page }) => {
  await page.goto("./people/29fc2eac-d610-5945-b6ec-7dc9f54a1233/");
  await expect(page.getByText("Dodd, Mead", { exact: false }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  await page.goto("./people/90b32c86-be18-5345-99d4-886f370e87a5/");
  await expect(page.getByText("UCLA")).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
});
