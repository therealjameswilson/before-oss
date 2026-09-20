import { expect, test } from "@playwright/test";

const cohort = [
  ["b8136114-b0c5-5c90-a9d3-652e5a86407f", "Peter Dinos", "Box 188"],
  ["7db85cd7-34f7-530d-80e1-f736f68f0c4b", "William R Dinsmore", "Box 188"],
  ["ab55eb53-3126-5258-97ed-aa9d43ac207a", "Arthur W Dintaman", "Box 188"],
  ["94888e92-996f-5b43-90b3-f6a2172cbb60", "James D Dinwiddie", "Box 188"],
  ["56ca8084-6df5-5156-ac25-9cacd37dcce2", "Damon S Diomandes", "Box 188"],
  ["de68e136-88f1-5190-919b-4f92258918c9", "James Diomatares", "Box 188"],
  ["3cc8718f-b37b-5b99-b2c3-a5fcd43b0f4a", "George J D'Ioria", "Box 188"],
  ["3ba3f743-17e0-5d12-ad08-3ad8b65d75f9", "Thomas DiPasqua", "Box 188"],
  ["c4fbd9ed-6d62-5551-97f2-afdc41212a82", "Anthony N Dipiano", "Box 188"],
  ["3d5fec79-7182-5ca9-86e3-55c4205952bd", "Charles R Dippel", "Box 188"],
  ["1739470c-c259-5ac8-b8d0-aff2736d1212", "William C Dippert", "Box 188"],
  ["8b8a5058-a0b1-57a3-b65c-c8c7fd039434", "Gene J DiQuinzo", "Box 188"],
  ["f8b14183-0e94-5728-9f1e-be80f04b2d8a", "Frank J DiRocco", "Box 189"],
  ["b2b7002e-34de-5f75-87b7-148ee490a242", "Victor J DiRocco", "Box 189"],
  ["a4bf228f-d30c-5456-991f-d0a5e60f9510", "William E Dirof", "Box 189"],
  ["e95a9e2d-2988-56ff-b194-28e570b1e179", "Erminio E DiSano Jr.", "Box 189"],
  ["627de1c4-0132-585b-b9a3-353599ba1669", "Joseph Disanto", "Box 189"],
  ["36d0ba4c-91fe-5a8f-96e1-5b2bfcc09d2d", "William Disanza", "Box 189"],
  ["4b3b1623-d4e0-5715-904b-fc694807c7bc", "Jean Dischamps", "Box 189"],
  ["115f7ad4-7ee5-5d82-99e0-06e1fdef991e", "Aurora Discioscio", "Box 189"],
] as const;

test("batch 587 preserves all twenty source-row profiles and their archival boxes", async ({ page }) => {
  for (const [id, name, box] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText(box, { exact: false }).first()).toBeVisible();
  }
});

test("Disanza's Army predecessor is not relabeled as a civilian employer", async ({ page }) => {
  await page.goto(`./people/${cohort[17][0]}/`, { waitUntil: "domcontentloaded" });
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate.locator(".affiliation-card")).toHaveCount(1);
  await expect(immediate.getByRole("link", { name: "United States Army" })).toBeVisible();
  await expect(civilian.locator(".affiliation-card")).toHaveCount(0);
  await expect(page.getByText("Civilian Conservation Corps", { exact: false }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: /Oral History: Disanza, William/ }).first()).toBeVisible();
});

test("OSS service and duplicate-looking names do not become employers", async ({ page }) => {
  for (const index of [4, 12, 13, 16]) {
    await page.goto(`./people/${cohort[index][0]}/`, { waitUntil: "domcontentloaded" });
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});
