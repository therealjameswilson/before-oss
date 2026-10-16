import { expect, test } from "@playwright/test";

const profiles = [
  ["0b6793e3-9953-5fa5-aea7-613fe91b23ec", "Hans Sahl"],
  ["ebf6be43-86bb-531a-8a47-70b6fea73eb0", "Nils G Sahlin"],
  ["9b1b8a17-fcd4-54e7-9de7-8a31123e5910", "Kataro Saimoto"],
  ["0c1240a9-e6b5-5b5a-9c09-91119165a82d", "James W Sain"],
  ["b0a4f766-6374-5474-9ec5-0f1692c28ef7", "Henry A Sajma"],
  ["79b5836f-bf08-5015-98d3-98c2ee288398", "Yoneo Sakai"],
  ["70fd00c3-28e9-57cb-bc84-dd5a1461513c", "Muneo Sakane"],
  ["af097e74-e050-5e9c-be9b-b947ad6d150b", "George C Sakellaris"],
  ["cbb9e10f-1dd9-5796-9b97-b3c34904afe8", "Songe S Sakornbut"],
  ["a856b361-838a-58d3-a0c7-ec4cebf4084b", "Vitaly W Sakouta"],
  ["d4f2c6cb-65de-5257-b1d0-329bf76e1aa9", "Matthew J Sakowski"],
  ["7978cc45-fcda-54cd-88ec-21b7fb35dc6c", "Louis Salamacha"],
  ["93c704f1-d779-574e-abb8-6e1e43d7892f", "Richard S Salant"],
  ["6c8ab049-4cc4-5f79-8a77-feb65859c5e4", "William A Salant"],
  ["0fa2f26e-4dd1-578a-9417-59d7e7c1cb0b", "Konstantine A Salaris"],
  ["5d2c4a52-adf3-50c8-ac0d-df2627e6836d", "Henry Salazar"],
  ["04a902dc-1e50-59ce-84ff-7efb400f6e20", "Edward T Saldana"],
  ["b3d46f1c-b67d-53e8-a376-ff9ff60403c1", "William J Sale"],
  ["cb17f787-5c60-51fe-9fd5-c0345ce38733", "Benedetto J Salerno"],
  ["dfb3ea35-7637-54b4-b523-f86b713ed51f", "Gaspare Salerno"],
  ["029baafb-90e0-58fc-9835-a75cc8f70001", "Joseph R Salerno"],
  ["e54179b1-86cc-56d5-b5e4-e3d55ee89e87", "Joseph E Sales"],
  ["b7598935-eae6-5cc1-9738-f2c305d88656", "Theodore S Saliaris"],
] as const;

test("Batch 833 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("George Sakellaris publishes Cities Service and enters the oil-company category", async ({ page }) => {
  await page.goto("./people/af097e74-e050-5e9c-be9b-b947ad6d150b/");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("Cities Service Company");
  await expect(civilian).toContainText("cost accountant");
  await expect(civilian).toContainText("confirmed");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("Camp Carson");

  await page.goto("./oil-companies/");
  const list = page.getByRole("region", { name: "Oil company work list" });
  await expect(list.locator(".oil-directory__person")).toHaveCount(11);
  await expect(list).toContainText("George C Sakellaris");
  await expect(list).toContainText("Cities Service Company");
  await expect(page.locator(".page-hero .lede")).toContainText("13 historically named oil");
});

test("Yoneo Sakai separates immediate language-school service from Asahi employment", async ({ page }) => {
  await page.goto("./people/79b5836f-bf08-5015-98d3-98c2ee288398/");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("U.S. Navy Japanese Language School");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("The Asahi Shimbun");
  await expect(civilian).toContainText("reporter");
  await expect(page.locator("main")).toContainText("Naval versus Military Intelligence");
});

test("the Salant profiles preserve separate government chronologies", async ({ page }) => {
  await page.goto("./people/93c704f1-d779-574e-abb8-6e1e43d7892f/");
  await expect(page.getByRole("region", { name: "Last civilian employer before service" }))
    .toContainText("Office of the Solicitor General");
  await expect(page.getByRole("region", { name: "Earlier pre-OSS affiliations" }))
    .toContainText("National Labor Relations Board");

  await page.goto("./people/6c8ab049-4cc4-5f79-8a77-feb65859c5e4/");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("The White House");
  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("Office of Price Administration");
  await expect(earlier).toContainText("Board of Governors of the Federal Reserve System");
});

test("Hans Sahl and Konstantine Salaris keep evidence boundaries explicit", async ({ page }) => {
  await page.goto("./people/0b6793e3-9953-5fa5-aea7-613fe91b23ec/");
  await expect(page.locator("main")).toContainText("Metro-Goldwyn-Mayer");
  await expect(page.locator("main")).toContainText("qualified");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" }))
    .toContainText("No reviewed claim currently meets the publication threshold");

  await page.goto("./people/0fa2f26e-4dd1-578a-9417-59d7e7c1cb0b/");
  const main = page.locator("main");
  await expect(main).toContainText("Company B, Special Reconnaissance Battalion");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText(/\b\d{7,9}\b/);
});
