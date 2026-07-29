import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";
import fs from "node:fs";

type Person = { person_id: string };
const firstPerson = (
  JSON.parse(
    fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
  ) as Person[]
)[0];

for (const route of [
  "",
  "people/",
  `people/${firstPerson.person_id}/`,
  "organizations/",
  "analysis/",
  "methodology/",
  "sources/",
  "downloads/",
]) {
  test(`no serious axe violations on /${route}`, async ({ page }) => {
    await page.goto(`./${route}`);
    if (route === "people/") {
      await expect(page.getByText(/results/)).toBeVisible({ timeout: 30_000 });
    }
    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .analyze();
    expect(
      results.violations.filter((item) =>
        ["serious", "critical"].includes(item.impact ?? ""),
      ),
    ).toEqual([]);
  });
}
