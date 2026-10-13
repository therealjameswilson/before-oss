import { expect, test } from "@playwright/test";

const profiles = [
  ["88be522f-4eab-5236-896d-19af42a90dba", "Isma L Price"],
  ["10d5f74b-d70a-55f1-bf12-7601f385673a", "John S Price"],
  ["ceb48d3e-df3f-5ba9-8972-9dfba1b75d5a", "Mercer L Price"],
  ["2af69069-4f6d-5179-ad16-076d5f31dd9f", "Norman B Price"],
  ["e4d07dc1-9a4d-56ea-b30d-41f57244d02b", "Norman S Price"],
  ["b9769f99-3acf-5a8b-8a94-61dc692e511c", "Raford C Price"],
  ["a7734958-ca68-5cc6-bada-c1507305cd3e", "Robert R Price"],
  ["164673d2-d30f-550f-b03c-67d4ff16f23e", "Ronald S Price"],
  ["ac6b1f33-22bb-56eb-ba7d-6e2da380f978", "Roy T Price"],
  ["541b8f86-8b8b-57e1-af5d-dfabf694a8fd", "Ursula E Price"],
  ["2249bdc4-154c-5382-b12c-fbdaac63ca49", "Wayne E Price"],
  ["192b5ab4-e4d7-58d4-8ea8-d12e489bf089", "Edgar A Prichard"],
  ["87f4792d-7e57-5f17-a0d1-68e2e36f8cdb", "Nancy M Prichard"],
  ["391e204e-1313-50e1-a460-463ce174ce5c", "Elise D Prickett"],
  ["eb45617b-e5c1-57d3-a263-177c4d160404", "Adolph H Prickril"],
  ["6836562f-9a36-5d89-9182-36a3e7db5e44", "Ellwood Pride"],
  ["2b87fac4-fe30-5e52-8f33-d0cc36e23deb", "Leo I Pride"],
  ["21296795-5042-5bc2-906f-c13654637219", "Walter I Prideaux"],
  ["f87191ae-c4f8-52cc-807a-8475130b59ea", "Raymond G Priebe"],
  ["7894df17-4d5b-59ac-81c4-a3b3428f86bf", "Sylvan A Priebe"],
  ["c499a063-4442-516f-a518-4f7877ba3b7d", "Robert E Prieshoff"],
  ["33780502-4f08-5e68-8758-72624916abd0", "Karl L Priester"],
  ["208a4e35-441a-54b8-81e8-a08061e55b15", "Charles E Prieve"],
] as const;

test("Batch 775 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 775 publishes Nancy Prichard's Smithsonian-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/87f4792d-7e57-5f17-a0d1-68e2e36f8cdb/");
  const main = page.locator("main");
  await expect(main).toContainText("Nancy Montague McCandlish Prichard");
  await expect(main).toContainText("Smithsonian Astrophysical Observatory");
  await expect(main).toContainText("Special Assistant to the Meteorologist");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Smithsonian Astrophysical Observatory",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Smithsonian Astrophysical Observatory",
  );
  await expect(main).toContainText("high confidence");
});

test("Batch 775 retains Raford Price's different-name official-record conflict", async ({ page }) => {
  await page.goto("./people/b9769f99-3acf-5a8b-8a94-61dc692e511c/");
  const main = page.locator("main");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("GRICEFR FORDOL NO N M");
  await expect(main).toContainText("conflicting");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 775 publishes Army identities without converting occupation codes into employers", async ({ page }) => {
  for (const id of [
    "10d5f74b-d70a-55f1-bf12-7601f385673a",
    "2af69069-4f6d-5179-ad16-076d5f31dd9f",
    "e4d07dc1-9a4d-56ea-b30d-41f57244d02b",
    "a7734958-ca68-5cc6-bada-c1507305cd3e",
    "ac6b1f33-22bb-56eb-ba7d-6e2da380f978",
    "2249bdc4-154c-5382-b12c-fbdaac63ca49",
    "6836562f-9a36-5d89-9182-36a3e7db5e44",
    "7894df17-4d5b-59ac-81c4-a3b3428f86bf",
    "c499a063-4442-516f-a518-4f7877ba3b7d",
    "208a4e35-441a-54b8-81e8-a08061e55b15",
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

test("home page exposes the rebuilt Batch 775 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,825");
  await expect(home).toContainText("45.22%");
  await expect(home).toContainText("13,109");
  await expect(home).toContainText("793");
  await expect(home).toContainText("354");
  await expect(home).toContainText("9,284");
});
