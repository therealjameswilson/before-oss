import { expect, test } from "@playwright/test";

const profiles = [
  ["712ccb18-6db4-5cc0-b440-4bcf7dce5dfa", "Grace D Robinson"],
  ["3f446142-ee46-5697-b556-b1bdc67a5875", "Harvey A Robinson"],
  ["379134f2-630a-5492-9687-ca637a4e75a6", "Henson L Robinson"],
  ["b3802e13-be19-5c85-8b7a-a422785811fd", "Hubert E Robinson"],
  ["ff134cf9-bd2d-52df-9b8e-97c1c562efac", "James C Robinson"],
  ["4fcd01cd-94dd-5cc9-8958-f3ff2d3459fc", "James R Robinson"],
  ["8c456f1b-b18d-5179-9ada-1282da1bad59", "Jay T Robinson"],
  ["984c24b9-353e-57b7-8adf-154e19919dbf", "John G Robinson"],
  ["b3d56044-3faa-5d42-b80c-e3e0788e806d", "John L Robinson"],
  ["327a1464-a228-5308-835e-f98b8afe806b", "John W Robinson Jr."],
  ["1eca7534-2756-5df5-92e4-d2b27aa3a98c", "Joseph A Robinson"],
  ["7480183a-51ad-583b-8e26-5141ed096406", "Kenneth L Robinson"],
  ["355a5da2-9250-548a-8d1c-84aae2b9f010", "Oren H Robinson"],
  ["b93063b8-fd4e-590c-b553-1136f2a330f5", "Phillip L Robinson"],
  ["f440fdec-5b86-5c61-bcde-5ba1fb37c8b9", "Roy M Robinson"],
  ["6d37459b-6f94-5d54-a8ff-62a4bccfd2c6", "Virginia C Robinson"],
  ["4a3b1be1-1a1a-5fe0-a6b5-720585b4c1d5", "Virginia M Robinson"],
  ["fce6b68c-ea31-5f90-8d06-4431af2164ac", "Wilfred L Robinson"],
  ["d450cebf-f586-58f8-bab2-15a057706781", "William H Robinson"],
  ["bc9949d3-d43f-55aa-bf06-4f534cc81f34", "Charles B Robison"],
  ["7147a3c9-cc8e-5246-a336-37c2de68b35b", "Paul E Robison"],
  ["212d0b03-5242-5b47-99b5-3ecbb6cf00ab", "Martha J Robyn"],
  ["0d138f54-b585-59b6-9dce-1cfc107792b0", "Maria T Rocca"],
] as const;

test("Batch 812 publishes all 23 profiles with terminal archival outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("requires archival review");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Phillip Robinson keeps the index spelling and exposes the Army variant", async ({ page }) => {
  await page.goto("./people/b93063b8-fd4e-590c-b553-1136f2a330f5/");
  const main = page.locator("main");
  await expect(main.getByRole("heading", { name: "Phillip L Robinson", level: 1 })).toBeVisible();
  await expect(main).toContainText("Philip L Robinson");
  await expect(main).toContainText("spelling");
});

test("Roy Robinson's postwar Union Oil namesake is excluded from the oil directory", async ({ page }) => {
  await page.goto("./people/f440fdec-5b86-5c61-bcde-5ba1fb37c8b9/");
  await expect(page.locator("main")).toContainText("1954");
  await expect(page.locator("main")).toContainText("rejected");

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(10);
  await expect(oilList).not.toContainText("Roy M Robinson");
});

test("home page exposes the rebuilt Batch 812 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,661");
  await expect(home).toContainText("48.71%");
  await expect(home).toContainText("12,272");
  await expect(home).toContainText("833");
  await expect(home).toContainText("374");
  await expect(home).toContainText("10,124");
});
