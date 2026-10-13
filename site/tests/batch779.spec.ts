import { expect, test } from "@playwright/test";

const profiles = [
  ["969b2dca-6878-535c-825c-b30431c25aa9", "Alvin G Psinas"],
  ["e9eff6f1-1c20-55bd-bc98-3c6e6520a54a", "George N Psoinos"],
  ["ec019661-ce81-5240-a139-d758bc66769a", "Alexander Psomas"],
  ["4c1e411f-4c25-5533-b3a4-7b52f23d7bfa", "Charles K Ptacek"],
  ["6cd5a2dd-cb25-51f1-bc6d-30dc4bd8ed5b", "Leo F Ptacek"],
  ["70017483-ee7a-5488-9f22-881fede30712", "Alexander L Puccinelli"],
  ["05e4c0c0-b0e9-56b7-bdf7-38ebf335c841", "Edward W Pucel"],
  ["88a1a123-000c-5aca-a576-e8c3b8c05d88", "Margaret R Puchner"],
  ["87acebde-5eb2-5027-95ab-0aeb429c38cc", "Tode Puchovich"],
  ["9a5afad3-5177-5887-8717-7946077bdee2", "Frankie B Puckett"],
  ["16284af6-2fdf-5f9f-9338-ca1cc9f7ed00", "Anna P Puett"],
  ["d802aefb-d40b-5d23-b953-b8b2a64f222d", "Gerald F Puetz"],
  ["c593a385-853a-5a83-8f0c-619914db0e8f", "Arthur Pugh"],
  ["a9485e71-de64-5e2e-8588-04f7bec3d790", "Leon L Pugh"],
  ["884bdc6c-451b-52c0-8fc7-e339e6e62a38", "Robert E Pugh"],
  ["7f547fe4-2311-5f04-ae79-1182857afa4c", "George J Pugliese"],
  ["202d94eb-e39a-5c71-8f66-30852a9c79b5", "Peter N Pugliese"],
  ["b3333944-0241-5a8f-9ec9-12d72f68ee1a", "Peter F Pugliese"],
  ["bc513fee-afb1-5a5a-a314-d38135a50cff", "Vincent Puglisi"],
  ["ec85969c-7715-5b56-b275-fd2ecce5e352", "Udom Puhpadhana"],
  ["a8c83267-d6e5-5db4-8acf-c19d61607457", "Jacques Pujol"],
  ["d0887e38-4f39-51b8-a6fc-5828b2b8474c", "Chester J Pulaski"],
  ["879ead91-5471-59f4-a470-766b0ba3c6a5", "Michael C Puleo"],
] as const;

test("Batch 779 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main.locator("dt").filter({ hasText: /^Serial$/ }).locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 779 publishes Udom Puhpadhana's student affiliation without calling it employment", async ({ page }) => {
  await page.goto("./people/ec85969c-7715-5b56-b275-fd2ecce5e352/");
  const main = page.locator("main");
  await expect(main).toContainText("Miami University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 779 publishes Psoinos's official OSS identity without inventing an employer", async ({ page }) => {
  await page.goto("./people/e9eff6f1-1c20-55bd-bc98-3c6e6520a54a/");
  const main = page.locator("main");
  await expect(main).toContainText("Greek-American radio operator");
  await expect(main).toContainText("Peking");
  await expect(main).toContainText("National Park Service");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
});

test("Batch 779 keeps rejected postwar and duplicate-name leads out of affiliations", async ({ page }) => {
  await page.goto("./people/6cd5a2dd-cb25-51f1-bc6d-30dc4bd8ed5b/");
  let main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toHaveCount(0);

  await page.goto("./people/202d94eb-e39a-5c71-8f66-30852a9c79b5/");
  main = page.locator("main");
  await expect(main).toContainText("separate Peter F Pugliese row");
  await expect(main).toContainText("unresolved");
});

test("Batch 779 preserves literal index notes without silently expanding them", async ({ page }) => {
  await page.goto("./people/7f547fe4-2311-5f04-ae79-1182857afa4c/");
  await expect(page.locator("main")).toContainText("Ind. Arm");
  await page.goto("./people/879ead91-5471-59f4-a470-766b0ba3c6a5/");
  await expect(page.locator("main")).toContainText("French");
});

test("home page exposes the rebuilt Batch 779 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,917");
  await expect(home).toContainText("45.60%");
  await expect(home).toContainText("13,017");
  await expect(home).toContainText("799");
  await expect(home).toContainText("356");
  await expect(home).toContainText("9,376");
});
