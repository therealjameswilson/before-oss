import { expect, test } from "@playwright/test";

const profiles = [
  ["f42c11eb-60cf-53b3-8b49-5fe219c8f6dc", "Thomas N Savino"],
  ["dd52483d-a422-5d66-a440-1f148aa96ccc", "Frank A Savio"],
  ["c10592a8-6d9e-5673-bf46-5296b828d186", "Joseph Savoldi Jr."],
  ["0723168f-e40d-53fd-84ea-0f6c2563e83f", "Edward A Sawasa"],
  ["7c2a41e6-0a82-5544-9411-d06b73b26702", "William A Sawhill"],
  ["fca5554b-2369-5282-a7b1-13efb722264b", "Charles H Sawyer"],
  ["4bd9842f-7cf0-53b5-afaf-ba62541d719e", "Charles W Sawyer"],
  ["631a6ec7-378b-57a0-a71b-c37507a234b3", "John F Sawyer"],
  ["d57a8f3b-5a15-55e5-a75a-6487f35d86cf", "William L Sawyer"],
  ["7ee860fd-9773-54d3-b3a5-57d7a7aa616b", "Issaac W Saxow"],
  ["3c821bf3-9339-507e-9498-4891ad9921d8", "Homer E Sayas"],
  ["b7e7a25e-5cd8-5fa9-9c20-d583098a8844", "Monteor M Sayce"],
  ["73c671a2-f9d4-5708-a3e1-39c18890e8e4", "Roger G Sayers"],
  ["a3e5f92a-1b20-53d9-8914-dfd8b8eab3a8", "Kenneth L Sayre"],
  ["e849fd0d-bef7-5ba8-a1b0-bc12247ec870", "Frank P Scaffidi"],
  ["8968d6b3-2a4d-55ac-8409-febec51eb6ba", "Alan M Scaiff"],
  ["dcb93128-1b3d-5022-8001-0e2ff5694c6b", "Gerard Scala"],
  ["6cd432a9-3496-5831-b558-74a27566a506", "Joseph Scala"],
  ["3654bfd2-2d20-52da-bbb0-b9564f5236fd", "Joseph A Scala"],
  ["e5b3d1ed-7993-5e7a-a108-b501b5147435", "Dorothy M Scammon"],
  ["252cb7cb-c4b3-5327-a1fb-fd5d105b8351", "Vincent J Scamporino"],
  ["dfff4dd9-60b9-5870-816a-d92b4744566c", "Frank L Scandura"],
  ["337fa5ea-b6fd-53ca-9864-cd23184e2984", "Frank Scanlin Jr."],
] as const;

test("Batch 841 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Charles H Sawyer separates Army, Worcester, and Phillips Academy pathways", async ({ page }) => {
  await page.goto("./people/fca5554b-2369-5282-a7b1-13efb722264b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Worcester Art Museum");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Phillips Academy");
  await expect(main).toContainText("NAID 2185148");
});

test("Joseph Savoldi publishes a qualified occupation without inventing an employer", async ({ page }) => {
  await page.goto("./people/c10592a8-6d9e-5673-bf46-5296b828d186/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("professional wrestler");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("no employer or promotion is identified");
  await expect(main).not.toContainText("self-employed");
});

test("Alan M Scaiff preserves index spelling and publishes Gulf Oil as last civilian employer", async ({ page }) => {
  await page.goto("./people/8968d6b3-2a4d-55ac-8409-febec51eb6ba/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Alan Magee Scaife");
  await expect(main).toContainText("Gulf Oil Corporation");
  await expect(main).toContainText("vice-president, director and finance committee member");
  await expect(main).toContainText("Last civilian employer before service");

  await page.goto("./oil-companies/");
  await expect(page.locator("main")).toContainText("Alan M Scaiff");
  await expect(page.locator("main")).toContainText("Gulf Oil Corporation");
});

test("Vincent Scamporino publishes a qualified legal occupation without inventing a firm", async ({ page }) => {
  await page.goto("./people/252cb7cb-c4b3-5327-a1fb-fd5d105b8351/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("lawyer in civilian life");
  await expect(main).toContainText("September 1942");
  await expect(main).toContainText("no employer or firm is identified");
  await expect(main).not.toContainText("self-employed");
});

test("accepted Batch 841 Army crosswalks publish identity but no coded occupation", async ({ page }) => {
  for (const id of [
    "f42c11eb-60cf-53b3-8b49-5fe219c8f6dc",
    "dd52483d-a422-5d66-a440-1f148aa96ccc",
    "7c2a41e6-0a82-5544-9411-d06b73b26702",
    "6cd432a9-3496-5831-b558-74a27566a506",
    "a3e5f92a-1b20-53d9-8914-dfd8b8eab3a8",
    "dfff4dd9-60b9-5870-816a-d92b4744566c",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(/private (?:official Army crosswalk|crosswalk|identifier)/i);
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("Batch 841 identity conflicts stay visible without leaking private candidates", async ({ page }) => {
  for (const id of [
    "4bd9842f-7cf0-53b5-afaf-ba62541d719e",
    "0723168f-e40d-53fd-84ea-0f6c2563e83f",
    "73c671a2-f9d4-5708-a3e1-39c18890e8e4",
    "e849fd0d-bef7-5ba8-a1b0-bc12247ec870",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText(/(?:private|protected) identifier/i);
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("adjacent Charles Sawyer rows remain separate and visibly reviewable", async ({ page }) => {
  await page.goto("./people/fca5554b-2369-5282-a7b1-13efb722264b/");
  let main = page.locator("main");
  await expect(main).toContainText("Duplicate groupduplicate-c71e0eedd5a4");
  await expect(main).toContainText("Charles H Sawyer");

  await page.goto("./people/4bd9842f-7cf0-53b5-afaf-ba62541d719e/");
  main = page.locator("main");
  await expect(main).toContainText("Duplicate groupduplicate-c71e0eedd5a4");
  await expect(main).toContainText("Charles W Sawyer");
});

test("unusual spellings remain exactly as printed", async ({ page }) => {
  await page.goto("./people/7ee860fd-9773-54d3-b3a5-57d7a7aa616b/");
  await expect(page.getByRole("heading", { name: "Issaac W Saxow", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Name as indexedSaxow | Issaac | W");

  await page.goto("./people/b7e7a25e-5cd8-5fa9-9c20-d583098a8844/");
  await expect(page.getByRole("heading", { name: "Monteor M Sayce", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Name as indexedSayce | Monteor | M");
});

test("unresolved Batch 841 profiles retain dignified archival guidance", async ({ page }) => {
  for (const id of [
    "631a6ec7-378b-57a0-a71b-c37507a234b3",
    "d57a8f3b-5a15-55e5-a75a-6487f35d86cf",
    "7ee860fd-9773-54d3-b3a5-57d7a7aa616b",
    "3c821bf3-9339-507e-9498-4891ad9921d8",
    "b7e7a25e-5cd8-5fa9-9c20-d583098a8844",
    "dcb93128-1b3d-5022-8001-0e2ff5694c6b",
    "3654bfd2-2d20-52da-bbb0-b9564f5236fd",
    "e5b3d1ed-7993-5e7a-a108-b501b5147435",
    "337fa5ea-b6fd-53ca-9864-cd23184e2984",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Review Box 680");
  }
});
