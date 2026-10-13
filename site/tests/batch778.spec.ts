import { expect, test } from "@playwright/test";

const profiles = [
  ["57cce77b-c5f3-5c75-9284-dbd141972a94", "George P Prosnik"],
  ["57841eb9-6c1d-5083-8049-80e4a36a82b5", "Walter R Prosser"],
  ["1ea12d19-a7d6-543b-b63f-b6504fd8cc5a", "Willie R Prostov"],
  ["60d56c97-3c22-50b1-879a-8ce34c4c59e0", "George Prott"],
  ["5f5706bd-abea-576b-a72b-3be7f85c6d7f", "Leonard S Prout"],
  ["3cca0106-1caa-58d9-ba9e-650d64dabe13", "Alice R Provensen"],
  ["ca55575c-4c73-5d57-acd6-2b3782c05580", "Charles Provenzano"],
  ["79d8fe44-5bbe-5fd2-8b0c-aca9c769ac82", "Palmiro P Provenzano"],
  ["0c455516-2da1-5b74-8020-a80c6e680173", "Charles N Province"],
  ["53d886e9-557c-550d-a0bd-978f88a262d8", "Earl B Provost"],
  ["a1c5f3ad-23a2-5101-a238-d30198fa2f0e", "Edward A Provost"],
  ["6d7a8f86-cd34-50db-a8a4-f5d4939f9416", "John S Pruden"],
  ["2661dc89-ec5e-50bb-81bf-2195d820c879", "Knox P Pruden"],
  ["09536e2b-c423-5e16-a3a7-a353e9c6303d", "George Prudhomme"],
  ["202eaadd-6e28-5cdb-a79c-5bf97c43925d", "James B Pruett"],
  ["8abd6cca-da2f-5c56-b578-4c8ea2d4dade", "William A Pruett"],
  ["e61dd7d9-8823-57ac-aba6-c74da2e7e396", "Henry A Prunier"],
  ["48a1ab31-5362-5769-9c68-c15a50732e22", "Leonard B Prus"],
  ["1f54094b-2dcb-546f-8e7c-89206a3dfc92", "Delbert A Pryor"],
  ["3db56762-56a0-59ba-9cdf-3b97810e8bc6", "Virginia Pryor"],
  ["5713b5e0-e531-5ecc-b16d-2c7d5a26cb87", "Edward S Przybyla"],
  ["e736da99-65fe-5ca9-801b-c453ebac21ae", "Spero Psarakis"],
  ["4eaf4f0e-c88b-5d97-99e9-484dfb49591b", "Charles D Psilopoulos"],
] as const;

test("Batch 778 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 778 preserves Provensen's clipped note without invention", async ({ page }) => {
  await page.goto("./people/3cca0106-1caa-58d9-ba9e-650d64dabe13/");
  const main = page.locator("main");
  await expect(main).toContainText("Extract fr");
  await expect(main).toContainText("unresolved");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 778 separates Pruden's state job from his military assignment", async ({ page }) => {
  await page.goto("./people/2661dc89-ec5e-50bb-81bf-2195d820c879/");
  const main = page.locator("main");
  await expect(main).toContainText("Ohio Bureau of Motor Vehicles");
  await expect(main).toContainText("auditor");
  await expect(main).toContainText("Ohio National Guard");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("documented prewar");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Batch 778 publishes Prunier's immediate Army path but not a civilian employer", async ({ page }) => {
  await page.goto("./people/e61dd7d9-8823-57ac-aba6-c74da2e7e396/");
  const main = page.locator("main");
  await expect(main).toContainText("Assumption College");
  await expect(main).toContainText("student");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "United States Army",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "explicit immediate",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 778 publishes Provenzano's identity variants without backdating his business", async ({ page }) => {
  await page.goto("./people/ca55575c-4c73-5d57-acd6-2b3782c05580/");
  const main = page.locator("main");
  await expect(main).toContainText("Calogero Provenzano");
  await expect(main).toContainText("enlisted naval personnel");
  await expect(main).toContainText("high confidence");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
  await expect(main).not.toContainText("Art & antiques");
});

test("Batch 778 publishes Virginia Pryor and Spero Psarakis as identities, not employers", async ({ page }) => {
  await page.goto("./people/3db56762-56a0-59ba-9cdf-3b97810e8bc6/");
  let main = page.locator("main");
  await expect(main).toContainText("Ceylon");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );

  await page.goto("./people/e736da99-65fe-5ca9-801b-c453ebac21ae/");
  main = page.locator("main");
  await expect(main).toContainText("Brooklyn");
  await expect(main).toContainText("Greek Operational Group");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 778 publishes Army identities without converting occupation codes into employers", async ({ page }) => {
  for (const id of [
    "57cce77b-c5f3-5c75-9284-dbd141972a94",
    "5f5706bd-abea-576b-a72b-3be7f85c6d7f",
    "79d8fe44-5bbe-5fd2-8b0c-aca9c769ac82",
    "0c455516-2da1-5b74-8020-a80c6e680173",
    "202eaadd-6e28-5cdb-a79c-5bf97c43925d",
    "5713b5e0-e531-5ecc-b16d-2c7d5a26cb87",
    "4eaf4f0e-c88b-5d97-99e9-484dfb49591b",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("enlisted army personnel");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
    await expect(main).not.toContainText("civilian_occupation_code");
  }
});

test("home page exposes the rebuilt Batch 778 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,894");
  await expect(home).toContainText("45.51%");
  await expect(home).toContainText("13,040");
  await expect(home).toContainText("798");
  await expect(home).toContainText("356");
  await expect(home).toContainText("9,353");
});
