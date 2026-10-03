import { expect, test } from "@playwright/test";

const profiles = [
  ["e315ce19-10a3-528a-b037-a7955a83766d", "Arthur H Nielsen"],
  ["934b2e8d-cde7-53cc-936f-c5215e3b51ec", "Carl A Nielsen"],
  ["ed7dc060-9e49-5c3b-a9b1-d67de9811bb7", "Edwin H Nielsen"],
  ["b83c702c-7a5a-557e-a45b-8b5cf4f60aa2", "Henry M Nielsen"],
  ["b4240c7b-c4a2-559a-80ef-6489fe579d46", "Milton H Nielsen"],
  ["8581b68a-4a2b-50b9-ada6-a62dad5ca3eb", "Robert B Nielsen"],
  ["fe867af8-e6a0-5b37-ac26-d991d73e2c88", "Henry R Nieman"],
  ["eea45a6c-d1a1-57d5-8862-f7e79bb166b5", "Lester C Nieman"],
  ["e4b8469b-db9e-51c1-87e6-4a5d1f5a2b1f", "Julian M Niemczyk"],
  ["fe67286b-71c0-58b1-a486-51d25bf6439f", "Ole Niesen"],
  ["70080611-60a9-589a-80b0-55f86c98fa0c", "Ennis W Nieswanger"],
  ["90982ee2-27b4-5a7a-8fe8-6a26cf54c04e", "Dorothy Niewenhous"],
  ["56ab9770-40c0-53b2-b5d6-c1932b29faca", "John E Nightingale"],
  ["d1a3097f-f118-50e7-8808-479de584724b", "Henry R Nigrelli"],
  ["0ef6ab0a-f8c5-5d00-b706-742d51c397f8", "Joseph Nigro"],
  ["ec03d1f8-0b16-5c59-a7fd-dd8127c9d56f", "Boonyong Nikrodananda"],
  ["d1cf6e00-a4b3-5970-9d83-90943b107196", "Jack T Nile"],
  ["281b1127-7777-5dfe-a5cb-f31922ed27c1", "Laila O Nilsen"],
  ["be5b5d5e-004a-5290-a0de-131a4a07eb83", "Nils C Nilson"],
  ["3def9a6e-4b5e-5e76-9286-3f5010983e08", "Toshio Nimomiya"],
  ["f7b12665-f3d4-5dab-9df6-effb546e0878", "Arthur R Ninci"],
  ["bf52948e-f198-55bd-8082-2baaa55119d3", "Halver H Nipe"],
  ["89bdeb1c-a8f5-5139-8adc-1c8569d05c40", "Verne F Nipper"],
] as const;

test("Batch 705 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{6,8}$/);
  }
});

test("Batch 705 publishes Julian Niemczyk's explicit Army-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/e4b8469b-db9e-51c1-87e6-4a5d1f5a2b1f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Battery commander; second lieutenant");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("University of Oklahoma");
  await expect(main).toContainText("student");
});

test("Batch 705 identifies WPTF as Henry Nigrelli's last civilian employer", async ({ page }) => {
  await page.goto("./people/d1a3097f-f118-50e7-8808-479de584724b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("WPTF Radio Company");
  await expect(main).toContainText("Announcer; later public relations director");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).not.toContainText("WPTF Radio Company was his immediate pre-OSS affiliation");
});

test("Batch 705 separates Boonyong Nikrodananda's student and volunteer affiliations from employment", async ({ page }) => {
  await page.goto("./people/ec03d1f8-0b16-5c59-a7fd-dd8127c9d56f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("Cornell University");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("Free Thai Society");
  await expect(main).toContainText("volunteer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 705 preserves Halver and Halvor while publishing the 99th Infantry pathway", async ({ page }) => {
  await page.goto("./people/bf52948e-f198-55bd-8082-2baaa55119d3/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Halvor H Nipe");
  await expect(main).toContainText("99th Infantry Battalion (Separate)");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("explicit immediate");
});

test("Batch 705 keeps the Lester Nieman duplicate conflict visible and unmerged", async ({ page }) => {
  await page.goto("./people/eea45a6c-d1a1-57d5-8862-f7e79bb166b5/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Lester C Niemann");
  await expect(main).toContainText("Lester C Neimann");
  await expect(main).toContainText("remain separate");
});

test("Batch 705 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,254");
  await expect(main).toContainText("38.66%");
  await expect(main).toContainText("320");
  await expect(main).toContainText("14,680");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
