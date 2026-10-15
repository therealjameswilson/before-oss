import { expect, test } from "@playwright/test";

const profiles = [
  ["66af92c7-d341-538f-91d6-f031ad38f1b0", "Carrie E Rider", "644"],
  ["6ef60de6-5d06-5c30-b4c8-a15ec6f55549", "Donald L Rider", "644"],
  ["74440a6d-0584-5341-812d-99ac3bc3460e", "Earle E Ridgely", "644"],
  ["a15b0ceb-192e-5ea9-b03d-01954b61d2f9", "Harry S Ridgely", "644"],
  ["ceb23774-209f-5cfb-a661-faa6fac778da", "Carl E Ridgeway", "644"],
  ["3f9a6a38-babc-5f4c-9cd6-efb4dc595cd8", "Brian M Ridgway", "644"],
  ["7b646c53-73fb-5d9e-8f4c-2d5a064a36db", "Margaret E Ridings", "644"],
  ["cf3aef49-6960-5cb9-86fc-b89994f5af08", "Dorothea M Ridlon", "644"],
  ["c827d299-4db6-599f-b27d-18a49c96eb8f", "Keunsung Rie", "644"],
  ["a743ae85-cf03-57e1-8591-6cbd9ebb686c", "Mary A Riedel", "644"],
  ["32de24b2-fe0a-5d4f-b93c-b5e3e5f21fff", "Bernard J Riedeman", "644"],
  ["2a107777-646e-5aa1-9e57-461cc3bf24cc", "Herman J Rief", "644"],
  ["df6dcd3a-ea92-5ca6-8b81-a0d2f931004e", "Alfred Riefman", "644"],
  ["ef89c5af-59cc-5f8b-bb49-d7f4a349e5e8", "Richard E Riegel", "644"],
  ["c482e22d-7a90-5f85-9896-56a345ed7cec", "Manek Riegelhaupt", "644"],
  ["da301ca3-2b53-5fa5-b51f-a5967a9a8047", "Dorothea P Rieger", "644"],
  ["3014afff-5582-59ef-ade1-af62505355d4", "Harry V Riehman", "644"],
  ["d1fe06e7-2ba8-5149-9e51-974e893db23f", "Gertrude Rient", "644"],
  ["83e5b21d-9c4e-5a20-ac12-6c085fc2230d", "Felix Riesenberg Jr.", "644"],
  ["f0109da7-9a05-59b7-9d3e-469d1933c493", "Elwood C Rieser", "644"],
  ["81ed6129-6f9c-59b5-b939-8843db3313cb", "Curt Riess", "645"],
  ["1e2ac0a6-7807-53cc-a1f7-1ac507512607", "George J Riester", "645"],
  ["bc175f32-7d15-5ae1-b251-c0999e714d4e", "Edward L Rigby", "645"],
] as const;

test("Batch 804 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Harry Ridgely presents the 1925 Justice role only as a qualified prewar claim", async ({
  page,
}) => {
  await page.goto("./people/a15b0ceb-192e-5ea9-b03d-01954b61d2f9/");
  const main = page.locator("main");
  await expect(main).toContainText("U.S. Department of Justice");
  await expect(main).toContainText("attorney");
  await expect(main).toContainText("medium documented pre-OSS");
  await expect(main).toContainText("not presented as immediate before OSS");
});

test("Manek Riegelhaupt preserves unnamed work and temporal uncertainty", async ({ page }) => {
  await page.goto("./people/c482e22d-7a90-5f85-9896-56a345ed7cec/");
  const main = page.locator("main");
  await expect(main).toContainText("busboy");
  await expect(main).toContainText("cashier");
  await expect(main).toContainText("diamond cutter");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("No employer name is inferred");
});

test("Gertrude Rient publishes the Moscow embassy role with visible qualification", async ({ page }) => {
  await page.goto("./people/d1fe06e7-2ba8-5149-9e51-974e893db23f/");
  const main = page.locator("main");
  await expect(main).toContainText("Embassy of the United States, Moscow");
  await expect(main).toContainText("Czech linguist");
  await expect(main).toContainText("medium strongly date bounded");
  await expect(main).toContainText("not proven to be the immediately preceding affiliation");
});

test("Felix Riesenberg keeps writer as an occupation rather than an invented employer", async ({
  page,
}) => {
  await page.goto("./people/83e5b21d-9c4e-5a20-ac12-6c085fc2230d/");
  const main = page.locator("main");
  await expect(main).toContainText("writer");
  await expect(main).toContainText("1939");
  await expect(main).toContainText("Writer is retained as an occupation");
  await expect(main).toContainText("neither source establishes a named employer");
});

test("Curt Riess clearly distinguishes a disapproved application from OSS service", async ({ page }) => {
  await page.goto("./people/81ed6129-6f9c-59b5-b939-8843db3313cb/");
  const main = page.locator("main");
  await expect(main).toContainText("freelance writer");
  await expect(main).toContainText("application was disapproved");
  await expect(main).toContainText("does not by itself prove OSS service");
  await expect(main).toContainText("No OSS employment, assignment, or service is inferred");
});

test("Alfred Riefman remains a separate visible conflict", async ({ page }) => {
  await page.goto("./people/df6dcd3a-ea92-5ca6-8b81-a0d2f931004e/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Alfred Reifman");
  await expect(main).toContainText("Duplicate group");
  await expect(main).toContainText("No evidence or employer claims are transferred");
});

test("Batch 804 preserves clipped notes without silent expansion", async ({ page }) => {
  await page.goto("./people/66af92c7-d341-538f-91d6-f031ad38f1b0/");
  await expect(page.locator("main")).toContainText("Record");

  await page.goto("./people/a15b0ceb-192e-5ea9-b03d-01954b61d2f9/");
  await expect(page.locator("main")).toContainText("folder is");

  await page.goto("./people/3014afff-5582-59ef-ade1-af62505355d4/");
  await expect(page.locator("main")).toContainText("photogra");
});

test("home page exposes the rebuilt Batch 804 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,479");
  await expect(home).toContainText("47.95%");
  await expect(home).toContainText("12,454");
  await expect(home).toContainText("824");
  await expect(home).toContainText("372");
  await expect(home).toContainText("9,942");
});
