import { expect, test } from "@playwright/test";

const profiles = [
  ["030fcb03-dd46-50f1-9344-32434bef077b", "Theadfield L Poehl"],
  ["d092c04a-1fbd-5257-8402-157ffb2697f6", "Jessie Poesch"],
  ["befc8f82-0033-5d9e-9346-0a8dcf76d2ec", "Danny A Poggioli"],
  ["6eab264a-e2dd-533a-b2c4-61308828deca", "Stanley M Pogwist"],
  ["dfcb80c5-c559-5ecb-92bd-a3cfeacd2477", "Herbert O Pohl"],
  ["ff7b0311-ce2d-5f1b-bc1b-1e790e33e4b7", "George W Pohle"],
  ["4beba8bc-09a5-5eb0-a5d5-976c2c3a60e5", "Joseph A Pohling"],
  ["9aaf44b1-904a-5486-b284-2c29271c151f", "William B Pohlman"],
  ["80a2a462-c6ba-5e34-84fc-abe3ed66e768", "Cornelius Poillon"],
  ["46c2d655-bf6e-541d-b7d7-25e37cd34c2e", "John D Poindexter"],
  ["e32f7f8b-38f1-5b69-9ccd-201c16665363", "Maurice C Poissant"],
  ["1e4758de-6312-5bbd-8345-2976e4d77f0d", "Edwin W Poitras"],
  ["b77e9378-06cc-5b45-b654-6a89df33a558", "John J Poklar"],
  ["34f2a3d8-afe3-5074-819a-e78ba342576a", "Stanley E Pokora"],
  ["3c0c040c-9d06-56fe-8f13-716f67015782", "Julian Pokrwyka"],
  ["8de8b9ea-7190-56cb-ad0a-33ae21e03f14", "Edward B Polak"],
  ["a834f3df-24b6-5d94-8a7f-3ddf1c30137c", "Andrew B Polansky"],
  ["2522ba23-1c5d-55c9-a5b3-b352f0284162", "Raymond F Polczak"],
  ["4f8376c1-02a2-51ea-90f1-9897202530cc", "Demetrios J Polemis"],
  ["e562f36e-a7f8-5e25-9213-402a7166f512", "Leonid Polevoy"],
  ["d61a6927-d48c-5d33-8835-54e9b2180493", "Thomas Polgar"],
  ["0ba3af6b-12ad-598c-bfdb-17269d3837d6", "Rose M Polito"],
  ["efc3b8b2-5296-517b-935b-af65f9d07292", "Joseph O Politte"],
  ["989b5479-5f34-5d36-8ce7-8a0ba058efec", "James P Polk"],
  ["426157a4-9c41-563a-a3b1-ffa3fc3b005e", "Mitchell A Polkowski"],
  ["a3b6641a-0a47-5467-9ac5-9ed6a5be5669", "David Pollack"],
  ["681c8619-1bf8-5c99-b56b-14843d69527c", "Nat Pollack"],
  ["3032fd87-81fa-595b-a4c0-c38ab6f31dce", "Robert E Pollack"],
] as const;

test("Batch 764 publishes all 28 profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 764 publishes Thomas Polgar's qualified Army predecessor without a civilian employer", async ({ page }) => {
  await page.goto("./people/d61a6927-d48c-5d33-8835-54e9b2180493/");
  const main = page.locator("main");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  const civilian = main.locator("section[aria-labelledby='civilian-employer']");
  await expect(immediate).toContainText("U.S. Army");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("medium");
  await expect(immediate).toContainText("explicit immediate");
  await expect(civilian).not.toContainText("U.S. Army");
  await expect(main).toContainText("Thomas Polgar, also a former OSS officer");
});

test("Batch 764 preserves source-name discrepancies and excludes Army codes", async ({ page }) => {
  for (const [id, expected] of [
    ["80a2a462-c6ba-5e34-84fc-abe3ed66e768", "POILLON CORNELIUS TRD"],
    ["4f8376c1-02a2-51ea-90f1-9897202530cc", "POLEMIS DEMETRIOS"],
    ["e562f36e-a7f8-5e25-9213-402a7166f512", "POLEVOY LEONID S"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(expected);
    await expect(main).not.toContainText("civilian occupation code");
    await expect(main).not.toContainText("army grade code");
  }
});

test("Batch 764 preserves Pokrwyka while exposing the search-only variant", async ({ page }) => {
  await page.goto("./people/3c0c040c-9d06-56fe-8f13-716f67015782/");
  await expect(page.getByRole("heading", { name: "Julian Pokrwyka", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("Julian Pokrywka");
  await expect(main).toContainText("test the Pokrywka spelling as a search alias only");
  await expect(main).toContainText("The page image confirms Pokrwyka");
});

test("Batch 764 leaves the Poesch and Poindexter namesakes unresolved", async ({ page }) => {
  for (const [id, withheldText] of [
    ["d092c04a-1fbd-5257-8402-157ffb2697f6", "lacks an OSS or personnel-file bridge"],
    ["46c2d655-bf6e-541d-b7d7-25e37cd34c2e", "age-incompatible namesake"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("unresolved");
    await expect(main).toContainText(withheldText);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
      "verified",
    );
  }
});

test("home page exposes the rebuilt Batch 764 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,581");
  await expect(home).toContainText("44.20%");
  await expect(home).toContainText("13,353");
  await expect(home).toContainText("783");
  await expect(home).toContainText("347");
  await expect(home).toContainText("9,039");
});
