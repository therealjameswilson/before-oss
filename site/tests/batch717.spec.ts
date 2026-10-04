import { expect, test } from "@playwright/test";

const profiles = [
  ["8fbcb0d7-7a8e-5db3-af32-0dfd0b4478e3", "Paul N Olafsen"],
  ["1dcc68da-bb38-5e6c-8c96-59caef1d9120", "Karl L Olberg"],
  ["412a58bb-ebec-5693-9f9a-1f48ec1281c6", "David Oldashi"],
  ["0cfcf729-5fc3-5ad9-b07d-c93ff189c7e0", "Courtenay Olden"],
  ["8ed5c627-4232-5986-91ae-07dd3666532d", "George T Olden"],
  ["8f34150d-1819-5b51-bc37-42b2147f2f41", "Julian S Older"],
  ["879937b9-f189-5fb1-b700-22c3b70a296b", "Ross C Oldford"],
  ["b6dc885d-806d-546a-b6f1-b40c60ac38f0", "John G Oldiges"],
  ["e884c9cd-4776-5200-bf81-62660fea1b69", "Arthur R Oldrey"],
  ["1ed78d89-57b9-5c56-a5b9-686414d19ae1", "David A Olds"],
  ["b58f40d0-800d-5896-a000-739c99c91902", "Gordon L Olds"],
  ["cb4a96be-7e0f-5502-826b-3e5daf0b475d", "Betty J Oleary"],
  ["7fadad03-b650-51d9-a1b1-098c77966d34", "James M Oleary"],
  ["98779d95-551c-5ab7-831c-a78fb9cfaf55", "Roy A Oleary"],
  ["abc9bb9c-72fb-51fd-aac8-42aad136c9c5", "William H Oleary"],
  ["234735bc-1884-5041-8a01-05d66854340c", "Roy A Olerud"],
  ["0872ccc8-9367-5377-9a86-6cd1a3061a67", "Spartaco Oliva"],
  ["5462f859-7bff-5fe2-bc9a-7f6ace877382", "Vladimir S Olive"],
  ["4f63367a-b6fa-5b04-b5ce-13403bbd6fa4", "Belle T Oliver"],
  ["c6157e60-816b-5b2f-b9bf-c41398ee80c7", "Darwin G Oliver"],
  ["2b2168dd-1828-5733-9109-078db4309ea0", "Helen L Oliver"],
  ["4de59e56-b43b-52aa-b2f1-50301667bd16", "James H Oliver"],
  ["24bd8344-49f5-5b1d-a162-912141f5d8f3", "Louise L Oliver"],
] as const;

test("Batch 717 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 717 qualifies James H Oliver and separates last civilian employment from immediate affiliation", async ({ page }) => {
  await page.goto("./people/4de59e56-b43b-52aa-b2f1-50301667bd16/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("James Henry Oliver");
  await expect(main).toContainText("Barnard College");
  await expect(main).toContainText("Assistant professor of history");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("medium B authoritative institutional");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 717 keeps George T Olden separate from the famous designer", async ({ page }) => {
  await page.goto("./people/8ed5c627-4232-5986-91ae-07dd3666532d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("cannot yet be equated with the OSS graphic designer known as Georg Olden");
  await expect(main).toContainText("George Elliott Olden");
  await expect(main).toContainText("No employment or student claim");
  await expect(main).toContainText("Box 571");
});

test("Batch 717 preserves the Roy Oleary and Roy Olerud duplicate conflict", async ({ page }) => {
  for (const [id, otherName] of [
    ["98779d95-551c-5ab7-831c-a78fb9cfaf55", "Roy A Olerud"],
    ["234735bc-1884-5041-8a01-05d66854340c", "Roy A Oleary"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("conflicting sources");
    await expect(main).toContainText("Duplicate group");
    await expect(main).toContainText(otherName);
    await expect(main).not.toContainText("1644634");
  }
});

test("Batch 717 publishes accepted Army identities without inventing employment", async ({ page }) => {
  for (const id of [
    "8fbcb0d7-7a8e-5db3-af32-0dfd0b4478e3",
    "1dcc68da-bb38-5e6c-8c96-59caef1d9120",
    "412a58bb-ebec-5693-9f9a-1f48ec1281c6",
    "879937b9-f189-5fb1-b700-22c3b70a296b",
    "b6dc885d-806d-546a-b6f1-b40c60ac38f0",
    "e884c9cd-4776-5200-bf81-62660fea1b69",
    "c6157e60-816b-5b2f-b9bf-c41398ee80c7",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("nonshared protected identifier agree with Army bulk ordinal");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 717 preserves printed notes without expanding them", async ({ page }) => {
  await page.goto("./people/0cfcf729-5fc3-5ad9-b07d-c93ff189c7e0/");
  await expect(page.locator("main")).toContainText("one fold");
  await page.goto("./people/1ed78d89-57b9-5c56-a5b9-686414d19ae1/");
  const main = page.locator("main");
  await expect(main).toContainText("also AS");
  await expect(main).toContainText("preserved without expansion");
});

test("Batch 717 publishes exact rebuilt coverage and preserves the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,529");
  await expect(main).toContainText("39.81%");
  await expect(main).toContainText("14,405");
  await expect(main).toContainText("724");
  await expect(main).toContainText("326");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("James H Oliver");
});
