import { expect, test } from "@playwright/test";

const profiles = [
  ["a416b1b1-0a9c-5254-8939-64a2f3e9791d", "Rose S Pollack"],
  ["af602ed1-b04e-5994-99b0-8a0ca4c8235c", "Magda Pollaczek"],
  ["ef0ea904-819c-5212-971f-e9a0e25a0bc5", "George Pollard"],
  ["55e508ab-7848-539f-9c4c-f39a9c972664", "Edna L Pollock"],
  ["b4a43491-4cee-5c09-a40e-2cad86761a2d", "Frederick Pollock"],
  ["5a5e4a70-0929-5d3a-aa88-330820397d05", "George S Pollock"],
  ["7f12c067-488b-568a-9533-c4063b0c285e", "Stephen L Pollock"],
  ["b1c52d1d-bf5d-515c-bafb-41d148594e15", "Abraham Polonsky"],
  ["89dbc741-a6d2-534d-812f-a269db9721e0", "Stanford I Polonsky"],
  ["8e0202a1-6dd7-5f62-afdf-d8899e42178e", "Joseph F Polony"],
  ["9d528b5f-b161-5f98-afaf-9561b8712691", "Allen E Polson"],
  ["aca1a900-e6fc-5bb2-83e0-4cbdc10b0b41", "Konstanty Poluszejko"],
  ["f104538b-4071-52ad-ad62-32d612b7ff9f", "Peter Polychronopo"],
  ["40a72175-9d89-51b7-bada-4d2eec726f3d", "Demetrios N Polyzos"],
  ["03e8f6bf-b385-5126-83af-e3295de3bc20", "Daniel Pomeranz"],
  ["36cd062a-3459-5594-a8cc-bfbfdec01570", "Chester M Pomeroy"],
  ["edba02d9-5e39-5342-8c03-b1e787bd4361", "Robert L Pomeroy"],
  ["c2a2d1c0-9e92-5f10-9dc8-92a0acef25d7", "Edward C Pomme"],
] as const;

test("Batch 765 publishes all 18 profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 765 separates Magda Pollaczek's employer from student status", async ({ page }) => {
  await page.goto("./people/af602ed1-b04e-5994-99b0-8a0ca4c8235c/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("Dana Hall");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Dana Hall");
  await expect(main).toContainText("Bryn Mawr College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("hired to teach French for a year at Dana Hall");
});

test("Batch 765 qualifies Abraham Polonsky's Paramount employment", async ({ page }) => {
  await page.goto("./people/b1c52d1d-bf5d-515c-bafb-41d148594e15/");
  const main = page.locator("main");
  const civilian = main.locator("section[aria-labelledby='civilian-employer']");
  await expect(civilian).toContainText("Paramount");
  await expect(civilian).toContainText("medium");
  await expect(civilian).toContainText("strongly date bounded");
  await expect(main).toContainText("Abraham Lincoln Polonsky");
});

test("Batch 765 preserves surname and damaged-name discrepancies", async ({ page }) => {
  await page.goto("./people/f104538b-4071-52ad-ad62-32d612b7ff9f/");
  await expect(page.getByRole("heading", { name: "Peter Polychronopo", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Peter Polychronopoules");
  await page.goto("./people/40a72175-9d89-51b7-bada-4d2eec726f3d/");
  await expect(page.locator("main")).toContainText("POLYZOS DE ETRIOS");
  await expect(page.locator("main")).toContainText("S/Sgt. Demetrios N. Polyzos");
});

test("Batch 765 withholds plausible but unbridged Frederick Pollock biography", async ({ page }) => {
  await page.goto("./people/b4a43491-4cee-5c09-a40e-2cad86761a2d/");
  const main = page.locator("main");
  await expect(main).toContainText("Friedrich Pollock");
  await expect(main).toContainText("no protected identifier or direct personnel-file bridge");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("verified");
});

test("home page exposes the rebuilt Batch 765 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,599");
  await expect(home).toContainText("44.27%");
  await expect(home).toContainText("13,335");
  await expect(home).toContainText("784");
  await expect(home).toContainText("348");
  await expect(home).toContainText("9,057");
});
