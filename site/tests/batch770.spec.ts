import { expect, test } from "@playwright/test";

const profiles = [
  ["d231dee4-0fb5-5ad4-8229-068c4d8c6280", "John M Potter"],
  ["24aa9a73-cafd-5244-9f38-627f46049dda", "Judith D Potter"],
  ["6d3c6212-6074-562e-9412-245dc6f18764", "Julius A Potter"],
  ["78e40151-4731-55da-a144-995f7be749fb", "Margaret L Potter"],
  ["3f62c48e-5546-5239-a69b-f7b1bebfb6bb", "Philip B. K. Potter"],
  ["c4b20b70-68b6-58a2-a812-edd16ba89869", "Virginia L Potter"],
  ["8cb2e349-539a-551c-af40-17480ea4bb42", "Warwick Potter"],
  ["1ef746d8-fbf9-5f1a-ab3c-2aa98ba3ac86", "Louis E Pottier"],
  ["830f5cab-4e18-5659-87ed-9ce50b93ca9d", "Benjamin R Potts"],
  ["605dca30-e49c-583a-8907-58ad4537add0", "Addie G. B. Pougher"],
  ["f3fef609-c8af-52a1-acc1-f81575210b36", "Theodore J Poulakos"],
  ["61db9c4c-9ae9-54bd-a4f5-829163170e89", "John A Poulicos"],
  ["f551c1dc-8cab-5730-b203-53ed3d1c0f87", "Arris Poulos"],
  ["5309b83b-09dd-5554-9c44-d88eb790b5cd", "Sam C Poulos"],
  ["f5a7af0a-fde1-5a17-a835-527956a4c5ae", "Jens A Poulsson"],
  ["6526cfc5-f1e0-581d-8196-ec7cf761bf9e", "David C Poulton"],
  ["fc8a0d0f-ee62-5f65-bca5-8ecebcbc45c9", "Willie S Pounds"],
  ["0be14101-7679-55b4-8ec3-b0f560a253dd", "Daniel Pounovich"],
  ["c6cd3564-a211-5b0a-975f-f44754ad8229", "Vincent V Poveromo"],
  ["aaee086e-6cab-54a7-be8f-a84d3a8a4bce", "Joti Povnsobhon"],
  ["a3f6f7fd-776b-5d4a-8722-4b446d7b9c0e", "Edward A Povrasnik"],
  ["511aadfd-2f8a-5a37-ad68-204695e51b43", "Charles W Powell"],
  ["221920b1-3a20-544f-889f-731e2c6d553e", "Davis B Powell"],
  ["32d16225-a415-5969-8f0d-0a85ef2fa5f0", "Davis B Powell"],
] as const;

test("Batch 770 publishes all 24 page profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 770 separates Warwick Potter's documented State Guard service from unresolved civilian employment", async ({ page }) => {
  await page.goto("./people/8cb2e349-539a-551c-af40-17480ea4bb42/");
  const main = page.locator("main");
  await expect(main).toContainText("New York State Guard");
  await expect(main).toContainText("regiment member");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("Special Operations chief operations officer");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 770 publishes Jens-Anton Poulsson's qualified training and Allied military pathway", async ({ page }) => {
  await page.goto("./people/f5a7af0a-fde1-5a17-a835-527956a4c5ae/");
  const main = page.locator("main");
  await expect(main).toContainText("Jens-Anton Poulsson");
  await expect(main).toContainText("2nd Division officer's candidate school");
  await expect(main).toContainText("Norwegian Independent Company 1");
  await expect(main).toContainText("student");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("not proven immediately pre-OSS");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 770 preserves the two Davis B Powell rows without merging their status or identifiers", async ({ page }) => {
  await page.goto("./people/221920b1-3a20-544f-889f-731e2c6d553e/");
  const civilian = page.locator("main");
  await expect(civilian).toContainText("CAF-9");
  await expect(civilian).toContainText("cannot be merged with the separate T/Sgt");
  await expect(civilian).not.toContainText("Davis B Powell Jr.");

  await page.goto("./people/32d16225-a415-5969-8f0d-0a85ef2fa5f0/");
  const enlisted = page.locator("main");
  await expect(enlisted).toContainText("T/Sgt");
  await expect(enlisted).toContainText("Davis B Powell Jr.");
  await expect(enlisted).toContainText("separate CAF-9");
});

test("Batch 770 exposes the Joti spelling ambiguity while redacting Benjamin Potts's malformed identifier", async ({ page }) => {
  await page.goto("./people/aaee086e-6cab-54a7-be8f-a84d3a8a4bce/");
  const joti = page.locator("main");
  await expect(joti).toContainText("Joti Povnashon");
  await expect(joti).toContainText("disagree between Povnsobhon and Povnashon");

  await page.goto("./people/830f5cab-4e18-5659-87ed-9ce50b93ca9d/");
  const benjamin = page.locator("main");
  await expect(benjamin).toContainText("••••34E0");
  await expect(benjamin).not.toContainText("1.20634e+0");
  await expect(benjamin).toContainText("[private identifier omitted]");
});

test("Batch 770 Army identity evidence does not turn coded occupations into employers", async ({ page }) => {
  for (const [id] of [profiles[2], profiles[4], profiles[10], profiles[11], profiles[12], profiles[13], profiles[15], profiles[18], profiles[21], profiles[23]]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/official Army|Official Army/);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
  }
});

test("home page exposes the rebuilt Batch 770 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,713");
  await expect(home).toContainText("44.75%");
  await expect(home).toContainText("13,221");
  await expect(home).toContainText("789");
  await expect(home).toContainText("350");
  await expect(home).toContainText("9,171");
});
