import { expect, test } from "@playwright/test";

const cohort = [
  ["b8c996b5-4cf4-54d7-b49e-c95bd341097d", "John D Dodge", "190"],
  ["8cb536d3-39ee-5d55-bd0d-5fabb5eda36b", "Stanley D Dodge", "190"],
  ["0d9432b3-fbd7-5934-9e46-7dea8aab6cc3", "Cordelia Dodson", "191"],
  ["6d863d41-26cb-513a-928f-dacde58273c5", "Robert G Dodson", "191"],
  ["65655591-b357-54eb-971b-9f12eb048236", "Donald G Doehring", "191"],
  ["e99ce47c-05d8-5043-b088-8784b84c7010", "Russell D'Oench", "191"],
  ["b4d85eb9-0779-5897-9874-87be9ade4953", "Wallace F Doer", "191"],
  ["98213177-e07b-5e51-96e6-c740b4b8c83b", "Joy H Doerflinger", "191"],
  ["2ef6578c-fec4-5ddd-bf81-8fad0bd18564", "Otto C Doering Jr.", "191"],
  ["167cd864-f67a-5348-aa83-8d95d364905c", "Karl P Doerr", "191"],
  ["f4f1c585-7ee0-57d6-9914-60f334f611c9", "Frank DoGenova", "186"],
  ["1d260cd5-ad75-505e-ad1e-2acffbacf55a", "Dale Doherty", "191"],
  ["148fd901-0ad6-557e-ab2e-2b8e0ed1703b", "Michael M Doherty", "191"],
  ["27df518a-9b21-57d4-9732-1df554a79b9e", "Thomas C Doherty", "191"],
  ["cd8cb4d6-e3dc-5e09-9d39-df78359e3d84", "Roy W Doidge", "191"],
  ["9e7c9b51-3532-514a-bb9a-6e52ae15216f", "Simon Doillon", "191"],
  ["383fcf02-8f8c-5aeb-966e-8cf7680b6d03", "Theodore A Doktor", "191"],
  ["abd72ca1-08b6-5df6-89b1-d5751b27e86e", "Andrew J Dolak", "191"],
  ["9a901b0b-c8ab-5346-aa02-55ad836484f1", "Brooke Dolan", "191"],
  ["602b29e2-d101-5ef3-8a91-145e8c0ce3b6", "Louis E Dolan", "191"],
  ["2d123b38-e91c-5b21-9f93-b5f29e2af00e", "Patrick Dolan", "191"],
  ["23ea0589-fb7a-5a53-a539-a0f91ef54181", "Frederic R Dolbeare", "191"],
  ["cc4647f8-11c3-5530-99d9-8528fb4abd2b", "Margaret Dole", "191"],
  ["924c1a93-4976-548f-a33f-4bbde9d3f403", "John Dolence", "191"],
  ["e946597b-ac14-5b13-bfc0-9885b05f64b4", "Rudolph Dolezal", "191"],
  ["d92f6963-e343-58a1-a8bb-d36035ea5db2", "Laura B Doll", "192"],
] as const;

test("batch 591 has all 26 direct profiles with original boxes and no invented civilian employers", async ({ page }) => {
  for (const [id, name, box] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText(`Box ${box}`, { exact: false }).first()).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 120" })).toBeVisible();
    if (name !== "Patrick Dolan") {
      await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
    }
  }
});

test("Patrick Dolan separates COI, Columbia Records, and the earlier Times job", async ({ page }) => {
  await page.goto("./people/2d123b38-e91c-5b21-9f93-b5f29e2af00e/");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(immediate.getByRole("link", { name: "Office of the Coordinator of Information" })).toBeVisible();
  await expect(immediate.getByText("medium", { exact: true })).toBeVisible();
  await expect(civilian.getByRole("link", { name: "Columbia Records" })).toBeVisible();
  await expect(civilian.getByText("high", { exact: true })).toBeVisible();
  await expect(earlier.getByRole("link", { name: "Times (Chicago)" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Patrick Dolan (1911-1987)" }).first()).toHaveAttribute("href", "https://doi.org/10.25969/mediarep/18337");
});

test("Brooke's Academy trustee role is an affiliation and Otto's counsel listing is occupation only", async ({ page }) => {
  await page.goto("./people/9a901b0b-c8ab-5346-aa02-55ad836484f1/");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]').getByRole("link", { name: "Academy of Natural Sciences of Philadelphia" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.getByText("Brooke Dolan II", { exact: false }).first()).toBeVisible();

  await page.goto("./people/2ef6578c-fec4-5ddd-bf81-8fad0bd18564/");
  await expect(page.getByText(/practiced law by October 1932/)).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.getByRole("link", { name: /United States v\. Appalachian Coals/ }).first()).toBeVisible();
});

test("qualified and foreign cases remain visibly qualified", async ({ page }) => {
  await page.goto("./people/9e7c9b51-3532-514a-bb9a-6e52ae15216f/");
  await expect(page.getByText("foreign or allied military personnel", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]').getByRole("link", { name: "Forces françaises de l'intérieur" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/abd72ca1-08b6-5df6-89b1-d5751b27e86e/");
  await expect(page.getByText(/surname is printed DOL/)).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/cc4647f8-11c3-5530-99d9-8528fb4abd2b/");
  await expect(page.getByText(/plausible but unconfirmed match/)).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Cordelia's documented government assignment does not masquerade as a civilian employer", async ({ page }) => {
  await page.goto("./people/0d9432b3-fbd7-5934-9e46-7dea8aab6cc3/");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(1);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
});
