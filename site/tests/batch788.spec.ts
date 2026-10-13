import { expect, test } from "@playwright/test";

const profiles = [
  ["91ce54fe-df5b-5ae8-9895-1180dd092913", "Joseph J Randazza"],
  ["3c8ff0a4-1b43-58d2-814c-487d239281b3", "James L Randles"],
  ["e87ece59-9b78-5655-9765-59e12451773d", "Dorothy G Randolph"],
  ["744e54c0-a7e7-5704-8559-603c8e448466", "Stephen T Randolph"],
  ["917d511f-6d8e-550c-a370-8eb55568ff60", "Richard A Rankin"],
  ["f4887f88-5b29-5975-beb5-09370cb58b0c", "James F Ranney"],
  ["92aeba29-2a13-56d0-96ae-2e8092d80330", "Filomena C Rano"],
  ["938d9600-399b-560a-a5c1-e678ab4fa976", "Josephine E Ransburg"],
  ["3549f90b-7090-5e79-a073-194e009491f4", "Paul B Ranslow"],
  ["d789c031-c056-5bd1-8684-fd427f2487a1", "Joseph S Ransmeier"],
  ["1acde04e-13d0-5539-bb90-5db18906feab", "Robert C Ransom"],
  ["cac14657-3aba-5a7f-addf-96b0fcb7b36d", "Robert E Ransom"],
  ["25e6c91e-b982-5fd2-aa26-1a6c3f4a22b2", "Thomas J Ransom"],
  ["28c5023e-2399-5699-b21a-5dd0b885ce6b", "Thomas J Ranson"],
  ["fc0fc9a9-2c37-5725-bfd1-32a4c897cad4", "Wesley E Ranta"],
  ["9d2f3941-71f2-5d43-953f-c03498eb741a", "Charlotte M Rantoul"],
  ["a30ab6fd-8bf8-5498-81bf-15e7ee7d2c1a", "Vincent P Rao"],
  ["0601485f-c5b3-5824-a874-96935e394e09", "* Raoul"],
  ["86fd0d8c-ca23-5721-a58c-c0dd426e5325", "Richard Raoul-Duval"],
  ["2a6391b9-a8e6-5e82-849f-2cb39f49cd9f", "Richard Raoul-Duval"],
  ["c53c3115-c159-5671-b4b1-9225df05854f", "Bergen B Rapalyea"],
  ["9d85ee60-f05b-5d2b-94ff-7ef20b720d60", "Bergen B Rapalyea"],
  ["05e018e5-6dd8-528f-b252-358aabaa3a39", "Michel Rapaport"],
] as const;

test("Batch 788 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 788 publishes Ransmeier's last civilian employer separately from earlier affiliation", async ({ page }) => {
  await page.goto("./people/d789c031-c056-5bd1-8684-fd427f2487a1/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Vanderbilt University");
  await expect(main).toContainText("Instructor in economics");
  await expect(main).toContainText("Brookings Institution");
  await expect(main).toContainText("Research Fellow");
  await expect(main).toContainText("Dartmouth Alumni Magazine");
  await expect(main).toContainText("strongly date bounded");
});

test("Batch 788 qualifies Raoul-Duval's 1938 legal practice and does not invent a bank employer", async ({ page }) => {
  await page.goto("./people/2a6391b9-a8e6-5e82-849f-2cb39f49cd9f/");
  const main = page.locator("main");
  await expect(main).toContainText("Self-employed legal practice");
  await expect(main).toContainText("Attorney");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("Hibernia Bank Building");
  await expect(main).toContainText("building is treated only as an address");
});

test("Batch 788 preserves both duplicate clusters without merging their source rows", async ({ page }) => {
  for (const ids of [
    ["86fd0d8c-ca23-5721-a58c-c0dd426e5325", "2a6391b9-a8e6-5e82-849f-2cb39f49cd9f"],
    ["c53c3115-c159-5671-b4b1-9225df05854f", "9d85ee60-f05b-5d2b-94ff-7ef20b720d60"],
  ] as const) {
    const groups: string[] = [];
    for (const id of ids) {
      await page.goto("./people/" + id + "/");
      const main = page.locator("main");
      await expect(main).toContainText("Duplicate group");
      const text = await main.textContent();
      const match = text?.match(/duplicate-[0-9a-f]+/);
      expect(match).toBeTruthy();
      groups.push(match![0]);
    }
    expect(groups[0]).toBe(groups[1]);
  }
});

test("Batch 788 exposes the Ransom and Rao conflicts without full protected identifiers", async ({ page }) => {
  for (const [id, counterpart] of [
    ["25e6c91e-b982-5fd2-aa26-1a6c3f4a22b2", "Paul P Christopher"],
    ["a30ab6fd-8bf8-5498-81bf-15e7ee7d2c1a", "Joseph Veselinovich"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(counterpart);
    const serial = await main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]").textContent();
    expect(serial).toMatch(/^••••\d{4}$/);
  }
});

test("Batch 788 preserves clipped notes exactly", async ({ page }) => {
  for (const [id, note] of [
    ["e87ece59-9b78-5655-9765-59e12451773d", "photogra"],
    ["917d511f-6d8e-550c-a370-8eb55568ff60", "Record"],
    ["25e6c91e-b982-5fd2-aa26-1a6c3f4a22b2", "Honorab"],
    ["0601485f-c5b3-5824-a874-96935e394e09", "no first n"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText(note);
  }
});

test("home page exposes the rebuilt Batch 788 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,122");
  await expect(home).toContainText("46.46%");
  await expect(home).toContainText("12,812");
  await expect(home).toContainText("805");
  await expect(home).toContainText("360");
  await expect(home).toContainText("9,581");
});
