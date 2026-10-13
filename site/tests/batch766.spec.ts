import { expect, test } from "@playwright/test";

const profiles = [
  ["f17817b5-7caf-5028-9e85-606b382b432f", "Seymour J Pomrenze"],
  ["01bcb07d-cd2c-57c8-8174-8ab1206792dd", "Jick Pon"],
  ["b1da1eeb-6127-5057-a1b4-350a0cc9d600", "John M Pon"],
  ["5e689692-76e1-5147-8db0-72ac978de221", "Clayton C Pond"],
  ["4aeabacf-69f1-5965-96d6-5320184448c8", "Jeanette Pond"],
  ["56474ed6-1ab8-5bb6-bc81-e16729262ca0", "William J Pond"],
  ["fd9a5e60-b2a6-5599-a533-f36e18b90b94", "Dirk Ponderoyen"],
  ["a97bd776-854f-5632-9c7b-2e18737a1319", "Curt L Ponger"],
  ["22c3a79f-25f9-590d-98a0-0a6dd732ba36", "William J Pontarelli"],
  ["25524ae0-f288-527d-adf0-db18662e3451", "Inez M Pontier"],
  ["8df7798f-f72a-5f77-807c-0c8a6026c642", "Samuel F Pontier"],
  ["b17991ad-7f1e-566e-8c38-eacf9b438594", "Ralph Ponton"],
  ["2baa93dc-7b31-5c51-8eb9-81e674cbf3cf", "Floyd S Pool"],
  ["e4767ec5-4474-54fc-b93e-04327cb8d62e", "Albert B Poole"],
  ["347780e2-7bfd-5484-9ac4-175c9f15b169", "Barbara M Poole"],
  ["9e3e40d7-4472-5c2c-bd55-dff74725eb2e", "Burnell Poole"],
  ["a23491d5-dd58-5d96-bc66-6aab0753d26e", "Corinne M Poole"],
  ["c9accc19-41c3-51ce-b173-2a51b4eea522", "DeWitt C Poole"],
  ["b36c10d0-35dd-5322-8253-50c053831fbf", "Edward D Poole"],
  ["f62520cd-48c3-5252-8a41-b5810aaa1b55", "Janet Poole"],
  ["3e8debd8-58b6-521d-9b17-96f437d7477a", "Kenyon Poole"],
  ["53d70ca4-1a8b-5abc-b670-b7492420dfd5", "Margeret C Poole"],
] as const;

test("Batch 766 publishes all 22 page profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 766 separates Seymour Pomrenze's Army pathway from civilian employment", async ({ page }) => {
  await page.goto("./people/f17817b5-7caf-5028-9e85-606b382b432f/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("United States Army");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("National Archives");
  await expect(main).toContainText("Works Progress Administration historic records survey in Chicago");
  await expect(main).toContainText("Sholom Jacob Pomrenze");
});

test("Batch 766 publishes Curt Ponger's supported identity without inferring an employer", async ({ page }) => {
  await page.goto("./people/a97bd776-854f-5632-9c7b-2e18737a1319/");
  const main = page.locator("main");
  await expect(main).toContainText("former OSS officer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 766 preserves the Floyd Pool identifier conflict", async ({ page }) => {
  await page.goto("./people/2baa93dc-7b31-5c51-8eb9-81e674cbf3cf/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("BEINHORN CHARLES A JR");
  await expect(main).toContainText("do not transfer Army metadata");
});

test("Batch 766 withholds probable and ambiguous biographies pending Box 611", async ({ page }) => {
  await page.goto("./people/5e689692-76e1-5147-8db0-72ac978de221/");
  await expect(page.locator("main")).toContainText("PONF");
  await expect(page.locator("main")).toContainText("probable");
  await page.goto("./people/3e8debd8-58b6-521d-9b17-96f437d7477a/");
  await expect(page.locator("main")).toContainText("Kenyon E. Poole");
  await expect(page.locator("main")).toContainText("plausible distinctive-name candidate");
  await expect(page.locator("main").locator("section[aria-labelledby='civilian-employer']")).not.toContainText("verified");
});

test("home page exposes the rebuilt Batch 766 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,620");
  await expect(home).toContainText("44.36%");
  await expect(home).toContainText("13,314");
  await expect(home).toContainText("785");
  await expect(home).toContainText("349");
  await expect(home).toContainText("9,078");
});
