import { expect, test } from "@playwright/test";

const profiles = [
  ["34867d63-ed99-5b06-814e-07a95c3ea588", "Tommie I Rammage"],
  ["9c6621e1-3844-5dd4-9182-279e358734a1", "Regina T Ramold"],
  ["6a06f29e-8dce-5ee0-9ea4-301847068c90", "Rosa C Ramos"],
  ["8fe8be03-6d86-574c-98b8-a8ff28cf7285", "Nick E Ramoundos"],
  ["b4ddff87-9574-5379-b6bb-e3fa71659cb3", "Jack E Ramsberger"],
  ["2e9471ca-9e4c-5f43-9426-7166fff63dd9", "Peter E Ramsbotham"],
  ["13c940b2-0be7-5754-8673-fea80853d6c0", "Charles F Ramsdell"],
  ["c9c17b29-fce9-52ac-8241-fb9d00eff92a", "Howard H Ramsey"],
  ["80f9ad1d-653f-5b32-ad01-2e9130a2ab6e", "James W Ramsey"],
  ["079f8263-afc0-54d5-bd7a-a6c5c26e1623", "Kenneth S Ramsey"],
  ["11e5f223-02d3-531b-b6ef-ec19f69021ef", "Marie E Ramsey"],
  ["709268fb-bb3c-5c59-a7e3-f28bc6da9228", "Winters P Ramsey"],
  ["bbaeb33b-8ee6-5e41-bf9a-e8784f0f3be7", "Elvira L Ramthum"],
  ["2115d277-ed00-5309-973a-726f6177e26d", "Philip L Rancourt"],
  ["191be3f4-c81a-56a7-a452-ac9ff9dd9207", "Philip L Rancourt"],
  ["cc2a0147-219f-5cfb-93f7-ca5c977a612d", "Henry J Rand"],
  ["40b0b870-4f28-568a-b17f-ee4716c57f0f", "Frank J Randall"],
  ["cf444fa1-a29f-59b7-81a0-5830692d2f30", "Gale M Randall"],
  ["2d8c9373-80ee-54f5-84eb-107ba0eb163f", "John R Randall"],
  ["2f848019-cf10-590e-a7f4-3dc9f928aa7b", "Kenneth C Randall"],
  ["354d45fe-82d3-5fa2-84b0-dd85ef0253a1", "Margaret A Randall"],
  ["cc206484-6a17-5239-8092-352a9f07705f", "Ruth E Randall"],
] as const;

test("Batch 787 publishes all 22 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 787 publishes Ramsbotham's qualified wartime affiliations without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/2e9471ca-9e4c-5f43-9426-7166fff63dd9/");
  const main = page.locator("main");
  await expect(main).toContainText("British War Office");
  await expect(main).toContainText("British Army Intelligence Corps");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Churchill Archives Centre");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 787 preserves clipped notes exactly", async ({ page }) => {
  for (const [id, note] of [
    ["8fe8be03-6d86-574c-98b8-a8ff28cf7285", "One fold"],
    ["2e9471ca-9e4c-5f43-9426-7166fff63dd9", "Record"],
    ["709268fb-bb3c-5c59-a7e3-f28bc6da9228", "Certificat"],
    ["bbaeb33b-8ee6-5e41-bf9a-e8784f0f3be7", "Record"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText(note);
  }
});

test("Batch 787 keeps the two Philip L Rancourt rows separate but visibly linked", async ({ page }) => {
  const groups: string[] = [];
  for (const id of ["2115d277-ed00-5309-973a-726f6177e26d", "191be3f4-c81a-56a7-a452-ac9ff9dd9207"]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Duplicate group");
    const text = await main.textContent();
    const match = text?.match(/duplicate-[0-9a-f]+/);
    expect(match).toBeTruthy();
    groups.push(match![0]);
  }
  expect(groups[0]).toBe(groups[1]);
});

test("Batch 787 exposes the Rammage conflict without a full protected identifier", async ({ page }) => {
  await page.goto("./people/34867d63-ed99-5b06-814e-07a95c3ea588/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Remmage");
  await expect(main).not.toContainText(/\b\d{8}\b/);
});

test("home page exposes the rebuilt Batch 787 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,100");
  await expect(home).toContainText("46.37%");
  await expect(home).toContainText("12,834");
  await expect(home).toContainText("803");
  await expect(home).toContainText("358");
  await expect(home).toContainText("9,559");
});
