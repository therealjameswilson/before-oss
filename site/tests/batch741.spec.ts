import { expect, test } from "@playwright/test";

const profiles = [
  ["1e6fadb9-0dad-5264-a12a-33ce642001e9", "Willard E Paxton"],
  ["afa7f700-3f06-5b70-90f8-044c2127a539", "Oliver H Paxton III"],
  ["5c5382b0-402f-56f7-8316-95c6af207937", "Francisque Paye"],
  ["9399b141-2fb8-5372-a25e-386586b9757a", "George A Payne"],
  ["6e3021c3-2224-5ea8-98b8-728607c72a46", "June W Payne"],
  ["4946949b-9158-56b9-82f9-080959706cc7", "Valentine Payne"],
  ["1a138590-8168-59e1-9994-558f4a83d906", "Virginia A Payne"],
  ["0b2ce3e3-f43d-5543-8fa4-d6cb0e8fcda2", "Henry M Paynter"],
  ["a30eca4a-bf65-553d-9c58-e432482ef941", "Jane Payson"],
  ["7b544df0-5a09-51a8-b9fe-278df90fedd2", "* Pcheny"],
  ["6ccbeed7-f468-5314-af1f-cffe55c1d5ce", "Natica Peabody"],
  ["111009ae-00e8-5b98-a666-5b80c2e06160", "Clarence E Peacock"],
  ["d4281dfe-3c68-5f00-8e56-f325a178d664", "Bryant O Pearce"],
  ["d1e98661-446c-5b22-9fb4-be910e28c4cc", "Charles A Pearce"],
  ["b98b6881-0482-5db8-a69c-869f7ea72c24", "Dorois C Pearce"],
  ["8d55a75a-8341-5e08-bc4c-d64220b0ceaf", "Frank J Pearce"],
  ["0e463550-b8cf-5b6c-96fd-f2dfe1127687", "George W Pearce"],
  ["fe689d05-94a6-5441-b927-1b5d329b6df1", "Hollingsworth, Pearce"],
  ["4b94dc56-43cb-5baf-aab7-6b31e1d8b845", "Joseph T Pearce"],
  ["f621205f-65b7-5ad3-858a-034390182f66", "Ronald H Pearce"],
  ["b03dcfb4-8a50-50f0-920e-df4ebf1da327", "Stanley R Pearce"],
  ["232f256d-3e77-593c-8843-1349703579af", "Dorothy N Pearson"],
  ["e3f0634d-11c6-5b14-8097-a44ef4c79f5e", "Eric E Pearson"],
] as const;

test("Batch 741 publishes all 23 page-361 profiles with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\d{4,8}$/);
  }
});

test("seven exact Army matches publish identity evidence without invented employers", async ({ page }) => {
  for (const id of [
    "1e6fadb9-0dad-5264-a12a-33ce642001e9",
    "111009ae-00e8-5b98-a666-5b80c2e06160",
    "d1e98661-446c-5b22-9fb4-be910e28c4cc",
    "8d55a75a-8341-5e08-bc4c-d64220b0ceaf",
    "0e463550-b8cf-5b6c-96fd-f2dfe1127687",
    "4b94dc56-43cb-5baf-aab7-6b31e1d8b845",
    "e3f0634d-11c6-5b14-8097-a44ef4c79f5e",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Oliver Paxton keeps the Paxson surname and suffix conflict visible", async ({ page }) => {
  await page.goto("./people/afa7f700-3f06-5b70-90f8-044c2127a539/");
  const main = page.locator("main");
  await expect(main).toContainText("Oliver H Paxson");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Paxton versus Paxson");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("incomplete and unusual index wording remains visible", async ({ page }) => {
  await page.goto("./people/7b544df0-5a09-51a8-b9fe-278df90fedd2/");
  await expect(page.locator("main")).toContainText("no first n");
  await expect(page.locator("main")).toContainText("asterisk");

  await page.goto("./people/fe689d05-94a6-5441-b927-1b5d329b6df1/");
  await expect(page.getByRole("heading", { name: "Hollingsworth, Pearce", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("trailing comma");

  await page.goto("./people/b98b6881-0482-5db8-a69c-869f7ea72c24/");
  await expect(page.locator("main")).toContainText("Dorois");
  await expect(page.locator("main")).toContainText("rather than silently corrected");
});

test("Batch 741 rebuilds exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("10,075");
  await expect(main).toContainText("42.09%");
  await expect(main).toContainText("13,859");
  await expect(main).toContainText("751");
  await expect(main).toContainText("335");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
