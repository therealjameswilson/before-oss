import { expect, test } from "@playwright/test";

const profiles = [
  ["30c5f381-c85a-5597-bf64-a439a71cdde9", "James C Parker"],
  ["a998a0f9-25b0-565c-b8a9-60e10be6e3e5", "Margie M Parker"],
  ["e300e373-15ca-54a3-93cd-090efe7aaf3a", "Mary K Parker"],
  ["bd7dc0e0-deb3-5288-a166-1d9013790bf8", "Morris M Parker"],
  ["e5f9edee-e454-51ce-9c4a-dff14b3c1042", "Pierre E Parker"],
  ["7c5804a2-1a9b-58af-b362-24793b34f1ca", "William N Parker"],
  ["ed15b71f-d847-57f3-8848-1cb8798fd4fe", "Lester Parkes"],
  ["7f4c48f4-c54f-53da-b317-94db785f8c0b", "Charles M Parkin Jr."],
  ["13ea7e65-69f8-5712-a652-9cd7bcb713fc", "Samuel H Parkins"],
  ["516d8792-b73b-53fd-8dbf-ff63b84d7063", "Robert P Parkinson"],
  ["4c1b6945-28b9-598e-a665-27695dfd3937", "Winston U Parkman"],
  ["f13568e4-7f19-53a5-932e-f008b49ff4b4", "Don L Parks"],
  ["9681d6fd-5956-5e9a-9516-4e52b2ffb4d5", "Paul S Parlati"],
  ["60e7a7d7-b4f1-5e90-89f1-e33527f6d371", "Devereux Parle"],
  ["37c57864-f14f-5c47-bd8a-2c9fb96f736b", "Mary J Parlink"],
  ["7ee64240-3a36-5522-892b-6c563464d055", "Maurice K Parnes"],
  ["1b0a1a51-7415-585d-b366-f27721497059", "William F Parobecher"],
  ["ee7cb979-48d1-550f-9f21-c91aefd3ba47", "Otmar B Parolla"],
  ["bcbfffa2-12b4-555a-98b2-795873ab76a4", "William Parosbeck"],
  ["3c1d6e40-8d38-52d0-90bc-613c1eccfaca", "Lawrence E Parr"],
  ["d915b5fd-92a5-5788-9b76-79af63e9d787", "Michael F Parrino"],
  ["47b86de9-0ac5-583a-9eae-707215c42f9f", "Robert R Parrish"],
  ["25079456-ded0-560e-abd0-790155469729", "Marian A Parrott"],
] as const;

test("Batch 735 publishes all 23 page-358 profiles with terminal dispositions", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 735 exposes the Lester Parkes protected-identifier conflict", async ({ page }) => {
  await page.goto("./people/ed15b71f-d847-57f3-8848-1cb8798fd4fe/");
  await expect(page.getByRole("heading", { name: "Lester Parkes", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Robert L Miller");
  await expect(main).toContainText("LESTER N PARKES");
  await expect(main).toContainText("Box 586");
  await expect(main).toContainText("critical");
});

test("Batch 735 preserves Parkin's immediate military assignment and student distinction", async ({ page }) => {
  await page.goto("./people/7f4c48f4-c54f-53da-b317-94db785f8c0b/");
  await expect(page.getByRole("heading", { name: "Charles M Parkin Jr.", level: 1 })).toBeVisible();
  const immediate = page.locator("section[aria-labelledby='immediate-affiliation']");
  const civilian = page.locator("section[aria-labelledby='civilian-employer']");
  const earlier = page.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(immediate).toContainText("Corps of Engineers School at Fort Belvoir");
  await expect(immediate).toContainText("military assignment");
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(earlier).toContainText("Penn State University");
  await expect(earlier).toContainText("student");
});

test("Batch 735 keeps Parrish's editing evidence as occupation only", async ({ page }) => {
  await page.goto("./people/47b86de9-0ac5-583a-9eae-707215c42f9f/");
  await expect(page.getByRole("heading", { name: "Robert R Parrish", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("assistant editor and sound editor");
  await expect(main).toContainText("John Ford is not converted into a corporate employer");
  await expect(page.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 735 rebuilds exact coverage without changing employer or affiliation totals", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,939");
  await expect(main).toContainText("41.52%");
  await expect(main).toContainText("13,995");
  await expect(main).toContainText("745");
  await expect(main).toContainText("334");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
