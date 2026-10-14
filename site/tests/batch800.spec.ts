import { expect, test } from "@playwright/test";

const profiles = [
  ["2cf022ed-d6e4-5967-b470-ee757c0f87a1", "Larry A Rhine"],
  ["1909fa5b-258d-5621-a4d9-7d5960621a0d", "William L Rhoads"],
  ["43281227-42c7-50e3-b379-a0dfb9e4e96b", "Harold E Rhodes"],
  ["f8bde712-cdba-500f-81e5-1105363b00da", "Langdon Rhodes"],
  ["a12bc45d-a24b-599c-9989-a4aed6224921", "Ralph Rhodes"],
  ["b12706c5-e7e1-5ca2-a01c-c9ac06fb4e29", "Meredith J Rhule"],
  ["652ddf3d-c570-51bd-934d-e878c8f28f46", "Hazel M Rhymes"],
  ["06d69324-f980-5c67-a5ff-95d5cd1b93fa", "Ledlie M Rial"],
  ["284f0366-540e-5636-820e-90d1c7a8fab7", "Mary L Rial"],
  ["4c1bd61b-c6c8-53be-82f7-9799ba40146a", "Jack Riback"],
  ["92d228b2-dcc0-5ef8-ab5c-6f2309e7b4c2", "Willie Riback"],
  ["d5b5dcb4-d0ab-55f6-b730-8200d369e8e8", "Anthony M Ribarich"],
  ["2f27fef2-e387-5cc3-8b62-56fb75b7da60", "Anthony Ribarich"],
  ["8c3e85a9-f976-5a8d-b363-cff91413037c", "Leon Ricard"],
  ["d0e2d60c-2859-54c4-ba09-72b67bd6ee8d", "John A Ricca"],
  ["316430ce-19b0-5f86-b301-e7aff834a475", "Andrew P Riccardi"],
  ["6385354b-c201-5e8c-854c-5c824a937681", "Burton Rice"],
  ["3b721baa-1fda-5927-b3bb-e6d29540b38a", "Earl C Rice"],
  ["c038251e-2bb3-545f-8ae9-ba3d424f7c0a", "Elizabeth Rice"],
  ["92d4df01-6192-5b79-9368-a05fa216d25d", "Jim L Rice"],
  ["1c02a956-4f51-57a2-a241-b5f931559037", "Judith C Rice"],
  ["08215191-2313-5094-a5fc-35e8521b5993", "Roy W Rice"],
  ["bdb548e3-b8d4-5ff2-84a5-554f48776b16", "Ruth M Rice"],
] as const;

test("Batch 800 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Meredith J Rhule separates Navy immediacy from the last civilian employer", async ({ page }) => {
  await page.goto("./people/b12706c5-e7e1-5ca2-a01c-c9ac06fb4e29/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("United States Navy");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Sangamon County Sheriff's Office",
  );
  await expect(main).toContainText("Chief deputy");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Meredith Rhule");
});

test("Anthony Ribarich publishes occupation only and preserves the adjacent-row ambiguity", async ({ page }) => {
  await page.goto("./people/2f27fef2-e387-5cc3-8b62-56fb75b7da60/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("former waiter");
  await expect(main).toContainText("medium");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main).toContainText("5 things you may not know about Sicily-Rome American Cemetery");

  await page.goto("./people/d5b5dcb4-d0ab-55f6-b730-8200d369e8e8/");
  await expect(page.locator("main")).toContainText("ambiguous");
  await expect(page.locator("main")).not.toContainText("former waiter");
});

test("Leon Ricard exposes the protected-identifier name conflict", async ({ page }) => {
  await page.goto("./people/8c3e85a9-f976-5a8d-b363-cff91413037c/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Fletcher N. Robertson");
  await expect(main).toContainText("Electronic Army Serial Number Merged File");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("John A Ricca stays qualified and does not publish the unbridged prosecutor lead", async ({ page }) => {
  await page.goto("./people/d0e2d60c-2859-54c4-ba09-72b67bd6ee8d/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("OSS Major John Ricca");
  await expect(main).not.toContainText("Wayne County Prosecutor's Office");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 800 organization pages expose the normalized Navy and sheriff institutions", async ({ page }) => {
  for (const [id, name] of [
    ["3960fa8e-a551-56cf-8305-b2b9e4961b9d", "United States Navy"],
    ["187429c1-cac2-5668-98f6-c6501b932b79", "Sangamon County Sheriff's Office"],
  ]) {
    await page.goto("./organizations/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("home page exposes the rebuilt Batch 800 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,388");
  await expect(home).toContainText("47.57%");
  await expect(home).toContainText("12,546");
  await expect(home).toContainText("819");
  await expect(home).toContainText("369");
  await expect(home).toContainText("9,851");
});
