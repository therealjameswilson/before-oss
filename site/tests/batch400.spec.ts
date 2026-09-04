import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 400 preserves Charter spelling and publishes only the qualified Army occupation", async ({ page }) => {
  const id = "c85518d7-32b2-5b90-bec9-a1182bf723f5";
  const person = profile(id);
  expect(person.display_name).toBe("Louis Y Charter");
  expect(person.name_variants).toContain("Louis Y. Chartier");
  expect(person.identity_status).toBe("high_confidence");
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.other_pre_oss_affiliations).toHaveLength(1);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    relationship_type: "unknown", temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium", organization_id: null,
  });
  await page.goto(`./people/${id}/`);
  await expect(page.getByRole("heading", { name: "Louis Y Charter", exact: true })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Other documented affiliations and occupations" })).toBeVisible();
  const occupation = page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card');
  await expect(occupation).toContainText("Lawyers and judges");
  await expect(occupation).toContainText("Recorded at 1942-10-05");
  await expect(occupation).not.toContainText("Through 1942-10-05");
});

test("Batch 400 keeps Charr's exact Army identity separate from disputed biography and occupation", async ({ page }) => {
  const id = "3dd2eb07-c525-56fe-b3b4-edd891978307";
  const person = profile(id);
  expect(person.identity_status).toBe("confirmed");
  expect(person.research_status).toBe("conflicting_sources");
  expect(person.other_pre_oss_affiliations).toEqual([]);
  expect(person.immediate_pre_oss_affiliations).toEqual([]);
  expect(person.last_civilian_pre_service).toEqual([]);
  expect(person.claims).toHaveLength(2);
  expect(person.claims.some((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toBe(true);
  await page.goto(`./people/${id}/`);
  await expect(page.locator("main")).toContainText("January 12, 1945");
  await expect(page.locator("main")).toContainText("November 1944");
  await expect(page.locator("main")).toContainText("birth-year");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card, section[aria-labelledby="civilian-employer"] .affiliation-card, section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator("main")).not.toContainText("Waiters and waitresses");
  await expect(page.locator("main")).not.toContainText("United States post office");
});

test("Batch 400 withholds the Chartrand missionary and Chase academic candidate claims", async ({ page }) => {
  for (const id of ["3214e809-f1bc-5763-8822-bf7431ef40d9", "b6b84469-bc14-561d-b7fe-7b679acdda5c"]) {
    const person = profile(id);
    expect(person.identity_status).toBe("probable");
    expect(person.research_status).toBe("needs_identity_review");
    expect(person.claims).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Identity-resolution note" })).toBeVisible();
    await expect(page.locator(".affiliation-card")).toHaveCount(0);
    await expect(page.locator("main")).toContainText("Box 119");
  }
});

test("Batch 400 preserves all six unresolved profiles with individual archival questions", async ({ page }) => {
  for (const id of ["dad12733-0ef3-501c-a6fb-e5f88acfaa9f", "c62f5f51-07a8-5941-985b-d03a485e70b8", "4ebcd2f6-ad23-5944-96f1-b0394969593b", "b855a928-8fcf-5a0a-a905-5d22e0017f98", "5b3fb33e-05e2-55c9-a27e-57e06aa4fb22", "5a73b6fc-3899-5487-823e-1b8465ff85d4"]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.research_attempt_count).toBeGreaterThan(0);
    expect(person.claims).toEqual([]);
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: person.display_name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.");
    await expect(page.locator("main")).toContainText("Box 119");
  }
});

test("Batch 400 finds the Army spelling without changing the printed Charter display", async ({ page }) => {
  await page.goto("./people/");
  await page.getByRole("searchbox", { name: "Search", exact: true }).fill("Louis Y Chartier");
  await expect(page.getByRole("link", { name: "Louis Y Charter", exact: true })).toBeVisible();
});
