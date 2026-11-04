import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page514-mallery-wooster-to-margaret-wright-review_batch-1024_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  emily: ["2555ddaa-472b-5630-b6f9-c52781aebe9e", "Emily H Workum"],
  wrachford: ["d35058ed-5a03-5b7b-8769-7650dda55859", "George E Wrachford"],
  edwin: ["2ec84e9a-5e64-5dc9-8227-cb806101b381", "Edwin M Wright"],
  kenneth: ["27bbe658-9a36-53cc-b114-9bf29cd4a1d1", "Kenneth M Wright"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1024 publishes every page 514 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 514);
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
      }
    }
  }
  expect(people).toBe(46);
  expect(sourceRows).toBe(46);
});

test("Emily Workum's volunteer and acting evidence is not presented as employment", async ({ request, page }) => {
  const emily = await publicPerson(request, profiles.emily);
  expect(emily).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(emily.last_civilian_pre_service).toHaveLength(0);
  expect(emily.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ relationship_type: "volunteer", canonical_organization: "Northern Westchester Planned Parenthood clinic" }),
    expect.objectContaining({ relationship_type: "unknown", occupation: "actress" }),
  ]));
  await page.goto(`./people/${profiles.emily[0]}/`);
  await expect(page.getByRole("heading", { name: "Emily H Workum", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("volunteer");
});

test("Edwin Wright's Columbia status remains student evidence with probable identity", async ({ request, page }) => {
  const edwin = await publicPerson(request, profiles.edwin);
  expect(edwin).toMatchObject({ identity_status: "probable", research_status: "occupation_only_found" });
  expect(edwin.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ relationship_type: "student", canonical_organization: "Columbia University" }),
  ]);
  expect(edwin.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.edwin[0]}/`);
  await expect(page.locator("main")).toContainText("doctoral study");
  await expect(page.locator("main")).toContainText("Probable");
});

test("Wrachford preserves the middle-initial conflict and Kenneth Wright excludes post-OSS fields", async ({ request }) => {
  const wrachford = await publicPerson(request, profiles.wrachford);
  expect(wrachford.identity_status).toBe("high_confidence");
  expect(wrachford.name_variants).toEqual(expect.arrayContaining(["George F Wrachford", "George Franklin Wrachford"]));

  const kenneth = await publicPerson(request, profiles.kenneth);
  expect(kenneth.identity_status).toBe("confirmed");
  expect(kenneth.research_status).toBe("requires_archival_review");
  expect(kenneth.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(kenneth.last_civilian_pre_service).toHaveLength(0);
  expect(kenneth.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 1024 evidence excludes secrets, identifiers, raw bulk records, and the hijacked host", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toContain("javadc.org");
});
