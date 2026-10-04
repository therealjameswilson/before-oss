import { expect, test } from "@playwright/test";

const profiles = [
  ["012fa262-c41a-5003-a981-d64bc38c635f", "Arthur H Onthank"],
  ["06582c51-2843-5488-aa29-1dfebc11c0f4", "Frank Oprandy"],
  ["1cd07395-2440-5460-991c-677ebf88f831", "Thaddeus W Opalinski"],
  ["3a89d518-c2f7-5b14-83ab-e04cf0366042", "Paul J Onofer"],
  ["40f2bbba-6fc7-5ca6-8de3-a0bfefe0303e", "Etienne Oostendorp"],
  ["42242d58-d549-59fd-a1fc-e2bbc9bfdba2", "Harry Oppenheimer"],
  ["456036c5-420a-5bbf-b764-23ef492de86e", "John J Opyd"],
  ["52da3c40-c241-548a-b162-0988cbb6fdb0", "Charles D Orangers"],
  ["5ca3a0ba-7656-52d8-9af1-0f83ca66918f", "Henry Oosthoer"],
  ["647000f0-dc42-5152-8658-96311c6270c1", "Frederick Orbach"],
  ["79d4f90a-875a-5094-a4ec-90065955604e", "Walter Oney"],
  ["7e3aaea8-79e4-5b84-b9a8-9d77ac700eb9", "Elmer M Opdahl"],
  ["987a02ad-5111-50f6-b74d-ef73e9ffa344", "Richard Opfar"],
  ["992aba49-dca2-594c-8224-403fbf193135", "Jo K Ong"],
  ["9e2e63b3-1871-5585-b604-dcb2401430bb", "Arthur Oppedisano"],
  ["ab004ee2-298a-5810-ad84-654de7570fc4", "James B Opsata"],
  ["ae797b6a-495d-5edd-a696-f5f4c83f0ac2", "Betty T Oppenheim"],
  ["ba2b62fa-633d-50aa-8096-a698b020e9d1", "Donald W Orahood"],
  ["c86ffdcc-a3d9-5c98-a790-3a763d85d88d", "Susan Oppenheim"],
  ["d411088c-4c3e-59df-97b7-3ea365679a79", "James F Opsahl"],
  ["dcfdf978-f138-5b06-9bbf-805911aaeaf6", "Arthur Oppenheimer"],
  ["e82e3792-133e-50a9-a88e-6898b8bf65fc", "Siegfried Oppenheim"],
  ["f35896cf-0a10-5d9b-bcf8-7b051a294c76", "Felix E Oppenheim"],
] as const;

test("Batch 721 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 721 publishes Arthur Onthank's date-bounded War Department work", async ({ page }) => {
  await page.goto("./people/012fa262-c41a-5003-a981-d64bc38c635f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("War Department Civilian Personnel Division");
  await expect(main).toContainText("Director of Personnel");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Signal Corps Information Letter");
});

test("Batch 721 publishes Arthur Oppenheimer's civilian and military chronology", async ({ page }) => {
  await page.goto("./people/dcfdf978-f138-5b06-9bbf-805911aaeaf6/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Office of Price Administration");
  await expect(main).toContainText("Bloomingdale Brothers");
  await expect(main).toContainText("Quartermaster Corps");
  await expect(main).toContainText("Information Digest");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Last civilian employer before service");
});

test("Batch 721 distinguishes James Opsata's COI predecessor assignment", async ({ page }) => {
  await page.goto("./people/ab004ee2-298a-5810-ad84-654de7570fc4/");
  const main = page.locator("main");
  await expect(main).toContainText("James Ball Opsata");
  await expect(main).toContainText("Coordinator of Information");
  await expect(main).toContainText("Personnel Officer");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("U.S. Department of Labor");
});

test("Batch 721 preserves Felix Oppenheim's protected-identifier conflict", async ({ page }) => {
  await page.goto("./people/f35896cf-0a10-5d9b-bcf8-7b051a294c76/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("WPPENHNIM FELIX");
});

test("Batch 721 preserves Susan Oppenheim's printed alias fragment", async ({ page }) => {
  await page.goto("./people/c86ffdcc-a3d9-5c98-a790-3a763d85d88d/");
  const main = page.locator("main");
  await expect(main).toContainText("aka Gjer");
  await expect(main).toContainText("requires archival review");
});

test("Batch 721 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,621");
  await expect(main).toContainText("40.19%");
  await expect(main).toContainText("14,313");
  await expect(main).toContainText("731");
  await expect(main).toContainText("328");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Arthur Oppenheimer");
});
