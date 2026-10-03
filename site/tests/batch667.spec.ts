import { expect, test } from "@playwright/test";

const profiles = [
  ["36c2fd83-1435-5599-80a2-9329ffa948f0", "Clinton E Mitschke"],
  ["47bf7b43-c018-55c5-9b2f-aeb213434838", "Alfred D Mittendore"],
  ["00d769d2-c4db-576c-b239-5b61f0d62eee", "Ernest Mitzner"],
  ["88aa3987-d14f-55aa-b0d3-ebde6f27b9aa", "Henry H Miwa"],
  ["1495ecc2-e76e-5f83-beb0-82de20592b85", "Hideo Miwa"],
  ["c0ab5e1e-0c44-53e6-a2da-2cfaa6e36554", "Frank E Mixa Jr."],
  ["efcf8d23-00c3-52dd-8f95-6e6d1f44f1d6", "James A Mixon"],
  ["c481f9ab-e546-5faf-97db-3521d9475c6a", "Kazyu C Miyadira"],
  ["42bed9f2-c3ab-5807-928f-f35994eb0d06", "Tetsuo S Miyakawa"],
  ["2cce6090-0a8d-5c6a-af63-44d2477e3b55", "Lanny H Miyamoto"],
  ["6c3d891e-98cf-58be-8845-6bdae15c6327", "Shotaro F Miyamoto"],
  ["901660cb-8543-5d98-9144-10abd9253e4a", "Tom N Miyamoto"],
  ["e7191f93-d941-5356-a6f4-9d4dfa79c0a7", "Ioannis H Moatsos"],
  ["93de718e-12b4-532e-a2b9-d3517dc84419", "Eric E Mockler-Ferrt"],
  ["3bb976d1-f23c-5a27-9a48-1bf99d490483", "Joseph J Modiz"],
  ["8c0863d1-60da-52b7-979c-36425764197b", "Rudolf Modley"],
  ["412da731-b821-5340-933f-6cfcd0b643fb", "Albert F Moe"],
  ["93c48837-d92c-5e4c-8374-12ead2b66fdc", "Edward O Moe"],
  ["a2e03729-880f-5e8a-aae3-65a85f47ddd0", "James Moe"],
  ["36f7caa4-06ef-5f03-bf58-d183c6df418b", "Paul A Moe"],
  ["9ef5bfe5-d565-5826-aa6f-25f82d44b173", "Irwin Moed"],
  ["912156dd-254e-5b34-8115-a899b7ccdd27", "Victor W Moefred"],
] as const;

test("Batch 667 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 667 publishes Henry Miwa's employer without merging Hideo Miwa", async ({ page }) => {
  await page.goto("./people/88aa3987-d14f-55aa-b0d3-ebde6f27b9aa/");
  const henryMain = page.locator("main");
  await expect(henryMain).toContainText("Fresno Buddhist Church");
  await expect(henryMain).toContainText("Executive secretary");
  await expect(henryMain).toContainText("1934–1942");
  await expect(henryMain).toContainText("last documented civilian employer");
  await expect(henryMain).toContainText("Wheel of Dharma");

  await page.goto("./people/1495ecc2-e76e-5f83-beb0-82de20592b85/");
  const hideoMain = page.locator("main");
  await expect(hideoMain).toContainText(
    "may be a separate Hideo Miwa or a variant of Henry Hideo Miwa",
  );
  await expect(hideoMain).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(hideoMain).not.toContainText("Fresno Buddhist Church");
});

test("Batch 667 qualifies Tetsuo Miyakawa's earlier named employer", async ({ page }) => {
  await page.goto("./people/42bed9f2-c3ab-5807-928f-f35994eb0d06/");
  const main = page.locator("main");
  await expect(main).toContainText("Tetsuo Scott Miyakawa");
  await expect(main).toContainText("South Manchurian Railway Office, New York");
  await expect(main).toContainText("Sources give 1940 or 1941 as the end year");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "A single last civilian employer",
  );
});

test("Batch 667 publishes Eric Mockler-Ferryman's allied military pathway", async ({ page }) => {
  await page.goto("./people/93de718e-12b4-532e-a2b9-d3517dc84419/");
  const main = page.locator("main");
  await expect(main).toContainText("Eric Edward Mockler-Ferryman");
  await expect(main).toContainText("Special Operations Executive");
  await expect(main).toContainText("German Intelligence Section, War Office");
  await expect(main).toContainText("Allied Force Headquarters");
  await expect(main).toContainText("joint command of Brigadier Mockler-Ferryman");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 667 separates Rudolf Modley's government and civilian affiliations", async ({ page }) => {
  await page.goto("./people/8c0863d1-60da-52b7-979c-36425764197b/");
  const main = page.locator("main");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "Coordinator of Information",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Pictograph Corporation",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "Pictorial Statistics, Inc.",
  );
  await expect(main).toContainText("March 28, 1942");
  await expect(main).toContainText("RG 226, Entry 224, Box 531");
});

test("Batch 667 withholds low-confidence Shotaro Miyamoto and James Moe leads", async ({ page }) => {
  const withheldProfiles = [
    ["6c3d891e-98cf-58be-8845-6bdae15c6327", "University of Washington"],
    ["a2e03729-880f-5e8a-aae3-65a85f47ddd0", "Army Corps of Engineers"],
  ] as const;

  for (const [id, organization] of withheldProfiles) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("needs identity review");
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText(
      organization,
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText(
      organization,
    );
  }
});

test("Batch 667 exposes the Miyadira-Miyabara identity conflict", async ({ page }) => {
  await page.goto("./people/c481f9ab-e546-5faf-97db-3521d9475c6a/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Kazuo C. Miyabara");
  await expect(main).toContainText("neither record is silently corrected or merged");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 667 updates coverage and preserves the eight-person oil category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,424");
  await expect(page.locator("body")).toContainText("35.19%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  await expect(oilList).not.toContainText("Anne F Mitcheson");
});
