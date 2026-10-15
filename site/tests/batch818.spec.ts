import { expect, test } from "@playwright/test";

const profiles = [
  ["daecd395-fab7-5073-98e2-c658105acaad", "Howard E Roman"],
  ["7f5c06fa-a514-5755-a98f-3c8035dc9833", "Thomas Roman"],
  ["76ec3a6d-06b8-5bc8-9eaa-29f7ba705942", "Edward F Romano"],
  ["cf08b0c0-42e9-52f7-bef1-a29d47c57d63", "Edwin P Romanoski"],
  ["49e94f5e-0ba3-5537-8b47-c039a04c745d", "Mildred M Romans"],
  ["76df7112-a4cf-5171-8fea-10946a4fcb65", "Ada P Rome"],
  ["ccfe1778-a76a-51d8-a0df-4d7455e659b0", "Sam V Romeo"],
  ["d1ad5260-233c-58ae-b4da-932a01d6ed02", "Fedencio J Romero"],
  ["9b7360d2-e9e5-54dc-a885-c1823f6273e0", "Jose Romero"],
  ["22ece9ec-0273-5e3d-9d93-62873d3ed7b4", "Kenneth Romney Jr."],
  ["f4ab0aee-d124-5859-8491-379f408942ce", "Serafino Romualdi"],
  ["19f10492-2f05-5696-8b29-65b726f6a6bc", "Vincenzo Roncoli"],
  ["90c12687-e35d-57c0-96a5-4af6b0ff94e2", "John R Rondeau"],
  ["814862c3-388b-500a-9d07-373a2f8e8d92", "Robert K Roodvoets"],
  ["edfbbbc2-3f67-51e5-bdba-2055348242ef", "William R Roof"],
  ["963a85d4-40b7-5cdc-a234-dd072e58bd3c", "George R Rook"],
  ["89591383-baf4-541e-8c3f-c7ca637d3258", "Edward J Rooney"],
  ["4670c5e5-5344-5f60-9618-4acecb578d95", "Frank M Rooney"],
  ["3c89f1cf-8ccc-52e4-bf47-0539a1fb7e73", "Helen M Rooney"],
  ["93845e09-8eb6-5027-8fb4-5b8336cd3f21", "Emmett Roorbach"],
  ["edfec968-b554-5ea3-bd2a-4de142c2d818", "Robert C Roos III"],
  ["bef6b3aa-fe41-5c63-9e12-8f629ae78ff7", "August Rooseboom"],
  ["66142cc6-36c6-519b-8765-986f995322e3", "Archibald B Roosevelt"],
] as const;

test("Batch 818 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Serafino Romualdi profile separates immediate government assignment and last civilian employer", async ({ page }) => {
  await page.goto("./people/f4ab0aee-d124-5859-8491-379f408942ce/");
  const main = page.locator("main");
  await expect(main).toContainText("Office of the Coordinator of Inter-American Affairs");
  await expect(page.getByRole("heading", { name: "Immediate pre-OSS affiliation", level: 2 })).toBeVisible();
  await expect(main).toContainText("International Ladies' Garment Workers' Union");
  await expect(page.getByRole("heading", { name: "Last civilian employer before service", level: 2 })).toBeVisible();
  await expect(main).toContainText("Il Mundo");
  await expect(main).toContainText("Free Italy Committee");
  await expect(main).toContainText("WN#12189");
});

test("Kenneth Romney profile publishes radio as an occupation without inventing an employer", async ({ page }) => {
  await page.goto("./people/22ece9ec-0273-5e3d-9d93-62873d3ed7b4/");
  const main = page.locator("main");
  await expect(main).toContainText("worked in radio before military service");
  await expect(main).toContainText("does not name his pre-service employer");
  await expect(main).toContainText("The Robert Lee Observer");
  await expect(main).toContainText("occupation only");
  await expect(page.locator("#immediate-affiliation").locator("xpath=..")).not.toContainText("American Broadcasting Company");
  await expect(page.locator("#civilian-employer").locator("xpath=..")).not.toContainText("American Broadcasting Company");
});

test("Batch 818 identity conflicts remain visible and do not inherit Army identities", async ({ page }) => {
  const conflicts = [
    ["ccfe1778-a76a-51d8-a0df-4d7455e659b0", "Harold Burdette"],
    ["90c12687-e35d-57c0-96a5-4af6b0ff94e2", "Roland J. Rondeau"],
    ["963a85d4-40b7-5cdc-a234-dd072e58bd3c", "Lewis B. Whitley"],
  ] as const;
  for (const [id, conflictingName] of conflicts) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("conflicting sources");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText("No reliable pre-OSS employer");
  }
});

test("The printed 2D LT variant is classified as a commissioned Army officer", async ({ page }) => {
  await page.goto("./people/cf08b0c0-42e9-52f7-bef1-a29d47c57d63/");
  const main = page.locator("main");
  await expect(main).toContainText("2D LT");
  await expect(main).toContainText(/commissioned army officer/i);
  await page.goto("./people/?commissioned=yes&q=Romanoski");
  await expect(page.locator("main")).toContainText("Edwin P Romanoski");
});
