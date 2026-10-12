import { expect, test } from "@playwright/test";

const profiles = [
  ["d4ce64bf-276f-5f45-be10-d25809255ff7", "Virgil O Petty"],
  ["f310fb1a-062e-58f0-8b35-69d43bf1b738", "Viola E Pew"],
  ["b4598545-a451-53af-a4ec-692759706032", "Bion D Pewitt"],
  ["66e01813-7345-5b6d-a7a4-3fa4a39ac540", "Eveline Peyronel"],
  ["696caaf9-fc1c-5ed8-997a-50d71774f76f", "Lon Peyton"],
  ["d76459bd-95da-5415-b505-c4ca98a91043", "William H Peyton"],
  ["b7e9ffaa-f543-53a8-b303-e7dd4d4bd47d", "Ralph A Pezzulo"],
  ["b2c67eb9-ec01-5495-8411-ef0a482b87ee", "Roger A Pfaff"],
  ["5261e98d-60ec-5c42-8f1e-7635c077bfe0", "John B Pfaifer"],
  ["a6847f8e-85ee-5761-ad61-db1680966a6b", "Jacob Pfanz"],
  ["6ec46898-7de4-50f0-ad2c-07cf2f4e8240", "Shirley L Pfaudler"],
  ["8a6dc029-0cfc-5c98-8db4-a7fe902ed2a8", "Harold M or Pfeifer"],
  ["4b6ffc8d-451b-5143-939a-b4c024ae5602", "Benjamin K Pfeiffer"],
  ["e33fd0ec-3a8a-52b5-8173-4d11cbd6fe4c", "Louise A Pfeiffer"],
  ["24dbcb52-ec13-598e-b56a-0106b43fe887", "Robert R Pfeiffer"],
  ["8d4b4cd9-c895-585f-8386-6090673cf171", "Timothy A Pfeiffer"],
  ["9810623e-e52b-5a05-ad20-48d6d6406477", "John M Pfenninger"],
  ["fb2dc27d-ef49-501b-9f33-c50252e40052", "James F Pfister"],
  ["5923b435-3402-58bb-8b5d-d8710e671d55", "Otto Pfister"],
  ["400f134f-e379-5a4a-bfa0-21c57d17b2b2", "Irving P Pflaum"],
  ["166cbeab-387b-510e-9f0c-b2d7bcdd359a", "Walter C Pfleeger"],
  ["7b4fe9a9-a80e-5e93-a50a-8a4d438058b8", "Robert P Pflieger"],
  ["883e495b-c676-5f97-87ab-669b34e361c2", "Joseph A Phaneuf"],
] as const;

test("Batch 753 publishes all 23 page-367 profiles with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 753 qualifies documented employment without claiming immediacy", async ({ page }) => {
  await page.goto("./people/66e01813-7345-5b6d-a7a4-3fa4a39ac540/");
  const peyronel = page.locator("main");
  await expect(peyronel).toContainText("Home Catalan");
  await expect(peyronel).toContainText("English teacher");
  await expect(peyronel).toContainText("documented prewar");
  await expect(peyronel.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );

  await page.goto("./people/400f134f-e379-5a4a-bfa0-21c57d17b2b2/");
  const pflaum = page.locator("main");
  await expect(pflaum).toContainText("United Press");
  await expect(pflaum).toContainText("correspondent");
  await expect(pflaum).toContainText("summer 1938");
});

test("Batch 753 distinguishes volunteer affiliation and self-employment", async ({ page }) => {
  await page.goto("./people/5923b435-3402-58bb-8b5d-d8710e671d55/");
  const pfister = page.locator("main");
  await expect(pfister).toContainText("Internationaler Sozialistischer Kampfbund");
  await expect(pfister).toContainText("volunteer");
  await expect(pfister.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/7b4fe9a9-a80e-5e93-a50a-8a4d438058b8/");
  const pflieger = page.locator("main");
  await expect(pflieger).toContainText("Paul Pflieger and Company");
  await expect(pflieger).toContainText("partner");
  await expect(pflieger).toContainText("self employment");
  await expect(pflieger).toContainText("not shown to be his final civilian role");
});

test("Batch 753 preserves both identity conflicts without merging people", async ({ page }) => {
  await page.goto("./people/696caaf9-fc1c-5ed8-997a-50d71774f76f/");
  const peyton = page.locator("main");
  await expect(peyton).toContainText("conflicting");
  await expect(peyton).toContainText("shared with a separate index person");
  await expect(peyton).toContainText("entities remain separate");

  await page.goto("./people/8a6dc029-0cfc-5c98-8db4-a7fe902ed2a8/");
  const pfeifer = page.locator("main");
  await expect(pfeifer).toContainText("conflicting");
  await expect(pfeifer).toContainText("middle initial conflicts");
  await expect(pfeifer).toContainText("printed M or text is preserved");
});

test("home page exposes the rebuilt Batch 753 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,348");
  await expect(home).toContainText("43.23%");
  await expect(home).toContainText("13,586");
  await expect(home).toContainText("773");
  await expect(home).toContainText("343");
  await expect(home).toContainText("8,807");
});
