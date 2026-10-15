import { expect, test } from "@playwright/test";

const profiles = [
  ["5b100ccd-6c81-5b75-9353-aeded1fd20de", "Otto Rossmeyer"],
  ["172c0446-b24f-5757-8fdd-420f4903a1e2", "Harold R Rossmiller"],
  ["bd5bd260-4e6f-5e5e-811f-49188b23b9e4", "Dominic Rossow"],
  ["7547fdbd-1721-5d9f-a455-5b21553e33dc", "Robert Rossow Jr."],
  ["23fe0d9f-2ca7-5e4e-abe2-465668858952", "Joseph A Rost"],
  ["6dff4a3a-1141-5a4c-8a77-2ea2a7c99ab0", "Walt W Rostow"],
  ["b0ea5034-13df-5bb6-8db1-595f1140a8c1", "Tovio D Roswall"],
  ["9e45fde1-efa4-56cb-8877-881794d48526", "Cecil W Rote"],
  ["5ef8cd33-8439-5ee8-bb61-434a6424a8fd", "George W Rote"],
  ["04959569-b52f-5400-a85d-bc875c23d650", "Nancy F Rotella"],
  ["ed773cd5-338b-5eff-a8f3-6cb5c4feb98b", "John S Roth"],
  ["c9d35f70-f87e-53c4-ba4f-dd59c7766bf5", "Morris L Roth"],
  ["2b6d96a2-e801-5b2a-a372-cf267e262b4c", "Sidney Roth"],
  ["63055abf-1882-50ed-8cf3-209fda3c9e29", "Egan G Rothelini"],
  ["0d889911-7408-58f2-afbf-bfce8339f5c6", "George B Rothenbuesch"],
  ["354a00be-2215-51e5-a7c4-5bbf9c5444f9", "Michael R Rotherus"],
  ["74ed4377-a709-562b-ae07-44e2195c944b", "James N Rothschild"],
  ["e0122953-291f-5864-b01a-8b9d4937ee32", "Margaret S Rothschild"],
  ["136fcac8-f106-5e35-a933-1044e87be4a7", "Walter Rothschild"],
  ["60baf833-2498-54c6-8699-8321e3a9e2c6", "Paul Rothstein"],
  ["e2ad2347-d384-5616-a043-4ab7763adaea", "Betty Rothweth"],
  ["03b97c94-dcc9-5050-9848-3e80c82c657b", "Margaret E Rott"],
  ["2b490178-2fd8-557d-9a74-08a8d8d2cd0f", "Saymour A Rottenberg"],
] as const;

test("Batch 823 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Army identity-only matches do not become employer claims", async ({ page }) => {
  for (const id of [
    "5b100ccd-6c81-5b75-9353-aeded1fd20de",
    "23fe0d9f-2ca7-5e4e-abe2-465668858952",
    "136fcac8-f106-5e35-a933-1044e87be4a7",
    "60baf833-2498-54c6-8699-8321e3a9e2c6",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Harold Rossmiller profile qualifies the medical-school match and does not call it employment", async ({ page }) => {
  await page.goto("./people/172c0446-b24f-5757-8fdd-420f4903a1e2/");
  const main = page.locator("main");
  await expect(main).toContainText("M.D. candidate");
  await expect(main).toContainText("student");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("not an employer");
});

test("Robert Rossow profile separates the documented State assignment from an immediate predecessor", async ({ page }) => {
  await page.goto("./people/7547fdbd-1721-5d9f-a455-5b21553e33dc/");
  const main = page.locator("main");
  await expect(main).toContainText("Foreign Service officer");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("does not prove it immediately preceded OSS service");
});

test("Walt Rostow keeps one Columbia affiliation after re-audit", async ({ page }) => {
  await page.goto("./people/6dff4a3a-1141-5a4c-8a77-2ea2a7c99ab0/");
  const main = page.locator("main");
  await expect(main).toContainText("Columbia University");
  await expect(main.getByText("Columbia University", { exact: true })).toHaveCount(1);
});

test("Tovio Roswall keeps the printed spelling and rejected conflicting Army candidate", async ({ page }) => {
  await page.goto("./people/b0ea5034-13df-5bb6-8db1-595f1140a8c1/");
  await expect(page.getByRole("heading", { name: "Tovio D Roswall", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("Thomas C. Brannigan");
  await expect(main).toContainText("conflict was rejected");
});

test("Saymour Rottenberg conflict exposes variants without merging the duplicate", async ({ page }) => {
  await page.goto("./people/2b490178-2fd8-557d-9a74-08a8d8d2cd0f/");
  await expect(page.getByRole("heading", { name: "Saymour A Rottenberg", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("Seymour A. Rottenberg");
  await expect(main).toContainText("Seymour A. Rattenberg");
  await expect(main).toContainText("conflicting sources");
});
