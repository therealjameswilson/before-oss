import { expect, test } from "@playwright/test";

const profiles = [
  ["30d3af8b-7da8-5e87-a299-99f2fdd41807", "John B Patterson"],
  ["00ec2917-a4c4-555d-93ed-824310524c7d", "Joseph A Patterson"],
  ["09bb1f16-1717-571e-9868-3d1edcd732a4", "Maureen L Patterson"],
  ["96c4c0a0-fcf8-5dd6-80f4-695ad82ef09a", "Peter Patterson"],
  ["0ec946f1-d3b0-5f25-8b4c-995a16bd366a", "Robert M Patterson"],
  ["6cf7b535-019a-5077-a19e-344b245b8326", "Troy Patterson"],
  ["23c288dd-521d-5571-9cd3-221f1b955ee5", "William N Patterson"],
  ["1cbc6929-487f-52fd-8b6c-fea38fe803a2", "William W Patterson"],
  ["c490f753-bc95-59f6-8f99-7ab2d2455293", "Archimedes L Patti"],
  ["288035c7-eeb1-52d8-ad96-ad638d83da64", "Joseph D Patti"],
  ["10a7c8f4-fd9e-56ca-8b62-52345997e9db", "Donald J Patton"],
  ["b40158fb-766b-5c61-8264-865a1b986e7c", "Elizabeth K Patton"],
  ["653a7e85-1d2a-56d2-97c3-9526a97deed6", "John B Patton"],
  ["f3544f9c-92bd-5a79-b473-1408e3298350", "Mattie C Patton"],
  ["5d6e1de5-1eba-56b6-94de-4c6ce6b9b19f", "Raymond E Patton"],
  ["5937208b-67ae-5ecf-aff0-ee63e4bb0858", "Raymond A Patton"],
  ["6a412ddf-9e28-5ebf-a6b2-f14a7fbad380", "Elizabeth Paul"],
  ["bc59bd79-e2e3-57ce-a0bc-249bbfbea59e", "Elizabeth M Paul"],
  ["8bec3007-3bed-518a-a2f2-46586ab9c6c8", "J G Paul"],
  ["e700aaf6-7111-5ce6-8fa0-3f69d9a0730f", "Miriam U Paul"],
  ["5f8211eb-ce9c-5360-ba4a-8ea3e799a4e0", "Oscar H Paul"],
  ["4b7d27af-409d-5f3c-b797-a2a8e74926a4", "Richard I Paul"],
  ["d8b37178-5670-5724-bb0c-0258e7a913c0", "Robert W Paul"],
] as const;

test("Batch 739 publishes all 23 page-360 profiles with terminal dispositions", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).toContainText("archival review");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\d{4,8}$/);
  }
});

test("Batch 739 publishes four official identity matches without inventing employers", async ({ page }) => {
  for (const id of [
    "00ec2917-a4c4-555d-93ed-824310524c7d",
    "1cbc6929-487f-52fd-8b6c-fea38fe803a2",
    "288035c7-eeb1-52d8-ad96-ad638d83da64",
    "653a7e85-1d2a-56d2-97c3-9526a97deed6",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("official Army");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 739 preserves ambiguous printed notes and identity limits", async ({ page }) => {
  await page.goto("./people/6cf7b535-019a-5077-a19e-344b245b8326/");
  let main = page.locator("main");
  await expect(main).toContainText("Danish c");
  await expect(main).toContainText("truncated");

  await page.goto("./people/288035c7-eeb1-52d8-ad96-ad638d83da64/");
  main = page.locator("main");
  await expect(main).toContainText("French");
  await expect(main).toContainText("does not override");
});

test("Batch 739 keeps Archimedes Patti's pre-OSS claim unresolved", async ({ page }) => {
  await page.goto("./people/c490f753-bc95-59f6-8f99-7ab2d2455293/");
  const main = page.locator("main");
  await expect(main).toContainText("Archimedes L. A. Patti");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("1940 census image");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 739 rejects the British film-pioneer namesake", async ({ page }) => {
  await page.goto("./people/d8b37178-5670-5724-bb0c-0258e7a913c0/");
  const main = page.locator("main");
  await expect(main).toContainText("British film pioneer died in 1943");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 739 rebuilds exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("10,029");
  await expect(main).toContainText("41.89%");
  await expect(main).toContainText("13,905");
  await expect(main).toContainText("748");
  await expect(main).toContainText("334");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
