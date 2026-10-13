import { expect, test } from "@playwright/test";

const profiles = [
  ["f14e37b7-8d7f-5645-866c-41626a85dfb7", "Herbert V Prochnow"],
  ["e14f651f-c9a1-5879-8881-7196a6980fd9", "Albert M Proctor"],
  ["6cb277f1-3cbb-5602-ac2e-611f9713d14c", "Gifford M Proctor"],
  ["6f02602b-76e2-526f-9be3-30a4434dc1fe", "Harrison H Proctor"],
  ["fd9aa752-e9d1-5aa7-9657-0b94cc949cb9", "Henry H Proctor"],
  ["2dfe700c-98cb-55a8-a6e5-19a2c187728d", "Julia M Proctor"],
  ["aa187e18-2625-531a-9da8-0eef3ad3c6a5", "Kathryn R Proctor"],
  ["27142da6-dcd2-56cc-8a3d-a064d378f6ef", "Lewis J Proctor"],
  ["ebdaa54f-885a-5a51-bf26-34f751bb63e8", "Diana R Proddow"],
  ["b365f29a-eb89-5209-8413-6bf2dc0a32ac", "Wenzel Profant"],
  ["3de5b5ea-736a-5d21-8bb3-934309350bc0", "Charles E Proffitt"],
  ["b65794f5-6c4b-5791-8012-8b2db1770bfd", "Arthur J Prohl"],
  ["f623e157-2dce-5579-b3be-95db246e9158", "Robert F Prokop"],
  ["4f2b8fb6-96e7-555d-bd44-88ebb9a6e3f5", "Marie L Proksch"],
  ["73ccd891-752e-53c4-80f9-f64aa82d21bb", "William E Proksch"],
  ["14c8c18b-2d87-5078-b268-ee78590492d2", "Louis Prom"],
  ["73693ea2-53f9-57db-bab0-b85130c5ea3e", "Dales S Proper"],
  ["a72e4ed8-9c1e-5a22-9112-62cb02d27e45", "Buster R Propes"],
  ["b0e56dc0-b9b9-57b2-a3fc-690e69d996c5", "Sherman C Propes"],
  ["6066e2dd-2b2f-5521-aacc-086c27fe0edf", "Edward S Prorok"],
  ["8d4ff734-c6e2-54ef-b1e8-439ed791ab27", "Edward S Prorok"],
  ["59c5a5c3-a579-54fd-8db7-113ee2373c20", "Leopold Proser"],
  ["cc65a46d-3504-5b3f-9b27-8cb8df9293ed", "Catherine L Prosnak"],
] as const;

test("Batch 777 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Batch 777 publishes Prochnow's bank employment without calling it immediate", async ({ page }) => {
  await page.goto("./people/f14e37b7-8d7f-5645-866c-41626a85dfb7/");
  const main = page.locator("main");
  await expect(main).toContainText("First National Bank of Chicago");
  await expect(main).toContainText("assistant vice president");
  await expect(main).toContainText("documented prewar");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 777 preserves Profant's occupation and resistance work as non-employment", async ({ page }) => {
  await page.goto("./people/b365f29a-eb89-5209-8413-6bf2dc0a32ac/");
  const main = page.locator("main");
  await expect(main).toContainText("sculptor");
  await expect(main).toContainText("ALWERAJE");
  await expect(main).toContainText("volunteer");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 777 visibly qualifies Proser's probable BBC employment", async ({ page }) => {
  await page.goto("./people/59c5a5c3-a579-54fd-8db7-113ee2373c20/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("British Broadcasting Corporation");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("radio writer");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Batch 777 keeps the two Edward Prorok rows separate", async ({ page }) => {
  await page.goto("./people/6066e2dd-2b2f-5521-aacc-086c27fe0edf/");
  const enlisted = page.locator("main");
  await expect(enlisted).toContainText("enlisted army personnel");
  await expect(enlisted).toContainText("high confidence");
  await expect(enlisted).toContainText("distinct French first-lieutenant row");

  await page.goto("./people/8d4ff734-c6e2-54ef-b1e8-439ed791ab27/");
  const officer = page.locator("main");
  await expect(officer).toContainText("foreign or allied military personnel");
  await expect(officer).toContainText("Commissioned officer");
  await expect(officer).toContainText("Yes");
  await expect(officer).toContainText("unresolved");
  await expect(officer).not.toContainText("official Army bulk record supports a high-confidence identity match");
});

test("Batch 777 publishes Army identities without converting occupation codes into employers", async ({ page }) => {
  for (const id of [
    "e14f651f-c9a1-5879-8881-7196a6980fd9",
    "27142da6-dcd2-56cc-8a3d-a064d378f6ef",
    "3de5b5ea-736a-5d21-8bb3-934309350bc0",
    "b65794f5-6c4b-5791-8012-8b2db1770bfd",
    "f623e157-2dce-5579-b3be-95db246e9158",
    "a72e4ed8-9c1e-5a22-9112-62cb02d27e45",
    "b0e56dc0-b9b9-57b2-a3fc-690e69d996c5",
    "6066e2dd-2b2f-5521-aacc-086c27fe0edf",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("enlisted army personnel");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
    await expect(main).not.toContainText("civilian_occupation_code");
  }
});

test("home page exposes the rebuilt Batch 777 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,871");
  await expect(home).toContainText("45.41%");
  await expect(home).toContainText("13,063");
  await expect(home).toContainText("796");
  await expect(home).toContainText("356");
  await expect(home).toContainText("9,330");
});
