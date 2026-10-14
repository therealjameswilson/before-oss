import { expect, test } from "@playwright/test";

const profiles = [
  ["39e40854-28dc-5498-a7e6-39e6d35189ca", "Clement Rault"],
  ["792088ca-2714-5afd-acbc-2406b209c746", "Pierre Ravarre"],
  ["31b17f13-5ba7-5249-ade1-347c9f633377", "Daniel Ravenel"],
  ["d7207755-9c9d-5a79-920e-84a06e6e3a9c", "Joseph D Ravette"],
  ["aea76acd-0679-57df-985f-94bc1435fafe", "David Rawle"],
  ["74d95c31-10b4-587c-918b-b3f9908d8f98", "John M Rawlins"],
  ["5b2e2aae-b777-560d-9fe8-bf020f60a2b2", "Edward Rawlinson"],
  ["e2c3978c-61da-5bda-9db6-681f3dbd6ca1", "Tadeusz Rawski"],
  ["0a1706a1-d99f-5d36-b26d-d70c11efbe0a", "Charles A Rawson"],
  ["b34561d1-ec31-5163-937d-d05898dfaa34", "Ann Ray"],
  ["7a9797b9-e39c-5ac5-95fb-81295495943a", "Bridget Ray"],
  ["b50c06f3-e5f3-5bca-a59c-c28c08dcd719", "David Ray"],
  ["455df9a8-30ee-5255-a83a-480a9e64b236", "Elsie C Ray"],
  ["fa1b6560-9f45-50a0-8855-4aa79c97ca32", "Eugene A Ray"],
  ["96635229-2a4b-5f63-9579-ca761cdf08b7", "George E Ray"],
  ["e10b933a-9ce8-5380-b125-e0a68ad1adcb", "Louis W Ray"],
  ["517bb424-dc13-5a23-b09e-48d885c39dbd", "Helen J Raynolds"],
  ["4517b8f0-f22f-55e5-ac88-f78b4144264f", "Clara M Raynor"],
  ["b4cebddf-f207-585e-be2f-1e34fd1c0750", "Maud M Raynsford"],
  ["95f948ea-b512-5671-9db6-e7a59930df15", "C P Rayon"],
  ["477fc37d-7f2f-54ac-9071-f34aa2eab9e7", "Faris N Razook"],
  ["e41cf94e-17b3-5e01-aba9-c5cad1420dde", "Thomas D Razovich"],
  ["ba934312-c9cc-501e-a8b5-1744eb11c868", "Gregory S Razran"],
] as const;

test("Batch 790 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 790 separates Razran's immediate employer from his earlier affiliation", async ({ page }) => {
  await page.goto("./people/ba934312-c9cc-501e-a8b5-1744eb11c868/");
  const main = page.locator("main");
  await expect(main).toContainText("Gregory S. Razran");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("Queens College");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Queens College");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Columbia University");
  await expect(main).toContainText("statistical consultant");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Queens Name Explorer / Queens College");
  await expect(main).toContainText("TIME");
});

test("Batch 790 publishes Ravarre and Ravenel identity evidence without inventing employers", async ({ page }) => {
  await page.goto("./people/792088ca-2714-5afd-acbc-2406b209c746/");
  let main = page.locator("main");
  await expect(main).toContainText("Jean Vernez");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Service historique de la Défense");
  await expect(main).toContainText("archival review");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("Service historique de la Défense");

  await page.goto("./people/31b17f13-5ba7-5249-ade1-347c9f633377/");
  main = page.locator("main");
  await expect(main).toContainText("Daniel Ravenel Jr.");
  await expect(main).toContainText("Naval Command, OSS Liaison Division");
  await expect(main).toContainText("A Century of U.S. Naval Intelligence");
  await expect(main).toContainText("archival review");
});

test("Batch 790 exposes the Ray Army-name conflicts and preserves masked identifiers", async ({ page }) => {
  for (const [id, armyName] of [
    ["fa1b6560-9f45-50a0-8855-4aa79c97ca32", "R Y EUGENE"],
    ["96635229-2a4b-5f63-9579-ca761cdf08b7", "R Y GEORGE E"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(armyName);
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 790 preserves clipped index notes", async ({ page }) => {
  await page.goto("./people/96635229-2a4b-5f63-9579-ca761cdf08b7/");
  await expect(page.locator("main")).toContainText("photogra");
  await page.goto("./people/4517b8f0-f22f-55e5-ac88-f78b4144264f/");
  await expect(page.locator("main")).toContainText("Record");
});

test("home page exposes the rebuilt Batch 790 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,167");
  await expect(home).toContainText("46.65%");
  await expect(home).toContainText("12,767");
  await expect(home).toContainText("807");
  await expect(home).toContainText("361");
  await expect(home).toContainText("9,627");
});
