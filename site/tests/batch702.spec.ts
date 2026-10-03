import { expect, test } from "@playwright/test";

const profiles = [
  ["2814f676-90bb-5655-adb7-3964e5529060", "Martin D Newman"],
  ["a30567d7-fefd-53c6-bd3d-a7c99ad78a14", "Morton Newman"],
  ["edf5ad9f-771d-509c-8910-5efb298f0d0b", "Richard R Newman"],
  ["b86d99db-0389-580c-b509-2208e4a7a696", "Sarah Newman"],
  ["fe6f15c6-72f7-5059-a752-d41cadd25a7d", "William L Newman"],
  ["2c6a2b66-1dc7-52b4-bfa7-f736437bbf9d", "Zelda R Newman"],
  ["32686d09-a3bb-537a-b78d-4d42e83bf9cd", "Franz L Newmann"],
  ["f072c29e-3a6c-55fe-9020-42c8fc7b5aae", "Stephen M Newmark"],
  ["3d150347-863e-56ed-952f-b61a74499d57", "Lester J Newquist"],
  ["f26d435d-c072-5f6e-9cca-8e79177cebfd", "Barbara W Newsham"],
  ["6c884311-ce1f-5b6e-a6d5-9e816ebf4101", "Richard A Newsham"],
  ["b6b02b42-7e65-5805-a167-bd267453c520", "Howard T Newsom"],
  ["de554a5e-8416-5641-9576-313c035fc7ea", "Rubye Newsome"],
  ["92559e51-db2e-59ce-9164-afbcb0f9ea95", "William S Newsome"],
  ["d04089e6-376c-52d8-ba5c-da8b5c8f70f0", "Margaret J Newson"],
  ["2f4105db-5faf-524c-80eb-6a4a5d077772", "Doris C Newton"],
  ["c475f9f1-8e07-5bba-a60b-8c259df4e45f", "Grover R Newton"],
  ["bfbc5982-821f-5743-945b-c7c2ecc8f804", "Vidma Newton"],
  ["87a07727-aa70-5475-8321-c52e1bd0745e", "Harry H Nexhip"],
  ["a9ca12a9-aa4e-5fe3-b3c1-0ca0a6a8b7a8", "Earl J Nichelson"],
  ["ba301451-9f92-51ad-9827-ef6593d39180", "Estelle K Nichnowiitz"],
  ["612a1f0a-55ac-5054-88fe-f4e1b82078d8", "Blake H Nicholas"],
] as const;

test("Batch 702 publishes all 22 direct profile routes with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{7,8}$/);
  }
});

test("Batch 702 publishes Newquist employment as qualified documented prewar evidence", async ({ page }) => {
  await page.goto("./people/3d150347-863e-56ed-952f-b61a74499d57/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Brown Brothers Harriman & Co.");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("not established as the immediate pre-OSS affiliation");
});

test("Batch 702 keeps Army identities separate from employer claims", async ({ page }) => {
  for (const id of [
    "2814f676-90bb-5655-adb7-3964e5529060",
    "a30567d7-fefd-53c6-bd3d-a7c99ad78a14",
    "b6b02b42-7e65-5805-a167-bd267453c520",
    "c475f9f1-8e07-5bba-a60b-8c259df4e45f",
    "bfbc5982-821f-5743-945b-c7c2ecc8f804",
    "612a1f0a-55ac-5054-88fe-f4e1b82078d8",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/b6b02b42-7e65-5805-a167-bd267453c520/");
  await expect(page.locator("main")).not.toContainText("Camco Oil Tool Supply");
});

test("Batch 702 leaves the Nichelson and Nicholson records visible and unmerged", async ({ page }) => {
  await page.goto("./people/a9ca12a9-aa4e-5fe3-b3c1-0ca0a6a8b7a8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("Earl J Nicholson");
  await expect(main).toContainText("remain unmerged");
  await expect(main).toContainText("Boxes 559 and 560");
});

test("Batch 702 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,187");
  await expect(main).toContainText("38.38%");
  await expect(main).toContainText("319");
  await expect(main).toContainText("14,747");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
