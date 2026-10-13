import { expect, test } from "@playwright/test";

const profiles = [
  ["b627e2cc-ef03-5419-88a5-14a82c714b8f", "Aldo Pistono"],
  ["16beee17-7f19-53bc-b7ab-c389ce690cf5", "Andre R Pissier"],
  ["71397925-086e-55c9-bde0-f222dbea556d", "Donald H Pippens"],
  ["10a47e01-6990-59d1-9598-5264536c9ba3", "Elmer F Pire"],
  ["a1e1b18f-9236-59e5-a8bb-24d4488945e7", "Emily J Pitkin"],
  ["ed6b9c1a-d6d1-50c5-9246-fd48d2684c88", "Fausto R Pitigliani"],
  ["a579622e-ee4f-575b-a60e-775c74d4c53a", "Frances M Pittard"],
  ["ed5ee73f-dd34-5782-9e33-baf6159aec3d", "Giovanni Pische"],
  ["1199e6f8-e237-5749-971b-5d88590c59b1", "Gus W Pirpitsakis"],
  ["fe576ae4-7521-5fc9-b4b3-b0dead6592fa", "James Piteri"],
  ["3da53ed2-e29c-5969-a8dc-96dd03edd2c8", "John J Pirch"],
  ["97cb42fe-27f4-5df7-a82d-c253a9cf0681", "John T Pirpos"],
  ["61e136a0-d79c-5083-9f46-40ca1c208c72", "Juliette E Pippens"],
  ["0762dc05-bb59-56b8-954a-f1d34252e8cc", "June M Pitkanen"],
  ["47eef67a-0ecc-54e4-9894-1d92b531fc88", "Luigi Pirastru"],
  ["69a2d1c0-b1a7-5ec2-928d-3eb82cda23be", "Orleans A Pitre"],
  ["225d66bc-a7e6-590e-8739-7ec97bb8f3e9", "Paul P Pipp"],
  ["90cc358f-ac40-52ea-b59b-4c52ef7f5cee", "Theodore B Pitman"],
] as const;

test("Batch 760 publishes all 18 page-370 profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 760 distinguishes Piteri's Army pathway from his unnamed civilian occupation", async ({
  page,
}) => {
  await page.goto("./people/fe576ae4-7521-5fc9-b4b3-b0dead6592fa/");
  const main = page.locator("main");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("strongly date bounded");
  await expect(main).toContainText("salesman");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "salesman",
  );
  await expect(main).toContainText("Proceedings of an OSS board examining personnel in Corsica");
});

test("Batch 760 publishes Pitigliani's earlier affiliations without treating either as immediate employment", async ({
  page,
}) => {
  await page.goto("./people/ed6b9c1a-d6d1-50c5-9246-fd48d2684c88/");
  const main = page.locator("main");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Brookings Institution");
  await expect(earlier).toContainText("research fellow");
  await expect(earlier).toContainText("Rivista Internazionale di Scienze Sociali");
  await expect(earlier).toContainText("professional affiliation");
  await expect(earlier).toContainText("documented pre-OSS");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "Brookings Institution",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "Brookings Institution",
  );
});

test("Batch 760 exposes the Pipp-Hipp identity conflict and withholds an employer", async ({ page }) => {
  await page.goto("./people/225d66bc-a7e6-590e-8739-7ec97bb8f3e9/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Paul P Hipp");
  await expect(main).toContainText("Boxes 336 and 606");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "United States Army",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "United States Army",
  );
});

test("Batch 760 publishes Pirpos's OSS roster evidence as identity context only", async ({ page }) => {
  await page.goto("./people/97cb42fe-27f4-5df7-a82d-c253a9cf0681/");
  const main = page.locator("main");
  await expect(main).toContainText("Greek Operational Group VI");
  await expect(main).toContainText("OSS Missions, SOE, Train Sabotage, Katerini, Tsirmulas");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "Greek Operational Group VI",
  );
});

test("home page exposes the rebuilt Batch 760 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,498");
  await expect(home).toContainText("43.85%");
  await expect(home).toContainText("13,436");
  await expect(home).toContainText("781");
  await expect(home).toContainText("345");
  await expect(home).toContainText("8,956");
});
