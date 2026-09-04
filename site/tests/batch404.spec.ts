import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);
const occupations = [
  ["d57de3a9-d823-5707-85cd-84e297781257", "Occupations in production of petroleum", "1942-11-18", "120"],
  ["47c32ed3-ce35-5c11-a4bc-3ba8dfc801d1", "Linemen and servicemen, telegraph, telephone, and power", "1943-02-24", "120"],
  ["501989a1-1b1c-5fa2-8c06-c40f41867ac7", "Upholsterers", "1942-06-01", "121"],
];

test("Batch 404 keeps three grouped occupations separate from employers and employment dates", async ({ page }) => {
  for (const [id, occupation, date, box] of occupations) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.commissioned_officer).toBeNull();
    expect(p.source_records[0]).toMatchObject({ pdf_page: 78, box, rank_as_indexed: null, archive_location: "230/86/28/06" });
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toHaveLength(1);
    expect(p.other_pre_oss_affiliations[0]).toMatchObject({ occupation, organization_id: null, relationship_type: "unknown", start_date: null, end_date: null, country: null, temporal_basis: "temporal_relation_uncertain", claim_confidence: "medium", publication_status: "publish_qualified" });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);
    expect(p.claims).toHaveLength(2);
    expect(p.claims.find((c: { claim_type: string }) => c.claim_type === "occupation").sources).toHaveLength(3);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
    await expect(earlier).toContainText(occupation);
    await expect(earlier).toContainText(date);
    await expect(earlier).toContainText("temporal relation uncertain");
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  }
});

test("Batch 404 does not decode undefined Army values or assign a later discharge rank", async ({ page }) => {
  for (const [id, code] of [
    ["72d0bc27-29d9-53e8-a50a-ae65fbf7c252", "999"],
    ["01b24b18-f221-5c20-bdd6-7fdcbcb38775", "992"],
    ["5009c20b-3ab1-56ed-a903-3cbe57e7982d", "999"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.commissioned_officer).toBeNull();
    expect(p.claims.map((c: { claim_type: string }) => c.claim_type)).toEqual(["identity"]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.identity_evidence).toContain(code);
    expect(p.research_status).toBe("requires_archival_review");
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  }
  expect(profile("72d0bc27-29d9-53e8-a50a-ae65fbf7c252").identity_evidence).toContain("differs");
});

test("Batch 404 preserves Saraadi and the uncorroborated names without publishing candidate biographies", async ({ page }) => {
  for (const [id, identity] of [
    ["f4f79d97-6960-5f88-906a-5f1074d0bbd3", "ambiguous"],
    ["78df2ee2-341b-563f-ba52-6dc95feb52b3", "unresolved"],
    ["0cb38f62-7bb2-5778-be66-c6f58f5dcf6a", "unresolved"],
    ["4667a68d-009b-50dc-baf4-121b592d71b0", "unresolved"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe(identity);
    expect(p.research_attempt_count).toBeGreaterThan(0);
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.name_variants).not.toContain("Savasdi Cheo-Sakul");
    expect(p.name_variants).not.toContain("Cecelia Cherry");
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: p.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
  }
});

test("Batch 404 directory search retains source spelling and permits omitted middle initials", async ({ page }) => {
  await page.goto("./people/");
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Saraadi Cheo-Sakul");
  await expect(page.getByRole("link", { name: "Saraadi Cheo-Sakul", exact: true })).toBeVisible();
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Lefty Cheramie");
  await expect(page.getByRole("link", { name: "Lefty J Cheramie", exact: true })).toBeVisible();
});

test("Directory token matching ranks exact names first and never combines different aliases", async ({ page }) => {
  // Synthetic search-only fixtures, never historical claims or exported data.
  const row = (id: string, n: string, v: string[] = []) => ({ id, n, nn: n.toUpperCase(), v, e: [], r: [], c: "unknown_or_indeterminate", o: null, s: [], g: [], i: "unresolved", rs: "not_started", ar: "unassessed", b: [] });
  await page.route("**/data/search-index.json", (route) => route.fulfill({ json: [
    row("initial", "Alex J Example"), row("exact", "Alex Example"),
    row("aliases", "Alex Smith", ["Jordan Example"]),
  ] }));
  await page.goto("./people/?q=Alex+Example");
  const links = page.locator("#person-results h2 a");
  await expect(links).toHaveText(["Alex Example", "Alex J Example"]);
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Example Alex");
  await expect(links).toHaveCount(2);
  await expect(page.getByRole("link", { name: "Alex Smith", exact: true })).toHaveCount(0);
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Alex Alex Example");
  await expect(links).toHaveCount(0);
});
