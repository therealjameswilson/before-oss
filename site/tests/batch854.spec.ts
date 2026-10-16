import { expect, test } from "@playwright/test";

const profiles = [
  ["c46cc34f-f27f-5935-9f92-bf78efa84cd2", "Anna F Schwiebert"],
  ["46d03926-66da-5b04-adf7-336c426cd4ec", "Jerry Sciales"],
  ["7db289b8-b71b-5a1b-8aca-e40ef94bea54", "Alfred Sciarrotta"],
  ["d7d9ce20-f063-59ea-906d-471f7fc838c6", "Edward A Scigliano"],
  ["f618c22d-7c9d-501a-b07b-ad43bedb94a4", "Phillip Scinto"],
  ["d42eb106-8aa0-577a-acd8-d23a689b5629", "Frank Sciortino"],
  ["e845d1a5-e8e4-5c22-8d8d-75275a7952cb", "Arthur Sclater"],
  ["e1103626-50c2-5679-ab0f-324c8705233c", "Kenneth Scoca"],
  ["18865885-fc6d-568d-abab-c89384919fd0", "Richard G Scoffone"],
  ["735f36f8-6e94-5d23-a384-7fd215c2f381", "Carleton F Scofield"],
  ["b99e6289-13f5-598b-a061-93ad8e6a6f7c", "Charles Scofield"],
  ["5f57190d-4987-50b0-9c84-b53f366065db", "Isabelle A Scofield"],
  ["c559bc10-2e25-55d5-a08e-1466de6bfaec", "Melvin W Scofield"],
  ["c70b52a1-9ac9-511d-9441-a65b2ade1298", "John W Scoggin"],
  ["f85cd6e5-e667-5cb9-9fee-8c062162afbe", "Patrick E Scoleri"],
  ["6fdf1d8d-0c01-5648-8d6e-f47b4199746b", "Glenn R Scoles"],
  ["e494b964-f3c3-5612-904e-549d71d03302", "* Scory"],
  ["5657736e-f8ad-5314-b76a-6d377200c8ce", "* Scott"],
  ["2eb1abba-67af-5540-bbb0-f81a6053c33f", "Beverly Scott"],
  ["3e7d71b8-78c2-52e3-80da-f0b37288ffbd", "Carl A Scott"],
  ["f03cb6c6-fb09-507f-aed0-9831b887e51a", "Caroline Scott"],
  ["d553649e-7be0-58e0-a3e3-81bf54dd2d4c", "Charles B Scott"],
  ["461de58f-1ab5-5240-8a48-62eb0d455b7d", "Clarence E Scott"],
] as const;

test("Batch 854 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Alfred Sciarrotta publishes a qualified occupation without inventing a named employer", async ({ page }) => {
  await page.goto("./people/7db289b8-b71b-5a1b-8aca-e40ef94bea54/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("engineer who worked on undersea weapons in Naples");
  await expect(main).toContainText("Alfredo Sciarrotta");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceNaval Torpedo Station");
});

test("Arthur Sclater publishes the direct official identity evidence but no pre-service employer", async ({ page }) => {
  await page.goto("./people/e845d1a5-e8e4-5c22-8d8d-75275a7952cb/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("Shetland Base");
  await expect(main).toContainText("OSS Awards and Decorations Board minutes and attachments");
  await expect(main).toContainText("PDF page 154, printed page 36");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Carleton Scofield publishes the University of Buffalo only as documented prewar employment", async ({ page }) => {
  await page.goto("./people/735f36f8-6e94-5d23-a384-7fd215c2f381/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("documented prewar employer found");
  await expect(main).toContainText("University of Buffalo");
  await expect(main).toContainText("Documented in a 1935 scholarly publication");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationUniversity of Buffalo");
  await expect(main).not.toContainText("Last civilian employer before serviceUniversity of Buffalo");
});
