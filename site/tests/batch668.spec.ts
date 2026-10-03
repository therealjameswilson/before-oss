import { expect, test } from "@playwright/test";

const profiles = [
  ["c540f8a7-3faa-59d7-ae3c-c66a8f0e7c70", "Glen E Moehring"],
  ["83c3cc3c-555c-5d0b-a516-405584e20137", "Siguardo F Moeller"],
  ["0a4da0e4-a4f1-5ae4-8c19-4afeb10683d7", "William J Moeller"],
  ["89d9a679-795f-5cc9-bb5e-4ba14568ac8b", "James Moffat"],
  ["b5dca909-b456-50b2-9a92-e15b512f715b", "Eli Moga"],
  ["73ea4533-bcfa-5d3e-82a6-9497e3452a8e", "John J Mogavero"],
  ["46f7b15f-57bb-5e76-a155-3256f693a835", "Bert Mogin"],
  ["0e109114-947d-5b8d-9c73-c2b1d087a4ef", "Faye K Mogin"],
  ["2144f442-cab1-51f6-b8ed-bd4106c1a54d", "Louis C Mohler"],
  ["08bf0ddf-b6b3-5bf5-9a62-cea523613109", "Paul O Mohn"],
  ["c5cc12bb-f4d1-5a3b-8750-c34d8d9ed78e", "Dorothy A Mohr"],
  ["28a1efc4-3107-51ee-807c-ec2a8d6584d4", "Charlie Moia"],
  ["cca7dafd-b924-5d51-98a2-3a5715cb4fa1", "Arthur J Mokin"],
  ["85841e79-5d6c-5c71-b77d-bc278c6ca943", "Howard P Mold"],
  ["ea45267b-2c07-5168-a9c5-87c8a72e52b1", "Harry J Moles"],
  ["41ceba1f-9c1d-5646-9fd4-17c99b150313", "Stanley A Moles"],
  ["56fd7409-4cba-5cea-ac48-685bc58abb3d", "Anthony N Molino"],
  ["1d42a434-5bf3-5ae3-8894-fa6599534203", "Henry C Moll"],
  ["63850c2d-0fa9-5e13-848d-c3d421319c23", "Mogene P Moller"],
  ["c3ad9ef2-4c8e-5523-903e-f7034470b159", "Sigmund L Molnar"],
  ["40cc09e6-d185-554f-8600-c565cfa6333b", "Samuel H Molodow"],
  ["b0304562-4747-5a5f-8570-9c1798ca35ab", "Kenneth Moloy"],
] as const;

test("Batch 668 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 668 qualifies Faye Mogin's documented USDA employment", async ({ page }) => {
  await page.goto("./people/0e109114-947d-5b8d-9c73-c2b1d087a4ef/");
  const main = page.locator("main");

  await expect(main).toContainText("United States Department of Agriculture");
  await expect(main).toContainText("Secretary");
  await expect(main).toContainText("documented prewar");
    await expect(main).toContainText("medium documented pre-OSS");
  await expect(main).toContainText("probably worked");
  await expect(main).toContainText("The Washington Post");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("Department of Agriculture");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Department of Agriculture");
});

test("Batch 668 publishes Army identities without inventing employers", async ({ page }) => {
  const armyMatches = [
    ["73ea4533-bcfa-5d3e-82a6-9497e3452a8e", "John J Mogavero"],
    ["46f7b15f-57bb-5e76-a155-3256f693a835", "Bert Mogin"],
    ["28a1efc4-3107-51ee-807c-ec2a8d6584d4", "Charlie Moia"],
    ["cca7dafd-b924-5d51-98a2-3a5715cb4fa1", "Arthur J Mokin"],
    ["ea45267b-2c07-5168-a9c5-87c8a72e52b1", "Harry J Moles"],
    ["56fd7409-4cba-5cea-ac48-685bc58abb3d", "Anthony N Molino"],
    ["1d42a434-5bf3-5ae3-8894-fa6599534203", "Henry C Moll"],
    ["c3ad9ef2-4c8e-5523-903e-f7034470b159", "Sigmund L Molnar"],
    ["40cc09e6-d185-554f-8600-c565cfa6333b", "Samuel H Molodow"],
  ] as const;

  for (const [id, name] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("Batch 668 preserves the Sam and Samuel Molodow variant", async ({ page }) => {
  await page.goto("./people/40cc09e6-d185-554f-8600-c565cfa6333b/");
  const main = page.locator("main");
  await expect(main).toContainText("Sam H Molodow");
  await expect(main).toContainText("conventional Sam/Samuel variant");
});

test("Batch 668 rejects unbridged William Moeller and James Moffat candidates", async ({ page }) => {
  await page.goto("./people/0a4da0e4-a4f1-5ae4-8c19-4afeb10683d7/");
  await expect(page.locator("main")).toContainText("no reliable result after protocol");
  await expect(page.locator("main")).not.toContainText("false pretenses");

  await page.goto("./people/89d9a679-795f-5cc9-bb5e-4ba14568ac8b/");
  await expect(page.locator("main")).toContainText("source or column-shift conflict");
  await expect(page.locator("main")).not.toContainText("Dominic A Centobene");
  await expect(page.locator("main")).not.toContainText("Verified employer");
});

test("Batch 668 updates exact coverage and preserves the oil category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,446");
  await expect(page.locator("body")).toContainText("35.28%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  await expect(oilList).not.toContainText("Faye K Mogin");
});
