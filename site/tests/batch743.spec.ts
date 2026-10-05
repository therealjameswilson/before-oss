import { expect, test } from "@playwright/test";

const profiles = [
  ["c2ab1a1b-507e-5a8a-999e-380a4b355385", "William J Peck"],
  ["30c8517d-7f50-5de0-a8f4-079323dedcef", "Joseph N Peckham"],
  ["15904ca6-9419-5ba7-8eac-2e6e92aa2677", "Andre E Pecquet"],
  ["ffda0610-9412-5439-998b-c52551f38605", "Lloyd. E Peddicord Jr."],
  ["09b58218-837d-5510-a156-74f123e46f84", "John C/G Peden"],
  ["aa2ac0cb-378c-56d6-bff0-6eae2570f032", "Andrew D Pedersen"],
  ["a4e4cc0c-eee1-532d-93da-65c2384bf416", "Herbert J Pedersen"],
  ["46d8b7f4-521c-5841-8083-53ea88ace759", "Karl A Pedersen"],
  ["4b7275a2-5cfc-5c40-b2f4-54b6ebc10600", "John Pedone"],
  ["b41947b8-a9c7-559c-a87c-83db38316202", "Charles E Pedonti"],
  ["dec23d33-6bf2-57e6-981b-a4a3023ae55f", "Richard L Pedrick"],
  ["c7671c55-a8a3-5e99-be68-d2f8aa5d1647", "Rene J Pedro"],
  ["27534f96-97fd-55ca-821a-4b4c26100870", "Mary E Peed"],
  ["9eb1eb3c-d93e-5d42-9b70-6babf2ee233d", "Frederick W Peel"],
  ["1fca4cec-87d6-5451-80d5-374448dea5a6", "Eunice B Peele"],
  ["6989c183-4a99-52c5-a208-5f7b95f354d7", "William R Peers"],
  ["d52d2286-aec0-55bb-a463-46eb79a8df76", "James B Peery"],
  ["342238a0-f04c-5f48-b3b4-9700bc0d75fc", "Edythe L Pegg"],
  ["d9591ba2-4fe5-5eaa-9667-cc78906fae1a", "Helen E Peirce"],
  ["aca5fd02-bbec-5a97-9d63-fa5dd19b4123", "Reuben Peiss"],
  ["e501646d-a5c1-5d5a-8b03-cc8e0be5b759", "Joseph G Pekar"],
  ["6977ff99-2c37-59d1-bb1b-998c856454cc", "James S Pekich"],
  ["3cb126c4-4412-53cb-8394-aba5b867e5d9", "Nicholas P Peledes"],
] as const;

test("Batch 743 publishes all 23 page-362 profiles with terminal reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\d{4,9}$/);
  }
});

test("Reuben Peiss publishes the explicit Harvard-to-OSS employment transition", async ({ page }) => {
  await page.goto("./people/aca5fd02-bbec-5a97-9d63-fa5dd19b4123/");
  const main = page.locator("main");
  await expect(main).toContainText("Harvard College Library");
  await expect(main).toContainText("cataloguer and editor");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Reuben Peiss, Librarianship: Berkeley");
});

test("Richard Pedrick keeps Norwich student affiliation separate from employment", async ({ page }) => {
  await page.goto("./people/dec23d33-6bf2-57e6-981b-a4a3023ae55f/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Norwich University");
  await expect(main).toContainText("student and cadet, Class of 1942");
  await expect(main).toContainText("strongly date bounded");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Lloyd Peddicord publishes only a documented earlier military assignment", async ({ page }) => {
  await page.goto("./people/ffda0610-9412-5439-998b-c52551f38605/");
  const main = page.locator("main");
  await expect(main).toContainText("Scout and Raider School");
  await expect(main).toContainText("Army first lieutenant and reconnaissance boat officer");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Nicholas Peledes resolves the Paledes variant and last civilian self-employment", async ({ page }) => {
  await page.goto("./people/3cb126c4-4412-53cb-8394-aba5b867e5d9/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Nicholas P. Paledes");
  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("grocery-store operator");
  await expect(main).toContainText("last civilian role");
  await expect(main).not.toContainText(/\b\d{7,9}\b/);
});

test("accepted Army matches publish identity evidence without invented employers", async ({ page }) => {
  for (const id of [
    "a4e4cc0c-eee1-532d-93da-65c2384bf416",
    "4b7275a2-5cfc-5c40-b2f4-54b6ebc10600",
    "b41947b8-a9c7-559c-a87c-83db38316202",
    "1fca4cec-87d6-5451-80d5-374448dea5a6",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("conflicts, printed punctuation, notes, and foreign status remain visible", async ({ page }) => {
  await page.goto("./people/c2ab1a1b-507e-5a8a-999e-380a4b355385/");
  await expect(page.locator("main")).toContainText("conflicting");

  await page.goto("./people/09b58218-837d-5510-a156-74f123e46f84/");
  await expect(page.locator("main")).toContainText("C/G");
  await expect(page.locator("main")).toContainText("probable");

  await page.goto("./people/c7671c55-a8a3-5e99-be68-d2f8aa5d1647/");
  await expect(page.locator("main")).toContainText("S/Lt");
  await expect(page.locator("main")).toContainText("French");

  await page.goto("./people/e501646d-a5c1-5d5a-8b03-cc8e0be5b759/");
  await expect(page.locator("main")).toContainText("Combine");
  await expect(page.locator("main")).toContainText("suffix");
});

test("home page exposes the rebuilt coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,119");
  await expect(home).toContainText("42.27%");
  await expect(home).toContainText("13,815");
  await expect(home).toContainText("755");
  await expect(home).toContainText("337");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
