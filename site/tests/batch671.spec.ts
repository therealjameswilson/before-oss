import { expect, test } from "@playwright/test";

const profiles = [
  ["7fd2057d-60ab-50e3-8342-519c50c99c16", "Anthony Monti"],
  ["de2b11d7-e3a6-5b6c-91c3-fc576b01d738", "Esther T Moon"],
  ["8793c41e-49fb-56b6-849b-6628c2b0e120", "Franklin F Moon"],
  ["b9976367-d47a-529d-b5ca-f8432224e93f", "James A Montgomery"],
  ["2569020e-4190-5df0-8459-e2217d8bd038", "Jeanne E Montgomery"],
  ["36c403f0-8319-5845-8122-c7c7757374d9", "John J Montouri"],
  ["a53f879d-66ef-54b8-be76-ea00b48e775d", "John U Montuori"],
  ["f993e747-94d1-5378-9548-93c06d6528c1", "Johnnie L Montgomery"],
  ["8feae46c-6bdc-54ea-80fc-21ee369d02bc", "Joseph A Montgomery"],
  ["8a379e7c-ea3e-5118-a671-fc4700bd02cb", "Julia G Montgomery"],
  ["1f2e69b8-dee3-5f58-87fa-3f0936623a06", "Kathleen K Montgomery"],
  ["29378f72-0b0c-5e48-9bec-7c2d1170e86e", "Laro Montland"],
  ["998e5351-d2aa-5b9c-a144-a0c516de9a5c", "Lawrence H Moon"],
  ["9ca66033-d81d-5195-9894-9db608db0bcf", "Mary G Montgomery"],
  ["3caab889-743e-5259-ada3-321acc459372", "Maurice A Mook"],
  ["72a38128-a4fa-5f34-8553-cfdc169992c5", "Mildred E Montgomery"],
  ["fd9fdd87-52ca-5b6d-8055-e8d26f87ef64", "Ralph A Monton"],
  ["f41578e0-b0ed-505b-8518-b246b5b5cb79", "Robert K Montgomery"],
  ["2abb802a-153f-5c90-b659-1cc366c04017", "Steve G Monti"],
  ["04f7ff3b-f7c9-5347-8f97-b18fd4989453", "Tony Monti"],
  ["d2075f4b-673a-593f-b715-09c17fcd8550", "Victor S Montrezza"],
  ["2334c107-56e3-5ec0-97d9-cef94c64377c", "Walter Montgomery"],
] as const;

test("Batch 671 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 671 publishes reviewed Army identities without deriving employers from codes", async ({ page }) => {
  const armyMatches = [
    ["7fd2057d-60ab-50e3-8342-519c50c99c16", "Anthony Monti"],
    ["f993e747-94d1-5378-9548-93c06d6528c1", "Johnnie L Montgomery"],
    ["8feae46c-6bdc-54ea-80fc-21ee369d02bc", "Joseph A Montgomery"],
    ["998e5351-d2aa-5b9c-a144-a0c516de9a5c", "Lawrence H Moon"],
    ["2abb802a-153f-5c90-b659-1cc366c04017", "Steve G Monti"],
  ] as const;

  for (const [id, name] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("Batch 671 qualifies John Montouri, Tony Monti, and Maurice Mook identity leads", async ({ page }) => {
  await page.goto("./people/36c403f0-8319-5845-8122-c7c7757374d9/");
  let main = page.locator("main");
  await expect(main).toContainText("probably the Bradford, Pennsylvania soldier");
  await expect(main).toContainText("805th Tank Destroyer Battalion roster");
  await expect(main).toContainText("whether the assignment preceded OSS remain uncertain");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/04f7ff3b-f7c9-5347-8f97-b18fd4989453/");
  main = page.locator("main");
  await expect(main).toContainText("probably the New Mexico member");
  await expect(main).toContainText("The OSS's Eighth Army Detachment in Italy");
  await expect(main).toContainText("identifies no pre-OSS employer");

  await page.goto("./people/3caab889-743e-5259-ada3-321acc459372/");
  main = page.locator("main");
  await expect(main).toContainText("probably the scholar associated with American University");
  await expect(main).toContainText("William Campbell Binkley Papers");
  await expect(main).toContainText("not proven to precede OSS");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 671 identifies Robert Montgomery's Jedburgh role without back-projecting an employer", async ({ page }) => {
  await page.goto("./people/f41578e0-b0ed-505b-8518-b246b5b5cb79/");
  const main = page.locator("main");

  await expect(main).toContainText("Jedburgh Team Tony");
  await expect(main).toContainText("code-named Dollar");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("not a pre-OSS employer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Federal Energy Administration");
});

test("Batch 671 keeps protected-identifier and duplicate-name conflicts visible", async ({ page }) => {
  await page.goto("./people/a53f879d-66ef-54b8-be76-ea00b48e775d/");
  await expect(page.locator("main")).toContainText("middle initial J");
  await expect(page.locator("main")).toContainText("conflicting");

  await page.goto("./people/29378f72-0b0c-5e48-9bec-7c2d1170e86e/");
  await expect(page.locator("main")).toContainText("Lars Motland");
  await expect(page.locator("main")).toContainText("prohibit an automatic merge");

  await page.goto("./people/fd9fdd87-52ca-5b6d-8055-e8d26f87ef64/");
  await expect(page.locator("main")).toContainText("Ralph A. Minton");
  await expect(page.locator("main")).toContainText("prohibit an automatic merge");

  await page.goto("./people/d2075f4b-673a-593f-b715-09c17fcd8550/");
  await expect(page.locator("main")).toContainText("two records under different, nonmatching names");
  await expect(page.locator("main")).not.toContainText("Verified employer");
});

test("Batch 671 keeps unsupported namesake employment out of unresolved profiles", async ({ page }) => {
  await page.goto("./people/8a379e7c-ea3e-5118-a671-fc4700bd02cb/");
  let main = page.locator("main");
  await expect(main).toContainText("1928-1930 Cincinnati directory entry");
  await expect(main).toContainText("remains an unpublished lead");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/2334c107-56e3-5ec0-97d9-cef94c64377c/");
  main = page.locator("main");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Spartan Mills");
});

test("Batch 671 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,510");
  await expect(page.locator("body")).toContainText("35.55%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  for (const [, name] of profiles) {
    await expect(oilList).not.toContainText(name);
  }
});
