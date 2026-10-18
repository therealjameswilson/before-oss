import { expect, test } from "@playwright/test";

const profiles = [
  ["3acab0b1-4870-538e-8a99-460202232bb9", "Arthur A Skiathitis"],
  ["7404a311-47ca-5546-9f27-109f73f68d54", "Sibilla Skidelsky"],
  ["77ac94fe-710a-5a42-a46e-6ca46c358e3f", "James W Skidmore"],
  ["22307a99-a544-50ad-9b08-f939e86ca4a1", "Richard C Skidmore"],
  ["3faee371-de4f-593d-ad67-d89872184e3b", "Nicholson Skilenes"],
  ["17aaf245-c010-5293-9c13-d5d7521152ab", "Einar Skinnarland"],
  ["733d623f-3e6c-53a8-a523-e162e0b750a4", "John P Skinner"],
  ["04227477-48e2-5a9d-b853-b432c33729e5", "Joseph Skinner"],
  ["26416685-82f3-539f-8f95-722a9adfce58", "Ralph C Skinner"],
  ["30c96ebf-f705-522f-b929-6af74c143e3b", "Samual F Skinner"],
  ["e2091fc8-1b40-5fc6-80ba-f872a77d80c0", "Selby M Skinner"],
  ["ff202418-01ca-5bde-a603-79ac2d8e13f2", "Thomas E Skinner"],
  ["fb98b896-640f-5586-a55a-ceac3e549f6c", "George B Skipper"],
  ["f5328981-10b8-52d7-9ea4-0f9a1e0ee5ac", "Christ Skiriotis"],
  ["cca66ffa-f980-598a-b0d0-b4121020a8db", "Hakon A Skjolsvik"],
  ["cd5d9c76-cd98-59db-b27e-50d6e371ee08", "Erling Skogstad"],
  ["ae961a33-7a0e-5c5e-94e9-029b813f7670", "Sidney P Skokos"],
  ["00957063-3d4a-5a8d-92f4-54da2c3b8905", "Frank J Skokoski"],
  ["0930e7b7-aab1-51d2-857e-3c7ceeffb337", "Folke K Skoog"],
  ["463fca81-940f-5324-96b6-fe87f8f73e04", "George P Skouras"],
  ["991a2674-8a19-5eb7-adf1-7473d6ff6fc1", "Emile B Skraly"],
  ["9d9e47d5-db9d-54fb-8568-9be0be13698f", "Stanley J Skuk"],
  ["daa35c7c-7a5e-5a97-9ffd-3bc0b7e77c1b", "Clarence W Skupic"],
] as const;

test("Batch 882 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 882 publishes Einar Skinnarland's immediate work site without inventing an employer", async ({ page }) => {
  await page.goto("./people/17aaf245-c010-5293-9c13-d5d7521152ab/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("Mårvatn Dam Works");
  await expect(immediate).toContainText("unknown");
  await expect(immediate).toContainText("explicit immediate");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 882 publishes Frank Skokoski's Army-to-OSS pathway as military assignments", async ({ page }) => {
  await page.goto("./people/00957063-3d4a-5a8d-92f4-54da2c3b8905/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("541st Parachute Infantry Regiment");
  await expect(immediate).toContainText("military assignment");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("79th Infantry Division");
  await expect(earlier).toContainText("Medic");
});

test("Batch 882 keeps probable academic and journalism matches visibly qualified", async ({ page }) => {
  for (const [id, expected] of [
    ["7404a311-47ca-5546-9f27-109f73f68d54", "New York Sun"],
    ["0930e7b7-aab1-51d2-857e-3c7ceeffb337", "Johns Hopkins University"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusprobable");
    await expect(main).toContainText(expected);
    await expect(main).toContainText("medium");
    await expect(main).toContainText("qualified");
  }
});

test("Batch 882 publishes George Skouras's theater-chain evidence as qualified, not immediate", async ({ page }) => {
  await page.goto("./people/463fca81-940f-5324-96b6-fe87f8f73e04/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  const civilian = main.locator("section[aria-labelledby='civilian-employer']");
  await expect(civilian).toContainText("Skouras Theatre Chain");
  await expect(civilian).toContainText("medium");
  await expect(civilian).toContainText("documented pre-OSS");
});

test("Batch 882 preserves the Hakon Skjolsvik conflict without exposing the identifier", async ({ page }) => {
  await page.goto("./people/cca66ffa-f980-598a-b0d0-b4121020a8db/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("both index entities remain separate");
  await expect(main).toContainText("Jointly review the Box 716 personnel files");
  const serial = main.locator("dt").filter({ hasText: /^Serial$/ })
    .locator("xpath=following-sibling::dd[1]");
  await expect(serial).toContainText("••••");
  await expect(serial).not.toHaveText(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
});

test("Batch 882 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 585,
    research_attempted_people: 13_248,
    verified_affiliation_people: 961,
    verified_employer_people: 433,
    archival_review_assessed_people: 11_715,
    published_claims: 8_008,
    public_sources: 5_424,
  });
});
