import { expect, test } from "@playwright/test";

const cohort = [
  ["dfcdb0ad-ac0b-5ed2-9026-71dbf9a8a53b", "Salvatore Disclafani"],
  ["0d7b56d9-da17-5d8e-a087-a9264f3195da", "Jacques B DiSibour"],
  ["8618dcd2-72a0-5da0-9fc2-61c295447a46", "Oscar F Disilvestro"],
  ["60a833c7-a941-5828-b986-7415f30f8ea1", "Leonard H Dismore"],
  ["c6a60cb1-fed9-583b-8347-9cb9a23ed297", "Carlo Ditonno"],
  ["7dda56d6-afff-5323-9cc0-088d455ba7e5", "Angelo Ditrabia"],
  ["c8d2b720-1054-5823-973f-4405754b707f", "Vance A Ditrinco"],
  ["4fa308a5-76bd-5160-a088-ffbbda8516aa", "John Dittmer"],
  ["038a4bf7-2912-51ca-b3d1-b21826b0485f", "Elizabeth B Divine"],
  ["30ad5b01-2a07-585b-9984-b82d27d74548", "Matthew A DiVito"],
  ["9fcd6682-278c-5f54-aca5-bb022f2426fe", "Vito J Divittorio"],
  ["b9bc59ab-1ff7-5dfa-9750-4d423d87f90f", "Howard W Dix"],
  ["2fb20311-10f3-580a-96f5-712558f3e3eb", "Jack C Dixon"],
  ["44e46238-a4f9-5813-91fa-138f4a7bffa9", "John Dixon"],
  ["6de71205-5b27-5c6f-842d-fe9e535fc8c9", "John W Dixon"],
  ["1c19a6b0-34e7-547e-a691-b71e764656a6", "Marcus A Dixon"],
  ["8186cbe5-c507-5a51-80b1-b8d70a125d1c", "Nicholas J Dixon"],
  ["09a18961-0fac-5b11-9479-f9ad3a7e4793", "Raleigh M Dixon"],
  ["d4fd0c57-abfe-58c3-9038-4c8d3c8ac6fe", "Milo Djonovich"],
  ["c71cf9e6-adf6-5c62-bb1c-96c4910db5a6", "Philip G Djuraskovic"],
] as const;

test("batch 588 preserves all twenty distinct Box 189 profiles", async ({ page }) => {
  for (const [id, name] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("Box 189", { exact: false }).first()).toBeVisible();
  }
});

test("Salvatore's polisher occupation is not invented into a named civilian employer", async ({ page }) => {
  await page.goto(`./people/${cohort[0][0]}/`);
  await expect(page.getByText(/worked as a polisher/).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate.getByRole("link", { name: "United States Army" })).toBeVisible();
  await expect(immediate.getByText("medium", { exact: true })).toBeVisible();
});

test("variant Jacques rows remain separate pending personnel-file comparison", async ({ page }) => {
  await page.goto(`./people/${cohort[1][0]}/`);
  await expect(page.getByText(/separately indexed Jacques B DeSibour/)).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("unbridged postwar Sohio namesake is excluded from oil-company employees", async ({ page }) => {
  await page.goto(`./oil-companies/`);
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(page.getByRole("link", { name: "John Dixon", exact: true })).toHaveCount(0);
  await page.goto(`./people/${cohort[13][0]}/`);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});
