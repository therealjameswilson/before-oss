import { expect, test } from "@playwright/test";

const profiles = [
  ["9ef8d657-0c05-5a5e-af6c-41974cc0c486", "Rudolf L Mosler"],
  ["d0a927f8-7d3e-5a61-aada-02fc1ab9fc2b", "Wilson H Mosley"],
  ["0c62c1ca-7f45-5da6-9d60-31363cb60a4e", "George H Moss"],
  ["9ffc5d00-d653-538d-9556-47f1168c60f7", "George W Moss"],
  ["fc76060c-8e95-59ee-b3bc-537adb0ad369", "Helen B Moss"],
  ["42d5fa23-44c3-5e6a-89ca-acbff7461b3e", "Robert F Moss"],
  ["cabb4167-6be0-5591-ab26-98319d396ff2", "Ellen P Mossberg"],
  ["debdd30b-16c1-5dc3-a21b-9e92044607ea", "John Mossberg"],
  ["07299978-1514-5729-9c78-dc98400e06cd", "George N Mossholder"],
  ["0fdaf441-03ce-5f9b-8452-fd8469de0fd6", "Samuel Mossious"],
  ["59312134-68da-594d-b362-5e2d324e3698", "Arnando Mostachetti"],
  ["1621e5e7-47cd-5637-bc2a-dd05d326e306", "Robert S Moth"],
  ["5aa5bdfc-01fb-56e7-8cdd-7d25e0a52796", "Frank P Motisi"],
  ["933c9639-5d63-57da-afc3-1a36e551cda1", "Lars Motland"],
  ["8ebb4ef1-4ef5-5069-8d31-4f99974868d4", "Mario V Motola"],
  ["2b4470de-820b-5764-ab28-9b4c71a4f059", "Rhoda Motraux"],
  ["fca5e849-02d7-5b03-8a6b-749a49788d9d", "Ervin E Mott"],
  ["86219d91-8a88-5b6a-87e3-75cf44743ff2", "George L Mott"],
  ["c93ee360-6f84-5bdc-94ce-e006b1f540c0", "Veral D Mott"],
  ["dc418390-ffb4-544a-9195-48c6b89fcc81", "Geoffrey A Mott-Smith"],
  ["1940c502-cd3a-508b-a64f-cad818de6dbe", "May Mott-Smith"],
  ["e30025c5-c63e-5d1c-904e-2b73e9e4ec46", "Dorothy M Mouinhan"],
  ["1587e27f-0959-5caa-a53b-4f7527868deb", "Helen L Moulder"],
] as const;

test("Batch 683 publishes all 23 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 332");
    await expect(page.locator("main")).toContainText("Archive box");
  }
});

test("Batch 683 publishes Geoffrey Mott-Smith's immediate editorial affiliation without inventing an employer", async ({ page }) => {
  await page.goto("./people/dc418390-ffb4-544a-9195-48c6b89fcc81/");
  const main = page.locator("main");
  await expect(main).toContainText("The Chess Correspondent");
  await expect(main).toContainText("Problem editor");
  await expect(main).toContainText("American Contract Bridge League");
  await expect(main).toContainText("Games Digest");
  await expect(main).toContainText("explicit immediate");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("The Chess Correspondent");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Games Digest");
});

test("Batch 683 supports Rudolf Mosler's identity while leaving his predecessor affiliation unresolved", async ({ page }) => {
  await page.goto("./people/9ef8d657-0c05-5a5e-af6c-41974cc0c486/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Artillery Officer Candidate School");
  await expect(main).toContainText("Camp Ritchie");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 683 publishes three protected-identifier Army identities without employer claims", async ({ page }) => {
  const armyIdentities = [
    "0c62c1ca-7f45-5da6-9d60-31363cb60a4e",
    "5aa5bdfc-01fb-56e7-8cdd-7d25e0a52796",
    "86219d91-8a88-5b6a-87e3-75cf44743ff2",
  ];

  for (const id of armyIdentities) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 683 keeps three Army name and identifier conflicts public and unresolved", async ({ page }) => {
  await page.goto("./people/59312134-68da-594d-b362-5e2d324e3698/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Arnando Mostachetti");
  await expect(main).toContainText("Armando Mostachetti");

  await page.goto("./people/fca5e849-02d7-5b03-8a6b-749a49788d9d/");
  main = page.locator("main");
  await expect(main).toContainText("Ervin E Mott");
  await expect(main).toContainText("Ervin S Mott");
  await expect(main).toContainText("conflicting");

  await page.goto("./people/933c9639-5d63-57da-afc3-1a36e551cda1/");
  main = page.locator("main");
  await expect(main).toContainText("Lars Motland");
  await expect(main).toContainText("Laro Montland");
  await expect(main).toContainText("Duplicate group");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 683 rejects the famous May Mott-Smith biography as an unsupported name-only match", async ({ page }) => {
  await page.goto("./people/1940c502-cd3a-508b-a64f-cad818de6dbe/");
  const main = page.locator("main");
  await expect(main).toContainText("unresolved");
  await expect(main).toContainText("not assigned on name alone");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 683 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,758");
  await expect(page.locator("body")).toContainText("36.58%");
  await expect(page.locator("body")).toContainText("307");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil companies");

  await page.goto("./people/");
  await expect(page.locator(".featured-directory-category li")).toHaveCount(8);
});
