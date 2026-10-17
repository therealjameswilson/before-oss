import { expect, test } from "@playwright/test";

const profiles = [
  ["23bc485b-d4ff-562e-9648-00d6ae89d688", "Francis D Severance"],
  ["8c8ff6d2-b9b1-5520-b7a6-05a5cd5c1e28", "Dante Severi"],
  ["2c6cb9b4-36e4-57f7-ad48-bee8f306a7b1", "William K Severin"],
  ["032421c1-d85e-5015-affe-6f9b264d086b", "Glen H Severt"],
  ["b006210a-6575-5f89-9f1d-95af055def2b", "Marjorie M Severyns"],
  ["5d5a9ac3-aac3-5cb2-88d5-07883c01507d", "Joe H Sevier"],
  ["fd9a057a-365a-5069-b5ba-28b8befe9950", "Lewis V Sevier"],
  ["edb2c9ff-ddb2-5362-8955-dcf6b50bf0b8", "Oscar C Sewall"],
  ["1c7829be-cf11-5a11-92c7-c65a5d81d638", "Andrew Sexton"],
  ["35ac0649-3bf8-581b-bcec-39a7eb94c47e", "Richard H L Sexton"],
  ["6d27cabf-88d3-5960-91bf-d1b98796537b", "Felizia M Seyd"],
  ["d57314b3-5a03-561c-a6e3-6b99b5dd394e", "Dale Seymour"],
  ["12efb282-d0b1-52c0-9690-afb320e2cd7b", "Elizabeth A Seymour"],
  ["2be3b7b6-441f-5111-a188-b38a20d2d70b", "George A Seymour"],
  ["81a4fc85-a0fc-5c95-bb14-0893ae05d117", "Pete S Sfikas"],
  ["0e6a9bd6-09f3-5555-bb16-2eec57075c5a", "Victor E Sgarlata"],
  ["800c9493-4883-5539-ae1f-9312139ea2f1", "Dorothy Shackelton"],
  ["1f5aed82-c560-5aa2-9caa-05a3b93373b4", "Daniel Shacter"],
  ["98a13df9-9195-5ed5-9065-9a4d495b0988", "Hazel Shadix"],
  ["e1b4c036-db33-5183-be1e-55bf6277da5b", "Jack Shafer"],
  ["8a3a50b2-4c64-5836-970e-077873ef49f8", "William F Shafer"],
  ["e32be85b-52cb-5b8f-97d5-7dc9c66d3da8", "Kurt P Shaffenberger"],
  ["de61c73b-e36b-5e05-924f-6783f01cff60", "Andrew W Shaffer"],
] as const;

test("Batch 861 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Kurt Schaffenberger separates last civilian employment from the immediate Army pathway", async ({ page }) => {
  await page.goto("./people/e32be85b-52cb-5b8f-97d5-7dc9c66d3da8/");
  const main = page.locator("main");
  await expect(main).toContainText("Kurt Schaffenberger");
  await expect(main).toContainText("Last civilian employer before serviceBinder Studio");
  await expect(main).toContainText("Comic-book artist");
  await expect(main).toContainText("Immediate pre-OSS affiliationUnited States Army");
  await expect(main).toContainText("Training-poster and display artist");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationBinder Studio");
});

test("Marjorie Severyns keeps education as student affiliation rather than employment", async ({ page }) => {
  await page.goto("./people/b006210a-6575-5f89-9f1d-95af055def2b/");
  const main = page.locator("main");
  await expect(main).toContainText("Marjorie Severyns Ravenholt");
  await expect(main).toContainText("University of Washington");
  await expect(main).toContainText("Fletcher School of Law and Diplomacy");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceUniversity of Washington");
});

test("Felizia Seyd publishes only a qualified occupation and does not turn her publisher into an employer", async ({ page }) => {
  await page.goto("./people/6d27cabf-88d3-5960-91bf-d1b98796537b/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("published author");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Last civilian employer before serviceViking");
});

test("Daniel Shacter keeps postwar evidence out of pre-OSS affiliations", async ({ page }) => {
  await page.goto("./people/1f5aed82-c560-5aa2-9caa-05a3b93373b4/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Library of Congress European Mission roster");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Interdepartmental Committee on Scientific and Cultural Cooperation");
});

test("Army identity bridges preserve variants without inventing employers", async ({ page }) => {
  await page.goto("./people/5d5a9ac3-aac3-5cb2-88d5-07883c01507d/");
  const sevier = page.locator("main");
  await expect(sevier).toContainText("Joe H. Sevier Jr.");
  await expect(sevier).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/81a4fc85-a0fc-5c95-bb14-0893ae05d117/");
  const sfikas = page.locator("main");
  await expect(sfikas).toContainText("Identity statushigh confidence");
  await expect(sfikas).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(sfikas).toContainText("postwar restaurant ownership is not pre-OSS evidence");
  await expect(sfikas).not.toContainText("Last civilian employer before serviceRestaurant");
});
