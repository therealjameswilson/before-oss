import { expect, test } from "@playwright/test";

const profiles = [
  ["3efb944b-7845-55f6-9b80-3302d982cf21", "Menelaos N Porfiris"],
  ["7637a522-a219-5268-b90c-b7e46419c52b", "Karl G Porges"],
  ["7d2bd1f0-47fc-5d89-a917-ab77ca035e31", "Inez Port"],
  ["97feca41-18af-5204-bc6c-0ffc0f5c2076", "Jack Porte"],
  ["aab97c7c-c5a2-5f91-a638-71c8bd5eb3e0", "Charles A Porter"],
  ["fb9a1f80-f89e-5fa0-b109-f08fb68f1f0a", "Doris S Porter"],
  ["968e8632-feed-5be8-81a9-ca1fa07dfdb7", "Florence Porter"],
  ["d599309b-c83b-5984-bb82-0aa5624b14c4", "Frank H Porter"],
  ["435c2738-045c-5944-bb27-3de5f900f82a", "George H Porter"],
  ["1d4d2df2-3072-5b72-8c58-52da22b836b5", "Hubert H Porter"],
  ["e3ae27cb-7105-518c-9216-80f4c27e6c1e", "Lee Porter"],
  ["514d9e16-ece0-5965-8511-7d07a1ce73a3", "Lester W Porter"],
  ["b2636da0-4608-5889-8076-933ee2bdf7b7", "Mary H Porter"],
  ["a40eb9f9-d408-551a-b045-04dad41077a4", "Paul R Porter"],
  ["282d06d2-f235-5481-842c-ab627f7ead2f", "Phil R Porter"],
  ["ba999bd5-b388-540a-969b-8527a185a5d4", "Floyd C Portner"],
  ["1d969384-626d-5488-9b13-ef8b0f91619f", "George J Porto"],
  ["3d027a9f-16d2-5953-80fa-05c60d1aa434", "Joseph A Porto"],
  ["fe94ee22-3fa1-5930-9e20-38d331f495b9", "Georgios P Portolos"],
  ["eea7cd16-12ee-5f57-bdee-fe8bdc705865", "William Portolos"],
  ["d0990908-a4c1-5907-b8f3-dbe14fa38e30", "George A Portoulas"],
  ["cfbd0644-7e1e-5b60-abc7-cb76ae600861", "Alexander C Poryzees"],
  ["5d21f73b-1225-54ca-ace0-973db80d0d95", "James A Poseley"],
  ["5826753c-deb7-51b1-a28b-d725f9ffa8be", "Monan M Posey"],
] as const;

test("Batch 768 publishes all 24 page profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 768 publishes official Portolos and Poryzees identity evidence without exposing identifiers", async ({ page }) => {
  await page.goto("./people/eea7cd16-12ee-5f57-bdee-fe8bdc705865/");
  const william = page.locator("main");
  await expect(william).toContainText("Bill Portolos");
  await expect(william).toContainText("Company C, 87th Infantry");
  await expect(william).toContainText("temporal relation uncertain");
  await expect(william).not.toContainText("32366348");

  await page.goto("./people/fe94ee22-3fa1-5930-9e20-38d331f495b9/");
  await expect(page.locator("main")).toContainText("Tec 5 Georgios P Portolos");
  await expect(page.locator("main")).not.toContainText("32366345");

  await page.goto("./people/cfbd0644-7e1e-5b60-abc7-cb76ae600861/");
  await expect(page.locator("main")).toContainText("Tec 5 Alexander C Poryzees");
  await expect(page.locator("main")).not.toContainText("13174992");
});

test("Batch 768 qualifies Karl Porges and preserves the two official-name conflicts", async ({ page }) => {
  await page.goto("./people/7637a522-a219-5268-b90c-b7e46419c52b/");
  const karl = page.locator("main");
  await expect(karl).toContainText("Company K, 85th Infantry");
  await expect(karl).toContainText("probable");

  await page.goto("./people/e3ae27cb-7105-518c-9216-80f4c27e6c1e/");
  await expect(page.locator("main")).toContainText("PORZER");
  await expect(page.locator("main")).toContainText("Conflict");

  await page.goto("./people/5826753c-deb7-51b1-a28b-d725f9ffa8be/");
  await expect(page.locator("main")).toContainText("NORMAN");
  await expect(page.locator("main")).toContainText("Conflict");
});

test("home page exposes the rebuilt Batch 768 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,667");
  await expect(home).toContainText("44.56%");
  await expect(home).toContainText("13,267");
  await expect(home).toContainText("786");
  await expect(home).toContainText("349");
  await expect(home).toContainText("9,125");
});
