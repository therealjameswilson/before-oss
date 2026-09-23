import { expect, test } from "@playwright/test";

const profiles = [
  ["5f99eb07-57e9-5b14-9777-bb82e69ae1df", "William S Mierzejewski"],
  ["c54cc4b7-832b-5b71-b144-ff68ab899c72", "Rafael P Miettunen"],
  ["3c5bcb0f-830e-5358-b917-67cc80dcb6ab", "Amelio Migliaccio"],
  ["c4a2aab5-9339-5eb8-99b4-735873428b63", "Huber E Migliolo"],
  ["0a7f74c4-cba5-5520-b176-5b3c15bbabbb", "Robert J Mignone"],
  ["532229af-71cd-5bcd-8446-5cbe847206ce", "Casimir J Migon"],
  ["f1620b31-615c-5703-85ca-4e09e25caff9", "Emil Mihatov"],
  ["75ea1124-2806-5003-b53c-1e6d9e239cd2", "John L Mihelich"],
  ["2c93fdfc-ac5c-5b52-8fc6-07363013c645", "Wallace J Mihelich"],
  ["9548dce0-8f44-5223-96b2-76b0bded0e67", "Paul G Mihos"],
  ["094ff396-dad4-5ef9-84cb-4302aadec235", "Wallace S Mikel"],
  ["8a138575-deaf-55c2-a3b6-b6e4db20aa98", "Isaac A Mikko"],
  ["982efa81-5730-5688-87ec-6d18b97e9eff", "Johnnie K Mikolas"],
  ["4fcbfd5c-1828-5507-abe5-50f6274f0879", "Edward A Mikos"],
  ["c3146eac-d1d0-553e-9d2b-e4ee5cb29156", "Frances M Miksic"],
  ["8d006353-2490-5f8b-b22a-cb6c9d1e4cb7", "John G Mikulski"],
  ["9dd1eb14-5573-59c8-a2cc-e3ba9b559c96", "Richard M Mikulski"],
  ["656fa27b-0048-5c1f-8570-3e210aa2d62d", "James Milan"],
  ["a8d58a55-d093-51d4-a200-2acf19d11ec3", "Russell S Milanick"],
  ["fd2d1fe7-e8ed-53a9-bcc6-dc683edf7a09", "Louis G Milas"],
  ["86337551-2275-590f-a94c-9d455d674c0c", "Tony J Milazzo"],
  ["c52c9899-f878-583a-9272-585511b23f88", "Eugene Milbauer"],
] as const;

test("Batch 657 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 657 publishes the bounded Mierzejewski identity evidence", async ({ page }) => {
  await page.goto("./people/5f99eb07-57e9-5b14-9777-bb82e69ae1df/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("documented in Yugoslavia");
  await expect(main).toContainText("Instytut Pamięci Narodowej");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 657 keeps both Mihelich rows separate and visible", async ({ page }) => {
  await page.goto("./people/75ea1124-2806-5003-b53c-1e6d9e239cd2/");
  let main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Detachment 101");
  await expect(main).toContainText("Compare both Box 523 Mihelich files");

  await page.goto("./people/2c93fdfc-ac5c-5b52-8fc6-07363013c645/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("official Army and unit records name John");
  await expect(main).toContainText("Box 523");
});

test("Batch 657 preserves the Rafael Miettunen spelling conflict", async ({ page }) => {
  await page.goto("./people/c54cc4b7-832b-5b71-b144-ff68ab899c72/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Rafael P. Mettuhen");
  await expect(main).toContainText("Boxes 520 and 522");
});

test("Batch 657 classifies the printed T-Sgt variant as enlisted Army personnel", async ({ page }) => {
  await page.goto("./people/9548dce0-8f44-5223-96b2-76b0bded0e67/");
  const main = page.locator("main");

  await expect(main).toContainText("enlisted army personnel");
  await expect(main).toContainText("T-Sgt");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 657 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,206");
  await expect(page.locator("body")).toContainText("34.28%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
