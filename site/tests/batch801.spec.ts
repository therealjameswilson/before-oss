import { expect, test } from "@playwright/test";

const profiles = [
  ["ce6217e3-551e-5c16-b4e9-e045c817cff0", "Samuel P Rice Sr."],
  ["cfa355ae-1905-5dee-b2fc-c692bcb5fb96", "William S Rice"],
  ["fee1fc82-2fac-516f-b086-8c2d0e664f37", "Abraham Rich"],
  ["05487a84-0592-5b43-b9e6-586a71964727", "Alexander C Rich"],
  ["bea86848-b7df-5e16-a954-875588a74015", "Charles F Rich"],
  ["71c2df31-2858-56fe-9789-64242afacb58", "Van B Rich"],
  ["e3fb278f-3ed5-5e36-9a90-51230248f510", "Vernon F Rich"],
  ["f4b8f6be-897e-5b5d-9f2a-f7a566e4d414", "Andre L Richard"],
  ["d1ac91fc-3fb5-5fec-8338-8f2e19df4f36", "Daniel O Richard"],
  ["89311814-8033-54e0-8db1-0bd41da745c6", "Edward E Richard"],
  ["b5b399ed-08c1-59a6-8d2a-558c3bb3a02f", "Ellis F Richard"],
  ["7ed0ae8b-209a-59e6-80d8-00f7c4b8b08e", "Laurent Richard"],
  ["2c77b68c-f9e4-5c79-92a1-8aa9cff2fdb2", "Raymond L Richard"],
  ["f2626cb2-b411-599d-8b41-9a8d23887d05", "Robert J Richard"],
  ["9c7abf56-a68a-5583-beb6-1b3f01a7c121", "Stefano Richard"],
  ["501fce94-da6f-52f1-8935-3a277606d6fe", "Anthony J Richards"],
  ["3eed4582-6d05-5bd8-b612-cbcb89e70379", "Atherton Richards"],
  ["1815d3ab-28b4-51e9-a1da-bffc4a8e7885", "Earl F Richards Jr."],
  ["41d1a951-a176-518b-9bf2-faa339dd23ef", "Eldred B Richards"],
  ["01010a2d-1ef9-5397-95d3-533e2866240c", "Franklin P Richards"],
  ["8fe79d22-8904-5155-878f-2a1cd531738d", "Frederick W Richards"],
  ["923cfb26-1b11-5617-ba2d-ba33ec808d31", "Ira Richards"],
  ["dde37375-4824-5fb8-9a6d-fd95bc1f4c04", "James W Richards"],
] as const;

test("Batch 801 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("642");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Atherton Richards separates the immediate employer from earlier work", async ({ page }) => {
  await page.goto("./people/3eed4582-6d05-5bd8-b612-cbcb89e70379/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Hawaiian Pineapple Company",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Hawaiian Pineapple Company",
  );
  await expect(main).toContainText("President");
  await expect(main).toContainText("Castle & Cooke");
  await expect(main).toContainText("Treasurer");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("William J. Donovan Part 2 of 7");
  await expect(main).toContainText("Donovan and the CIA");
});

test("Van B Rich exposes the protected-identifier name conflict", async ({ page }) => {
  await page.goto("./people/71c2df31-2858-56fe-9789-64242afacb58/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Albert M. Steele");
  await expect(main).toContainText("Electronic Army Serial Number Merged File");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Vernon F Rich preserves the French note without inventing nationality details", async ({ page }) => {
  await page.goto("./people/e3fb278f-3ed5-5e36-9a90-51230248f510/");
  const main = page.locator("main");
  await expect(main).toContainText("French");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("requires archival review");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Ira Richards rejects the incompatible Army namesake", async ({ page }) => {
  await page.goto("./people/923cfb26-1b11-5617-ba2d-ba33ec808d31/");
  const main = page.locator("main");
  await expect(main).toContainText("Lt USNR");
  await expect(main).toContainText("unresolved");
  await expect(main).not.toContainText("Eighth Cavalry");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 801 organization pages expose both historical employers", async ({ page }) => {
  for (const [id, name] of [
    ["5ad573a8-d665-50de-ad3e-93179d842c27", "Hawaiian Pineapple Company"],
    ["b6480f12-0a7f-5fbc-8e0b-e8b1427929d8", "Castle & Cooke"],
  ]) {
    await page.goto("./organizations/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Atherton Richards");
  }
});

test("home page exposes the rebuilt Batch 801 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,411");
  await expect(home).toContainText("47.67%");
  await expect(home).toContainText("12,523");
  await expect(home).toContainText("820");
  await expect(home).toContainText("370");
  await expect(home).toContainText("9,874");
});
