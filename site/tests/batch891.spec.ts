import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page435-smith-continuation-review_batch-891_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["438a81b6-647c-51bf-b5b6-a53c2c158ca5", "Robert W Smith", "725"],
  ["e635478f-5c1b-546e-ba4d-e7b46324038c", "Robert G Smith", "725"],
  ["8bf823dd-6f4b-5e1b-9d06-cee2ad34f635", "Robert K Smith", "725"],
  ["71eef5f5-ba52-5047-8e54-b4598fc66dee", "Robert F Smith", "724"],
  ["b11baf40-7e25-5fd2-81a2-ea737792e016", "Robert B Smith", "724"],
  ["74aa846e-915c-5872-a53c-255d72176a2b", "Robert M Smith", "725"],
  ["0949e62d-df9f-5a21-bb88-65c0013c8cb8", "Robert B Smith", "724"],
  ["7864e8d2-56bd-56f7-a746-57720209284f", "Robert A Smith", "724"],
  ["d72b29b0-777d-594b-943c-fccdb06b72ac", "Robert A Smith", "724"],
  ["3dce0dac-b055-5a94-aed0-5ac33e5b902a", "Robert F Smith", "724"],
  ["33f6ed9b-9f87-528f-b9dc-b230626c621d", "Russell K Smith", "725"],
  ["cf561725-0f49-5f2c-9766-f65dc2b46a28", "Ruth A Smith", "725"],
  ["aaf55d5f-f53e-5d7c-929a-eb7a4e6b69f6", "Ruth E Smith", "725"],
  ["bb02ba81-a9f3-5333-bdbb-c24bbf698b98", "Ruthanna Smith", "725"],
  ["1095ac4a-7293-5fac-97fe-16e5d0b6e7bf", "Sam M Smith", "725"],
  ["1c688f94-0919-52dd-94ec-011395f677b2", "Sands Smith", "725"],
  ["36b49e6d-0451-50ab-a0a4-2383592db6f1", "Sara E Smith", "725"],
  ["0ac0ee95-fec0-5792-b835-6b8f91ceb453", "Saul Smith", "725"],
  ["72b0a311-b136-5130-a35e-2a36c1f2904c", "Saul M Smith", "725"],
  ["24867299-a213-5a46-b0d9-1f70d3909fc2", "Sidney B Smith", "725"],
  ["f86c15f2-9a6f-5be9-90c9-d30a56556303", "Stella T Smith", "725"],
  ["02f23a7e-922f-5848-935a-25e0b166371d", "Stephen J Smith", "725"],
  ["da092c48-923d-5c64-8cbc-52f2c0791c8c", "Sunday B Smith", "725"],
] as const;

test("Batch 891 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 891 publishes nine qualified non-employer findings", async ({ page }) => {
  const checks = [
    ["e635478f-5c1b-546e-ba4d-e7b46324038c", "Welders and flame cutters"],
    ["b11baf40-7e25-5fd2-81a2-ea737792e016", "Salesmen, insurance"],
    ["0949e62d-df9f-5a21-bb88-65c0013c8cb8", "historical student category"],
    ["d72b29b0-777d-594b-943c-fccdb06b72ac", "Sports instructors, athletes, and sports officials"],
    ["3dce0dac-b055-5a94-aed0-5ac33e5b902a", "Chauffeurs and drivers, bus, taxi, truck, and tractor"],
    ["1095ac4a-7293-5fac-97fe-16e5d0b6e7bf", "Clerks, general office"],
    ["1c688f94-0919-52dd-94ec-011395f677b2", "historical student category"],
    ["02f23a7e-922f-5848-935a-25e0b166371d", "Architects"],
    ["da092c48-923d-5c64-8cbc-52f2c0791c8c", "Attendants, filling stations and parking lots"],
  ] as const;
  for (const [id, finding] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(finding);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("same-name rows remain separate and visibly grouped", async ({ page, request }) => {
  const groups = [
    [["7864e8d2-56bd-56f7-a746-57720209284f", "d72b29b0-777d-594b-943c-fccdb06b72ac"], "duplicate-915e56209551"],
    [["b11baf40-7e25-5fd2-81a2-ea737792e016", "0949e62d-df9f-5a21-bb88-65c0013c8cb8"], "duplicate-3db0b44af163"],
    [["c4738870-9e3f-5a3c-b157-b93bdc6b8673", "71eef5f5-ba52-5047-8e54-b4598fc66dee", "3dce0dac-b055-5a94-aed0-5ac33e5b902a"], "duplicate-d292bbaf9a24"],
  ] as const;
  for (const [ids, publicGroup] of groups) {
    for (const id of ids) {
      const response = await request.get(`./people/${id}/`);
      expect(response.ok()).toBeTruthy();
      await page.goto(`./people/${id}/`);
      await expect(page.locator("main")).toContainText(publicGroup);
    }
    expect(new Set(ids).size).toBe(ids.length);
  }
});

test("Army suffixes remain variants and M/Sgt remains the indexed later rank", async ({ page }) => {
  for (const [id, indexed, variant] of [
    ["0949e62d-df9f-5a21-bb88-65c0013c8cb8", "Robert B Smith", "Robert B Smith Jr"],
    ["1c688f94-0919-52dd-94ec-011395f677b2", "Sands Smith", "Sands Smith Jr"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(`Indexed form${indexed}`);
    await expect(main).toContainText(variant);
  }
  await page.goto("./people/b11baf40-7e25-5fd2-81a2-ea737792e016/");
  const main = page.locator("main");
  await expect(main).toContainText("M/Sgt");
  await expect(main).toContainText("private grade at entry");
  await expect(main).toContainText("enlisted army personnel");
});

test("Batch 891 evidence inputs exclude protected identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 891 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 594,
    research_attempted_people: 13_451,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_921,
    published_claims: 8_133,
    public_sources: 5_476,
  });
});
