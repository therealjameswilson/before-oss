import { expect, test } from "@playwright/test";

const profiles = [
  ["3ac3f2cd-47d0-51b1-82b5-5b153b027db8", "Elizabeth A Robertson"],
  ["90de6406-032e-5c1d-b841-1ec760a3c438", "Henry T Robertson"],
  ["4955179b-f8b8-5205-a987-ac9af0ab527d", "Nancy J Robertson"],
  ["3a234ddd-5bb2-5590-827d-81b10b8d1c64", "Sterling C Robertson"],
  ["6a5a2e7a-d55f-581c-9d08-cbc761dde947", "Thomas A Robertson"],
  ["74abdcbc-879c-535a-ae3d-14710bd369be", "Thomas J Robertson"],
  ["18536b9c-06dd-5d2b-9148-a3a654017071", "William D Robertson"],
  ["f92b9e82-b2ea-52a0-8470-db22fc4d9638", "William R Robertson"],
  ["ffe6174d-cb68-533d-b6ee-9e237444e790", "Winifred L Robertson"],
  ["2b93b7ec-ead3-595b-8e52-803d22a48378", "Eunice E Robey"],
  ["73e71f23-2a35-52a9-85db-cb00ca05a57a", "Gerald W Robey"],
  ["fd756c3c-399b-54eb-9458-fc80410a682c", "Hubert G Robey"],
  ["05cdc815-dde6-5352-8936-c7e4d032d200", "Marcel Robich"],
  ["fe88f70a-3bbc-502e-9ee8-c40eca1a933d", "Albert Robichaud"],
  ["6f75a239-b7b4-5f89-b01a-d8ca67259431", "Edward F Robichaud"],
  ["0287844d-2c64-5a18-915f-e9eea2234b5f", "Louis E Robichaud"],
  ["3e4ee11e-3c8e-5f3d-8279-582ccb372926", "Darrell S Robins"],
  ["e9eb73f1-5de1-5714-ad3b-3eb88c4ce383", "William E Robins"],
  ["e909510a-c0a7-53e3-adb2-4e0c29f8a601", "Arthur H Robinson"],
  ["cb55f1b2-2844-5bcc-8a42-2d722e9b199c", "David W Robinson"],
  ["c8b80ec2-4bec-5939-90c6-c902c8457a2d", "George W Robinson"],
  ["fa110fc0-6908-51ce-b266-0d0e39e79002", "Gerald B Robinson"],
  ["e6f133b8-bd4a-5796-978c-b91076896fef", "Geroid T Robinson"],
] as const;

test("Batch 811 publishes all 23 profiles with attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Albert Robichaud separates occupation from immediate military affiliation", async ({ page }) => {
  await page.goto("./people/fe88f70a-3bbc-502e-9ee8-c40eca1a933d/");
  const main = page.locator("main");
  await expect(main).toContainText("schoolmaster");
  await expect(main).toContainText("French literature and Latin");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("school is not identified");
});

test("Marcel Robich separates businessman occupation from the 34th Bomb Group pathway", async ({ page }) => {
  await page.goto("./people/05cdc815-dde6-5352-8936-c7e4d032d200/");
  const main = page.locator("main");
  await expect(main).toContainText("businessman");
  await expect(main).toContainText("34th Bomb");
  await expect(main).toContainText("employer is named");
});

test("David W Robinson exposes the post-dissolution chronology problem", async ({ page }) => {
  await page.goto("./people/cb55f1b2-2844-5bcc-8a42-2d722e9b199c/");
  const main = page.locator("main");
  await expect(main).toContainText("November 10, 1945");
  await expect(main).toContainText("after OSS dissolution");
  await expect(main).toContainText("requires archival review");
});

test("Thomas A Robertson preserves the printed possible note without interpretation", async ({ page }) => {
  await page.goto("./people/6a5a2e7a-d55f-581c-9d08-cbc761dde947/");
  const main = page.locator("main");
  await expect(main).toContainText("possible");
  await expect(main).toContainText("preserved literally");
});

test("home page exposes the rebuilt Batch 811 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,638");
  await expect(home).toContainText("48.62%");
  await expect(home).toContainText("12,295");
  await expect(home).toContainText("833");
  await expect(home).toContainText("374");
  await expect(home).toContainText("10,101");
});
