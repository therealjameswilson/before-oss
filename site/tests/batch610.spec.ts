import { expect, test } from "@playwright/test";

test("Nelson Glueck's institutional roles stay earlier and qualified", async ({ page }) => {
  await page.goto("./people/61e39cb1-9c3d-5f1e-badb-712e2694b4f7/");
  await expect(page.getByRole("heading", { name: "Nelson Glueck", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 171" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(immediate).not.toContainText("Hebrew Union College");
  await expect(civilian).not.toContainText("Hebrew Union College");
  await expect(earlier).toContainText("Hebrew Union College");
  await expect(earlier).toContainText("American School of Oriental Research in Jerusalem");
  await expect(earlier).toContainText("documented pre-OSS");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("does not establish that HUC was the immediate predecessor");
});

test("different-identifier William Glazier rows remain separate profiles", async ({ page }) => {
  const cases = [
    "422af803-f699-5e5d-9828-49a06a988b09",
    "d2138c67-1436-5672-addb-bdc6c50972cb",
  ];
  for (const id of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "William H Glazier", level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: "Page 171" })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("different private identifiers");
  }
});

test("Charles S Green and Greene remain separate variant profiles", async ({ page }) => {
  const cases = [
    ["51791935-d646-5835-b530-dfd80185fab9", "Charles S Green", "Page 179"],
    ["04f2d4f6-3160-5a9e-bdfd-2fcc6837e458", "Charles S Greene", "Page 180"],
  ];
  for (const [id, name, sourcePage] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.getByRole("link", { name: sourcePage })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
  }
});

test("the oil-company category remains evidence-scoped after batch 610", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Nelson Glueck");
});
