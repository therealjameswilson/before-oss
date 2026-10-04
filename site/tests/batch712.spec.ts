import { expect, test } from "@playwright/test";

const profiles = [
  ["ca4c211e-8323-5b31-92c7-a7e0040f7388", "Donald W Obenshain"],
  ["2d3293b9-93a2-5cf9-8d48-e6822da458e2", "John M Obereiner"],
  ["5cb189c1-d69d-5a2d-bb28-08988f56593f", "Julian F Oberg"],
  ["3f6d7afb-9e1b-5369-884c-effd44d25ea6", "Roger W Oberg"],
  ["ee764727-602e-5393-99eb-70cc01b61ad3", "Henry E Obermanns"],
  ["7bee69f7-b984-5850-96e1-38253676750e", "Serge Obolensky"],
  ["ef674efa-f051-596a-b285-5b2160d119f2", "Frank J Obrien"],
  ["3e3ffd8b-91bc-50ca-913a-33caa202f3bd", "George M Obrien"],
  ["cef2f476-9e8b-546f-ab80-46cb92f60072", "Herbert J Obrien"],
  ["67519d90-bd92-53ec-9201-053dbb81bde5", "John J Obrien"],
  ["27f06bd5-c7ef-5ed3-9aba-be2f15459470", "John R Obrien"],
  ["d7dcecb7-f8d4-59f3-b192-e5fe0956de44", "John L Obrien"],
  ["570491ac-ad3a-5c2a-b126-fe1ba5419af3", "John C Obrien"],
  ["90a0e07b-595f-5347-8197-9200ff5e7a04", "Joseph P Obrien"],
  ["bc3b37f8-19e6-5b83-bc53-bc7a444c4307", "Justin M Obrien"],
  ["7d1f8cff-c081-523b-abe7-45e4e2177f60", "Lewis C Obrien"],
  ["522de6e8-b95d-58af-aa08-7ae9bc365721", "Michael J Obrien"],
  ["c9d6f837-a688-5153-9229-8117d9a3bf7e", "Richard Obrien"],
  ["c350f9f6-db83-560e-988f-200550b96b0e", "Richard G Obrien"],
  ["b99c1ce8-c0ac-543a-92b0-b3693b1101be", "Walter E Obrien"],
  ["657bc7a2-1e87-5c1c-93a5-eb2cb7a43579", "William G Obrien"],
  ["9e63ba89-6c6f-5ba4-8bf6-094b9926dbee", "Elinor E Obryan"],
  ["3101af51-9d73-5808-bbc3-9e7f7c04a0a8", "Joseph D Obucina"],
] as const;

test("Batch 712 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 712 publishes reviewed Army identities without inventing employers", async ({ page }) => {
  for (const id of [
    "ca4c211e-8323-5b31-92c7-a7e0040f7388",
    "3f6d7afb-9e1b-5369-884c-effd44d25ea6",
    "cef2f476-9e8b-546f-ab80-46cb92f60072",
    "570491ac-ad3a-5c2a-b126-fe1ba5419af3",
    "90a0e07b-595f-5347-8197-9200ff5e7a04",
    "c9d6f837-a688-5153-9229-8117d9a3bf7e",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 712 preserves the Micheal spelling variant while accepting the identifier match", async ({ page }) => {
  await page.goto("./people/522de6e8-b95d-58af-aa08-7ae9bc365721/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Micheal J Obrien");
  await expect(main).toContainText("spelling difference is preserved");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 712 uses the Detachment 101 record for identity only", async ({ page }) => {
  await page.goto("./people/2d3293b9-93a2-5cf9-8d48-e6822da458e2/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("OSS Special Unit Detachment 101 Promotions and Citations");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 712 retains Obolensky's earlier reviewed chronology", async ({ page }) => {
  await page.goto("./people/7bee69f7-b984-5850-96e1-38253676750e/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("New York National Guard");
  await expect(main).toContainText("St. Regis Hotel");
  await expect(main).toContainText("banking and real estate");
  await expect(main).toContainText("documented prewar employer found");
});

test("Batch 712 publishes unresolved common-name outcomes and exact coverage", async ({ page }) => {
  for (const id of [
    "ef674efa-f051-596a-b285-5b2160d119f2",
    "27f06bd5-c7ef-5ed3-9aba-be2f15459470",
    "b99c1ce8-c0ac-543a-92b0-b3693b1101be",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("no reliable result after protocol");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,414");
  await expect(main).toContainText("39.33%");
  await expect(main).toContainText("14,520");
  await expect(main).toContainText("720");
  await expect(main).toContainText("325");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
