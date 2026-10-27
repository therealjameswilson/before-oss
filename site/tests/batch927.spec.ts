import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page454-richard-w-stubbs-to-anton-m-sturrett-review_batch-927_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["e5e776b8-838a-5134-9260-ab3689b45911", "Richard W Stubbs"],
  ["7cfbdb61-a69c-52d0-a5e6-0e231dcd7b94", "Henri Stuber"],
  ["f74af8e7-fcfa-59f7-ac55-15f09a6dc691", "Charles H Stubing"],
  ["11275515-e068-5f2d-a6aa-2948b20653a0", "Albert E Stucchio"],
  ["7fffeae0-b21a-59fd-8459-07c091f1a6a1", "Frances J Stuckart"],
  ["aa07696d-4d28-52cf-b475-bf3d4bddcef4", "Milburn Stuckwish"],
  ["ec3bf3ea-b87e-5082-a555-dbe8b0193dbe", "Herbert L Studer"],
  ["efd15875-a9d2-5057-ae7f-86b219a950cb", "Andre Studler"],
  ["e0d20032-a8a6-5969-ac0d-7b8b4b0f8825", "Andre Studler"],
  ["9a99693e-5e8e-5169-8d79-dcc67092fcd1", "Raymond E Stuehrmann"],
  ["9b759a46-6f5c-55e3-a43c-7cb5defe636d", "Chester A Stull"],
  ["0187e76b-697c-50f6-b339-dd21113fc090", "Thomas L Stuller"],
  ["c60f1480-7bf2-51b5-97cf-22490aa910da", "Herbert Q Stump"],
  ["9850650d-d563-5820-96d2-5ef1531fc79d", "St. Claire D Stumper"],
  ["22ee62e0-b002-58a3-9457-a32070fdb2ce", "* Stur"],
  ["4526cad1-9e66-5fdb-b2e2-be181091b4ad", "Melvin Sturcz"],
  ["84a73577-2e7a-51de-8c84-2b57d0740b94", "Curtis E Sturgeon"],
  ["06cae7dc-f03d-503e-a737-7540ee80be5c", "Orvil D Sturgeon"],
  ["a1b14ddc-bc9d-5967-b71e-abab7126851c", "Harry D Sturges"],
  ["5bac785c-c25d-5df9-8727-52f18314b1a8", "Harry W Sturges"],
  ["5c56dbfd-1ee8-5e72-8db0-7993c3d29b3b", "Harriet M Sturgis"],
  ["a0233aea-bec1-5f0c-8cc2-17b83e6be0f8", "Norman R Sturgis"],
  ["daa577d8-28fa-5ae1-a29a-e56c693b3451", "Anton M Sturrett"],
] as const;

test("Batch 927 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Milburn Stuckwish publishes WSOY separately from the Signal Corps pathway", async ({ page }) => {
  await page.goto("./people/aa07696d-4d28-52cf-b475-bf3d4bddcef4/");
  const main = page.locator("main");
  await expect(main).toContainText("Milburn H Stuckwish");
  await expect(main).toContainText("WSOY");
  await expect(main).toContainText("chief engineer");
  await expect(main).toContainText("United States Army Signal Corps");
  await expect(main).toContainText("Broadcasting, June 1, 1942");
  await expect(main).toContainText("verified employer found");
  await expect(main).toContainText("probable immediate");
});

test("seven employer-free Army occupation findings stay qualified", async ({ page }) => {
  const cases = [
    ["7fffeae0-b21a-59fd-8459-07c091f1a6a1", "Mechanics and repairmen, motor vehicle"],
    ["ec3bf3ea-b87e-5082-a555-dbe8b0193dbe", "Clerks in trade, n.e.c."],
    ["9a99693e-5e8e-5169-8d79-dcc67092fcd1", "Stock clerks"],
    ["c60f1480-7bf2-51b5-97cf-22490aa910da", "Miners and mining-machine operators"],
    ["84a73577-2e7a-51de-8c84-2b57d0740b94", "Clerks, general office"],
    ["06cae7dc-f03d-503e-a737-7540ee80be5c", "Farm hands, general farms"],
    ["a1b14ddc-bc9d-5967-b71e-abab7126851c", "Students"],
  ] as const;
  for (const [id, occupation] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText(
      "no employer, school, workplace or OSS-transfer date is named",
    );
    await expect(main).toContainText("occupation only found");
  }
});

test("undefined Army occupation codes are not converted into occupations", async ({ request, page }) => {
  const response = await request.get("./data/people/a.json");
  const people = await response.json();
  for (const id of [
    "11275515-e068-5f2d-a6aa-2948b20653a0",
    "efd15875-a9d2-5057-ae7f-86b219a950cb",
  ]) {
    const person = people.find((item: { person_id: string }) => item.person_id === id);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
  await page.goto("./people/11275515-e068-5f2d-a6aa-2948b20653a0/");
  await expect(page.locator("main")).toContainText("code 093 remains uninterpreted");
});

test("Andre Studler rows remain separate, linked, and biography-free", async ({ request, page }) => {
  const ids = [
    "efd15875-a9d2-5057-ae7f-86b219a950cb",
    "e0d20032-a8a6-5969-ac0d-7b8b4b0f8825",
  ] as const;
  const response = await request.get("./data/people/a.json");
  const people = await response.json();
  const studlers = people.filter((item: { person_id: string }) =>
    (ids as readonly string[]).includes(item.person_id),
  );
  expect(studlers).toHaveLength(2);
  expect(studlers[0].possible_duplicate_group).toBe(studlers[1].possible_duplicate_group);
  for (const person of studlers) {
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(JSON.stringify(person)).not.toContain("distillerie");
  }
  for (const [id, other] of [[ids[0], ids[1]], [ids[1], ids[0]]] as const) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Possible duplicate group");
    await expect(page.locator(`a[href*="/people/${other}/"]`)).toContainText("Andre Studler");
  }
});

test("the incomplete Stur row preserves the index note and requests archival review", async ({ page }) => {
  await page.goto("./people/22ee62e0-b002-58a3-9457-a32070fdb2ce/");
  const main = page.locator("main");
  await expect(main).toContainText("no first n");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("critical");
});

test("Batch 927 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 927 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 627,
    research_attempted_people: 14_268,
    verified_affiliation_people: 1_013,
    verified_employer_people: 457,
    archival_review_assessed_people: 12_741,
    published_claims: 8_758,
    public_sources: 5_797,
  });
});
