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
  "organizations/7fe1f71a-6ae9-5437-812e-946a18e377a4/",
  "analysis/",
  "methodology/",
  "sources/",
  "downloads/",
]) {
  test(`no serious axe violations on /${route}`, async ({ page }) => {
    // The sources table grows with every reviewed batch; give axe enough time
    // to inspect the complete rendered citation list on slower CI runners.
    if (route === "sources/") {
      test.setTimeout(90_000);
    }
    await page.goto(`./${route}`);
    if (route === "people/") {
      await expect(page.getByText(/results/)).toBeVisible({ timeout: 30_000 });
    }
    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      // The public Sources page contains thousands of citation entries. Return
      // only violations so axe does not serialize every passing/inapplicable
      // node back through the browser protocol on constrained mobile runs.
      .options({ resultTypes: ["violations"] })
      .analyze();
    expect(
      results.violations.filter((item) =>
        ["serious", "critical"].includes(item.impact ?? ""),
      ),
    ).toEqual([]);
  });
}
