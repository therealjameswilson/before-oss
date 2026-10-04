import { expect, test } from "@playwright/test";

const profiles = [
  ["018c0321-fde2-5c29-bafe-348491a30f26", "Barbara L Owens"],
  ["08c20dc6-8811-5ee1-b979-176630a7b0a4", "Auburn E Owen"],
  ["0c48ea7d-3251-5d18-9439-77546e9f9230", "Alvin M Overall"],
  ["1feab978-c5ed-5049-a3d2-fe0b23f85e98", "Jerome H Ourada"],
  ["2b68794c-c58a-5135-9f6c-81ca0a53be66", "Jose R Oural"],
  ["3305ec22-fc56-5378-80f6-b8dbd3899c78", "Oaul Ouer"],
  ["351074f5-899d-5721-a395-579381c8baa2", "Paul L Otwell"],
  ["360c2ed3-cb24-5dd2-be8b-3c554a89d3d0", "George H Owen"],
  ["376d3cdb-1db3-5dbf-a970-447527c1f432", "Alice M Ovington"],
  ["44eedf6b-0591-5963-a1e7-0bc38e3d3f5d", "Mildred B Oulahan"],
  ["476d6c7e-6c85-54d2-aaa8-e3f92809857e", "Carla R Overly"],
  ["4b85a960-3737-551c-80dc-1d5a76d0dd5c", "Robert M Overton"],
  ["50314bec-36a3-58a4-a4f8-209131515b56", "Catherine H Overton"],
  ["56c45fd0-cb63-5531-8f0e-0e029f4225dc", "Jane H Overton"],
  ["5a253830-d4ee-531e-9a75-b914077f08ef", "Stephen Ovary"],
  ["761264d1-d013-57ff-bf0d-28c89acc6844", "David A Owens"],
  ["8cec7619-4786-55db-8d3c-59bc6634ad09", "Adrien Outellett"],
  ["ac8f6179-576d-5d1c-9fed-827d2be32387", "Robert W Owen"],
  ["b8e1b607-ed24-500a-9b13-eeb89bee69e9", "George W Overton"],
  ["c092ca4a-ae57-5259-a10a-959398f621be", "Betty N Otwell"],
  ["e93ea898-8efe-5a10-988e-ffc2db424496", "Sven Overbo"],
  ["ee050ea8-49a5-5ff0-b661-6e175354c9ed", "Charles W Owen"],
  ["f25c6cfd-6d31-5f57-8c39-28ec95152161", "Nellie J Overhulser"],
] as const;

test("Batch 726 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 726 publishes Jose Oural's bounded Army-before-OSS chronology", async ({ page }) => {
  await page.goto("./people/2b68794c-c58a-5135-9f6c-81ca0a53be66/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("José Ramón Oural López");
  await expect(main).toContainText("Army of the United States");
  await expect(main).toContainText("June 17, 1943");
  await expect(main).toContainText("May 1944 OSS mission");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("Jose Oural Oral History Interview");
  await expect(main).toContainText("Passport, Josefa Oural, 1936");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationArmy of the United States");
  await expect(main).not.toContainText("Sherwin-Williams");
});

test("Batch 726 preserves the Carla and Carl Overly conflict", async ({ page }) => {
  await page.goto("./people/476d6c7e-6c85-54d2-aaa8-e3f92809857e/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Carl R Overly");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).not.toContainText("Army of the United States");
});

test("Batch 726 preserves Oaul Ouer and the exceptional archive location", async ({ page }) => {
  await page.goto("./people/3305ec22-fc56-5378-80f6-b8dbd3899c78/");
  const main = page.locator("main");
  await expect(main).toContainText("Oaul Ouer");
  await expect(main).toContainText("230/86/37/07");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Paul Ouer");
});

test("Batch 726 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,735");
  await expect(main).toContainText("40.67%");
  await expect(main).toContainText("14,199");
  await expect(main).toContainText("738");
  await expect(main).toContainText("330");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Jose R Oural");
});
