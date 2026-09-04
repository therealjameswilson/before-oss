import { expect, test } from "@playwright/test";
import fs from "node:fs";

const analytics = JSON.parse(fs.readFileSync(new URL("../src/data/generated/analytics.json", import.meta.url), "utf8"));

test("home features reviewed people and real employer summaries without prototype claims", async ({ page }) => {
  await page.goto("./");
  await expect(page.getByRole("heading", { name: "Profiles with reviewed employer evidence" })).toBeVisible();
  for (const person of analytics.featured_profiles) {
    await expect(page.getByRole("link", { name: person.name, exact: true })).toHaveAttribute("href", `/before-oss/people/${person.person_id}/`);
  }
  await expect(page.locator("main")).not.toContainText("Featured profiles will appear only after review");
  await expect(page.getByRole("heading", { name: "Documented last civilian employers", exact: true })).toBeVisible();
});

test("analysis charts expose denominators, filters, counted people, and downloadable evidence paths", async ({ page, request }) => {
  await page.goto("./analysis/");
  await expect(page.locator("main")).not.toContainText("no confirmed or high-confidence employer claim");
  for (const chart of analytics.charts) {
    const section = page.locator(`section[aria-labelledby="chart-${chart.key}"]`);
    await expect(section.getByRole("heading", { name: chart.title, exact: true })).toBeVisible();
    await expect(section).toContainText(`Denominator: ${chart.denominator.toLocaleString("en-US")} qualifying unique people.`);
    await expect(section).toContainText("uncertain temporal relationships excluded");
    await expect(section).toContainText("Research coverage:");
    if (chart.rows.length) {
      await section.locator("summary").click();
      await expect(section.locator(`a[href="/before-oss/people/${chart.rows[0].person_ids[0]}/"]`).first()).toBeVisible();
    }
  }
  const response = await request.get("./data/analytics.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toEqual(analytics);
});
