import { expect, test } from "@playwright/test";

const profiles = [
  ["18f32ca1-d06d-5eed-93f6-6d10b9ff7118", "Dean E Reed"],
  ["033d93c8-cf17-5c58-a1e0-d18f213b1120", "Howard A Reed"],
  ["69477e15-bcab-5781-877d-01bfad51ea15", "Martha S Reed"],
  ["b792ee00-fd88-57ab-b1d2-450e8f4d28d1", "Marvin J Reed"],
  ["e024acb2-01c6-5115-8b15-b565d61c1f0d", "Mary C Reed"],
  ["cbf1402d-bfc0-50f2-8123-91f89bad2d92", "Russell J Reed"],
  ["2fb0beb4-7bc0-5e91-8e66-f70d3c0ee3bb", "Thomas S Reed"],
  ["f6c512af-78ed-571c-8602-57b41f200e30", "William Reeda Jr."],
  ["98f15e87-6d41-58e4-9730-ffdc10af3502", "Marvin B Reeder"],
  ["1bbc67cd-ea86-55c2-a6a3-0a19f2071722", "Walter Reeder"],
  ["4aa24972-3199-5220-93c0-8bafafb68f40", "William F Reedy"],
  ["2e65370a-7cbe-5157-aeaa-61f8f651e518", "Clifford H Reeh"],
  ["268f08a7-3b61-58d0-84ad-8dddfc110033", "Emory K Rees"],
  ["cae06758-e584-54f4-9389-0298e21c8137", "John E Rees"],
  ["3bf6d66a-74af-5234-99b5-64e06d3b890d", "Lewis Y Rees"],
  ["2c62fb61-32bf-5224-963a-68b9f787e798", "Patricia A Rees"],
  ["660a52b3-051e-56f8-8945-8fc16bb7a16c", "Burton E Reese"],
  ["636fbab1-ffe2-55d1-bf2c-775955a18128", "Charles T Reese"],
  ["75571d38-e678-5f9f-81a3-d5ba51298838", "Donald Reese"],
  ["a8bc095d-62d4-548c-8ca5-550633195d87", "Merlin C Reese"],
  ["a21e6f9d-3eff-5a8e-ad6b-6a0edacb17ce", "Thomas W Reese"],
  ["cd00004c-17af-5f07-b4a6-627507502628", "Dallas Reeves"],
  ["07ada91e-46db-5a80-9e39-9f4eababcea9", "Jack J Reeves"],
] as const;

const officialIdentityProfiles = [
  "b792ee00-fd88-57ab-b1d2-450e8f4d28d1",
  "4aa24972-3199-5220-93c0-8bafafb68f40",
  "2e65370a-7cbe-5157-aeaa-61f8f651e518",
  "268f08a7-3b61-58d0-84ad-8dddfc110033",
  "3bf6d66a-74af-5234-99b5-64e06d3b890d",
  "a8bc095d-62d4-548c-8ca5-550633195d87",
] as const;

test("Batch 793 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).toContainText("archival review");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 793 publishes six official identity claims without inventing employers", async ({ page }) => {
  for (const id of officialIdentityProfiles) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Official Army bulk data supports a high-confidence identification");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 793 keeps rejected namesakes and clipped notes qualified", async ({ page }) => {
  await page.goto("./people/4aa24972-3199-5220-93c0-8bafafb68f40/");
  const reedy = page.locator("main");
  await expect(reedy).not.toContainText("choir director");
  await expect(reedy).not.toContainText("taxicab");

  await page.goto("./people/cae06758-e584-54f4-9389-0298e21c8137/");
  await expect(page.locator("main")).not.toContainText("Buena Vista College");

  await page.goto("./people/a21e6f9d-3eff-5a8e-ad6b-6a0edacb17ce/");
  const thomas = page.locator("main");
  await expect(thomas).toContainText("photogra");
  await expect(thomas.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "photographer",
  );
});

test("home page exposes the rebuilt Batch 793 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,234");
  await expect(home).toContainText("46.93%");
  await expect(home).toContainText("12,700");
  await expect(home).toContainText("808");
  await expect(home).toContainText("362");
  await expect(home).toContainText("9,694");
});
