import { expect, test } from "@playwright/test";

const profiles = [
  ["1f6e7b2f-9e42-53ef-8836-15a7e298ecc6", "Steele Powers"],
  ["eb550a55-df58-5cd5-934a-09dbe782b503", "Thomas E Powers"],
  ["efb0dc97-8d87-5aea-bd8d-67df6e704656", "Walter E Powers"],
  ["5171501b-5c39-5f05-8363-162a13e5388a", "Walter Powers"],
  ["2da2ff44-3630-5f68-9098-62ce5ed02d68", "William F Powers"],
  ["adf3c0dc-d095-51d2-bba7-79846d7c7ab8", "Tekla Powlack"],
  ["1d164bb2-fdfd-5482-a991-9d5cf866f204", "Armand R Poyant"],
  ["ba1ca76f-6cb0-5747-9849-c716365012fe", "Nelson P Poynter"],
  ["a8c8ffe9-4d05-55b2-b562-a9ddf46edfd4", "Jan Pradzynski"],
  ["83a75be5-fcd5-52fc-a20a-9d6dc81418ec", "Anne L Prael"],
  ["63a4f3e6-26cc-575e-9370-a4822007400c", "Reno Prandini"],
  ["50f1f0f8-42b6-5890-a401-c8d1949f577b", "Arnold L Prange"],
  ["5dd8069e-4c40-5b35-b73e-cdc209705b04", "Joseph L Prasnjak"],
  ["04efa01c-f722-5d90-b704-d619c660fdf5", "Branko Prastalo"],
  ["108df5e2-193f-5a3d-a442-5e14efb25224", "Joanne R Prater"],
  ["e9cd9f29-bc5f-5da5-a04e-d164b71e176c", "Leland J Prater"],
  ["4476a051-947a-511f-94ca-f1c8529ea4ca", "Yolande Y Prather"],
  ["e4ab8944-29d7-5533-ad65-f163dad40db3", "Antonia Pratt"],
  ["bdbdc2c1-25c3-5707-94e9-88da283f7313", "Antonio Pratt"],
  ["eb5abe92-9ef0-59c1-a7e9-046837a3815e", "Catherine O Pratt"],
  ["71ce2297-4749-58cf-9d90-a8da5a754d25", "Davis J Pratt"],
  ["81176968-c401-5cbd-9938-f4bd5a7b8fab", "George O Pratt"],
  ["92eedd8d-88ab-5840-9947-16bdbaa93b24", "George T Pratt"],
  ["7b95caac-e65b-56a4-bae4-b750432ee085", "Jack C Pratt"],
] as const;

test("Batch 772 publishes all 24 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 772 separates Nelson Poynter's immediate government assignment from his last civilian employer", async ({ page }) => {
  await page.goto("./people/ba1ca76f-6cb0-5747-9849-c716365012fe/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("Office of the Coordinator of Inter-American Affairs");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("government assignment");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Times Publishing Company");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("editor");
  await expect(main).toContainText("William Donovan");
  await expect(main).toContainText("explicit immediate");
});

test("Batch 772 exposes the Walter E Powers identifier-name conflict without adopting Jr as an alias", async ({ page }) => {
  await page.goto("./people/efb0dc97-8d87-5aea-bd8d-67df6e704656/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("POWERS WALTER JR");
  await expect(main).toContainText("middle-initial or suffix conflict");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 772 publishes Branko Prastalo's OSS Bari identity but no inferred recruitment path", async ({ page }) => {
  await page.goto("./people/04efa01c-f722-5d90-b704-d619c660fdf5/");
  const main = page.locator("main");
  await expect(main).toContainText("Branko Praštalo");
  await expect(main).toContainText("OSS Bari Yugoslav Section");
  await expect(main).toContainText("does not identify a pre-OSS employer");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 772 Army identity matches never turn coded occupations into employers", async ({ page }) => {
  for (const id of [
    "1d164bb2-fdfd-5482-a991-9d5cf866f204",
    "63a4f3e6-26cc-575e-9370-a4822007400c",
    "50f1f0f8-42b6-5890-a401-c8d1949f577b",
    "e9cd9f29-bc5f-5da5-a04e-d164b71e176c",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/official Army|Official Army/);
    await expect(main).toContainText("enlisted army personnel");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 772 preserves the indexed commissioned and civilian classifications", async ({ page }) => {
  for (const id of [
    "5171501b-5c39-5f05-8363-162a13e5388a",
    "5dd8069e-4c40-5b35-b73e-cdc209705b04",
    "92eedd8d-88ab-5840-9947-16bdbaa93b24",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("commissioned army officer");
  }
  for (const id of [
    "83a75be5-fcd5-52fc-a20a-9d6dc81418ec",
    "ba1ca76f-6cb0-5747-9849-c716365012fe",
    "4476a051-947a-511f-94ca-f1c8529ea4ca",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("civilian professional or administrative grade");
  }
});

test("home page exposes the rebuilt Batch 772 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,759");
  await expect(home).toContainText("44.94%");
  await expect(home).toContainText("13,175");
  await expect(home).toContainText("791");
  await expect(home).toContainText("352");
  await expect(home).toContainText("9,217");
});
