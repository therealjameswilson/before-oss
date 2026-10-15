import { expect, test } from "@playwright/test";

const profiles = [
  ["b1d00675-6fde-5c54-8235-a3e0fc9911c8", "Franz W Rosenthal"],
  ["2526a392-080d-5ab3-a730-bb424939c75e", "Hilda G Rosenthal"],
  ["00a99c04-51f1-5735-b11b-ddb5a366c628", "Laura L Rosenthal"],
  ["8f12b16d-9a1b-52a4-bb01-30b76567cf97", "Leslie Rosenzweig"],
  ["2a5478a5-aebb-55a6-a7bf-ce0400ccc28e", "Francis C Rosett"],
  ["c88b90aa-01bc-514f-9a0c-7b61f605e125", "Stephen O Rosetti"],
  ["e100744d-6f60-53c5-8345-7ef58f85132a", "Douglas A Rosher"],
  ["f1a99620-e303-539a-ba94-078972258bea", "Malcolm L Rosholt"],
  ["8394b8fd-f577-545f-8c42-c40261660dbf", "Martha Rosi"],
  ["fbad18dc-02fd-5e94-8788-a823e73ebd1a", "Joseph M Rosia"],
  ["279fd6c9-551f-5606-9009-31f04dae4284", "Donald G Rosine"],
  ["a9f99e5f-7050-5cee-b7e6-c258bd9e0465", "Chester J Rosinski"],
  ["2d319e2b-a254-5f82-93d1-120e6a1e2964", "Barbara B Rositzke"],
  ["ee7f5c2b-7c9b-51d3-95ad-5ff84b3be141", "Harry A Rositzke"],
  ["03032157-7e54-53e4-8688-1e748da55d10", "Andrew Roskos"],
  ["ac305497-1bed-5109-a824-65486b9ed05a", "Oscar H Rosner"],
  ["d5b76156-7603-546d-81af-f80eeaca6b4d", "Bruno J Rospenda"],
  ["b5cdd8c6-36d3-5fb0-a287-c788edf14c82", "Adrion N Ross"],
  ["bd92a264-68fa-51de-9f82-9bba42474231", "Alfred J Ross"],
  ["e2d0b4f5-db4d-5bbb-a486-61f9758c6477", "Anthony E Ross"],
  ["0bf6ddfb-4afc-5277-9ce4-21bdcbef6d8d", "Barbara Ross"],
  ["1f0b3c7c-ed8c-53b2-b5be-80d00836c507", "Beecher B Ross"],
  ["86c00b9c-7e9d-5bda-a53f-440f122f3d9c", "Darrell E Ross"],
] as const;

test("Batch 821 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Franz Rosenthal profile separates his civilian employer from his Army-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/b1d00675-6fde-5c54-8235-a3e0fc9911c8/");
  const main = page.locator("main");
  await expect(main).toContainText("Hebrew Union College");
  await expect(main).toContainText("last documented civilian employer");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("After basic training, he joined the Office of Strategic Services");
});

test("Malcolm Rosholt profile distinguishes two newspaper employers and qualifies the military timing", async ({ page }) => {
  await page.goto("./people/f1a99620-e303-539a-ba94-078972258bea/");
  const main = page.locator("main");
  await expect(main).toContainText("China News Service");
  await expect(main).toContainText("China Press");
  await expect(main).toContainText("Fourteenth Air Force");
  await expect(main).toContainText("exact relationship to OSS service remains uncertain");
});

test("Harry Rositzke profile publishes Rochester as the last documented civilian employer", async ({ page }) => {
  await page.goto("./people/ee7f5c2b-7c9b-51d3-95ad-5ff84b3be141/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Rochester");
  await expect(main).toContainText("instructor");
  await expect(main).toContainText("last documented civilian employer before wartime OSS service");
});

test("Barbara Rositzke profile visibly qualifies the directory-based employment match", async ({ page }) => {
  await page.goto("./people/2d319e2b-a254-5f82-93d1-120e6a1e2964/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Rochester");
  await expect(main).toContainText("film assistant");
  await expect(main).toContainText("match remains qualified");
  await expect(main).toContainText("Probable rather than high confidence");
});

test("Army identity-only matches do not become employer claims", async ({ page }) => {
  for (const id of [
    "8f12b16d-9a1b-52a4-bb01-30b76567cf97",
    "279fd6c9-551f-5606-9009-31f04dae4284",
    "03032157-7e54-53e4-8688-1e748da55d10",
    "ac305497-1bed-5109-a824-65486b9ed05a",
    "1f0b3c7c-ed8c-53b2-b5be-80d00836c507",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("official Army bulk record");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("rejected identifier conflicts remain unresolved archival-review cases", async ({ page }) => {
  for (const [id, conflictingName] of [
    ["a9f99e5f-7050-5cee-b7e6-c258bd9e0465", "Loreine W. Tooke"],
    ["e2d0b4f5-db4d-5bbb-a486-61f9758c6477", "Carmelo A. Guaette"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("requires archival review");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText("was rejected");
  }
});
