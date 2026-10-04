import { expect, test } from "@playwright/test";

const profiles = [
  ["0313a000-4458-5b8c-8d58-4f2e90b2e6a7", "Barbara G Ottinger"],
  ["17d4f8de-61ca-5e91-ab08-9c6b1b9b6c3c", "Richard M Otter"],
  ["23dd9f25-e680-5e76-8239-1e0d7b32dfd1", "Heinz J Otto"],
  ["2c1f040a-a0e1-5038-8dc9-14d331e905e6", "Henry S Otto"],
  ["2c21b1f3-5572-5b99-8f74-f535781d7d12", "Sarah A Ott"],
  ["2ef9f938-ad08-534c-a166-98f312321239", "Fred R Ostheimer"],
  ["38c3d84b-9e86-5d3f-960c-576341d7294b", "John W Ostheimer"],
  ["45d385e0-9e50-50e1-8416-1515d659ea6f", "Roy N Osthus"],
  ["460da3f4-7372-56fd-ac2a-4561e6137836", "Steve S Ostrowski"],
  ["5845d504-7c41-5048-9957-1358ee90d6e1", "Cecilia B Otter"],
  ["63aed05e-f0f7-523a-a37a-a79e6e5493c9", "Robert J Osterbur"],
  ["68020175-4f4b-5663-8000-e57294b3cdac", "Gustav F Osterman"],
  ["6d3267f5-686b-55e0-82ac-988753a9f150", "Paul O Ottwell"],
  ["84e52858-7504-5baa-bebe-0c36a23f6a31", "W E Ostrander"],
  ["87e24c64-4d82-5010-965c-0c97116b9b22", "Julius Ostroff"],
  ["972a86d8-5b60-5e3d-85bc-9e1d54273ebe", "Gerald Ottersland"],
  ["9fd0fb18-460a-593f-986f-129274212700", "Frank F Otto"],
  ["aa838dcd-d071-5786-b984-67658aac4043", "Lawrence G Otera"],
  ["afd46327-a731-53e6-b07b-347ac77b1ff9", "Walter S Oswalo"],
  ["cc5c392f-5e2b-55a1-97a6-183f65891b67", "Raymond R Otake"],
  ["d459bfdc-b45c-5051-a17e-40d080aae854", "Paul Ostroner"],
  ["dfbb7842-3ef8-5710-ad94-6cd9948ba023", "Garth B Oswald"],
  ["f9803249-0f38-5965-881c-e1c6c0904a05", "James Otoole"],
] as const;

test("Batch 725 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 725 publishes Julius Ostroff's first-person occupation without inventing an employer", async ({ page }) => {
  await page.goto("./people/87e24c64-4d82-5010-965c-0c97116b9b22/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Salesman");
  await expect(main).toContainText("employer not named");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("Board interviews at OSS Headquarters, Cairo");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationSalesman");
});

test("Batch 725 qualifies Gerald Ottersland's military and unnamed-shipyard pathways", async ({ page }) => {
  await page.goto("./people/972a86d8-5b60-5e3d-85bc-9e1d54273ebe/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Gjerulf Ottersland");
  await expect(main).toContainText("99th Infantry Battalion (Separate)");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("a shipyard in Brooklyn (organization not named)");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("occupation only found");
});

test("Batch 725 verifies Fred Ostheimer's OSS identity but leaves employment unresolved", async ({ page }) => {
  await page.goto("./people/2ef9f938-ad08-534c-a166-98f312321239/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Award of Unit Certificate of Merit");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("no reliable result after protocol");
});

test("Batch 725 preserves both protected-identifier conflicts", async ({ page }) => {
  await page.goto("./people/cc5c392f-5e2b-55a1-97a6-183f65891b67/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("Raymond K Otake");

  await page.goto("./people/6d3267f5-686b-55e0-82ac-988753a9f150/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("William H Thomas");
});

test("Batch 725 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,712");
  await expect(main).toContainText("40.57%");
  await expect(main).toContainText("14,222");
  await expect(main).toContainText("737");
  await expect(main).toContainText("330");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Julius Ostroff");
  await expect(page.locator("#oil-companies")).not.toContainText("Gerald Ottersland");
});
