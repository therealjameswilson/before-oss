import { expect, test } from "@playwright/test";

const profiles = [
  ["906584da-834a-54d8-84fc-3fcc669aee65", "Joseph C Peters"],
  ["e35d621d-ed45-57a2-9c13-97b6a4cbde68", "Le Moyne Peters"],
  ["4e7dcdd4-137b-563a-a229-3ee62cc5b5bc", "Stephen Peters"],
  ["1d3c195e-6be1-5a7d-8d3e-0cb4cf57170d", "Virginia D Peters"],
  ["1e6c948c-bec5-5332-b4c6-5de36d0c3407", "Charles R Petersen"],
  ["51e64e52-963b-59c5-838c-b8bd74ce00c3", "Elmer A Petersen"],
  ["a2b021c3-8a94-5a04-a6a5-6e7acbd9484a", "Emil Petersen"],
  ["113943ff-6cc9-5a32-9d0c-b9d783891239", "Glenn R Petersen"],
  ["1871e1ad-ee88-5246-b3a2-57839b2f80bd", "Henry Petersen"],
  ["1122ff2f-71ef-5dc6-bec9-6e11a5e06540", "John A Petersen"],
  ["f0a96bf7-6bd0-506c-b5b7-89700dff56f7", "John H Petersen"],
  ["221753d9-24ab-5547-ab2d-35c324648e04", "Robert W Petersen"],
  ["435fe6be-3df8-5d24-9e10-34dea6732834", "Ross T Petersen"],
  ["ec2fd7dc-9041-5406-972d-bf64efa6b17a", "Ann B Peterson"],
  ["28e49e84-a95b-5787-bcb0-73641a8a185b", "Charlotta Peterson"],
  ["3ddaf3c4-8912-5402-919c-553089eb7d41", "Chester E Peterson"],
  ["832939e5-de6a-59ae-be14-5c8fde41bb47", "Chester E Peterson"],
  ["0736b5fb-371d-5d6a-85b1-d70e510fbb65", "Edward R Peterson"],
  ["358a6c61-4263-5b76-85a4-108b539f1cd0", "Edwin I Peterson"],
  ["360ea1b0-a896-51dc-9c66-d49b39122012", "Elizabeth K Peterson"],
  ["df55b498-14a7-50c3-8c73-e7d1565be088", "Harold E Peterson"],
  ["fd2fcfab-412a-59eb-94f2-1b163dc02d49", "John A Peterson"],
  ["936d00ec-1073-51b4-82b9-c8778f5e2eea", "John R Peterson"],
] as const;

test("Batch 750 publishes all 23 page-365 person profiles with reviewed outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 750 publishes four official high-confidence Army identity claims", async ({ page }) => {
  const matchedProfiles = [
    ["113943ff-6cc9-5a32-9d0c-b9d783891239", "Glenn R Petersen"],
    ["1871e1ad-ee88-5246-b3a2-57839b2f80bd", "Henry Petersen"],
    ["f0a96bf7-6bd0-506c-b5b7-89700dff56f7", "John H Petersen"],
    ["435fe6be-3df8-5d24-9e10-34dea6732834", "Ross T Petersen"],
  ] as const;

  for (const [id, name] of matchedProfiles) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(`The indexed ${name} row is linked at high confidence`);
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("not a named pre-OSS employer");
  }
});

test("Batch 750 keeps the John A Petersen-Peterson rows separate and qualified", async ({ page }) => {
  await page.goto("./people/1122ff2f-71ef-5dc6-bec9-6e11a5e06540/");
  const petersen = page.locator("main");
  await expect(petersen).toContainText("probable");
  await expect(petersen).toContainText("same identifier is printed on a separate John A Peterson row");
  await expect(petersen).toContainText("Both index entities remain separate");

  await page.goto("./people/fd2fcfab-412a-59eb-94f2-1b163dc02d49/");
  const peterson = page.locator("main");
  await expect(peterson).toContainText("conflicting");
  await expect(peterson).toContainText("official Army spelling is John A Petersen");
  await expect(peterson).toContainText("entities remain unmerged");
});

test("Batch 750 preserves both Chester E Peterson rows and the Army-name conflict", async ({ page }) => {
  await page.goto("./people/3ddaf3c4-8912-5402-919c-553089eb7d41/");
  const ranked = page.locator("main");
  await expect(ranked).toContainText("conflicting");
  await expect(ranked).toContainText("Andrew D Pedersen");
  await expect(ranked).toContainText("different identifier");

  await page.goto("./people/832939e5-de6a-59ae-be14-5c8fde41bb47/");
  const unranked = page.locator("main");
  await expect(unranked).toContainText("ambiguous");
  await expect(unranked).toContainText("separate Chester E Peterson source row");
  await expect(unranked).toContainText("identical names are not merged");
});

test("home page exposes the rebuilt Batch 750 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,279");
  await expect(home).toContainText("42.94%");
  await expect(home).toContainText("13,655");
  await expect(home).toContainText("764");
  await expect(home).toContainText("340");
  await expect(home).toContainText("8,738");
});
