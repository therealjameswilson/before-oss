import { expect, test } from "@playwright/test";

const profiles = [
  ["5b33ad31-3142-5f14-8cba-5742f5ed22de", "Arthur F Reinhardt"],
  ["2f7415e8-9f7d-5bac-8ab4-a144d2710db0", "Harry J Reinhardt"],
  ["aac6d7b5-5889-569d-8744-56c32fc878e8", "Olav S Reinholdtsen"],
  ["dd15fe61-0db8-5d91-a2e4-4803a3e35d2d", "Chris Reinisch"],
  ["230477a8-e4c9-5f06-92dd-6d231f4fb5cf", "Richard P Reinsch"],
  ["fd716d32-bb72-5da8-bddf-91d659b0f36a", "Harry Reis"],
  ["2b22eec2-56ff-5180-a16f-2fddb3ba1426", "Roy R Reis"],
  ["17e66692-47f8-551f-90b4-a30f7a4a9d57", "Leonard F Reisig"],
  ["508cbc69-1270-51b9-9468-39c178ca2afe", "Morris Reisman"],
  ["c93fb302-f95a-57aa-b0b0-bec192035b4f", "Dorothy G Reisner"],
  ["b3cd8b18-4294-57c8-9c90-b4d5a2ee4ab3", "Edmund Reiss"],
  ["e2ade996-28ed-50ab-8719-22895ce77a85", "Milton Reissman"],
  ["5668762d-a62c-5f7d-a8e4-7196c597c2a3", "Calvin W Reister"],
  ["81e73746-1109-5c4d-88d7-02f33b609e71", "Rene C Reitenbach"],
  ["65c9eade-0071-539f-9949-d5ec35280aba", "Gilbert J Reiter"],
  ["7495006f-5930-5e3b-934f-abbca9dc3159", "Carl C Reith"],
  ["731b734d-da5b-54fc-8fe5-2a32177324e4", "Gertrude M Reith"],
  ["958f1e49-04cd-57ee-a5ad-8c4a2435f218", "John W Reith"],
  ["868d7deb-24bf-590e-8031-3384122e9349", "Robert Reitzer"],
  ["b43512c5-8aff-5a91-8346-b1511411524b", "John W Rejda"],
  ["65947684-b11c-573a-acdd-c260abed58fc", "Steve Rejko"],
  ["2b078bb5-fe2b-50de-8b32-98add415d416", "Herbert G Reller"],
  ["5ca52071-3eb7-56b7-8a3f-d8ff4111ab41", "Erich M Remarque"],
] as const;

const officialIdentityProfiles = [
  "aac6d7b5-5889-569d-8744-56c32fc878e8",
  "dd15fe61-0db8-5d91-a2e4-4803a3e35d2d",
  "fd716d32-bb72-5da8-bddf-91d659b0f36a",
  "2b22eec2-56ff-5180-a16f-2fddb3ba1426",
  "17e66692-47f8-551f-90b4-a30f7a4a9d57",
  "e2ade996-28ed-50ab-8719-22895ce77a85",
  "7495006f-5930-5e3b-934f-abbca9dc3159",
  "958f1e49-04cd-57ee-a5ad-8c4a2435f218",
  "65947684-b11c-573a-acdd-c260abed58fc",
] as const;

test("Batch 796 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 796 publishes official identity evidence without inventing employers", async ({ page }) => {
  for (const id of officialIdentityProfiles) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/official (Army|service)/i);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Reiter publishes a qualified last civilian employer, not an immediate affiliation", async ({ page }) => {
  await page.goto("./people/65c9eade-0071-539f-9949-d5ec35280aba/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Krause's Cafe");
  await expect(main).toContainText("medium");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).toContainText("Gilbert Reiter Obituary");
});

test("Remarque publishes immediate self-employment and earlier editorial roles", async ({ page }) => {
  await page.goto("./people/5ca52071-3eb7-56b7-8a3f-d8ff4111ab41/");
  const main = page.locator("main");
  await expect(main).toContainText("Erich Maria Remarque");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("Self-employed");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Self-employed");
  await expect(main).toContainText("Echo Continental");
  await expect(main).toContainText("Sport im Bild");
  await expect(main).toContainText("Erich Maria Remarque: In Depth");
  await expect(main).toContainText("Emigration in die USA 1939-1949");
});

test("Reitzer publishes identity and OSS service without an employer claim", async ({ page }) => {
  await page.goto("./people/868d7deb-24bf-590e-8031-3384122e9349/");
  const main = page.locator("main");
  await expect(main).toContainText("Sous-Lieutenant Robert Reitzer, Army of France");
  await expect(main).toContainText("Robert Reitzer - Distinguished Service Cross");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 796 keeps both Army-name conflicts explicit and employer-free", async ({ page }) => {
  for (const [id, conflictingName] of [
    ["508cbc69-1270-51b9-9468-39c178ca2afe", "REECE MICHAEL M"],
    ["2b078bb5-fe2b-50de-8b32-98add415d416", "ROLLER HERBERT G"],
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText("conflict");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("home page exposes the rebuilt Batch 796 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,300");
  await expect(home).toContainText("47.20%");
  await expect(home).toContainText("12,634");
  await expect(home).toContainText("812");
  await expect(home).toContainText("366");
  await expect(home).toContainText("9,761");
});
