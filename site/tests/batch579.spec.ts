import { expect, test } from "@playwright/test";

const cohort = [
  ["fcad5639-3834-56c7-b2e2-c9c25cf41472", "Robert C DeWeese Jr."],
  ["9edcd9c2-ea84-5788-a550-9c4c6467d1ff", "Albert P Dewey"],
  ["1b4dc2c0-9ca7-52d9-ae32-874f7ecd9359", "Dorothy Dewey"],
  ["310d4d18-a480-5e79-8632-063a95670514", "Eugene E Dewey"],
  ["b84dcb1c-b480-596c-ac9f-afcd6a88a6a8", "Charles Dewey Jr."],
  ["f5400d27-0cf0-5ab3-b920-51341fb13812", "John N Dewey Jr."],
  ["d4248544-6fbb-5a3d-8b0c-ee6f73e38c91", "P C Dewiart"],
  ["65a6d7b0-f56d-5ef6-b4d6-204be19d7df8", "Howard P Dewitt"],
  ["88e5d5a0-f197-54ee-b79e-8ee163e94af3", "Joe A Dewsbury"],
  ["6a3b92fa-8715-5e30-894b-5ffe0e2bf4ab", "Jack W Dexter"],
] as const;

test("batch 579 gives all ten people a terminal archival-review profile", async ({ page }) => {
  for (const [id, name] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.getByText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
      { exact: true },
    ).first()).toBeVisible();
    await expect(page.getByText("Box 184", { exact: false }).first()).toBeVisible();
  }
});

test("Army bulk crosswalks publish identity evidence but no employer", async ({ page }) => {
  for (const id of [cohort[0][0], cohort[7][0], cohort[9][0]]) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" }).first()).toBeVisible();
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  }
});

test("Albert P Dewey's discrepant identity stays qualified", async ({ page }) => {
  await page.goto(`./people/${cohort[1][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByText(/service-identifier discrepancy prevents a confirmed match/i)).toBeVisible();
  await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  await expect(page.getByRole("link", { name: "OSS in Action: The Pacific and the Far East" }).first()).toBeVisible();
});
