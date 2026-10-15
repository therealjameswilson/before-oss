import { expect, test } from "@playwright/test";

const profiles = [
  ["ccbc8188-41c5-5f17-8389-6dc3288a715a", "Ann Rodefeld"],
  ["a1e91808-c582-5b2b-95ca-67ccd4742fab", "James A Rodeghiero"],
  ["468321a5-f1c1-5a97-91e0-a34d4f9d169d", "Fred Rodell"],
  ["78243791-cc76-52be-8f08-067b05807568", "Agnes L Rodenberg"],
  ["cef70047-bf63-5377-8358-8af266eb559f", "Robert R Rodenberg"],
  ["d7cebc36-fe4b-5ab9-8a84-eef081788b79", "Gertrude S Roderick"],
  ["60c9729a-0eda-5c50-ac7d-493ad65ac2c0", "John P Roderick"],
  ["131dd1d4-e4af-5afb-b4d6-e32e3f8cd692", "Robert W Roderick"],
  ["92c57d3b-5722-5c77-aff2-977b09f8891b", "James C Rodes"],
  ["c4ec8458-b419-5c4d-9566-010ae0b1bbd5", "Robert E Rodes"],
  ["5e2d5c68-4ba0-5264-9bb1-fa84410bf43b", "Dorothy M Rodgers"],
  ["7f23c511-8b27-5ea3-824c-fd3903e35a77", "Esther A Rodgers"],
  ["6ed251d8-fec0-52e5-965c-ed222e2d38c4", "George E Rodgers"],
  ["58974f25-9dd2-557d-97aa-ff19a9395fb3", "Gloria Rodgers"],
  ["2c67ee67-ecb3-5c6a-9425-aefce911a660", "Helen P Rodgers"],
  ["66eaa97e-85bb-5b3f-b2b3-14e89fd417ed", "James E Rodgers"],
  ["06f1f060-656f-5355-80cb-c6d8f7aed4e0", "John B Rodgers Jr."],
  ["034c4166-05af-590d-adb2-a6bb1e22e45b", "Herbert R Rodiger"],
  ["cbc6d761-ee00-5f1b-a895-8d72a3620730", "Charles A Rodit"],
  ["c8111905-9186-55c9-bf66-e0b683929f83", "Edouard H Roditi"],
  ["19d49d68-517d-5d98-b9e9-1807c16d7494", "Joseph Rodman Jr."],
  ["6776597b-8e61-5de5-b809-3ce3fe700d62", "Selden Rodman Jr."],
  ["19d3d198-cdc5-56f6-a151-f08ad0a58482", "David Rodnick"],
] as const;

test("Batch 814 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Selden Rodman separates civilian, Army, and student relationships", async ({ page }) => {
  await page.goto("./people/6776597b-8e61-5de5-b809-3ce3fe700d62/");
  const main = page.locator("main");
  await expect(main).toContainText("Common Sense");
  await expect(main).toContainText("last civilian");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("immediate pre-OSS");
  await expect(main).toContainText("Yale University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Guide to the Selden Rodman Papers");
});

test("Fred Rodell exposes the verified Yale Law employment with temporal qualification", async ({ page }) => {
  await page.goto("./people/468321a5-f1c1-5a97-91e0-a34d4f9d169d/");
  const main = page.locator("main");
  await expect(main).toContainText("Yale Law School");
  await expect(main).toContainText("last civilian");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Built by Association: Fred Rodell");
  await expect(main).toContainText("confirmed");
});

test("David Rodnick publishes the NPS role without claiming immediacy", async ({ page }) => {
  await page.goto("./people/19d3d198-cdc5-56f6-a151-f08ad0a58482/");
  const main = page.locator("main");
  await expect(main).toContainText("National Park Service");
  await expect(main).toContainText("Branch of Historic Sites");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
});

test("Edouard Roditi preserves the unresolved OWI chronology", async ({ page }) => {
  await page.goto("./people/c8111905-9186-55c9-bf66-e0b683929f83/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Office of War Information");
  await expect(main).toContainText("does not establish");
  await expect(main).toContainText("Box 654");
});

test("George Rodgers publishes the accepted identity without an inferred employer", async ({ page }) => {
  await page.goto("./people/6ed251d8-fec0-52e5-965c-ed222e2d38c4/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("official Army record");
  await expect(main).toContainText("No reliable pre-OSS employer");
});

test("home page exposes the rebuilt Batch 814 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,707");
  await expect(home).toContainText("48.91%");
  await expect(home).toContainText("12,226");
  await expect(home).toContainText("837");
  await expect(home).toContainText("376");
  await expect(home).toContainText("10,170");
});
