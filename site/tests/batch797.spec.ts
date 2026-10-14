import { expect, test } from "@playwright/test";

const profiles = [
  ["8cd1b5ed-4052-5b1f-b4dd-ab0939a5a045", "Anton H Remenih"],
  ["2da25f0d-1148-57f0-b356-810e445c281b", "Charles F Remer"],
  ["7d93d571-76db-5260-b9fc-8dd9460ee80f", "George Remetta Jr."],
  ["0ab40307-8b07-55bd-94b3-47b4a56e9105", "Char-Anne Remington"],
  ["255b0a0e-86ac-5575-8788-8cd4b129f91d", "Hilton Remley"],
  ["ab8b66fa-4bd0-5bc6-8a46-0d0f86617c19", "Tommie I Remmage"],
  ["aa341465-b6fb-5e7d-8a9e-64dae1335859", "Jane Renard"],
  ["06cd1ba6-6b20-55d4-86fe-bc925b9e5d25", "Rosendo F Rendon"],
  ["08b4d830-fec5-51aa-a09d-939dc2dcb782", "Stephen G Rendulic"],
  ["468743f0-a31b-5513-8a3e-5f29829412a2", "Raymond A Rene"],
  ["aae86a18-cf69-5db7-adc1-23f537db49bc", "Peter Renehan"],
  ["d66ce189-8176-5626-8e9f-36a1b3f4043f", "William S Renehan"],
  ["ffd7aad3-bac1-5101-b874-9e9ccdba8a3a", "Melton S Renfrew"],
  ["d297726b-4199-5d97-8588-6b04496bd1a3", "Fred Renganeschi"],
  ["c03d50f9-7e04-5cc5-af7c-7bb88a05cb13", "Lory Renganeschi"],
  ["51d60b55-2fc8-50de-848e-4d334ac6dfbc", "Melvin H Rennie"],
  ["f1f6d4ed-8635-5c2c-b8dc-65782c81470b", "Norbert F Rennie"],
  ["c17a5d26-3333-5db5-9dc4-1a1061e12c45", "William D Rennie"],
  ["b8ced6c3-6602-53c9-8b4f-2db3f0fedfce", "John H Reno"],
  ["4d4c525f-3a54-5b33-99d2-f00ab75d3fbc", "Virginia R Renshaw"],
  ["66c3f35f-ef00-5c3e-9647-e11ef642155d", "James D Rentfro"],
  ["91e90843-c4eb-58ca-b242-ecb48222e4d9", "Anker Rentse"],
  ["435e14f2-9f91-55de-a663-9579ce0aa4bf", "George S Rentz"],
] as const;

const officialArmyIdentityProfiles = [
  "8cd1b5ed-4052-5b1f-b4dd-ab0939a5a045",
  "7d93d571-76db-5260-b9fc-8dd9460ee80f",
  "468743f0-a31b-5513-8a3e-5f29829412a2",
  "06cd1ba6-6b20-55d4-86fe-bc925b9e5d25",
  "08b4d830-fec5-51aa-a09d-939dc2dcb782",
  "c17a5d26-3333-5db5-9dc4-1a1061e12c45",
  "d66ce189-8176-5626-8e9f-36a1b3f4043f",
] as const;

test("Batch 797 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 797 publishes official Army identity evidence without inventing employers", async ({ page }) => {
  for (const id of officialArmyIdentityProfiles) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/official Army/i);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Remley separates a qualified WGN last employer from earlier utility work", async ({ page }) => {
  await page.goto("./people/255b0a0e-86ac-5575-8788-8cd4b129f91d/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("WGN");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("medium");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("New Mexico Power Company");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).toContainText("Year Book of the Institute of Radio Engineers, 1937");
  await expect(main).toContainText("1944 Broadcasting Yearbook Number");
  await expect(main).toContainText("WGN Family Letter");
});

test("Rentse publishes Kelantan Government only as last civilian employment", async ({ page }) => {
  await page.goto("./people/91e90843-c4eb-58ca-b242-ecb48222e4d9/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Kelantan Government");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("high");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).toContainText("Major Accessions to London University");
  await expect(main).toContainText("Patani Through Foreign Eyes");
});

test("Remmage conflict remains separate and employer-free", async ({ page }) => {
  await page.goto("./people/ab8b66fa-4bd0-5bc6-8a46-0d0f86617c19/");
  const main = page.locator("main");
  await expect(main).toContainText("TOMMIE I RAMMAGE");
  await expect(main).toContainText("TOMMIE I REMMAGE");
  await expect(main).toContainText(/conflict/i);
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Rentz exposes namesake ambiguity without adopting either biography", async ({ page }) => {
  await page.goto("./people/435e14f2-9f91-55de-a663-9579ce0aa4bf/");
  const main = page.locator("main");
  await expect(main).toContainText("George Snavely Rentz");
  await expect(main).toContainText("George S. Rentz Jr.");
  await expect(main).toContainText("ambiguous");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 797 organization pages expose the three reviewed employers", async ({ page }) => {
  for (const [id, name] of [
    ["48c1e12e-380e-5be1-91c3-47cc6c79e948", "New Mexico Power Company"],
    ["50b8a9a0-1c42-5e7b-af74-2e4cdace2ded", "WGN"],
    ["6aa91820-766c-598c-91bd-39d923c847d7", "Kelantan Government"],
  ]) {
    await page.goto("./organizations/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("home page exposes the rebuilt Batch 797 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,322");
  await expect(home).toContainText("47.30%");
  await expect(home).toContainText("12,612");
  await expect(home).toContainText("814");
  await expect(home).toContainText("368");
  await expect(home).toContainText("9,783");
});
