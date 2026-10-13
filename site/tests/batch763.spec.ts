import { expect, test } from "@playwright/test";

const profiles = [
  ["e5886753-5e34-52d8-a9d5-f95749a1e245", "Karl J Platz"],
  ["22a8155e-482d-57d9-a541-80d94b764b51", "Maja H Platzer"],
  ["09587954-f1b6-59ad-81c6-580e6ed026e9", "James S Plaut"],
  ["6e46769d-216d-5380-aa82-0af3139fba52", "Margaret F Player"],
  ["2326020d-34ac-5c19-a8c7-b0b535b2aa44", "Delia T Pleasants"],
  ["458aaaf1-4f06-5083-bc1a-df3dd5acf99f", "Frederick R Pleasants"],
  ["6b5fa50b-49fc-5079-9dbd-ac8896931b56", "Helen L Pleasants"],
  ["a7f78e16-69af-54df-8d5e-aec14606d7bc", "Pierre Plechot"],
  ["31ec9e21-f0ce-59c9-b937-183819281453", "William P Pleitz"],
  ["04528624-e6aa-5991-b410-5c094ffefbda", "Richard J Pleska"],
  ["4f25e578-46ac-51ff-ad0b-44808566f565", "Ralph A Plesko"],
  ["80a3ca9c-2e28-5fe2-b04e-be9bc1eb282a", "Edward G Pleva"],
  ["fe92a306-f9dd-55a0-8eb4-bd52275a70eb", "Henry P Plourde"],
  ["e26bf0e5-9b39-588c-ba1a-6d06cc3befe4", "Harry B Plowman"],
  ["35c1df80-bee8-5a4b-b1a1-f99de081cbb5", "Anne E Plumb"],
  ["1de3b7be-3be5-5c92-b54f-b9e66cc41ce7", "Vincent W Plumeri"],
  ["46fa2829-3ec6-53b3-9168-5527d009fbd5", "Nathan Plung"],
  ["f55e8419-afd7-5470-87df-4786454accba", "Richard F Plunkett"],
  ["d06b349d-51a1-5bf8-a7be-6cf4d0d7a37e", "Stanley A Pobutkiewicz"],
  ["acdffe40-6aac-5d93-b0a6-e90d76a33741", "Francis M Poche"],
  ["9151f184-005d-54ef-9f29-0083441245e9", "Peter G Pocock"],
  ["5f16d8ef-504e-523a-ae5c-d10bc6411675", "Nicholas Podar"],
  ["efbfe9fa-8251-5148-9f52-5b219968c8ba", "Robert G Podewils"],
  ["f12f5718-0560-5a3c-9b28-ed37a86f21cd", "Andy N Podolak"],
  ["b289b7b3-f978-5576-97bc-7951364e3ffb", "Charles M Poe"],
  ["e11f3a3d-0755-51d7-84a1-77027f3fa33e", "Lois Poe"],
  ["3a15c72a-0abc-51c8-b261-b4b728bd3ed3", "Ophelia Poe"],
] as const;

test("Batch 763 publishes all 27 profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 763 separates James Plaut's military predecessor from civilian employment", async ({ page }) => {
  await page.goto("./people/09587954-f1b6-59ad-81c6-580e6ed026e9/");
  const main = page.locator("main");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  const civilian = main.locator("section[aria-labelledby='civilian-employer']");
  await expect(immediate).toContainText("Office of Naval Intelligence");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("confirmed");
  await expect(civilian).toContainText("Boston Institute of Modern Art");
  await expect(civilian).toContainText("Director");
  await expect(civilian).not.toContainText("Office of Naval Intelligence");
});

test("Batch 763 publishes Frederick Pleasants's Peabody Museum employment", async ({ page }) => {
  await page.goto("./people/458aaaf1-4f06-5083-bc1a-df3dd5acf99f/");
  const main = page.locator("main");
  await expect(main).toContainText("Frederick Rhodes Pleasants");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Peabody Museum of Archaeology and Ethnology",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Assistant to the Director",
  );
  await expect(main).toContainText("1940");
  await expect(main).toContainText("1942");
});

test("Batch 763 keeps official-name conflicts visible and transfers no Army employer", async ({ page }) => {
  for (const [id, conflictingName] of [
    ["e5886753-5e34-52d8-a9d5-f95749a1e245", "WILLARD MARTIN H"],
    ["fe92a306-f9dd-55a0-8eb4-bd52275a70eb", "PLOTRUV YVVRY P"],
    ["f12f5718-0560-5a3c-9b28-ed37a86f21cd", "PODOL ANDY N"],
    ["b289b7b3-f978-5576-97bc-7951364e3ffb", "JOE CHARLES M"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(conflictingName);
    await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
      "United States Army",
    );
  }
});

test("Batch 763 preserves Plumb spelling and both Plunkett source rows", async ({ page }) => {
  await page.goto("./people/35c1df80-bee8-5a4b-b1a1-f99de081cbb5/");
  await expect(page.getByRole("heading", { name: "Anne E Plumb", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("surname Plumb and CAF-3 grade");

  await page.goto("./people/f55e8419-afd7-5470-87df-4786454accba/");
  const plunkett = page.locator("main");
  await expect(plunkett).toContainText("Index row 2");
  await expect(plunkett).toContainText("Boxes 609 and 625");
  await expect(plunkett).toContainText("M/Sgt");
  await expect(plunkett).toContainText("T/Sgt");
});

test("home page exposes the rebuilt Batch 763 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,553");
  await expect(home).toContainText("44.08%");
  await expect(home).toContainText("13,381");
  await expect(home).toContainText("783");
  await expect(home).toContainText("347");
  await expect(home).toContainText("9,011");
});
