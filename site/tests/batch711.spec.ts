import { expect, test } from "@playwright/test";

const profiles = [
  ["2b0e005a-6426-512b-8367-60b94f87a6b1", "Robert C Nusbaum"],
  ["13b5abf5-04c5-5e42-9eee-caf4226e3ea5", "David T Nutt"],
  ["6b727c34-f717-58e1-b819-db15b1aa1d9c", "Gloria Nuttal"],
  ["49fdb2c2-5fca-592c-b9db-b3ffe14391b2", "Julius Nyarady"],
  ["8e52f53c-4990-5281-b914-a4c108f0fb0c", "Margaret G Nyberg"],
  ["33fc4cd1-2678-5d80-80bf-7314b70c4737", "Paul Y Nyden"],
  ["28d8b74c-f0b2-5eaf-bab3-59c6d7ce12b2", "Seymour Nydorf"],
  ["87b554b2-08a9-518a-aa19-d051e540037b", "June M Nygaro"],
  ["f2eca409-754f-5f6a-bffc-d482eabe2df5", "Hans A Nyholm"],
  ["9594570b-53e5-5d15-8bd2-2a30355bdce8", "Willem A Nyland"],
  ["1242d7f3-8dc6-595b-95cc-e885e7394e8e", "Philip J Nyquist"],
  ["a6315b58-feaa-5f3e-9c37-2c5799b78d9c", "Roger B Oake"],
  ["d20fcb2b-9d28-5a5f-8ee6-6132814d5831", "Frank E Oakes"],
  ["ac76189e-521b-5657-a303-af6aaef86d3e", "John B Oakes"],
  ["27d1379f-7628-5435-83e1-8b7536471335", "Ruth P Oakes"],
  ["6deaa4ae-9ce8-58b8-b1ea-47a7d2196fc7", "Dale W Oakley"],
  ["2512507a-f0e9-539e-ac3e-bd7167c4e3cd", "Emma B Oakley"],
  ["b7fe7ced-f128-5136-96f9-f23f24a85fa3", "Helen M Oakley"],
  ["5e8e5ee7-82b6-5762-8e90-d6672c85b664", "Robert L Oakley"],
  ["7dbfba10-12f1-5eb4-af59-730ad25c57b8", "Hugh F Oates"],
  ["3a7f097e-d73b-508b-9c6a-fd38f5ae6eb7", "William J Oates"],
  ["67a8af3b-f929-5bbf-becb-aa8522538e6a", "William R Oates"],
  ["489e3e9b-444c-51e1-8905-abe49ccb2cab", "Chiura Z Obata"],
] as const;

test("Batch 711 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 711 distinguishes Nusbaum's Army pathway from Harvard student status", async ({ page }) => {
  await page.goto("./people/2b0e005a-6426-512b-8367-60b94f87a6b1/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Harvard College");
  await expect(main).toContainText("Undergraduate student");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 711 publishes Oakes's last civilian employer and earlier newspaper work", async ({ page }) => {
  await page.goto("./people/ac76189e-521b-5657-a303-af6aaef86d3e/");
  const main = page.locator("main");
  await expect(main).toContainText("John Bertram Oakes");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("The Washington Post");
  await expect(main).toContainText("Political and features reporter");
  await expect(main).toContainText("Trenton Times");
  await expect(main).toContainText("1936");
  await expect(main).toContainText("OSS X-2");
});

test("Batch 711 publishes documented prewar roles without inventing OSS sequence", async ({ page }) => {
  await page.goto("./people/f2eca409-754f-5f6a-bffc-d482eabe2df5/");
  let main = page.locator("main");
  await expect(main).toContainText("Hans Alfred Nyholm");
  await expect(main).toContainText("Royal Danish Navy");
  await expect(main).toContainText("Orlogskaptajn");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("sequence relative to OSS");

  await page.goto("./people/489e3e9b-444c-51e1-8905-abe49ccb2cab/");
  main = page.locator("main");
  await expect(main).toContainText("Zoroku Obata");
  await expect(main).toContainText("University of California, Berkeley");
  await expect(main).toContainText("Professor in the Art Practice Department");
  await expect(main).toContainText("1932");
  await expect(main).toContainText("1942");
  await expect(main).toContainText("do not infer OSS service");
});

test("Batch 711 preserves conflicts and withholds the Nyland occupation lead", async ({ page }) => {
  for (const id of [
    "1242d7f3-8dc6-595b-95cc-e885e7394e8e",
    "6deaa4ae-9ce8-58b8-b1ea-47a7d2196fc7",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("conflicting sources");
    await expect(main).not.toContainText("civilian occupation code");
  }

  await page.goto("./people/9594570b-53e5-5d15-8bd2-2a30355bdce8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).not.toContainText("Columbia University");
});

test("Batch 711 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,392");
  await expect(main).toContainText("39.23%");
  await expect(main).toContainText("720");
  await expect(main).toContainText("325");
  await expect(main).toContainText("14,542");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
