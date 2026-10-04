import { expect, test } from "@playwright/test";

const profiles = [
  ["ef9c3a2d-3f3b-553d-b80b-e79b6813c342", "John H Ohara"],
  ["6f3d875c-976a-5761-af02-d1dc30aada97", "Pauline C Ohara"],
  ["d59226fe-9637-5b42-80f4-db3d03b74caf", "Kurt Ohlson"],
  ["463bf9e9-901d-521b-8182-07c40952e230", "Francis Ohshita"],
  ["3327c7d8-ddd2-5f6f-950c-3e4fcc751d87", "Takashi Ohta"],
  ["ae212139-b6b1-5fbd-b91c-3940d0d3684b", "Ole P Oines"],
  ["572b79a3-ab75-5e32-a4e3-f18e2440886d", "Junichiro Oishi"],
  ["0f1c0bd4-cf28-5a02-9390-1be5f3b2f4df", "Leif Oistad"],
  ["7d8766e6-4b66-5e5e-bffb-796de49fd41a", "Tor Ojesdal"],
  ["0a5aedca-8ba4-5b4c-af49-53e324fb7dd0", "Louis A Ojibway"],
  ["35b1b882-ca90-5f6f-9200-e53a1715b57e", "Fred K Okamoto"],
  ["a0420e5a-b06b-5810-b16e-afcd119b6b11", "Mary N Okamoto"],
  ["43628fac-b0a9-59b6-a65c-a5eb12f80b1a", "Tito U Okamoto"],
  ["70a60eb8-7fa7-598f-bb4d-4fe614cbf335", "Yone Okamura"],
  ["bc28c60b-26f8-5e6f-8df6-954b4b07d8a4", "George J Okeefe"],
  ["e01552a7-858b-5c17-85ba-8236ec20dff5", "John H Okeefe"],
  ["dd626e1f-4269-5679-88e5-40722c9f1213", "Daniel G Okeeffe"],
  ["ce6d95d1-c61c-510e-8323-9a141669e0d3", "John P Okeeffee"],
  ["c5afa09a-1e9a-5b39-b3c5-1719e7ee2458", "Alys M Okie"],
  ["8f0cc585-5702-596c-85d5-ea7e20492a4a", "John B Okie"],
  ["e3f40362-ff22-5652-837e-d62274d0efd9", "Setsuji C Okumoto"],
  ["f21406eb-5216-5bd6-9721-52a8acfbe242", "Prince Olaf"],
  ["20c8a88f-3873-5207-8817-0c6cccbf303e", "Aase Olafsen"],
] as const;

test("Batch 716 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 716 distinguishes Louis O'Jibway's military, student, and occupation evidence", async ({ page }) => {
  await page.goto("./people/0a5aedca-8ba4-5b4c-af49-53e324fb7dd0/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Louis Austin O'Jibway");
  await expect(main).toContainText("Cavalry Replacement Training Center, Fort Riley");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("University of New Mexico");
  await expect(main).toContainText("student");
  await expect(main).toContainText("roughneck in oil fields and steel yards");
  await expect(main).toContainText("no employer is named");
});

test("Batch 716 publishes Leif Oistad's immediate military pathway without inventing an oil employer", async ({ page }) => {
  await page.goto("./people/0f1c0bd4-cf28-5a02-9390-1be5f3b2f4df/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("99th Infantry Battalion (Separate)");
  await expect(main).toContainText("Sergeant and ski instructor");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("deckhand on commercial vessels");
  await expect(main).toContainText("no employer is established");
  await expect(main).toContainText("does not establish that Texaco employed Oistad");
});

test("Batch 716 visibly qualifies Takashi Ohta's documented prewar theatre work", async ({ page }) => {
  await page.goto("./people/3327c7d8-ddd2-5f6f-950c-3e4fcc751d87/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Corrected Copy: Invitational Travel Orders");
  await expect(main).toContainText("Provincetown Players");
  await expect(main).toContainText("Maverick Theatre");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("medium C reputable contemporary or scholarly");
  await expect(main).toContainText("A single last civilian employer before wartime or military service has not yet been established");
});

test("Batch 716 publishes accepted Army identities without inventing employment", async ({ page }) => {
  for (const id of [
    "ae212139-b6b1-5fbd-b91c-3940d0d3684b",
    "43628fac-b0a9-59b6-a65c-a5eb12f80b1a",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("nonshared protected identifier agree with Army bulk ordinal");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 716 preserves Prince Olaf's unresolved archival disposition", async ({ page }) => {
  await page.goto("./people/f21406eb-5216-5bd6-9721-52a8acfbe242/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("recomm");
  await expect(main).toContainText("could not be safely connected to Crown Prince Olav");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 716 publishes exact rebuilt coverage and preserves the evidence-threshold oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,506");
  await expect(main).toContainText("39.71%");
  await expect(main).toContainText("14,428");
  await expect(main).toContainText("724");
  await expect(main).toContainText("326");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  const oilDirectory = page.locator("#oil-companies");
  await expect(oilDirectory).not.toContainText("Leif Oistad");
  await expect(oilDirectory).not.toContainText("Louis A Ojibway");
});
