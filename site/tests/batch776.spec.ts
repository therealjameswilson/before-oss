import { expect, test } from "@playwright/test";

const profiles = [
  ["9555da07-494b-5ace-a674-6fea4349a437", "Vangjel Prifti"],
  ["905c69cc-ae5b-590d-9de8-c452ad4101d7", "Agnes M Prime"],
  ["06dcfd6e-da5b-597a-a4e6-8a98f0d4bd61", "Russell G Primeaux"],
  ["6d7bb300-141a-56b2-af3f-57840728c0b9", "Kenneth L Primm"],
  ["25ea163b-67fe-5430-b303-b8d636fe610a", "Ruth N Primm"],
  ["cf306bba-93df-5cad-ab10-19b824d99b55", "George H Primmer"],
  ["6d387d9f-c5fa-5329-a1b8-794e0df08cd9", "Elizabeth A Prince"],
  ["6bb3da4b-8e75-5b80-8952-68e0c3c5a8dc", "Roland Prince"],
  ["4765225a-7485-57ab-a86d-7cbf02293c4f", "Salvatore T Principato"],
  ["4785b37c-8ffc-53a3-b876-cb533932b1ef", "James P Prindle"],
  ["100a5aae-dcf0-5fb6-a4fd-71154af3d56d", "Glen E Pringle"],
  ["9fb65a31-bede-51f1-a646-8ad394bcc0c4", "Katharine Pringle"],
  ["d031f59c-c5f8-5cfb-9fa0-d7a2fdbd75d2", "Ralph P Pringle"],
  ["af920d23-d9ea-5aef-b0cd-9cd0663147d6", "Nick Prioletti"],
  ["52784845-88ec-5e13-a4e1-d7ea5b4f3099", "Roger A Prior"],
  ["0a0d95d0-f59e-5d5d-9a6a-baa7d93ad621", "Raymond W Priore"],
  ["8c2f73a0-83db-5934-81c8-a5b9c5e7ae36", "Dolores M Pristow"],
  ["02f8ed6a-8423-5a97-852e-5c13fa3a82a8", "Edgar A Pritchard"],
  ["19dbeaab-1fc9-5ae5-bc42-1cd719bd6e85", "George K Pritchard"],
  ["f43aeb08-1e2b-5389-866a-ba93dd69e54a", "Nancy M Pritchard"],
  ["9f1a2f2d-1bc6-5964-b4f0-f013d53be929", "Wayne A Pritchard"],
  ["3fb9d917-6adb-5aa0-a8f7-d0f904a2101c", "James J Prizio"],
  ["851049f9-9e2e-59ca-ae12-ce72e1770184", "Mario J Procaccini"],
] as const;

test("Batch 776 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 776 qualifies Katharine Pringle's OWI pathway and earlier Time employment", async ({ page }) => {
  await page.goto("./people/9fb65a31-bede-51f1-a646-8ad394bcc0c4/");
  const main = page.locator("main");
  await expect(main).toContainText("Katharine Douglas Massel");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Office of War Information",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "medium",
  );
  await expect(main).toContainText("Time, Inc.");
  await expect(main).toContainText("documented prewar");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 776 keeps Edgar Pritchard's conflicting row separate", async ({ page }) => {
  await page.goto("./people/02f8ed6a-8423-5a97-852e-5c13fa3a82a8/");
  const main = page.locator("main");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("Edgar A Prichard; Edgar A Pritchard");
  await expect(main).toContainText("conflicting");
  await expect(main).not.toContainText("company clerk");
  await expect(main).not.toContainText("Tulsa journalist");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 776 keeps Nancy Pritchard separate from Nancy Prichard", async ({ page }) => {
  await page.goto("./people/f43aeb08-1e2b-5389-866a-ba93dd69e54a/");
  const main = page.locator("main");
  await expect(main).toContainText("ambiguous");
  await expect(main).toContainText("Compare Boxes 620 and 621");
  await expect(main).not.toContainText("Smithsonian Astrophysical Observatory");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 776 publishes Army identities without converting occupation codes into employers", async ({ page }) => {
  for (const id of [
    "06dcfd6e-da5b-597a-a4e6-8a98f0d4bd61",
    "6bb3da4b-8e75-5b80-8952-68e0c3c5a8dc",
    "4765225a-7485-57ab-a86d-7cbf02293c4f",
    "100a5aae-dcf0-5fb6-a4fd-71154af3d56d",
    "af920d23-d9ea-5aef-b0cd-9cd0663147d6",
    "0a0d95d0-f59e-5d5d-9a6a-baa7d93ad621",
    "3fb9d917-6adb-5aa0-a8f7-d0f904a2101c",
    "851049f9-9e2e-59ca-ae12-ce72e1770184",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("enlisted army personnel");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
    await expect(main).toContainText("coded occupation is not employer evidence");
  }
});

test("home page exposes the rebuilt Batch 776 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,848");
  await expect(home).toContainText("45.32%");
  await expect(home).toContainText("13,086");
  await expect(home).toContainText("794");
  await expect(home).toContainText("355");
  await expect(home).toContainText("9,307");
});
