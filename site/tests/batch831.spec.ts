import { expect, test } from "@playwright/test";

const profiles = [
  ["2a6693af-f97c-554d-a5af-9caf9e04e0da", "Joseph M F Ryan Jr."],
  ["300f3ff7-3b0e-5c99-80bb-bda371340215", "Keith W Ryan"],
  ["0abf3d38-5377-5db5-a70b-420617a2552a", "Mary A Ryan"],
  ["7f0acd75-97e9-5547-8a3e-6b59adb7129c", "Theodore Ryan"],
  ["0705018d-b573-5a2c-9da4-a276b8670757", "Theodore S Ryan"],
  ["de0538a3-cfb7-5a26-afcf-51cffa590850", "William C Ryan"],
  ["ef1b3efb-7427-5dc3-a59e-1c0442da3e28", "William H Ryan"],
  ["4d1e9ee5-c7d9-5443-a14c-b74d785cd659", "William P Ryan"],
  ["f3d32fd2-05e6-516f-aa70-871bcc25cb3b", "William S Ryan"],
  ["09f0913e-ff37-58a4-b50a-cb14d9d13856", "Albert P Ryavec"],
  ["20623341-a130-593d-8e2b-07394255dbbe", "Robert L Rybovich"],
  ["e15b91af-69c2-57bc-ac51-d097919bcdb4", "Oliver A Ryder"],
  ["3ebafc6b-42ad-55b5-8f43-899b57d4a8f7", "John Rydgis"],
  ["8ba5c2bc-4212-56c6-9529-f805746cd634", "Edward S Rydvinski"],
  ["dbaed9f4-9733-56a7-83c2-7439b14153e9", "William L Rye"],
  ["bf283d62-3881-52dd-a6f4-84fd7e31cfcb", "Viola Rygg"],
  ["3af10459-e1af-52fd-bf9a-c782b890900d", "Steven Ryjewski"],
  ["9851ad5e-31d3-5473-bb2f-acdf57e6ecda", "Joseph M Rzonca"],
  ["0f813310-6042-583a-9151-1bdee1d96a09", "William F Saale"],
  ["e5310f4d-4d3a-5ecb-88e0-6347d7d3d112", "Egro Saarinew"],
  ["02429e2a-5235-51d6-9694-978c6f6155a3", "Manuel Sabat"],
  ["c1f131ea-fd3e-52fc-b79e-56a2c6929480", "Jacques Sabathe"],
  ["0f03f125-68a9-51b3-a68f-ec1a9c074a39", "Gerald V Sabatino"],
] as const;

test("Batch 831 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Joseph Ryan profile presents an Army Air Forces pathway without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/2a6693af-f97c-554d-a5af-9caf9e04e0da/");
  const main = page.locator("main");
  await expect(main).toContainText("Joseph Michael Francis Ryan Jr.");
  await expect(main).toContainText("high confidence");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("United States Army Air Forces");
  await expect(immediate).toContainText("photographic interpreter and weather officer");
  await expect(immediate).toContainText("military assignment");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(civilian).not.toContainText("Saint Joseph");
  await expect(civilian).not.toContainText("UCLA");
});

test("Egro Saarinew profile preserves the index spelling and documents the Eero Saarinen identity bridge", async ({ page }) => {
  await page.goto("./people/e5310f4d-4d3a-5ecb-88e0-6347d7d3d112/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Egro Saarinew", level: 1 })).toBeVisible();
  await expect(main).toContainText("Eero Saarinen");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("printed-name corruption");

  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("Saarinen and Swanson");
  await expect(immediate).toContainText("founding partner, architect and designer");
  await expect(immediate).toContainText("self employment");

  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("Saarinen and Swanson");

  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("Cranbrook Academy of Art");
  await expect(earlier).toContainText("professional affiliation");
});

test("the two Theodore Ryan profiles expose the unresolved pair and withhold the tempting Aspen employer", async ({ page }) => {
  for (const id of ["7f0acd75-97e9-5547-8a3e-6b59adb7129c", "0705018d-b573-5a2c-9da4-a276b8670757"]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("ambiguous");
    await expect(main).toContainText(/Boxes 669 and 670|Box 669 and 670/);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Highland Bavarian Corporation");
  }
});

test("Army identifier conflicts remain visible and do not leak the rejected names as affiliations", async ({ page }) => {
  const cases = [
    ["4d1e9ee5-c7d9-5443-a14c-b74d785cd659", "Pliskin Harold M."],
    ["20623341-a130-593d-8e2b-07394255dbbe", "Tankersley Wallace E."],
    ["3ebafc6b-42ad-55b5-8f43-899b57d4a8f7", "Mc Gowan K D."],
  ] as const;
  for (const [id, conflictingName] of cases) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" })).not.toContainText(conflictingName);
  }
});

test("accepted Army identities publish no coded occupations or unmasked identifiers", async ({ page }) => {
  for (const id of [
    "de0538a3-cfb7-5a26-afcf-51cffa590850",
    "ef1b3efb-7427-5dc3-a59e-1c0442da3e28",
    "09f0913e-ff37-58a4-b50a-cb14d9d13856",
    "dbaed9f4-9733-56a7-83c2-7439b14153e9",
    "c1f131ea-fd3e-52fc-b79e-56a2c6929480",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});
