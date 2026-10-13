import { expect, test } from "@playwright/test";

const profiles = [
  ["c471c1e6-a4b7-58d1-8fa7-b872371cca23", "Bertrand F Pike"],
  ["ca5b072e-f198-52d8-b59c-02791d68f0f8", "Emily G Pike"],
  ["b53fff09-e600-5e3c-9acb-ed0c4d51c007", "Enis H Pike"],
  ["cd94065a-15cd-5dec-af13-4f52c5c6c84e", "Adam E Pikul"],
  ["74fbf422-7b06-58c5-a960-c3a8ffe3aeae", "Albert L Pilaroscia"],
  ["acc3f0d0-ff2f-57ed-9ff8-7569823ffb7e", "Edward Pilert"],
  ["79f1a199-3c76-5a93-8b65-20b1512781d1", "Max Pilger"],
  ["b90e9bf9-56a3-5d57-995a-cd635a32353c", "Antonio Pilichi"],
  ["17c9f7cd-96c7-5b4d-ba0e-7894c82f8062", "Harlan Pilkington"],
  ["e7757a75-f563-50e1-a874-067caf5c97ac", "Michael A Pilla"],
  ["4fcb53dd-b576-5452-965d-6da31dec5ee7", "John A Pillepich"],
  ["ee31cc03-a5f8-5efb-8aab-a72ef6522caa", "Robert Pillet"],
  ["9daad00c-365e-54cc-b26e-97e21bfd29c7", "Edward F Pilley"],
  ["06ad407a-c5ff-566f-bbd5-0e38e707a37a", "Edward F Pilley"],
  ["25829555-0768-5d39-8d98-56a4bf966836", "John A Pilley"],
  ["6e0f3d15-164b-5593-9b62-0f6df39401b6", "Alphonse A Pilliccieri"],
  ["9822ad02-b465-5a17-81ac-61dbf6908f83", "Paul Pillois"],
  ["ca0f5777-3e7e-5da5-b292-3a2ba5ecdab5", "Mary E Pillsbury"],
] as const;

test("Batch 758 publishes all 18 page-369 profiles with terminal outcomes", async ({ page }) => {
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

test("Batch 758 publishes John Pillepich's Norwich student affiliation without calling it employment", async ({
  page,
}) => {
  await page.goto("./people/4fcb53dd-b576-5452-965d-6da31dec5ee7/");
  const main = page.locator("main");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Norwich University");
  await expect(earlier).toContainText("student and Guidon assistant editor");
  await expect(earlier).toContainText("Documented on 14 November 1940");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "Norwich University",
  );
  await expect(main).toContainText("Norwich Guidon, Volume XXVII, Issue 9");
  await expect(main).toContainText("John Andrew Pillepich, 1942");
});

test("Batch 758 qualifies both Edward Pilley occupation leads and preserves the duplicate", async ({
  page,
}) => {
  for (const id of [
    "9daad00c-365e-54cc-b26e-97e21bfd29c7",
    "06ad407a-c5ff-566f-bbd5-0e38e707a37a",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("resident engineer");
    await expect(main).toContainText("medium");
    await expect(main).toContainText("possible-duplicate group");
    await expect(main).toContainText("County Commission Lets Contract On Four Farm-To-Market Roads");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 758 keeps postwar Enis Pike and Albert Pilaroscia careers out of employer fields", async ({
  page,
}) => {
  await page.goto("./people/b53fff09-e600-5e3c-9acb-ed0c4d51c007/");
  let main = page.locator("main");
  await expect(main).toContainText("Enis H. Pike's Obituary");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("Sears");

  await page.goto("./people/74fbf422-7b06-58c5-a960-c3a8ffe3aeae/");
  main = page.locator("main");
  await expect(main).toContainText("Service Held For Albert Pilaroscia");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "attorney",
  );
});

test("home page exposes the rebuilt Batch 758 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,462");
  await expect(home).toContainText("43.70%");
  await expect(home).toContainText("13,472");
  await expect(home).toContainText("778");
  await expect(home).toContainText("345");
  await expect(home).toContainText("8,921");
});
