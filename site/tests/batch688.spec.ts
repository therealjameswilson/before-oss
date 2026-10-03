import { expect, test } from "@playwright/test";

const profiles = [
  ["cf9970c0-0685-5c85-96fb-57cf1d5cafdf", "Corlyn F Munger"],
  ["9e9b784d-b928-5692-b6e9-5d8bcd5034a9", "Catherine M Munley"],
  ["e5eebb04-f53b-5c11-a926-bc1450aab815", "Audice O Munn"],
  ["86c2e291-ad2d-5295-a4a8-9fdf9f60ba8c", "Frances R Munn"],
  ["a9b0f5e5-c3ce-5f45-b3de-8fe88645bfe4", "Avary C Munroe"],
  ["1e199b8c-7d9f-50ce-baf3-9b2137b19239", "John Munroe"],
  ["fd4fcd3b-836f-58fc-9c05-22ae2aa97054", "Vernon Munroe"],
  ["d29c193a-de50-53aa-9e3a-058bc3400efa", "Lyle H Munson"],
  ["aa08f60b-32b2-5f7a-b27e-e0883f215d5d", "Paul Munster"],
  ["4f8ad9c6-b794-553b-ad42-713e153b1d9d", "Lucille I Munyan"],
  ["65220b5b-43f7-5446-a2ef-c73119bade79", "Winthrop R Munyan"],
  ["21bd2dbd-1c18-5e93-80d9-0b7986980c8d", "Kanryo Murakami"],
  ["44e4b891-113b-5e93-bec7-3169d4a40324", "Tadao Murata"],
  ["620890fc-70f7-5b30-b5e7-a285b7614d68", "Benk Murayame"],
  ["6fc85f06-e594-5717-9570-a60c118e8180", "Nick Murdick"],
  ["c63e3899-aaff-5dad-8389-0760d12f3a60", "James O Murdock"],
  ["8275a4d8-cdf8-5205-88b7-add0eb06b3db", "Joseph Muredon"],
  ["c5b3e2d5-8ddc-55a5-aa0c-739ce2592d56", "Charles H Murphey"],
  ["bbbee60c-44af-5e65-b36d-0844eaa930f0", "Adrian M Murphy"],
  ["4711d0f3-3a3e-5f3f-9ec9-065ff430a9fd", "Ann K Murphy"],
  ["4e9f87b1-9fcc-5f43-ac29-147b01954761", "Annel Murphy"],
  ["73a6b1ba-43dd-5f2a-89c7-54faa21100ca", "Augustine J Murphy"],
  ["aaf0e025-bd7f-5022-a6e0-2934aeabf2ac", "Catherine H Murphy"],
] as const;

test("Batch 688 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Page 334");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 688 publishes two protected-identifier matches without inventing employers", async ({ page }) => {
  for (const id of [
    "44e4b891-113b-5e93-bec7-3169d4a40324",
    "73a6b1ba-43dd-5f2a-89c7-54faa21100ca",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 688 preserves all three identifier conflicts without merging people", async ({ page }) => {
  for (const [id, indexed, conflictingName] of [
    ["a9b0f5e5-c3ce-5f45-b3de-8fe88645bfe4", "Avary C Munroe", "Avary C Monroe"],
    ["6fc85f06-e594-5717-9570-a60c118e8180", "Nick Murdick", "Michael Larrick"],
    ["8275a4d8-cdf8-5205-88b7-add0eb06b3db", "Joseph Muredon", "Joseph Mureddu"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: indexed, level: 1 })).toBeVisible();
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(conflictingName);
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 688 keeps plausible postwar and spelling leads qualified", async ({ page }) => {
  await page.goto("./people/65220b5b-43f7-5446-a2ef-c73119bade79/");
  await expect(page.locator("main")).toContainText("postwar attorney biography");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Curtis");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Curtis");

  await page.goto("./people/620890fc-70f7-5b30-b5e7-a285b7614d68/");
  const murayame = page.locator("main");
  await expect(murayame).toContainText("Ben K Murayama");
  await expect(murayame).toContainText("search alias");
  await expect(murayame).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 688 preserves the literal truncated index note", async ({ page }) => {
  await page.goto("./people/c63e3899-aaff-5dad-8389-0760d12f3a60/");
  const main = page.locator("main");
  await expect(main).toContainText("docume");
  await expect(main).toContainText("truncated");
  await expect(main).not.toContainText("documented employer");
});

test("Batch 688 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,873");
  await expect(body).toContainText("37.06%");
  await expect(body).toContainText("310");
  await expect(body).toContainText("15,061");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
