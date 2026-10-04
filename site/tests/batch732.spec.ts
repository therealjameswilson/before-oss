import { expect, test } from "@playwright/test";

const profiles = [
  ["76366ecc-490e-521a-9e8b-708288baee62", "Neal M Panzarella"],
  ["0b46479d-446f-5123-bcde-c2ed96fda4bc", "Emily J Panzarino"],
  ["4f3d4667-5f14-5c4d-9140-bb7a3f056a26", "William E Paone"],
  ["affffb92-b1e4-5199-8282-77623af71636", "Fillipo Papa"],
  ["29281682-12ea-5516-9434-4cbc05741a99", "Constantine Papadopoulos"],
  ["b3ea973d-22a8-5388-8b93-99901e659cbf", "Thomas L Papadopoulos"],
  ["8588a59b-e017-5628-b34d-a86d2fb8cb3e", "Athanasios A Papageorgiou"],
  ["99413406-0145-5d51-8c8c-a3b284e23491", "John N Papajani"],
  ["f174aa11-2e94-509d-b37b-932eefdb7e5c", "Frank M Papale Jr."],
  ["2d0d1b86-72cf-5d0a-95ad-28560edab953", "Nicholas D Papanu"],
  ["6604f4a1-53f9-58e3-9dd6-90acc5415295", "George J Papastrat"],
  ["5c16a499-5dd9-5eb4-920d-94cf515fb7c5", "James Papavassiliou"],
  ["825975ed-8600-589d-b4d8-7795318724aa", "Spiridon Papayiannakis"],
  ["e763ef0c-1dee-57c2-9d7c-092f0e7d1fda", "George Papazoglou"],
  ["abc125a8-a7a8-547d-9023-d055f81923e7", "Arthur A Pape"],
  ["62fce643-db4b-5bd6-af2e-744e9ab8aaff", "Frederick D Pape"],
  ["02bd6250-6fd0-58b5-84a6-f0ce3e600f83", "Pearl S Pape"],
  ["64044eb8-64ff-5413-a8bb-f84195258a7f", "Raymond H Pape"],
  ["538e26fa-5577-5029-a90b-e3f2ebfac801", "Carl J Papenfuss"],
  ["11a617ba-f3d3-5634-948f-e7ed869f1d54", "Arthur A Paper"],
  ["19cb8b27-80d4-536d-8c6f-1e5a932970ed", "Edward M Papierski"],
  ["b6041ee9-6a57-5ccb-83d0-ae1fc0bf92e6", "Silvia Papini"],
  ["fda6e9c7-81ec-5fae-9113-df8f1f43b941", "Arthur D Papoulias"],
  ["a5f9d179-5388-523f-9a32-01bd715ffa9c", "Arthur A Pope"],
] as const;

test("Batch 732 publishes all 23 page-356 profiles and the linked Pope conflict", async ({ page }) => {
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

test("Batch 732 qualifies the 122nd Battalion pathway as military rather than civilian employment", async ({ page }) => {
  for (const [id, name] of [
    ["2d0d1b86-72cf-5d0a-95ad-28560edab953", "Nicholas D Papanu"],
    ["6604f4a1-53f9-58e3-9dd6-90acc5415295", "George J Papastrat"],
    ["5c16a499-5dd9-5eb4-920d-94cf515fb7c5", "James Papavassiliou"],
    ["825975ed-8600-589d-b4d8-7795318724aa", "Spiridon Papayiannakis"],
    ["e763ef0c-1dee-57c2-9d7c-092f0e7d1fda", "George Papazoglou"],
    ["fda6e9c7-81ec-5fae-9113-df8f1f43b941", "Arthur D Papoulias"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("122nd Infantry Battalion (Separate)");
    await expect(main).toContainText("military assignment");
    await expect(main).toContainText("probable immediate");
    await expect(main).toContainText("medium");
    await expect(main).not.toContainText("Last civilian employer before service122nd Infantry Battalion");
  }
});

test("Batch 732 preserves roster variants and official-record conflicts", async ({ page }) => {
  await page.goto("./people/2d0d1b86-72cf-5d0a-95ad-28560edab953/");
  await expect(page.locator("main")).toContainText("Nicholas D Papapanu");
  await expect(page.locator("main")).toContainText("transpos");

  await page.goto("./people/825975ed-8600-589d-b4d8-7795318724aa/");
  await expect(page.locator("main")).toContainText("Spiridon B Papayannakis");

  await page.goto("./people/e763ef0c-1dee-57c2-9d7c-092f0e7d1fda/");
  await expect(page.locator("main")).toContainText("first lieutenant");
  await expect(page.locator("main")).toContainText("captain");

  await page.goto("./people/fda6e9c7-81ec-5fae-9113-df8f1f43b941/");
  await expect(page.locator("main")).toContainText("Arthur J Papoulias");
  await expect(page.locator("main")).toContainText("middle-initial conflict");
});

test("Batch 732 never merges the Pape, Paper, and Pope identifier conflict", async ({ page }) => {
  for (const [id, name] of [
    ["abc125a8-a7a8-547d-9023-d055f81923e7", "Arthur A Pape"],
    ["11a617ba-f3d3-5634-948f-e7ed869f1d54", "Arthur A Paper"],
    ["a5f9d179-5388-523f-9a32-01bd715ffa9c", "Arthur A Pope"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText("Pape, Arthur A Paper, and Arthur A Pope");
    await expect(main).toContainText("remain separate");
  }
});

test("Batch 732 exposes Silvia and Silvio as a conflict rather than a correction", async ({ page }) => {
  await page.goto("./people/b6041ee9-6a57-5ccb-83d0-ae1fc0bf92e6/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Silvia Papini", level: 1 })).toBeVisible();
  await expect(main).toContainText("Silvio Papini");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Box 584");
});

test("Batch 732 rebuilds exact coverage while leaving verified-employer coverage unchanged", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,872");
  await expect(main).toContainText("41.24%");
  await expect(main).toContainText("14,062");
  await expect(main).toContainText("743");
  await expect(main).toContainText("333");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
