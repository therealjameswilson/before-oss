import { expect, test } from "@playwright/test";

const profiles = [
  ["5080c4ac-4fb4-51aa-b1f0-28cae414389e", "Jules Milton"],
  ["1c02838e-e1a5-51ba-8855-aa8d49f39c3e", "Russell S Milton"],
  ["cfcd43f4-44ce-5956-b747-f94ff87927a1", "Stavos J Milton"],
  ["6714afe7-3d0d-5be9-9fb7-a90f3de6e102", "Terrence W Miltower"],
  ["fa671d9c-28f3-5d11-a988-7b0b298177d6", "Henry E Minard"],
  ["2ad5cd8a-7818-570b-9556-ec7be3433427", "Thomas G Minas"],
  ["9db3c9d1-98de-579f-a57f-c22c52f3548c", "Emil Mincu"],
  ["77a2451a-27a4-5296-9657-b5ddd93449cb", "Harold E Miner"],
  ["25711aa6-ab40-5ea3-8b36-34d299a89a67", "Joseph G Miner"],
  ["8d99f639-5574-5618-8a41-01a2b468df13", "Robert G Miner"],
  ["59fcac47-726a-5b54-959f-8480c707f5ef", "Robert H Miner"],
  ["097f8ace-25a1-5d84-b168-8571b6d9631d", "Emile R Minerault"],
  ["ecf7c41d-58d1-5a74-b85a-424c47f2d18d", "John J Minich"],
  ["d40dc8af-d565-590e-b74a-22f86489f28f", "James M Minihe"],
  ["92440612-6f9f-5b42-97d6-bf43956bff6a", "Eugeneis Minisini"],
  ["cf65266b-1e8c-5f34-af5b-709f5927e4d5", "Orin P Minnis"],
  ["ae253ec9-3a66-5386-8dc8-daf7a5dfe9f4", "John P Minogianis"],
  ["3b06d809-ebe7-5157-bef8-218575381d99", "Miller G Minor"],
  ["04b4f30f-6c1c-532a-8d27-ad4953f7a86b", "Feodor Minorsky"],
  ["58c3ce85-7f62-599b-96fd-534daa9d3e73", "Jerome Minot"],
  ["bb0bbed4-9799-5a9a-a89b-700f17a28985", "Leonard E Mins"],
  ["2d6b7f4e-5c2d-5434-aece-5ad253026b0e", "Leonard E Mins"],
] as const;

test("Batch 664 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 664 publishes Emil Mincu's maritime employment without inventing the later company name", async ({ page }) => {
  await page.goto("./people/9db3c9d1-98de-579f-a57f-c22c52f3548c/");
  const main = page.locator("main");

  await expect(main).toContainText("Serviciul Maritim Român");
  await expect(main).toContainText("Deck officer; later second officer");
  await expect(main).toContainText("unnamed private shipping company");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 664 keeps John Minogianis's military pathway distinct from civilian employment", async ({ page }) => {
  await page.goto("./people/ae253ec9-3a66-5386-8dc8-daf7a5dfe9f4/");
  const main = page.locator("main");

  await expect(main).toContainText("122nd Infantry Battalion");
  await expect(main).toContainText("Greek Battalion");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("probable immediate");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 664 exposes Emile Minerault's rank conflict", async ({ page }) => {
  await page.goto("./people/097f8ace-25a1-5d84-b168-8571b6d9631d/");
  const main = page.locator("main");

  await expect(main).toContainText("Emile Raymond Minerault");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("Sergeant");
  await expect(main).toContainText("First Lieutenant");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 664 keeps the two Leonard Mins rows separate and unassigned", async ({ page }) => {
  for (const [id] of profiles.slice(-2)) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("ambiguous");
    await expect(main).toContainText("Boxes 528 and 527");
    await expect(main).toContainText("archival review");
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText("Marx-Lenin Institute");
  }
});

test("Batch 664 keeps Feodor Minorsky's archival lead private", async ({ page }) => {
  await page.goto("./people/04b4f30f-6c1c-532a-8d27-ad4953f7a86b/");
  const main = page.locator("main");

  await expect(main).toContainText("probable");
  await expect(main).toContainText("HS 9/1039/5");
  await expect(main).not.toContainText("Ted Harris");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 664 updates exact coverage and retains the oil-company category at the top", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,358");
  await expect(page.locator("body")).toContainText("34.91%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(category).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil, petroleum, refining, or exploration companies");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
