import { expect, test } from "@playwright/test";
import fs from "node:fs";

type Person = { person_id: string; display_name: string };
const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
) as Person[];
const firstPerson = people[0];
type Stats = {
  verified_affiliation_people: number;
  verified_employer_people: number;
};
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
) as Stats;

test("home reports the complete index and incomplete research honestly", async ({ page }) => {
  await page.goto("./");
  await expect(page.getByRole("heading", { name: /Who were they before OSS/i })).toBeVisible();
  await expect(page.getByText("23,978", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("Verified employer found", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      `${stats.verified_employer_people} entities currently have confirmed/high published employment or self-employment evidence.`,
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page.getByText(
      `The broader affiliation measure currently covers ${stats.verified_affiliation_people} entities.`,
      { exact: false },
    ),
  ).toBeVisible();
  await expect(page.getByText(/The directory is complete; the historical research is not/i)).toBeVisible();
});

test("directory search, commissioned filter, and URL state work", async ({ page }) => {
  await page.goto("./people/");
  await expect(page.getByText(/23,941 results/)).toBeVisible({ timeout: 30_000 });
  await page
    .getByRole("searchbox", { name: "Search", exact: true })
    .fill(firstPerson.display_name);
  await expect(page.getByRole("link", { name: firstPerson.display_name }).first()).toBeVisible();
  await expect(page).toHaveURL(/q=/);
  await page.getByLabel("Commissioned status").selectOption("true");
  await expect(page).toHaveURL(/commissioned=true/);
  await expect(page.locator("#result-summary")).not.toHaveText(/23,941 results/);
});

test("direct person route preserves source evidence and masks serials", async ({ page }) => {
  await page.goto(`./people/${firstPerson.person_id}/`);
  await expect(page.getByRole("heading", { name: firstPerson.display_name, exact: true })).toBeVisible();
  await expect(page.getByRole("heading", { name: "How the person appears in the index" })).toBeVisible();
  const content = await page.locator("body").innerText();
  expect(content).not.toMatch(/\b\d{7,8}\b/);
});

test("organizations, analysis, methodology, sources, and downloads are direct routes", async ({ page }) => {
  for (const route of ["organizations/", "analysis/", "methodology/", "sources/", "downloads/"]) {
    const response = await page.goto(`./${route}`);
    expect(response?.ok(), route).toBeTruthy();
    await expect(page.locator("h1")).toBeVisible();
  }
  const download = await page.request.get("./downloads/personnel_public.csv");
  expect(download.ok()).toBeTruthy();
  expect((await download.text()).split("\n")[0]).toContain("serial_masked");
});

test("a researched profile displays claim-level citations", async ({ page }) => {
  await page.goto(
    "./people/21a6b6f2-5daa-5569-826e-6d193f387d4a/",
  );
  await expect(page.getByRole("heading", { name: "Evidence and citations" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Sources for this claim" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "Mort Bobrow Obituary (1923–2019)" }).first()).toHaveAttribute(
    "href",
    /legacy\.com/,
  );
  await expect(page.getByText("Accessed 2026-07-29.", { exact: false }).first()).toBeVisible();
});

test("the confirmed McWilliams profile separates immediate and civilian affiliations", async ({
  page,
}) => {
  await page.goto(
    "./people/a417086c-3c99-5b5a-a198-35e1dc27f553/",
  );
  await expect(
    page.getByRole("heading", { name: "Julia C McWilliams", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("Julia Child", { exact: false }).first()).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "Office of War Information", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "W. & J. Sloane", exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "NAID 2180661", exact: true }),
  ).toHaveAttribute("href", "https://catalog.archives.gov/id/2180661");
});

test("the reviewed NARA batch preserves each person's distinct pre-OSS pathway", async ({
  page,
}) => {
  const profiles = [
    {
      id: "0cde0770-6d7d-5642-a1d3-d3e0b94c6dfc",
      name: "Ralph J Bunche",
      immediate: "Howard University",
      catalogId: "2168596",
    },
    {
      id: "6e014675-a236-513e-94cc-fadb5d986aa9",
      name: "William J Casey",
      immediate: "Board of Economic Warfare",
      catalogId: "2169187",
    },
    {
      id: "604d1099-bc8e-526c-a002-eeaa723c44e3",
      name: "Arthur J Goldberg",
      immediate: "Self-employed",
      catalogId: "2174048",
    },
    {
      id: "f02c5c3b-b8ff-5cb8-990d-3735dbbe0e19",
      name: "Sterling W Hayden",
      immediate: "United States Marine Corps Reserve",
      catalogId: "2175283",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByRole("link", { name: `NAID ${profile.catalogId}`, exact: true }),
    ).toHaveAttribute("href", `https://catalog.archives.gov/id/${profile.catalogId}`);
  }
});

test("the reviewed CIA batch distinguishes military, government, and civilian pathways", async ({
  page,
}) => {
  const profiles = [
    {
      id: "491ada54-8954-5518-b03e-88e0ed92d573",
      name: "Morris Berg",
      immediate: "Office of Inter-American Affairs",
      lastCivilian: "Boston Red Sox",
      source: "Moe Berg: Baseball Player, Linguist, Lawyer, Intel Officer",
    },
    {
      id: "d66cd8d4-b1c4-5dff-9432-a69a90e7caa4",
      name: "Virginia Hall",
      immediate: "Special Operations Executive",
      source: "The Office of Strategic Services: America's First Intelligence Agency",
    },
    {
      id: "0a1cbed6-2239-51a5-8ada-245100eb6fa0",
      name: "Richard M Helms",
      immediate: "United States Naval Reserve",
      lastCivilian: "The Indianapolis Times",
      source: "Richard Helms: The Intelligence Professional Personified",
    },
    {
      id: "7a26fb60-b1e2-5377-9092-f16406580dfd",
      name: "William E Colby",
      immediate: "United States Army",
      source: "Office of Strategic Services Compass",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(
          "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
          { exact: true },
        ),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
  }
});

test("the second reviewed CIA batch keeps student, military, employer, and identity-review evidence distinct", async ({
  page,
}) => {
  const profiles = [
    {
      id: "7d6735a8-041f-5f74-9a6b-d59f868201d8",
      name: "John Ford",
      immediate: "United States Naval Reserve",
      source: "Hollywood and the Office of Strategic Services",
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
    {
      id: "3566565e-bc22-57c6-945e-88a7c8983bfc",
      name: "Christian J Lambertsen",
      immediate: "University of Pennsylvania School of Medicine",
      lastCivilian: "Ohio Chemical and Manufacturing Company",
      source: "Christian Lambertsen and the Secret Story Behind Scuba",
    },
    {
      id: "411028ea-e6ef-5d8e-b5c2-574d65e8da21",
      name: "Alfonso Rodriguez",
      immediate: "United States Army G-2",
      source:
        'The "Glorious Amateurs" of OSS: A Diverse Group of Characters Who Helped Win a World War',
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
    {
      id: "8061a334-7c98-5f3e-9e20-d8771f19bd50",
      name: "Sidney L Bartlett",
      immediate: "United States Army",
      source: "Hollywood and the Office of Strategic Services",
      missingCivilian: "No reviewed claim currently meets the publication threshold.",
      needsIdentityReview: true,
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(profile.missingCivilian!, { exact: true }),
      ).toBeVisible();
    }
    if (profile.needsIdentityReview) {
      await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
  }
});

test("the alias batch preserves indexed names, documented variants, and unnamed occupations", async ({
  page,
}) => {
  const profiles = [
    {
      id: "852fe132-4da7-54f3-8b43-9e496bb8bc4c",
      name: "Rene Veuve",
      variant: "Rene Joyeuse",
      affiliation: "French Resistance",
    },
    {
      id: "aa60664e-da42-5dd7-a4d0-d8bbfb43368e",
      name: "Jun Atshushi Iwamatsu",
      variant: "Taro Yashima",
      affiliation: "United States Office of War Information",
      authorityId: "n82056657",
    },
    {
      id: "1456d4d2-f29f-56ed-a26c-a9318ed40fab",
      name: "Tomoe Iwamatsu",
      variant: "Mitsu Yashima",
      affiliation: "Art student",
      authorityId: "n82056669",
    },
    {
      id: "c10592a8-6d9e-5673-bf46-5296b828d186",
      name: "Joseph Savoldi Jr.",
      variant: "Joseph Anthony Savoldi",
      affiliation: "Professional wrestler",
      needsIdentityReview: true,
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(page.getByText(profile.variant, { exact: false }).first()).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.affiliation, exact: true }).first(),
    ).toBeVisible();
    if (profile.authorityId) {
      await expect(
        page.getByRole("link", { name: new RegExp(`Yashima, .+19`) }).first(),
      ).toHaveAttribute(
        "href",
        `https://id.loc.gov/authorities/names/${profile.authorityId}`,
      );
    }
    if (profile.needsIdentityReview) {
      await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
      await expect(
        page.getByText("No reviewed claim currently meets the publication threshold.", {
          exact: true,
        }),
      ).toBeVisible();
    }
  }
});

test("the wartime-pathways batch separates military, government, civilian, and student affiliations", async ({
  page,
}) => {
  const profiles = [
    {
      id: "75964751-419e-529e-9fbf-4c755aa42091",
      name: "Peter J Ortiz",
      immediate: "United States Marine Corps",
      earlier: "French Foreign Legion",
      source:
        'The "Glorious Amateurs" of OSS: A Diverse Group of Characters Who Helped Win a World War',
      category: "commissioned marine corps officer",
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
    {
      id: "00580293-bf23-52eb-9a5b-352989863c88",
      name: "Fisher Howe",
      immediate: "Coordinator of Information",
      lastCivilian: "Webb School",
      earlier: "Coats and Clark Thread Company",
      source: "The Spymaster's Assistant",
    },
    {
      id: "73b65df0-9cd0-5750-b796-ed8693999501",
      name: "Betty A Lussier",
      immediate: "Air Transport Auxiliary",
      lastCivilian: "Aircraft plant nightshift worker",
      earlier: "University of Maryland",
      source: "The Intrepid Woman: Betty Ann Lussier",
    },
    {
      id: "0d9432b3-fbd7-5934-9e46-7dea8aab6cc3",
      name: "Cordelia Dodson",
      immediate: "U.S. Military Intelligence",
      earlier: "Reed College",
      source: 'The "Glorious Amateurs" of OSS: A Sisterhood of Spies',
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.earlier, exact: true }).first(),
    ).toBeVisible();

    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(profile.missingCivilian!, { exact: true }),
      ).toBeVisible();
    }

    if (profile.category) {
      await expect(
        page.getByText(profile.category, { exact: true }).first(),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
  }
});

test("the education-and-service batch does not turn schools or a spouse's work into employers", async ({
  page,
}) => {
  const profiles = [
    {
      id: "2f189352-aabb-5d3e-899c-ffaafef19aad",
      name: "James Angleton",
      immediate: "United States Army",
      earlier: "Harvard Law School",
      source: "James Angleton: Master Spy Hunter",
      terminalMissingCivilian: true,
    },
    {
      id: "2201ee7c-3d64-5672-b519-0aad4625d185",
      name: "Edna W Andrade",
      immediate: "The Hecht Company",
      lastCivilian: "The Hecht Company",
      earlier: "Pennsylvania Academy of the Fine Arts",
      secondEarlier: "H. Sophie Newcomb Memorial College",
      source: "Edna Andrade: From the OSS to Op Art",
      secondSource: "Oral history interview with Edna Andrade, 1987 April 1-29",
    },
    {
      id: "f87b5adb-6496-5f61-a50f-2b098032d189",
      name: "Jane Burrell",
      earlier: "Smith College",
      secondEarlier: "Columbia University",
      source:
        "The Mystery of Jane Wallis Burrell: The First CIA Officer To Die in the Agency's Service",
      terminalMissingCivilian: true,
    },
    {
      id: "697f0736-ba27-55b6-ae7a-6550dd87aa3c",
      name: "Edmund M Burke",
      earlier: "University of Pennsylvania",
      source: "Hollywood and the Office of Strategic Services",
      terminalMissingCivilian: true,
    },
    {
      id: "990ec032-d116-5a93-bace-517a5dbc9c6d",
      name: "Robert C Broughton",
      immediate: "United States Army",
      lastCivilian: "Walt Disney Studios",
      earlier: "University of California, Los Angeles",
      source: "From Walt Disney to War Movies: Bob Broughton",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.earlier, exact: true }).first(),
    ).toBeVisible();
    if (profile.secondEarlier) {
      await expect(
        page
          .getByRole("heading", { name: profile.secondEarlier, exact: true })
          .first(),
      ).toBeVisible();
    }

    const immediateSection = page.locator(
      'section[aria-labelledby="immediate-affiliation"]',
    );
    if (profile.immediate) {
      await expect(
        immediateSection.getByRole("heading", {
          name: profile.immediate,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        immediateSection.getByText(
          "No reviewed claim currently meets the publication threshold.",
          { exact: true },
        ),
      ).toBeVisible();
    }

    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(
          profile.terminalMissingCivilian
            ? "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
            : "No reviewed claim currently meets the publication threshold.",
          { exact: true },
        ),
      ).toBeVisible();
    }

    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
    if (profile.secondSource) {
      await expect(
        page.getByRole("link", { name: profile.secondSource, exact: true }).first(),
      ).toHaveAttribute("href", /aaa\.si\.edu/);
    }
  }
});

test("the official-pathways batch preserves employers, military assignments, and provisional identities", async ({
  page,
}) => {
  const profiles = [
    {
      id: "7227c423-8f14-5430-9824-e79ccac87230",
      name: "Barbara J Lauwers",
      immediate: "Women's Army Corps",
      lastCivilian: "Embassy of Czechoslovakia in Washington",
      source: "Barbara Lauwers: Deceiving the Enemy",
    },
    {
      id: "404292b8-801c-58f0-8f74-6fd447da6adf",
      name: "Franklin P Holcomb",
      immediate: "Office of Naval Intelligence",
      earlier: "Georgetown University",
      source: 'The "Scholastic" Marine Who Won a Secret War',
      category: "commissioned marine corps officer",
    },
    {
      id: "db23d265-0e22-5004-96ad-ab1762b43b92",
      name: "Jeanne H Taylor",
      earlier: "Works Progress Administration, Index of American Design",
      source: 'The "Glorious Amateurs" of OSS: A Sisterhood of Spies',
      needsIdentityReview: true,
    },
    {
      id: "b78087f9-4898-5aae-bf3d-43dba862cb78",
      name: "Sherman Kent",
      immediate: "Coordinator of Information",
      lastCivilian: "Yale University",
      source: "Sherman Kent and the Profession of Intelligence Analysis",
    },
    {
      id: "d94ecc56-f483-5cd6-8577-22447eb6a8d7",
      name: "Walter C Langer",
      immediate: "Self-employed",
      lastCivilian: "Self-employed",
      source: "Official OSS Exhibition Catalogue",
    },
    {
      id: "e9aac0ee-0132-5166-b8ab-1e9e8d89fe93",
      name: "William L Langer",
      immediate: "Harvard University",
      lastCivilian: "Harvard University",
      earlier: "Clark University",
      source: "The Historian-Autobiographers",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();

    const immediateSection = page.locator(
      'section[aria-labelledby="immediate-affiliation"]',
    );
    if (profile.immediate) {
      await expect(
        immediateSection.getByRole("heading", {
          name: profile.immediate,
          exact: true,
        }),
      ).toBeVisible();
    }

    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    }

    if (profile.earlier) {
      await expect(
        page.getByRole("heading", { name: profile.earlier, exact: true }).first(),
      ).toBeVisible();
    }
    if (profile.category) {
      await expect(page.getByText(profile.category, { exact: true }).first()).toBeVisible();
    }
    if (profile.needsIdentityReview) {
      await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toBeVisible();
  }
});

test("Batch 009 preserves civilian, military, government, and duplicate-row boundaries", async ({
  page,
}) => {
  const profiles = [
    {
      id: "52aacf03-c330-5566-9091-7bc961b1266b",
      name: "William J Donovan",
      immediate: "Coordinator of Information",
      lastCivilian: "Donovan, Leisure, Newton & Irvine",
      source: "William Donovan: Spymaster, War Hero, and Columbia Law School Graduate",
    },
    {
      id: "a0f164c7-505d-5cb9-88e1-0c3c1f1be22f",
      name: "Carl F Eifler",
      immediate: "K Company, 35th Infantry Regiment",
      lastCivilian: "United States Customs Service",
      source: "Colonel Carl F. Eifler, US Army, Retired",
    },
    {
      id: "c353768b-d393-5b1c-92ba-47d7cbfe28dc",
      name: "David K Bruce",
      immediate: "American Red Cross",
      lastCivilian: "American Red Cross",
      source: "David K. E. Bruce Oral History Interview",
    },
    {
      id: "7ac0f4ab-1444-5819-9a43-ee750f6f5617",
      name: "Frank G Wisner",
      immediate: "Office of Naval Intelligence",
      lastCivilian: "Carter, Ledyard & Milburn",
      source: "General Walter Bedell Smith as Director of Central Intelligence, October 1950-February 1953, Volume II",
    },
    {
      id: "fdfd99fd-2cdd-5f1e-a101-0d1a36440f06",
      name: "John A Bross",
      immediate: "United States Army Air Forces",
      lastCivilian: "Self-employed legal practice",
      source: "John Bross Receives Army Air Forces Commission (April 1942)",
    },
    {
      id: "221b804d-039b-5da1-ad65-c62ea650a63b",
      name: "Kermit Roosevelt Jr.",
      immediate: "California Institute of Technology",
      lastCivilian: "California Institute of Technology",
      source: "Zendebad, Shah! The Central Intelligence Agency and the Fall of Iranian Prime Minister Mohammad Mossadeq, August 1953",
    },
    {
      id: "8f01ec1e-7a03-5d7b-8ebd-8144fdfd6d85",
      name: "Samson Lane Faison",
      immediate: "United States Naval Reserve",
      lastCivilian: "Williams College",
      source: "Legendary Art History Teacher and Long-time Williams Faculty Member Lane Faison Dies",
    },
    {
      id: "a2d66764-90d0-5d8d-8102-30c2e0b03ba1",
      name: "Peter M F Sichel",
      immediate: "United States Army Medical Corps",
      source: "The Secrets of My Life: Vintner, Prisoner, Soldier, Spy",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: profile.immediate, exact: true }),
    ).toBeVisible();
    if (profile.lastCivilian) {
      await expect(
        page
          .locator('section[aria-labelledby="civilian-employer"]')
          .getByRole("heading", { name: profile.lastCivilian, exact: true }),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./people/1bf7bd5e-a790-51d0-9a46-e6046cab07f2/");
  await expect(
    page.getByRole("heading", { name: "Peter M Sichel", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
  await expect(page.getByText("duplicate-1f825d1c2a6f", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "The Peter M. Sichel row remains separate from the adjacent Peter M. F. Sichel row pending direct service-number linkage.",
      { exact: true },
    ),
  ).toBeVisible();
});

test("Batch 010 preserves military, government, civilian-employer, fellowship, and unresolved boundaries", async ({
  page,
}) => {
  const profiles = [
    {
      id: "b6f213df-1110-5f54-8821-8787886a7633",
      name: "Aaron Bank",
      immediate: "Unspecified Transportation Railroad Battalion",
      earlier: "Unidentified resort in Biarritz",
      source: "Colonel Aaron Bank: 1902-2004",
    },
    {
      id: "7f111cc6-d046-5eac-93ab-63f6387c204b",
      name: "Arthur M Schlesinger",
      immediate: "United States Office of War Information",
      earlier: "Harvard Society of Fellows",
      source: "Schlesinger, Arthur Meier, Jr., 1917-2007",
    },
    {
      id: "e972f0e6-54f0-5b2e-a07c-035c83718850",
      name: "John K Singlaub",
      immediate: "515th Parachute Infantry Regiment",
      source: "Interview with Maj. Gen. John K. Singlaub, U.S. Army, Ret.",
    },
    {
      id: "e091453b-28d3-5f35-a907-415c62dfc364",
      name: "John King Fairbank",
      lastCivilian: "Harvard University",
      source: "John K. Fairbank: The Life of John King Fairbank",
    },
    {
      id: "6dff4a3a-1141-5a4c-8a77-2ea2a7c99ab0",
      name: "Walt W Rostow",
      lastCivilian: "Columbia University",
      source: "Walt Rostow, 86; Top Advisor on Vietnam",
    },
    {
      id: "4ed9479d-32f1-5c48-9d6e-645d0405c42f",
      name: "Roger Hilsman",
      immediate: "5307th Composite Unit (Provisional)",
      source: "Roger Hilsman, foreign policy adviser to JFK, dies at 94",
    },
    {
      id: "a48e130d-4c6d-58b0-9257-bc88435ed84b",
      name: "Lyman B Kirkpatrick",
      immediate: "United States Army",
      lastCivilian: "United States News",
      source: "Lyman Bickford Kirkpatrick Jr. '38",
    },
    {
      id: "d8754b27-3c32-5445-a5fe-063299aa869c",
      name: "Ray S Cline",
      immediate: "United States Department of the Navy",
      earlier: "Harvard Society of Fellows",
      source: "Ray S. Cline Papers",
    },
    {
      id: "12930941-5301-558f-9ded-a45a0d6e4b82",
      name: "Paul Mellon",
      immediate: "United States Army",
      earlier: "Mellon Bank (historical name as found)",
      source: "Paul Mellon, Founder",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    if (profile.immediate) {
      await expect(
        page
          .locator('section[aria-labelledby="immediate-affiliation"]')
          .getByRole("heading", { name: profile.immediate, exact: true }),
      ).toBeVisible();
    }
    if (profile.lastCivilian) {
      await expect(
        page
          .locator('section[aria-labelledby="civilian-employer"]')
          .getByRole("heading", { name: profile.lastCivilian, exact: true }),
      ).toBeVisible();
    }
    if (profile.earlier) {
      await expect(
        page
          .locator('section[aria-labelledby="earlier-affiliations"]')
          .getByRole("heading", { name: profile.earlier, exact: true }),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./people/c490f753-bc95-59f6-8f99-7ab2d2455293/");
  await expect(
    page.getByRole("heading", { name: "Archimedes L Patti", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 589 and Army personnel records to establish the immediate pre-OSS assignment and last civilian employer.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "OSS in Action: The Pacific and the Far East", exact: true }),
  ).toBeVisible();
});

test("Batch 011 preserves concurrent employment, predecessor agencies, military pathways, and non-employer affiliations", async ({
  page,
}) => {
  await page.goto("./people/928871ef-6c5b-54dd-8967-08e8afcd7efc/");
  await expect(
    page.getByRole("heading", { name: "Carleton S Coon", exact: true }),
  ).toBeVisible();
  for (const organization of [
    "Harvard University",
    "Peabody Museum of Archaeology and Ethnology",
  ]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
    await expect(
      page
        .locator('section[aria-labelledby="civilian-employer"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page.getByRole("link", { name: "Carleton Stevens Coon papers", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/9e161c56-f13d-52f7-bc8c-778fe6ff8677/");
  await expect(
    page.getByRole("heading", { name: "Norman H Pearson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Yale University", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page.getByRole("link", { name: "History of the Department", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/86d85b71-ed82-5b7f-87dd-0d456d58ff3d/");
  await expect(
    page.getByRole("heading", { name: "Philip E Mosely", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Cornell University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "United States Department of State, Division of Special Research",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Cornell Alumni News", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/cae068be-d703-5d95-adc7-a645430834fd/");
  await expect(
    page.getByRole("heading", { name: "Millard P Goodfellow", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army G-2", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "M. Preston Goodfellow's unnamed business",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "OSS Training in the National Parks and Service Abroad in World War II: Chapter 1, Origins of the OSS",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/3f476b5c-bf12-532d-8879-1646130029e0/");
  await expect(
    page.getByRole("heading", { name: "Whitney Shepardson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Council on Foreign Relations", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 703 and CFR archival records to identify Shepardson's immediate pre-OSS status and last civilian employer without treating his officer role as employment.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "The Office of Strategic Services: America's First Intelligence Agency",
        exact: true,
      })
      .first(),
  ).toBeVisible();
});

test("Batch 012 preserves qualified military pathways, unnamed employers, student status, and archival uncertainty", async ({
  page,
}) => {
  await page.goto("./people/495e4e73-3aa2-5afa-b5b3-838e28cc7957/");
  await expect(
    page.getByRole("heading", { name: "William A Eddy", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Marine Corps", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Hobart and William Smith Colleges",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Presidents and Deans", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/66142cc6-36c6-519b-8765-986f995322e3/");
  await expect(
    page.getByRole("heading", { name: "Archibald B Roosevelt", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Unidentified Spokane and San Francisco newspapers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "New York Herald Tribune", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "Archibald Roosevelt Jr. Papers", exact: true })
      .first(),
  ).toBeVisible();

  await page.goto("./people/01360217-ccc5-5754-a6d5-9d126bfc08f0/");
  await expect(
    page.getByRole("heading", { name: "John H Hemingway", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Dartmouth College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "The Son Also Rises: Jack Hemingway", exact: true })
      .first(),
  ).toBeVisible();

  await page.goto("./people/142be2db-06a1-51ef-8725-027388a3d15e/");
  await expect(
    page.getByRole("heading", { name: "Gertrude Legendre", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "American Museum of Natural History",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 443 and Mss 0182 wartime files to identify her immediate pre-OSS status and any civilian employer without converting property ownership or expedition participation into employment.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "The Gertrude Sanford Legendre papers",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/c9accc19-41c3-51ce-b173-2a51b4eea522/");
  await expect(
    page.getByRole("heading", { name: "DeWitt C Poole", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Princeton University School of Public Affairs",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Donovan and the CIA: A History of the Establishment of the Central Intelligence Agency",
        exact: true,
      })
      .first(),
  ).toBeVisible();
});

test("Batch 013 preserves career-military, civilian-cover, academic, probable-identity, and qualified-employer pathways", async ({
  page,
}) => {
  await page.goto("./people/a93ac760-896e-50b9-9746-754d434a1200/");
  await expect(
    page.getByRole("heading", { name: "John Magruder", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "U.S. Military Mission to China", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Origins of Central Intelligence",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/f443009b-dd5f-542b-9a0c-3af2d21f8611/");
  await expect(
    page.getByRole("heading", { name: "Donald C Downes", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Free World Association", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Free World Association", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Robert College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Guide to the Donald Chase Downes Papers",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/8dd153b1-fab9-5ab0-a015-3f2e6bcfaac1/");
  await expect(
    page.getByRole("heading", { name: "Bruce C Hopper", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Papers of Bruce Campbell Hopper, 1918-1971",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/62745da7-0c09-58fa-be20-99a797c8d9aa/");
  await expect(
    page.getByRole("heading", { name: "Leopold Schwarsschild", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Das Neue Tage-Buch", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 690 to confirm the spelling, birth details, immigration history, and whether the CAF-11 record belongs to editor Leopold Schwarzschild.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Leopold Schwarzschild / Photograph by Fred Stein",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/a9b1ec13-509a-57f2-bb04-d2453d49e908/");
  await expect(
    page.getByRole("heading", { name: "Paul C Child", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Avon Old Farms School", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Avon Old Farms School", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("medium", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Julia Child: Cooking Up Spy Ops for OSS",
        exact: true,
      })
      .first(),
  ).toBeVisible();
});

test("Batch 014 preserves Allied transfers, concurrent employers, student status, government pathways, and unnamed self-employment", async ({
  page,
}) => {
  await page.goto("./people/b635033f-c426-5c5c-b55d-73c37acb9cd7/");
  await expect(
    page.getByRole("heading", { name: "Stewart J Alsop", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "King's Royal Rifle Corps, 60th Regiment",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Doubleday, Doran & Company", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Joseph Alsop and Stewart Alsop Papers",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/d5ef765f-15f7-5b73-bfa8-40b49281e265/");
  await expect(
    page.getByRole("heading", { name: "Ross Lee Finney", exact: true }),
  ).toBeVisible();
  for (const organization of ["Mount Holyoke College", "Hartt School of Music"]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
    await expect(
      page
        .locator('section[aria-labelledby="civilian-employer"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Smith College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "Ross Lee Finney Papers", exact: true })
      .first(),
  ).toBeVisible();

  await page.goto("./people/6cf300e3-bf39-5847-a2ab-50c7320d26cd/");
  await expect(
    page.getByRole("heading", { name: "Doris A Sharrar", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Montgomery Blair High School", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 700 for Sharrar's activity between 1940 graduation and post-Pearl Harbor OSS entry; no pre-OSS employer is documented online.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "The Glorious Amateurs of OSS: A Sisterhood of Spies",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/a908557f-c6ef-52b3-a94f-878cbf920f79/");
  await expect(
    page.getByRole("heading", { name: "Chauncy D Harris", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Department of State, Office of the Geographer",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Chicago", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Guide to the Chauncy D. Harris Papers 1893-2003",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/4f5707b0-a4d3-5fb1-940e-223b8d0e0d41/");
  await expect(
    page.getByRole("heading", { name: "Stanley P Lovell", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("heading", {
      name: "Lovell was running his own Massachusetts company when Donovan recruited him to lead OSS Research and Development.",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "OSS Exhibition Catalogue", exact: true })
      .first(),
  ).toBeVisible();
});

test("Batch 015 preserves academic, fashion, military, student, and unnamed-employer pathways", async ({
  page,
}) => {
  await page.goto("./people/c691c388-f4c1-51be-9047-eea867abc968/");
  await expect(
    page.getByRole("heading", { name: "Gardner Ackley", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Office of Price Administration",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "The Ohio State University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/c1f57bc0-8b8e-5fbe-b4b8-1e146322c366/");
  await expect(
    page.getByRole("heading", { name: "Marie Aline Griffith", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Hattie Carnegie", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/0b96a6dd-4d77-53b2-aad5-e942aebe4d3a/");
  await expect(
    page.getByRole("heading", { name: "John W Gardner", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Marine Corps", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Mount Holyoke College", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();

  await page.goto("./people/2dc32dd2-4124-5470-9c31-7fe64bfbb9f7/");
  await expect(
    page.getByRole("heading", { name: "Hugh Montgomery", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();

  await page.goto("./people/5e7905c6-6565-5f51-8b37-03e0f57205a1/");
  await expect(
    page.getByRole("heading", { name: "Lucien E Conein", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Unidentified Kansas City printer",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Kansas National Guard, Company G, 137th Infantry Regiment",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "\"No Boy Scout\": CIA Operations Officer Lucien Conein: A Study in Contrasts and Controversy",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /cia\.gov/);
});

test("Batch 016 preserves academic, design, military, government, alias, and occupation-only pathways", async ({
  page,
}) => {
  await page.goto("./people/039ff924-7560-5963-be0d-3e15c917d9d2/");
  await expect(
    page.getByRole("heading", { name: "Henry A Murray", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard Psychological Clinic", exact: true }),
  ).toBeVisible();

  await page.goto("./people/d1b224f9-97fc-5bc8-8aac-088a4f139d48/");
  await expect(
    page.getByRole("heading", { name: "Conyers Read", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Pennsylvania", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "William F. Read and Sons Company", exact: true }),
  ).toBeVisible();

  await page.goto("./people/b716d0a6-b18c-55c9-addd-721ae710f134/");
  await expect(
    page.getByRole("heading", { name: "Donal McLaughlin", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Raymond Loewy industrial design office", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "National Park Service", exact: true }),
  ).toBeVisible();

  await page.goto("./people/2c22bdd2-c625-51d7-b16d-10602a1770fa/");
  await expect(
    page.getByRole("heading", { name: "Lincoln Lundquist", exact: true }),
  ).toBeVisible();
  await expect(page.getByText(/Oliver Lincoln Lundquist/).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States War Department", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Raymond Loewy industrial design office", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();

  await page.goto("./people/232b3c0e-0988-59b0-a34c-9984cc3170c8/");
  await expect(
    page.getByRole("heading", { name: "William J Morgan", exact: true }),
  ).toBeVisible();
  await expect(page.getByText(/Anthony J\. Mitrano/).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(page.getByText(/school psychologist/i).first()).toBeVisible();
});

test("Batch 017 preserves membership, overlapping employment, qualified government pathways, and indexed variants", async ({
  page,
}) => {
  await page.goto("./people/d5fddfcc-304b-5207-878a-e5231e647295/");
  await expect(
    page.getByRole("heading", { name: "Felix Gilbert", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Institute for Advanced Study", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText(/professional affiliation/i),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Scripps College", exact: true }),
  ).toBeVisible();

  await page.goto("./people/9d917a08-06a5-5ec3-bebf-5c43b422a5aa/");
  await expect(
    page.getByRole("heading", { name: "Franz L Neumann", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Board of Economic Warfare",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("medium", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Institute for Social Research", exact: true }),
  ).toBeVisible();

  await page.goto("./people/690eab64-a21e-57dc-ae33-6dc576d5ea07/");
  await expect(
    page.getByRole("heading", { name: "Haje Holborn", exact: true }),
  ).toBeVisible();
  await expect(page.getByText(/Dr\. Hajo Holborn;.*Hajo Holborn/).first()).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Yale University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/1a923c3f-6b6e-5107-a470-9804a030c2bd/");
  await expect(
    page.getByRole("heading", { name: "Edward M Earle", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Institute for Advanced Study", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/4ebb85b3-0542-5281-b254-b36e810242bb/");
  await expect(
    page.getByRole("heading", { name: "Sigmund Neumann", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Wesleyan University", exact: true }),
    ).toBeVisible();
  }
});

test("Batch 018 separates continuing academic employment, Army transitions, and student status", async ({
  page,
}) => {
  await page.goto("./people/1adc6b42-2c4d-5611-ba6e-8cdbfd8ac6e0/");
  await expect(
    page.getByRole("heading", { name: "Crane Brinton", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Harvard University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/b47e5c36-3250-5574-a213-c8902573806a/");
  await expect(
    page.getByRole("heading", { name: "Harold C Deutsch", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Minnesota", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/c974e4f4-d9ea-5e9f-bcef-8bb019cb9f1f/");
  await expect(
    page.getByRole("heading", { name: "Perry G.E. Miller", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/78c03a2c-11e1-5f34-bf53-bc76c5f33817/");
  await expect(
    page.getByRole("heading", { name: "Franklin L Ford", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Cornell University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByText("Graduate student", { exact: true }),
  ).toBeVisible();

  await page.goto("./people/fb9b02f9-9dfb-5965-8514-fa5b73e3b2c9/");
  await expect(
    page.getByRole("heading", { name: "Gordon A Craig", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Princeton University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("medium", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("Doctoral student", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
});

test("Batch 019 separates federal and academic employment, Army service, and doctoral study", async ({
  page,
}) => {
  await page.goto("./people/5fc9dce9-664e-591d-bbed-c0d6b517c1e3/");
  await expect(
    page.getByRole("heading", { name: "Charles P Kindleberger", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "Board of Governors of the Federal Reserve System",
          exact: true,
        }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Bank for International Settlements", exact: true }),
  ).toBeVisible();

  await page.goto("./people/2e169a05-3d86-50b7-b195-4e5bb9b7cf0d/");
  await expect(
    page.getByRole("heading", { name: "Abram Bergson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Texas at Austin", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/3afb0ff0-6fae-57d7-812e-3a6143a4db19/");
  await expect(
    page.getByRole("heading", { name: "Stuart H Hughes", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Brown University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/d086f590-f86d-5535-8411-aa60aa252f01/");
  await expect(
    page.getByRole("heading", { name: "Carl E Schorske", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("Doctoral student in German history", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();

  await page.goto("./people/2ed25b69-80d3-5c7b-91cd-d70bca18cd2a/");
  await expect(
    page.getByRole("heading", { name: "Richard Hartshorne", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Wisconsin-Madison", exact: true }),
    ).toBeVisible();
  }
});

test("Batch 020 separates student, civilian-employer, and government-assignment pathways", async ({
  page,
}) => {
  await page.goto("./people/e909510a-c0a7-53e3-adb2-4e0c29f8a601/");
  await expect(
    page.getByRole("heading", { name: "Arthur H Robinson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "The Ohio State University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("Graduate student pursuing a Ph.D. in geography", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();

  await page.goto("./people/79d464a9-2e5e-5f96-b326-e8bbb03d7a79/");
  await expect(
    page.getByRole("heading", { name: "Edward A Ackerman", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Harvard University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/ae91f5d4-44b6-5096-89e9-9f6debbf5a24/");
  await expect(
    page.getByRole("heading", { name: "Emile Despres", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "Board of Governors of the Federal Reserve System",
          exact: true,
        }),
    ).toBeVisible();
  }

  await page.goto("./people/803386f6-0ee8-59b5-ae2a-4c0c086993a7/");
  await expect(
    page.getByRole("heading", { name: "Carl Kaysen", exact: true }),
  ).toBeVisible();
  for (const organization of [
    "National Bureau of Economic Research",
    "Columbia University",
  ]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "National Bureau of Economic Research",
        exact: true,
      }),
  ).toBeVisible();

  await page.goto("./people/e3b15c03-9d62-5a59-8ac0-117fe8e68bef/");
  await expect(
    page.getByRole("heading", { name: "Edward S Mason", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "U.S. Office of Production Management",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "U.S. Department of Labor", exact: true }),
  ).toBeVisible();
});

test("Batch 021 separates academic, Federal Reserve, NBER, and OPA pathways", async ({
  page,
}) => {
  await page.goto("./people/e6f133b8-bd4a-5796-978c-b91076896fef/");
  await expect(
    page.getByRole("heading", { name: "Geroid T Robinson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Columbia University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/d633583e-637d-519b-a417-0eeb7ee8305b/");
  await expect(
    page.getByRole("heading", { name: "Barrington Moore", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("No reviewed claim currently meets the publication threshold.", {
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Yale University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/1d4ac037-dc29-51c0-81b4-c55b3b536f46/");
  await expect(
    page.getByRole("heading", { name: "Calvin B Hoover", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Duke University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/025318bc-bb51-5ebd-9d13-fb4c728dbfa8/");
  await expect(
    page.getByRole("heading", { name: "Chandler Morse", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Board of Governors of the Federal Reserve System",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Federal Reserve Bank of New York", exact: true }),
  ).toBeVisible();

  await page.goto("./people/d38ec240-05df-5155-abc9-3ed54484ff5f/");
  await expect(
    page.getByRole("heading", { name: "Sidney S Alexander", exact: true }),
  ).toBeVisible();
  for (const organization of [
    "National Bureau of Economic Research",
    "United States Office of Price Administration",
  ]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "National Bureau of Economic Research",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
});

test("Batch 022 separates museum, university, research, and student pathways", async ({
  page,
}) => {
  await page.goto("./people/1147408f-3793-5ab4-9176-58a04dd8ad5f/");
  await expect(
    page.getByRole("heading", { name: "Gregory Bateson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "The Museum of Modern Art", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/ae597b0c-6982-5c47-8b87-f74cfb29b92c/");
  await expect(
    page.getByRole("heading", { name: "John F Embree", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Toronto", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "University of Hawaii", exact: true }),
  ).toBeVisible();

  await page.goto("./people/90b3258d-f890-5535-982f-6fd2b275caf9/");
  await expect(
    page.getByRole("heading", { name: "Ralph Linton", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Columbia University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/0c060ee9-da85-5446-94b6-77bc939fd231/");
  await expect(
    page.getByRole("heading", { name: "Rhoda Metraux", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "National Research Council", exact: true }),
    ).toBeVisible();
  }
  for (const organization of ["Oxford University Press", "Yale University"]) {
    await expect(
      page
        .locator('section[aria-labelledby="earlier-affiliations"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/59eb0f93-2dc1-51db-8fe3-100a43fef801/");
  await expect(
    page.getByRole("heading", { name: "Raymond Kennedy", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Yale University", exact: true }),
    ).toBeVisible();
  }
});

test("Batch 023 separates civilian employers from COI and Army predecessor assignments", async ({
  page,
}) => {
  await page.goto("./people/0481f178-4ac5-565a-8a7a-09733f86f6fa/");
  await expect(
    page.getByRole("heading", { name: "James P Baxter III", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Williams College", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("WO C", { exact: true })).toBeVisible();
  await expect(
    page.getByText("unknown or indeterminate", { exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/6c04259d-0aaf-5c19-87e9-6fb1d7000112/");
  await expect(
    page.getByRole("heading", { name: "Saul K Padover", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "United States Department of the Interior",
          exact: true,
        }),
    ).toBeVisible();
  }
  await expect(page.getByText("Assistant to the Secretary", { exact: true }).first()).toBeVisible();

  await page.goto("./people/988b1615-a74b-5020-a82d-cbd8831f21c9/");
  await expect(
    page.getByRole("heading", { name: "C. Martin Wilbur", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Field Museum of Natural History", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/2da25f0d-1148-57f0-b356-810e445c281b/");
  await expect(
    page.getByRole("heading", { name: "Charles F Remer", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "NAID 2184121", exact: true })).toHaveAttribute(
    "href",
    "https://catalog.archives.gov/id/2184121",
  );

  await page.goto("./people/b5293d31-eab2-5557-a664-0c2097017949/");
  await expect(
    page.getByRole("heading", { name: "Morris Janowitz", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "United States Department of Justice", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "New York University", exact: true }),
  ).toBeVisible();
});

test("Batch 024 preserves academic, government, military, and uncertain pathways", async ({
  page,
}) => {
  await page.goto("./people/61638d98-2b07-50f1-b1fd-ee8f1254c3e6/");
  await expect(
    page.getByRole("heading", { name: "Edward A Shils", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Chicago", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable immediate", { exact: true })).toBeVisible();

  await page.goto("./people/6885339c-afe2-5326-982a-6e0d6735c28c/");
  await expect(
    page.getByRole("heading", { name: "Sterling Dow", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Harvard University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/424a424a-9dbb-5ed8-a29c-69aa4c2e9831/");
  await expect(
    page.getByRole("heading", { name: "Donald C McKay", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/bc1757bd-9946-593f-8575-8c470dd6c61f/");
  await expect(
    page.getByRole("heading", { name: "John L Clive", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Hans Leo Kleyff");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "University of North Carolina at Chapel Hill",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS civilian employer has yet been identified",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  await page.goto("./people/fe8ec29a-718c-56f3-af64-d619600f4f0d/");
  await expect(
    page.getByRole("heading", { name: "Robert L Wolff", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("temporal relation uncertain", { exact: true })).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByText("medium", { exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "does not establish whether it preceded or followed OSS",
  );
});

test("Batch 025 separates academic employment, student status, and military or government predecessors", async ({
  page,
}) => {
  await page.goto("./people/29a830f4-a1d4-5821-af64-d014e89c71da/");
  await expect(
    page.getByRole("heading", { name: "Preston E James", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Coordinator of Information",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();

  await page.goto("./people/08a92bff-7683-5a94-bd92-09a33ef5e667/");
  await expect(
    page.getByRole("heading", { name: "Norman O Brown", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Nebraska Wesleyan University",
        exact: true,
      }),
  ).toBeVisible();

  await page.goto("./people/56b8952b-c21c-5f0f-b653-22fb22980b15/");
  await expect(
    page.getByRole("heading", { name: "Leonard Krieger", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Yale University", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS civilian employer has yet been identified",
  );
});

test("Batch 025 keeps the two Paul M Sweezy rows separate and withholds the biographical candidate", async ({
  page,
}) => {
  const profiles = [
    "ead0d460-6fcd-51cd-a6d4-01862ecc82f8",
    "8686bb8e-3b16-5aa2-bb72-bdd2e6a6f3aa",
  ];
  for (const personId of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: "Paul M Sweezy", exact: true }),
    ).toBeVisible();
    await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.getByText("critical", { exact: true })).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "accessible sources do not map either number",
    );
    await expect(page.locator("body")).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    expect(await page.locator("article.claim-card").count()).toBe(0);
    expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
  }
});

test("Batch 026 separates civilian work, military assignment, and student status for five women", async ({
  page,
}) => {
  await page.goto("./people/9b51ae67-0705-5366-84d1-75d1266f4e1e/");
  await expect(
    page.getByRole("heading", { name: "Mary D Bancroft", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Reminiscences of Mary Bancroft, 1979-1980",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://researchworks.oclc.org/archivegrid/archiveComponent/269253002",
  );

  await page.goto("./people/dce57294-738d-5a94-980d-df3821ed4b3e/");
  await expect(
    page.getByRole("heading", { name: "Stephanie Czech", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Women's Army Corps", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Texas Oil Company", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("commissioned army officer", { exact: true }).first()).toBeVisible();

  await page.goto("./people/16cc0420-e809-5938-bbb5-042b165dcfc4/");
  await expect(
    page.getByRole("heading", { name: "Elizabeth P MacDonald", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Scripps-Howard News Service", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Honolulu Advertiser", exact: true }),
  ).toBeVisible();

  await page.goto("./people/614cf208-c223-5a74-b23d-f4d3edd1bfda/");
  await expect(
    page.getByRole("heading", { name: "Jane Foster", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Mills College", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("student");
  await expect(page.locator("body")).toContainText(
    "No reliable named pre-OSS employer has yet been identified",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Transitioning into CIA: The Strategic Services Unit in Indonesia",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/static/Transitioning-into-CIA.pdf",
  );

  await page.goto("./people/128fcc95-79fa-5d1f-8893-90ba9c5defb6/");
  await expect(
    page.getByRole("heading", { name: "Stella T Uzdawinis", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Stella Uzdawinis's Office of Strategic Services Pendant",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/legacy/museum/artifact/stella-uzdawiniss-office-of-strategic-services-pendant/",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 027 separates employers, independent scholarship, military status, and unnamed financial work", async ({
  page,
}) => {
  await page.goto("./people/5dd07840-484a-5a8d-be2c-4b1b16545ed6/");
  await expect(
    page.getByRole("heading", { name: "Joseph R Hayden", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Michigan", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .getByRole("link", {
        name: "Joseph Ralston Hayden Papers, 1854-1975",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://findingaids.lib.umich.edu/catalog/umich-bhl-851643",
  );

  await page.goto("./people/20cd1668-459e-529d-ac47-85b422f746e4/");
  await expect(
    page.getByRole("heading", { name: "Wilmarth S Lewis", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Independent Horace Walpole scholarship and collecting",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText("professional affiliation");

  await page.goto("./people/aaa83b52-5ab0-5c86-9146-db6dc477dd9e/");
  await expect(
    page.getByRole("heading", { name: "Junius S Morgan", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "J.P. Morgan & Co.", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("commissioned naval officer", { exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/fd719ab0-0e3d-56dd-b163-810da257da6e/");
  await expect(
    page.getByRole("heading", { name: "William L Rehm", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "one of the largest investment trusts in the United States",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/dac80940-34d9-5545-8d3b-b3b509a69238/");
  await expect(
    page.getByRole("heading", { name: "R H Goddard", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Goddard Brothers", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Robert H. Ives Goddard");
  await expect(page.locator("body")).toContainText("professional affiliation");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 028 separates government, business, military, fellowship, and student pathways", async ({
  page,
}) => {
  await page.goto("./people/78a869fb-aa25-5d6a-aca6-59feb5e38171/");
  await expect(
    page.getByRole("heading", { name: "Paul Baran", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Office of Price Administration",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "Brookings Institution research fellowship",
  );
  await expect(page.locator("body")).toContainText(
    "his uncles' timber business",
  );

  await page.goto("./people/4004a23d-52bc-5ce6-b450-36238827b287/");
  await expect(
    page.getByRole("heading", { name: "G E Buxton", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "B. B. & R. Knight Company",
          exact: true,
        }),
    ).toBeVisible();
  }
  await expect(page.locator("body")).toContainText(
    "exact B. B. & R. Knight departure date, 1939-1941 activities",
  );

  await page.goto("./people/30ddbc7e-f6fe-56ab-8651-8f743563cd7c/");
  await expect(
    page.getByRole("heading", { name: "James R Forgan", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText(
    "No reviewed claim currently meets the publication threshold.",
  );
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Glore, Forgan & Co.", exact: true }),
  ).toBeVisible();

  await page.goto("./people/0d2d73be-e7ba-5b98-8494-0e9b9adaa189/");
  await expect(
    page.getByRole("heading", { name: "Everette H Hunt Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "Brown is not classified as his employer",
  );

  await page.goto("./people/ab9ab673-8090-56bf-9973-36b0edc77610/");
  await expect(
    page.getByRole("heading", { name: "Shaw Livermore Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Mercersburg Academy");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 029 separates SOE, police, military, maritime, student, and unnamed work pathways", async ({
  page,
}) => {
  await page.goto("./people/44112d43-06b1-5114-aa17-91a6cffb1939/");
  await expect(
    page.getByRole("heading", { name: "William E Fairbairn", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Special Operations Executive", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Shanghai Municipal Police", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("British A");

  await page.goto("./people/789afa1d-9778-5d84-904a-0f341884f736/");
  await expect(
    page.getByRole("heading", { name: "Frank V Huston", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Navy", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("United States Coast Guard");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/bd3c2c04-e39d-57a9-b1ed-6e01285235e3/");
  await expect(
    page.getByRole("heading", { name: "Edward E Nicholas Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "University of Illinois Urbana-Champaign",
  );
  await expect(page.locator("body")).toContainText("University of Chicago");

  await page.goto("./people/83cada86-f7bc-557c-a378-6b9af5a5f4a1/");
  await expect(
    page.getByRole("heading", {
      name: "Vincent L Gonzalez Jr.",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Merchant Marine",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Runner");
  await expect(page.locator("body")).toContainText("unnamed employer");
  await expect(page.locator("body")).toContainText("professional affiliation");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/3e307074-39c7-5736-8318-0203a3a813b6/");
  await expect(
    page.getByRole("heading", { name: "Roger L Belanger", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Air Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 030 separates named employers, military and government paths, student status, and an unnamed journalism employer", async ({
  page,
}) => {
  await page.goto("./people/192b5ab4-e4d7-58d4-8ea8-d12e489bf089/");
  await expect(
    page.getByRole("heading", { name: "Edgar A Prichard", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("journalist in Oklahoma");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/dc965089-2d9c-538d-8eaa-96001a5e06b2/");
  await expect(
    page.getByRole("heading", { name: "Jerry M Sage", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Procter & Gamble", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Salesman");

  await page.goto("./people/22cdf385-f081-5297-8f59-5db0c83088d5/");
  await expect(
    page.getByRole("heading", { name: "Elmer Harris", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Marine Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "General Petroleum Company",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("USMCR");

  await page.goto("./people/6c066bb5-f2ad-5a1c-a5e6-85de659ea560/");
  await expect(
    page.getByRole("heading", { name: "George H White", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Federal Bureau of Narcotics",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/7f4c48f4-c54f-53da-b317-94db785f8c0b/");
  await expect(
    page.getByRole("heading", {
      name: "Charles M Parkin Jr.",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Pennsylvania State University",
  );
  await expect(page.locator("body")).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 031 separates Area B military pathways from student and qualified athletic affiliations", async ({
  page,
}) => {
  await page.goto("./people/a57ba5cd-7218-58e5-a325-6a9e70d925f5/");
  await expect(
    page.getByRole("heading", { name: "Albert Robinso Guay", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("American University");
  await expect(
    page.getByText("enlisted army personnel", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/4626fb9d-f7ed-56b4-a7ec-492c76374b2b/");
  await expect(
    page.getByRole("heading", { name: "Arden W Dow", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Army lieutenant in Military Police");
  await expect(page.locator("body")).toContainText("Washington State University");

  await page.goto("./people/d0e64eee-71c2-58eb-bf99-0e98b74a880a/");
  await expect(
    page.getByRole("heading", { name: "Frank A Gleason", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Pennsylvania State University",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/832d939e-cbb0-5979-9c57-bb0c0e27113d/");
  await expect(
    page.getByRole("heading", { name: "Joseph Collart", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Washington State University");
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );

  await page.goto("./people/576aa158-a1be-56a6-96fc-c6c536de6381/");
  await expect(
    page.getByRole("heading", { name: "Rex Applegate", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("209th Military Police Company");
  await expect(page.locator("body")).toContainText("University of Oregon");
  await expect(page.locator("body")).toContainText("Oregon State University");
  await expect(page.locator("body")).toContainText(
    "exact nature and dates of that institutional association remain uncertain",
  );
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Roll Call: Lieutenant Colonel Rex Applegate (1914-1998)",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.dvidshub.net/news/476096/roll-call-lieutenant-colonel-rex-applegate-1914-1998",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 032 preserves Area B command, engineer, occupation-only, and identity-review boundaries", async ({
  page,
}) => {
  await page.goto("./people/c4b9c664-cdcf-56e7-8bd1-eaa7d5c13a4a/");
  await expect(
    page.getByRole("heading", { name: "Ainsworth Blogg", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Reserve infantry officer assigned to Military Police",
  );
  await expect(page.locator("body")).toContainText(
    "insurance-company executive in Seattle",
  );
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/17ca80e8-cf1a-59e0-b414-e4b748013fa3/");
  await expect(
    page.getByRole("heading", { name: "Louise D Cohen", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("needs identity review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Box 133");
  await expect(page.locator("body")).toContainText(
    "no reviewed service-number or file linkage establishes",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/3049d936-8a0c-5bc3-9e6d-4024e9f59dd3/");
  await expect(
    page.getByRole("heading", { name: "Morris M Kessler", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "probably is the psychiatrist and Captain Morris M. Kessler",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/aaffd5ea-3b75-54a0-b333-ea7e962ed025/");
  await expect(
    page.getByRole("heading", { name: "Joseph E/M Lazarsky", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Joseph E. Lazarsky");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Sergeant and demolitions instructor",
  );
  await expect(
    page
      .getByRole("link", {
        name: "The Office of Strategic Services (OSS) in World War II",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://coph.fullerton.edu/collections/OHP_18_OSS%20Finding%20Aid.pdf",
  );

  await page.goto("./people/c1fe22b5-0087-5440-9858-6484c72c46e6/");
  await expect(
    page.getByRole("heading", { name: "Leopold Karwoski", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Leopold Karwaski");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.getByText("Capt", { exact: true }).first()).toBeVisible();

  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 033 preserves civilian, Army, SOE, qualified-employer, and occupation-only boundaries", async ({
  page,
}) => {
  await page.goto("./people/521c80ee-c975-552a-b41f-d565c60a921b/");
  await expect(
    page.getByRole("heading", { name: "George S Wuchinich", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Fairbanks, Morse and Company",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "determine whether Fairbanks, Morse and Company remained his employer until Army enlistment",
  );
  await expect(
    page
      .getByRole("link", { name: "Carnegie Alumnus", exact: true })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://iiif.library.cmu.edu/file/ALU_1939_025_002_12001939/ALU_1939_025_002_12001939.pdf",
  );

  await page.goto("./people/f28308b3-7c6e-5819-834d-62ec9ef7a65f/");
  await expect(
    page.getByRole("heading", { name: "Hans V Tofte", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Special Operations Executive",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Tofte's immediate pre-OSS affiliation was United States Army service",
  );

  await page.goto("./people/43d0bb66-4c39-5627-85a1-3a85350d973d/");
  await expect(
    page.getByRole("heading", { name: "Howard E Manning", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Self-employed legal practice",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Manning's last documented civilian work before Army service was his individual legal practice in Raleigh",
  );
  await expect(page.locator("body")).not.toContainText("Manning & Manning");
  await expect(
    page
      .getByRole("link", {
        name: "Hill's Raleigh (Wake County, N.C.) City Directory [1940]",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", "https://lib.digitalnc.org/record/25789?ln=en");

  await page.goto("./people/2bb10033-1c66-53cc-8c22-f465a0085b9d/");
  await expect(
    page.getByRole("heading", { name: "John F Navarro", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "restaurateur in New England",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/59b8e455-1c85-5ea4-a087-e756d4d1f5b3/");
  await expect(
    page.getByRole("heading", { name: "Peter G Mero", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "investment executive in Chicago",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 034 preserves radio, cryptology, military, student, and unnamed-institution boundaries", async ({
  page,
}) => {
  await page.goto("./people/f4887f88-5b29-5975-beb5-09370cb58b0c/");
  await expect(
    page.getByRole("heading", { name: "James F Ranney", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "engineer at an unnamed radio station in Youngstown",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/d0270e61-812f-5936-95cf-52fed2d3ec42/");
  await expect(
    page.getByRole("heading", {
      name: "Spyridon G Kapponnis",
      exact: true,
    }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Spiro Cappony");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Navy", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Michigan State College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "Final Report of the Evros Mission", exact: true })
      .first(),
  ).toHaveAttribute("href", /elia\.org\.gr/);

  await page.goto("./people/5b33ad31-3142-5f14-8cba-5742f5ed22de/");
  await expect(
    page.getByRole("heading", { name: "Arthur F Reinhardt", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Air Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("extract fr");
  await expect(page.locator("body")).not.toContainText(
    "family farm was his employer",
  );

  await page.goto("./people/481bfe0a-c476-5e72-9f85-02a45791f78e/");
  await expect(
    page.getByRole("heading", { name: "Gail F Donnalley", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Ohio Wesleyan University", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Sophomore student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/f1f25aef-0f06-516c-ac04-4cc449634133/");
  await expect(
    page.getByRole("heading", { name: "John W Brunner", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "college (institution not identified)",
  );
  await expect(page.locator("body")).toContainText(
    "NPS says the Army sent Brunner to study Chinese",
  );
  await expect(page.locator("body")).toContainText(
    "The official history documents the subjects and student status but names no institution.",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 035 preserves communications, occupation-only, Army-pathway, and self-employment boundaries", async ({
  page,
}) => {
  await page.goto("./people/50c70f7c-dfec-5a4e-9c02-5ca83112c7f3/");
  await expect(
    page.getByRole("heading", { name: "Timothy R Marsh", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("United States Army Signal Corps");
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Coyne Radio School", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("civilian Signal Corps radio operator");

  await page.goto("./people/f7687b71-e238-5390-a43c-2552d9e641d6/");
  await expect(
    page.getByRole("heading", { name: "Lawrence W Lowman", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Columbia Broadcasting System",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Columbia Broadcasting System");
  await expect(page.locator("body")).toContainText("vice president in charge of operations");
  await expect(
    page
      .getByRole("link", {
        name: "A Wartime Organization for Unconventional Warfare",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/a-wartime-organization-for-unconventional-warfare.htm",
  );

  await page.goto("./people/2ae252cc-7164-560c-b4b9-d8e91d49e05d/");
  await expect(
    page.getByRole("heading", { name: "John M Balsamo", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "The indexed John M. Balsamo is probably",
  );
  await expect(page.locator("body")).toContainText("Wall Street telegrapher");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).not.toContainText("Western Union");

  await page.goto("./people/6989c183-4a99-52c5-a208-5f7b95f354d7/");
  await expect(
    page.getByRole("heading", { name: "William R Peers", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "probably commissioned service in the United States Army",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Intelligence Operations of OSS Detachment 101",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-4-no-3/intelligence-operations-of-oss-detachment-101/",
  );

  await page.goto("./people/45f220f1-4668-5395-b0e4-f7a4921b254f/");
  await expect(
    page.getByRole("heading", { name: "Nicol Smith", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Nichol Smith");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Self-employed");
  await expect(page.locator("body")).toContainText("travel writer and author");
  await expect(
    page
      .getByRole("link", {
        name: "War of a Different Kind: OSS and Free Thai Operations in World War II",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/static/OSS-and-Free-Thai.pdf",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 036 preserves communications pathways, unnamed employers, student status, and duplicate uncertainty", async ({
  page,
}) => {
  await page.goto("./people/46e3bd6e-3f4a-59d4-b4e3-52a9aeb1a3a0/");
  await expect(
    page.getByRole("heading", { name: "Lawrence Hollander", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Lawyer", exact: true }),
  ).toBeVisible();
  const civilianEmployerSection = page.locator(
    'section[aria-labelledby="civilian-employer"]',
  );
  await expect(civilianEmployerSection).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    civilianEmployerSection.getByRole("heading", {
      name: "Self-employed",
      exact: true,
    }),
  ).toHaveCount(0);
  await expect(page.locator("body")).toContainText("duplicate-36fe462e632d");
  await expect(
    page
      .getByRole("link", {
        name: "OSS Training in the National Parks and Service Abroad in World War II",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /ossreborn\.com/);

  await page.goto("./people/dfef5646-c18d-5421-b981-9b3f3b573cf8/");
  await expect(
    page.getByRole("heading", { name: "L L Hollander", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-36fe462e632d");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText(
    "Hollander was a lawyer in Chicago immediately before OSS recruitment.",
  );

  await page.goto("./people/00a5d0a9-dc9b-5185-a142-b81a5395cbed/");
  await expect(
    page.getByRole("heading", { name: "Marvin S Flisser", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Brooklyn College", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText(
    "student",
  );

  await page.goto("./people/2d2a4f2a-652a-56f0-94f4-c7f0af234134/");
  await expect(
    page.getByRole("heading", { name: "Willis S Georgia Jr.", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("W. Scudder Georgia Jr.");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Navy", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Hobart and William Smith Colleges",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/96468b14-dc3d-58df-b454-ba38f51d4cfe/");
  await expect(
    page.getByRole("heading", { name: "Robert R Kehoe", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "a chemical plant (not named)",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "A Memoir of Jed Team Frederick: An Allied Team with the French Resistance, 1944",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/static/Allied-Team-French-Resistance.pdf",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 037 resolves an Allied pathway while preserving unknown staff backgrounds and the two Herbert rows", async ({
  page,
}) => {
  await page.goto("./people/8c8af948-dd3b-536e-8ba0-988f6cf3d97f/");
  await expect(
    page.getByRole("heading", { name: "Benton E Bickham Jr.", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Benton E. Bickham from Louisiana.");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/fae94705-43d9-5e0b-8567-70e624282604/");
  await expect(
    page.getByRole("heading", { name: "Milton W Griffith", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Milton Giffith");
  await expect(page.locator("body")).toContainText(
    "whether 'bus driver' described camp duty or prewar employment",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/654e73f7-0645-5c3c-a3c8-529f5f049b7f/");
  await expect(
    page.getByRole("heading", { name: "Louis Lostfogel", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("physician");
  await expect(page.locator("body")).toContainText(
    "pre-OSS practice, employer, and Medical Corps entry chronology",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/638047fa-fbbe-53c7-96d4-77c794b814c2/");
  await expect(
    page.getByRole("heading", { name: "Edmund I Stromholt", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Edward Stromholt");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Norwegian Army", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Veteran of Lofoten Raid", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://princealbertlibrary.ca/padh/1941/October/Oct%2015%2C%201941.pdf",
  );

  await page.goto("./people/5ba837c6-75af-5db2-88f8-648243ded832/");
  await expect(
    page.getByRole("heading", { name: "James Herbert", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-f6de91a0d711");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("United States Navy");

  await page.goto("./people/f91af878-e2dc-5144-80f5-76aae6e74d1b/");
  await expect(
    page.getByRole("heading", { name: "James E Herbert", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-f6de91a0d711");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("United States Navy");

  await page.goto("./organizations/7fe1f71a-6ae9-5437-812e-946a18e377a4/");
  await expect(
    page.getByRole("heading", { name: "Norwegian Army", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Edmund I Stromholt" })).toBeVisible();

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 038 distinguishes the Velleman brothers and withholds incomplete Area B identities", async ({
  page,
}) => {
  await page.goto("./people/833cab1f-839d-5766-baf2-4bebff78cada/");
  await expect(
    page.getByRole("heading", { name: "Moritz Velleman", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "a friend's office in Lisbon (organization not named)",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/9a81eee3-9800-507c-b604-ef49aafc3da3/");
  await expect(
    page.getByRole("heading", { name: "Arthur H Velleman", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("OSS Documents Division");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/858dafc5-02bc-5660-a2f3-1027fdc6e0af/");
  await expect(
    page.getByRole("heading", { name: "George A George", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Georges George");

  for (const [personId, displayName] of [
    ["abee3674-bf36-50b9-bf28-b28905129288", "Howard C Ressler"],
    ["264a44a0-6a03-5451-a2aa-8fd8805c0cf0", "Raymond W Deisher"],
  ] as const) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold.");
  }

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 039 preserves film, media, military, and occupation-only boundaries", async ({
  page,
}) => {
  await page.goto("./people/b7a8a36f-3f0e-54c1-a0ff-23c840498501/");
  await expect(
    page.getByRole("heading", { name: "Seymour W Schulberg", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Budd Wilson Schulberg");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Naval Reserve", exact: true }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Columbia Pictures",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("RKO");
  await expect(page.locator("body")).toContainText("Selznick Pictures");

  await page.goto("./people/63d92813-94cd-578e-942a-c2bdc37a92d8/");
  await expect(
    page.getByRole("heading", { name: "Stuart H Schulberg", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("enlisted marine corps personnel");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Marine Corps");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Washington Daily News",
  );

  await page.goto("./people/47b86de9-0ac5-583a-9eae-707215c42f9f/");
  await expect(
    page.getByRole("heading", { name: "Robert R Parrish", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("assistant editor and sound editor");
  await expect(page.locator("body")).toContainText("CSP P");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/92b2503f-4ea7-5399-8362-16f04547fe7d/");
  await expect(page.getByRole("heading", { name: "Sol Kaplan", exact: true })).toBeVisible();
  await expect(page.locator("body")).toContainText("pianist and composer");
  await expect(page.locator("body")).toContainText("Army Signal Corps");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/cb463c42-75dd-58ee-8222-d192e2b2c684/");
  await expect(page.getByRole("heading", { name: "Corey Ford", exact: true })).toBeVisible();
  await expect(page.locator("body")).toContainText("commissioned army officer");
  await expect(page.locator("body")).toContainText("Vanity Fair");
  await expect(page.locator("body")).toContainText("The Saturday Evening Post");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 040 preserves field pathways, occupation boundaries, spelling variants, and separate Mayer rows", async ({
  page,
}) => {
  await page.goto("./people/72ba8a20-2fdf-56be-b228-6dbb45dde0af/");
  await expect(
    page.getByRole("heading", { name: "Roderick G.S. Hall", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "270th Engineer Combat Battalion, United States Army",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Yale University");

  await page.goto("./people/cde21206-1f2d-5241-82c6-7b30c8f95aa0/");
  await expect(
    page.getByRole("heading", { name: "Miles A Copeland", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("professional jazz musician");
  await expect(page.locator("body")).not.toContainText("Benny Goodman");

  await page.goto("./people/6df71376-3491-5715-91af-53606a60d0fd/");
  await expect(
    page.getByRole("heading", { name: "George S Musolin", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("George S. Musulin");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("115th Infantry Regiment");
  await expect(page.locator("body")).toContainText("professional football");

  await page.goto("./people/59f66a94-282a-5f09-b5d1-ea7cdeed4705/");
  await expect(
    page.getByRole("heading", { name: "Frederick Mayer", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(page.locator("body")).toContainText("Ford Motor Company");
  await expect(page.locator("body")).toContainText("General Motors");
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);

  await page.goto("./people/ed9e4da5-f917-555a-9fda-052036f02574/");
  await expect(
    page.getByRole("heading", { name: "Frederick Mayer", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("Ford Motor Company");
  await expect(page.locator("body")).not.toContainText("General Motors");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 041 preserves Mediterranean military pathways, veterans affiliations, unnamed occupations, and separate Felsen rows", async ({
  page,
}) => {
  await page.goto("./people/97b90b5c-774c-5d9c-8e52-ca3a4aaeaeec/");
  await expect(
    page.getByRole("heading", { name: "Milton Felsen", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Abraham Lincoln Brigade");
  await expect(page.locator("body")).toContainText("Recording Secretary");
  await expect(page.locator("body")).toContainText("University of Iowa");
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);

  await page.goto("./people/42f68c35-d165-58cf-9ad3-365a27b9cec0/");
  await expect(
    page.getByRole("heading", { name: "Milton Felsen", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("University of Iowa");

  await page.goto("./people/4b1fbe1c-9f20-51e5-ae9f-0ef466d3c5b8/");
  await expect(
    page.getByRole("heading", { name: "Irving Goff", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("National Executive Secretary");
  await expect(page.locator("body")).toContainText("adagio dancer");
  await expect(page.locator("body")).toContainText(
    "Unnamed adagio-dance employer or engagement",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/af3332e4-4282-5f1d-8bd2-4dc0f8097b9a/");
  await expect(
    page.getByRole("heading", { name: "Paul H Gale", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "1st Infantry Division, United States Army",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Captain and staff officer");

  await page.goto("./people/7bee69f7-b984-5850-96e1-38253676750e/");
  await expect(
    page.getByRole("heading", { name: "Serge Obolensky", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "New York National Guard", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("St. Regis Hotel");
  await expect(page.locator("body")).toContainText(
    "Unnamed New York banking and real-estate organizations",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 042 preserves academic, broadcast, Allied, naval, and Coast Guard pathways", async ({
  page,
}) => {
  await page.goto("./people/b76c60a1-20b9-547e-a824-20217835f29b/");
  await expect(
    page.getByRole("heading", { name: "Clarence A Berdahl", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "University of Illinois Urbana-Champaign",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "University of Illinois",
  );

  await page.goto("./people/a583532b-5750-5264-90a4-cbb5ca567a71/");
  await expect(
    page.getByRole("heading", { name: "Hugh M Beville", exact: true }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "National Broadcasting Company",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/b5c889e5-13d7-5a47-bb1d-f8536f24be22/");
  await expect(
    page.getByRole("heading", { name: "Richard G Arnold-Baker", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("British Army Intelligence Corps");
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/1f9ace73-691d-5b96-8349-203d8c7594f4/");
  await expect(
    page.getByRole("heading", { name: "Everett J Athens", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Everette J. Athens");
  await expect(page.locator("body")).toContainText("commissioned naval officer");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/19c983e0-37cb-5b11-8e40-1c4bd39b7103/");
  await expect(
    page.getByRole("heading", { name: "John P Booth", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("commissioned coast guard officer");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Coast Guard", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Operational Swimmer Group II");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 043 separates students, earlier employment, and civilian and military ONI service", async ({
  page,
}) => {
  await page.goto("./people/404292b8-801c-58f0-8f74-6fd447da6adf/");
  await expect(
    page.getByRole("heading", { name: "Franklin P Holcomb", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Office of Naval Intelligence", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Marine Reserve officer at ONI");
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Office of Naval Intelligence", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Western Hemisphere Division portfolio officer");

  await page.goto("./people/bb6a423b-f07a-55b3-829a-492f44faf418/");
  await expect(
    page.getByRole("heading", { name: "Cora Dubois", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Hunter College", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Boston Psychopathic Hospital");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("professional affiliation");

  for (const profile of [
    ["d086f590-f86d-5535-8411-aa60aa252f01", "Carl E Schorske"],
    ["78c03a2c-11e1-5f34-bf53-bc76c5f33817", "Franklin L Ford"],
    ["fb9b02f9-9dfb-5965-8514-fa5b73e3b2c9", "Gordon A Craig"],
    ["813fb48c-b658-5cdf-a265-ce63acb776fc", "James C Luce"],
  ]) {
    await page.goto(`./people/${profile[0]}/`);
    await expect(
      page.getByRole("heading", { name: profile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
  }

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 044 adds supported employers while preserving student, military, and duplicate boundaries", async ({
  page,
}) => {
  await page.goto("./people/2201ee7c-3d64-5672-b519-0aad4625d185/");
  await expect(
    page.getByRole("heading", { name: "Edna W Andrade", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "The Hecht Company", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "The Hecht Company", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "H. Sophie Newcomb Memorial College",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Oral history interview with Edna Andrade, 1987 April 1-29",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /aaa\.si\.edu/);

  await page.goto("./people/6b90e0e8-f17e-585f-8d21-ecde2a323f1b/");
  await expect(
    page.getByRole("heading", { name: "Conrad F Lagueux", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "University of Rhode Island", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/a2d66764-90d0-5d8d-8102-30c2e0b03ba1/");
  await expect(
    page.getByRole("heading", { name: "Peter M F Sichel", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Medical Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "H. Sichel Söhne", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "The adjacent Peter M. Sichel row has a different service number and remains separate.",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  await page.goto("./people/1bf7bd5e-a790-51d0-9a46-e6046cab07f2/");
  await expect(
    page.getByRole("heading", { name: "Peter M Sichel", exact: true }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText(
    "H. Sichel Söhne",
  );
  await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();

  for (const terminalProfile of [
    ["21a6b6f2-5daa-5569-826e-6d193f387d4a", "Mort S Bobrow", "completed"],
    ["697f0736-ba27-55b6-ae7a-6550dd87aa3c", "Edmund M Burke", "requires archival review"],
    ["f87b5adb-6496-5f61-a50f-2b098032d189", "Jane Burrell", "requires archival review"],
    ["01360217-ccc5-5754-a6d5-9d126bfc08f0", "John H Hemingway", "completed"],
    ["a93ac760-896e-50b9-9746-754d434a1200", "John Magruder", "completed"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText(terminalProfile[2], { exact: true }).first(),
    ).toBeVisible();
  }
});

test("Batch 045 publishes the Allied pathway while routing unresolved cases to archival review", async ({
  page,
}) => {
  await page.goto("./people/b9907bf8-4544-55fe-85a2-e99e9530df73/");
  await expect(
    page.getByRole("heading", { name: "Etienne Ancergues", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Bureau Central de Renseignements et d'Action",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "French Navy", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", {
      name: "Dossier individuel de personnel de ANCERGUES, ETIENNE ANDRÉ GEORGES",
      exact: true,
    }),
  ).toHaveAttribute("href", /servicehistorique\.sga\.defense\.gouv\.fr/);
  await expect(page.locator("body")).toContainText("PDF page 8");
  await expect(page.locator("body")).toContainText("Box 14");
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  await page.goto("./people/6ea50bee-54e9-54f1-91ca-b052afc98eda/");
  await expect(
    page.getByRole("heading", { name: "Philip H Chadbourn Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  for (const terminalProfile of [
    ["933cbc8e-758f-51de-90fc-afd7d32dba55", "Billie F Akin"],
    ["c407e9fa-3a4c-5cfc-b5ec-d0664ab4133d", "Julia N Barnhart"],
    ["64b5b181-046f-5037-8595-fcf2ea049259", "Jacqueline M Landry"],
    ["329114e6-1dbc-5227-b149-74eb8d7468a1", "Gus Macriyanni"],
    ["1c0bf216-76cf-5444-ba1a-ac373bc715ae", "Carl D Marshall"],
    ["29281682-12ea-5516-9434-4cbc05741a99", "Constantine Papadopoulos"],
    ["26117ce0-c1d9-5bf3-a036-63c23c6b868e", "Lawrence N Stevens"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }
});

test("Batch 046 separates student status, a named employer, an earlier government assignment, and an unnamed employer", async ({
  page,
}) => {
  await page.goto("./people/5a8ea4f7-acc3-5a6f-8bca-c4de1746cc49/");
  await expect(
    page.getByRole("heading", { name: "S D Cater Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", { name: "A Tribute to Douglass Cater", exact: true })
      .first(),
  ).toHaveAttribute("href", /congress\.gov/);

  await page.goto("./people/0413c4b8-fd84-5f0f-b0b7-b6d0651b66a6/");
  await expect(
    page.getByRole("heading", { name: "Marshall W Houts", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Eastern Air Lines", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Eastern Air Lines", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Federal Bureau of Investigation",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Garrison Investigation of Kennedy Assassination: Marshall Wilson Houts",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /archives\.gov/);

  await page.goto("./people/5bc32ab9-22d4-5f2f-ada5-25ec431c6181/");
  await expect(
    page.getByRole("heading", { name: "Jane Lester", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("a brokerage in Buffalo");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("a brokerage in Buffalo");
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).not.toContainText("Merrill Lynch");

  for (const terminalProfile of [
    ["be18a8aa-49d3-5600-8d66-eae7b28afb78", "Millard A Copeland"],
    ["86a952a7-c08e-50b9-be06-fbcdb2af8f37", "Jacques Delmas"],
    ["83359650-6c9b-52c4-a60d-22de5ee4885e", "Grier Durant"],
    ["a66a0f48-fda1-5169-84f6-77fa0fd2acfa", "Shigekata Ikeda"],
    ["3c26f2a2-98c8-5a66-9455-ee7e70de8f83", "Jackson E Nordin"],
    ["b2d1f2ba-8862-5b16-b620-3ffbbd9c67d6", "Lucille E Temple"],
    ["2c5e78d0-84b4-5ccb-9604-40ebe233fc06", "Dorothy I Tolley"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(page.locator("body")).not.toContainText("14122318");
  }
});

test("Batch 047 publishes the 99th Infantry pathway and keeps nine names unresolved", async ({
  page,
}) => {
  await page.goto("./people/90851873-c347-5a03-a11f-fac184e844ae/");
  await expect(
    page.getByRole("heading", { name: "Olaf H Aanonsen", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army, 99th Infantry Battalion (Separate)",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", { name: "10th Mountain Division Name Index", exact: true }).first(),
  ).toHaveAttribute("href", /denverlibrary\.org/);
  await expect(
    page
      .getByRole("link", {
        name: "Among the Firsts: Lieutenant Colonel Gerhard L. Bolland's Unconventional War",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /casematepublishers\.com/);
  await expect(page.locator("body")).toContainText("PVT");
  await expect(page.locator("body")).toContainText("Pfc.");
  await expect(page.locator("body")).toContainText("Cpl");

  for (const terminalProfile of [
    ["f8b9fde8-b58d-5008-a43c-6306f5e79dd8", "Sigurd J Aalbu"],
    ["c0207d96-2125-5ebe-ba47-1e1fba48c9f7", "Helen G Abbenante"],
    ["271bfa40-ff5a-5ab2-8382-bc7e02036d7c", "Charles R Abele"],
    ["ddd74408-e908-507d-b288-cd5cdf380b0e", "Herbert A Abele Jr."],
    ["010bc8e2-5848-5363-ba32-80e5a119c703", "Norman W Abendschein"],
    ["cb7a4651-b52c-5555-baee-f5a76dbd104c", "Michael K Abraham"],
    ["c33df873-b7d9-5f77-aa01-ad5ae4effe3e", "Alexander A Abromaitis"],
    ["24dc19da-1915-55b1-8331-e3f8b54d3c94", "Salvatore H Acampora"],
    ["6042194f-2110-58d4-a4ff-0b7f5e9aa6df", "John Achelis"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    expect(await page.locator("body").innerText()).not.toMatch(/\b\d{6,8}\b/);
  }
});

test("Batch 048 separates immediate military pathways, civilian employers, and earlier affiliations", async ({
  page,
}) => {
  await page.goto("./people/fe42994f-c24f-5ccd-877f-d4f19ce8339f/");
  await expect(
    page.getByRole("heading", { name: "Moses Abrahamovitz", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "National Bureau of Economic Research",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "War Production Board", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("Moses Abramovitz", { exact: false }).first()).toBeVisible();

  await page.goto("./people/d1d45462-bcb9-52d7-9744-8424b27d6480/");
  await expect(
    page.getByRole("heading", { name: "Albert Abrahamson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "National Refugee Service", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Bowdoin College", exact: true }),
  ).toBeVisible();

  await page.goto("./people/06b73b73-212c-5b38-8b59-eea4cb7ee257/");
  await expect(
    page.getByRole("heading", { name: "Allen Abrams", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Marathon Corporation", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();

  await page.goto("./people/38c62333-9630-5fe8-a014-401f8f1350a0/");
  await expect(
    page.getByRole("heading", { name: "Vincent A Abrignani", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText(
    "No reviewed claim currently meets the publication threshold.",
  );
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "71st Infantry Regiment, New York National Guard",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{6,8}\b/);
});

test("Batch 049 preserves an incomplete printed name and routes ten unresolved common-name cases to Box 1", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["611c81b3-54a7-5c1a-a233-6c6b9581ef5a", "Caf-3 E Aaberg"],
    ["0a389c36-5a98-5e04-9053-d608250a5f56", "Frank Abbote"],
    ["d315b651-4752-55ba-b732-6df89544609e", "John A Abbote"],
    ["3ffe31e6-0f44-5270-b7cf-c688ebc7d1f2", "Delbert H Abbott"],
    ["beec8347-ccd6-50df-87d9-07e07622fb7a", "Floyd H Abbott"],
    ["05ec6d1d-2196-59b9-8a64-4dc15c0e2fcc", "Frederick K Abbott"],
    ["324f3b70-e14c-5391-bc98-cff4f2605d7a", "James E Abbott"],
    ["73e33700-fdae-5574-879a-17b36c017efc", "James F Abbott"],
    ["29abc44d-1bd9-52be-a4ef-d32d07d3841c", "Norman Abbott"],
    ["58e53125-1044-5ff9-937a-b0fc08fe8629", "Robert J Abbott"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(page.locator("body")).toContainText("Box 1");
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/611c81b3-54a7-5c1a-a233-6c6b9581ef5a/");
  await expect(page.locator("body")).toContainText(
    "Aaberg | Caf-3 | E",
  );
  await expect(
    page.getByText("critical", { exact: true }).first(),
  ).toBeVisible();
});

test("Batch 050 routes ten unresolved Abbott-through-Achin records to their indexed archival boxes", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["7088db2a-da18-5a1a-b0fa-058c50d4f7be", "Victor J Abbott", "1"],
    ["9737ab8a-966a-5355-80ce-b0f97a19dcb1", "Robert V Abee", "1"],
    ["89d29fd5-4bac-55f4-9510-622853453a8e", "Arthur A Abel", "1"],
    ["f375230c-f337-5251-8d34-90c5b7dd72f0", "Calvin J Abel", "1"],
    ["ed582713-c52c-5745-8971-a742fafa17db", "John C Abel", "1"],
    ["bba65c39-e1b9-52a3-ad1b-8fa343f42104", "James D Abernathy", "1"],
    ["2b3188cd-9595-57ac-a4e9-ca10cc4293a0", "James K Abney", "1"],
    ["79a323b7-5075-5fb9-b98d-421a24460e07", "John H Achenbach", "2"],
    ["3ca8fbd1-b6d1-5ecd-9cb8-f99c7a42c3d9", "Edward C Acheson", "2"],
    ["c4771919-35b2-5e2c-9d5d-74a8c775cafe", "Paul P Achin", "2"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }
});

test("Batch 051 preserves ten unresolved Ackelmire-through-Acord profiles and their Box 2 review paths", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["c1462464-a46c-5e24-b15a-b7b483ccabb7", "John G Ackelmire"],
    ["90350c1a-b25a-58d4-b08d-32f7943e4f19", "Mignon S Acker"],
    ["3d951ae3-0734-5e18-97b3-08f369b7db7a", "Walter W Acker"],
    ["cc204427-a08d-543c-9daa-c325e4fb60cd", "Eugene L Ackerman"],
    ["bf12e4f7-95bf-57a5-baad-f680ed96eaa3", "Moris Ackerman"],
    ["c900291b-40fa-5219-adae-3fe78ff6abe9", "Benjamin R Ackerson"],
    ["d7effc9c-3f36-5e02-ad1c-31d469214fe5", "Julia E Ackert"],
    ["16ce1e2c-8ee1-520c-b134-da4ff94b747c", "Barbara H Ackles"],
    ["3d1db48a-f080-5d35-82b1-8d1f8d7fc834", "Lester W Ackley"],
    ["10010105-b843-5b2c-bd94-081b60bbccc2", "Joe F Acord"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("2", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/c1462464-a46c-5e24-b15a-b7b483ccabb7/");
  await expect(page.locator("body")).toContainText(
    "103d Infantry Division officer",
  );
  await expect(page.locator("body")).toContainText(
    "may be treated as pre-OSS without dated linkage",
  );
});

test("Batch 052 preserves grade and rank distinctions while routing ten Acosta-through-Adams profiles to archival review", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["ba724894-06f3-5fdc-b01a-c7e47c34e2bb", "Francis. J Acosta Jr.", "2"],
    ["fe2e1bff-6cb4-5b19-a02f-eb7a6e1d0c58", "Gilmore J Acosta", "2"],
    ["7e9a1132-887b-5fca-8377-31da1a7d4d87", "William L Acree", "2"],
    ["4bce82dd-9a96-519f-9c3b-26a9a4766100", "Doris D Adair", "3"],
    ["cf526949-0343-5e66-a95a-f69b08cb52c4", "Milo J Adair", "3"],
    ["62a14599-d3a6-5556-b032-6266601d4def", "Ben Adam", "3"],
    ["6fd2ad38-7b17-5ae0-9dc2-0e8861389bb0", "Allen G Adams", "3"],
    ["41bc6be2-00a7-5149-9867-0922b5671da4", "Alton G Adams", "3"],
    ["48ad393c-4ef0-55c2-ba41-fc67dc6e549f", "Andrew D Adams", "3"],
    ["9fd314c5-4ada-5e1d-8ea0-a54d8ceffc70", "Arthur F Adams", "3"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/7e9a1132-887b-5fca-8377-31da1a7d4d87/");
  await expect(page.locator("body")).toContainText(
    "Virginia Tech class-of-1942 lead only if the file supplies corroborating education or hometown evidence",
  );

  await page.goto("./people/6fd2ad38-7b17-5ae0-9dc2-0e8861389bb0/");
  await expect(page.locator("body")).toContainText("commissioned army officer");

  await page.goto("./people/41bc6be2-00a7-5149-9867-0922b5671da4/");
  await expect(page.locator("body")).toContainText("enlisted naval personnel");
});

test("Batch 053 publishes Donald Keith Adams's Duke pathway and preserves nine unresolved Adams profiles", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["acaa96ad-5242-565b-96e8-86f61e2966b7", "Carl Adams Jr."],
    ["382c6ec0-2199-5de7-9dd5-84553b44d400", "Cleva L Adams"],
    ["0fb0ed85-23e8-5e70-88e1-7e145efd917b", "Clyde J Adams"],
    ["8d630b07-b0dd-5474-aa0c-51bc67a57aa3", "Dean D Adams"],
    ["aea9b4ca-9944-502d-a468-92ce0430b349", "Diana M Adams"],
    ["a5c16d60-21b2-5ab2-80de-87bdcca90154", "Dorothea Adams"],
    ["bf16069b-79b0-5703-aae4-07478948d2aa", "Eula Adams"],
    ["5cd66f1a-75bd-5035-af52-2cbfeecc8da8", "George K Adams Jr."],
    ["8d137c21-161a-5c58-945c-9986b5e53331", "Glenn D Adams"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("3", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/c3eeda33-d44b-5791-9cb7-1a7f6953660e/");
  await expect(
    page.getByRole("heading", { name: "Donald K Adams", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Duke University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Duke University", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Associate Professor of Psychology and Psychiatry",
  );
  await expect(page.locator("body")).toContainText(
    "Black Mountain College 1943 Catalogue",
  );
  await expect(page.locator("body")).toContainText(
    "Adams, Donald Keith",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto("./people/8d137c21-161a-5c58-945c-9986b5e53331/");
  await expect(page.locator("body")).toContainText(
    "unlinked 1941 Dallas directory copywriter lead",
  );
});

test("Batch 054 preserves ten common-name Adams cases and their Box 3 or Box 4 archival routes", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["5cdfcf25-c06d-5dc6-a352-07307ebc2bff", "James T Adams", "3"],
    ["93e94718-f1a9-5824-9887-1c0d601d79d7", "John H Adams", "3"],
    ["f1a4c3b6-0d4b-519b-8fb7-4935911e56fd", "Lou A Adams", "3"],
    ["6b352679-550a-5c4d-bd0e-9e4b85f2b2d4", "Paul Adams", "3"],
    ["62a30117-937c-570d-99a4-dce86c19cc30", "Phillip Adams", "3"],
    ["02eb8833-34f7-553c-857e-0fbb16dcd2fa", "Robert E Adams", "4"],
    ["90ec5a1a-02e9-56fc-b9d7-ad8bd8d3a375", "Ruth D Adams", "4"],
    ["cc1f026b-d636-56e9-a487-4f95aee46c92", "Sidney M Adams", "4"],
    ["0d873fa4-51aa-5d01-9262-ca773bfe985e", "Thomas F Adams", "4"],
    ["6b9e3edd-e0ce-5389-8798-4e10375db04e", "Willard A Adams", "4"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/0d873fa4-51aa-5d01-9262-ca773bfe985e/");
  await expect(page.locator("body")).toContainText(
    "Adams, McEntee & Co. photograph-file lead",
  );

  await page.goto("./people/02eb8833-34f7-553c-857e-0fbb16dcd2fa/");
  await expect(page.locator("body")).toContainText(
    "commissioned army officer",
  );
});

test("Batch 055 publishes Kenneth Addicott's qualified museum-to-Army pathway and preserves nine archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["732a3de7-b0e6-55c8-bb90-cdfa67dd31e4", "William T Adams"],
    ["3b303694-f915-5ce2-a751-deb3bd1e8141", "William C Adams"],
    ["84dab33f-b0ca-5653-ad78-0bff0a4761db", "William H Adams"],
    ["90f35664-6ee8-5d77-b53c-f021b8af6bd8", "William M Adams"],
    ["fa18617b-bcc0-5bfc-bb68-32c32a3d1c31", "William N Adams"],
    ["0578df03-5bbb-50e8-b779-d38f3ac1b463", "William S Adams Jr."],
    ["9302c6da-895c-592a-bdf5-f9e6b1a15119", "Pinckney J Adamson"],
    ["58350381-05c5-53d1-837c-fe5110f2e858", "Salvatore S Adelfio"],
    ["c0440f07-59ab-552a-b50b-66d74c0e2c3d", "Reginald Adeling"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("4", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/35c4500e-4d99-5938-8cb2-e144a144161d/");
  await expect(
    page.getByRole("heading", { name: "Kenneth K Addicott", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "American Museum of Natural History",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "transfer sequence remains unconfirmed",
  );
  await expect(page.locator("body")).toContainText(
    "The Development of Pedagogical Authority Through Teacher Programs",
  );
  await expect(page.locator("body")).toContainText(
    "CIA's Clandestine Services: Histories of Civil Air Transport",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);
});

test("Batch 056 publishes Burton Adkinson's qualified university role, corrects Sonia Adelson's normalized name, and preserves nine archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["7a02160d-6ed8-55ed-a161-b61b5d12a038", "George W Adelman"],
    ["4210a353-de81-5116-aa10-f524e35f3289", "Ivan J Adels"],
    ["190ca40e-d78b-52dc-94fe-09e8d4b0d525", "Ruth M Adels"],
    ["4e7dd907-82f6-55be-aa57-fc8f83c4b856", "Sonia Adelson"],
    ["edf8ab5d-3c41-56ef-a28b-3e1259e0f367", "Dean J Adinamis"],
    ["9094f471-2cd5-563f-8616-94ad5d74e86c", "John C Adison"],
    ["808803cf-80aa-525b-9c82-f9729760a582", "Glenn J Adkins"],
    ["12715fea-b544-5d75-8d5f-ed81e21a7dd4", "Robert S Adkins"],
    ["9242df8a-bd16-57ab-90be-9b5dc025ebbf", "Carmen G Adkisson"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("4", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/4e7dd907-82f6-55be-aa57-fc8f83c4b856/");
  await expect(
    page.getByRole("heading", { name: "Sonia Adelson", exact: true }),
  ).toBeVisible();
  await expect(page.locator(".profile-aside")).toContainText(
    "civilian professional or administrative grade",
  );
  await expect(page.locator(".index-record").first()).toContainText(
    "Adelson | Sonia | P-2",
  );

  await page.goto("./people/a0aa49cd-76c2-53dd-ac35-1165231cd008/");
  await expect(
    page.getByRole("heading", { name: "Burton W Adkinson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByText("documented prewar employer found", { exact: true })
      .first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "University of Washington",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).toContainText(
    "last documented civilian employer found before his wartime OSS service",
  );
  await expect(page.locator("body")).toContainText(
    "University of Washington General Catalog, 1942-1943",
  );
  await expect(page.locator("body")).toContainText(
    "Assistant Chief of the Map Intelligence Section",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto("./people/edf8ab5d-3c41-56ef-a28b-3e1259e0f367/");
  await expect(page.locator("body")).toContainText(
    "whether the Fitzsimons T/5 is Dean J. Adinamis",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText(
    "T/5 Dean Adinamis",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText(
    "T/5 Dean Adinamis",
  );
});

test("Batch 057 distinguishes student and religious affiliations from employers and preserves eight archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["01de5ef4-3268-54f6-a94a-2e9bd7b27656", "F P Adler", "4"],
    ["1a769a5a-6e0f-5bef-9f4f-b078efd23f9f", "Maxine Adler", "4"],
    ["a2ba8347-2109-5194-9137-5154419b1f37", "Louis D Adlon", "4"],
    ["30c9db1e-d89a-5917-bfd6-8d9d94be411a", "Alex C Adrian", "4"],
    ["ed266912-fe51-5dd7-b939-f2174a5debdc", "Leonard Adrian", "4"],
    ["ba040b97-398e-5ce2-b5df-36e4dec1c596", "Demetra Aeton", "5"],
    ["a5f8c0c0-32e0-50b1-abf3-1c780d395b08", "Percy C Afferton", "5"],
    ["533cb41c-e235-5aa3-85f6-9ef0bc73f908", "Nehmet Aga-Ogla", "5"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/ae2ce160-ad06-54e0-9fa5-31809c7c80ea/");
  await expect(
    page.getByRole("heading", { name: "Ernest H Adolph", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Cornell University", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "this is a student affiliation, not an employer finding",
  );
  await expect(page.locator("body")).toContainText(
    "served in the OSS (MO) from 1943 until 1945",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto("./people/d9b0c480-badf-50cc-9ba2-24f4d4b6e037/");
  await expect(
    page.getByRole("heading", { name: "Merrill S Ady", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "American Presbyterian Mission",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "field agent in Secret Intelligence with U.S. Army Office of Strategic Services in China",
  );
  await expect(page.locator("body")).toContainText(
    "Merrill S. Ady, of the American Presbyterian Mission",
  );
});

test("Batch 058 publishes Aglione's Army pathway, confirms two roster identities, and preserves seven review cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["6002e291-755d-5b83-879b-2e05c1439854", "Frederick B Agee Jr."],
    ["303d483f-6fd7-5f76-9327-3d12020eaa33", "Susie W Agee"],
    ["fc892342-811c-5b16-8bcc-27c6ebf7bd08", "Athanas Aggo"],
    ["cbe852be-9d30-5eb2-b68f-58e3e3940c2c", "Cornelius R Agnew"],
    ["a42c8e38-18b0-5d29-bea7-f2c54255eac4", "Joseph A Agrillo"],
    ["e585e775-2188-5ece-b92c-123e15445a2d", "Antonio Agugliaro"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("5", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/931925ce-767a-5905-957c-7b1c32ba8d3f/");
  await expect(
    page.getByRole("heading", { name: "Albert H Agert", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("needs identity review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Albert Hippolyte Agert is a plausible candidate",
  );
  await expect(page.locator("body")).not.toContainText(
    "Special Operations Executive personnel file: Albert",
  );

  await page.goto("./people/9d0ea528-05c0-505f-a982-b4cb416e3abf/");
  await expect(
    page.getByRole("heading", { name: "Evangelo Ageloras", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Evangelo Agelopas");
  await expect(page.locator("body")).toContainText(
    "confirms identity and OSS service but not a pre-OSS affiliation",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);

  await page.goto("./people/e96a1c0e-6b4f-5736-b1e0-42179955dc2f/");
  await expect(
    page.getByRole("heading", { name: "Arthur J Agoritsas", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Technical Grade 5 Arthur J. Agoritsas",
  );
  await expect(page.locator("body")).toContainText(
    "sources print different enlisted-grade labels",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);

  await page.goto("./people/35afb022-93c2-532d-a08b-60ac54c81b9f/");
  await expect(
    page.getByRole("heading", { name: "Peter M Aglione", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "best-supported immediate pre-OSS affiliation was United States Army service",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "Entered the Army January 1941. Was recruited by Captain Bonfiglio and Lieutenant Daddario",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);
});

test("Batch 059 publishes Ahlstrom's qualified prewar faculty role and preserves nine archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["c6d95182-4820-5a22-b650-b6e9c3be2f25", "Pedgro J Aguirre"],
    ["47abd0de-8fa9-5285-8147-d02cb1c9578c", "German Agustini"],
    ["5d9d660a-6d35-554e-b01f-81f002f029a4", "Cornelius J Ahearn"],
    ["f7bdeada-d129-517f-b69d-dea4d5d9dbeb", "David Ahearn"],
    ["dca8ac2c-3fb0-5b2d-a36d-9f3904e8c5ae", "Margaret Ahearn"],
    ["153bb624-79ed-56ec-8b86-838f4059c4f8", "Leonard Ahern"],
    ["53bbd21a-a7ec-53f6-bb7f-25b78ee59160", "Philston Ahn"],
    ["d71ea9e1-88a5-58a6-b9da-4d9f73fa0cf9", "Kenneth E Ahola"],
    ["9424dece-0e80-5f8c-9db8-f18512bdd3bd", "Amedeo M Aiello"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(/^[56]$/, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/dc625dce-f632-5092-9329-bee6db98b005/");
  await expect(
    page.getByRole("heading", { name: "Alvida Ahlstrom", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "La Crosse State Teachers College",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("French faculty");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", { name: "La Crosse", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.e-yearbook.com/yearbooks/University_Wisconsin_La_Crosse_La_Crosse_Yearbook/1940/Page_28.html",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto(
    "./organizations/de9fc8b5-5d0a-5ca5-b39b-392da9358c3d/",
  );
  await expect(
    page.getByRole("heading", {
      name: "La Crosse State Teachers College",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Alvida Ahlstrom", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "other documented pre-OSS affiliation",
  );
  await expect(
    page.getByText("medium", { exact: true }).first(),
  ).toBeVisible();
});

test("Batch 060 preserves a transposed-name duplicate, publishes Aiton's earlier university employment, and routes eight archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["7cf7b3d0-1260-59c3-8543-1a39da5f4b43", "Salvatore Aiello", "6"],
    ["b9883af7-7ab7-5b23-b8c8-2dc9cf3ac401", "James A Aiken", "6"],
    ["0e575e76-5d33-5e19-af3f-1526fa8a5db0", "Estella L Aikman", "6"],
    ["766c0cd6-23f0-512e-a363-807eb7935812", "Alice Aird", "6"],
    ["382fb70e-490e-5777-b264-f3dac5764df7", "Gilbert S Aitken", "6"],
    ["69bee485-9cbc-5d03-a7a2-27bae3f5ab05", "Robert T Aitken", "6"],
    ["d23a902b-bb0c-561c-a783-e5f47f3b03ac", "Belle B Aizen", "6"],
    ["86d62ffb-cfba-560b-a832-82745d911dfd", "Christian Akeo Jr.", "7"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/00a094cd-16e2-50fa-9e0e-784a2a7af6e6/");
  await expect(
    page.getByRole("heading", { name: "Blogg Ainsworth", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("needs identity review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-02ab1d7dcdda");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.getByRole("link", {
      name: "Instructing for Dangerous Missions",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText("Not printed");

  await page.goto("./people/c4b9c664-cdcf-56e7-8bd1-eaa7d5c13a4a/");
  await expect(
    page.getByRole("heading", { name: "Ainsworth Blogg", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-02ab1d7dcdda");

  await page.goto("./people/05072153-d5a0-55b6-bac5-1137fdd9ed7b/");
  await expect(
    page.getByRole("heading", { name: "Arthur S Aiton", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .getByText("documented prewar employer found", { exact: true })
      .first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Instructor, later professor of Latin American history",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", {
      name: "Arthur Scott Aiton papers, 1922-1959",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://findingaids.lib.umich.edu/catalog/umich-bhl-85852",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("NR");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText("Not printed");

  await page.goto(
    "./organizations/4ee8a858-3cd1-5a2d-94a7-0d3c7a3fdb3a/",
  );
  await expect(
    page.getByRole("heading", {
      name: "University of Michigan",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Arthur S Aiton", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "other documented pre-OSS affiliation",
  );
  await expect(
    page.getByText("high", { exact: true }).first(),
  ).toBeVisible();
});

test("Batch 061 publishes Alacevich's Army and civilian pathways while preserving Akiya duplicate uncertainty and seven archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["9b737137-cbf1-50c6-a510-f90762ccf59a", "Ralph L Akers"],
    ["933cbc8e-758f-51de-90fc-afd7d32dba55", "Billie F Akin"],
    ["2cbd8128-5fd8-5fdc-809f-11fcaf5ab1c4", "James L Akins"],
    ["6d23abaa-4b18-5618-9894-f0f7c7a31be9", "Frank Akston"],
    ["8c7da31b-0eba-5815-8ba5-fa63095e229c", "William A Alaniva"],
    ["3f956b79-98aa-57e4-ab45-e5df31941bd6", "Eveline Alarie"],
    ["a01ddc82-c9c8-5e8a-a217-4de50349c27f", "Abraham A Albala"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("7", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  for (const duplicateProfile of [
    ["171a6449-3114-59a7-8611-b054d3676a0f", "Ichiro Akiya"],
    ["dd445e77-9239-566e-843e-1d3b6cd9a7dc", "Karl Akiya"],
  ]) {
    await page.goto(`./people/${duplicateProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: duplicateProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("probable", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("needs identity review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText("duplicate-7202f7a67b62");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold.");
    await expect(
      page.getByRole("link", {
        name: "Guide to the Karl Ichiro Akiya Papers",
        exact: true,
      }),
    ).toHaveAttribute(
      "href",
      "https://findingaids.library.nyu.edu/tamwag/tam_236/",
    );
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText("Not printed");
  }

  await page.goto("./people/75c1cabd-a7ee-5e01-ab6b-0c9f41b88fd3/");
  await expect(
    page.getByRole("heading", { name: "Manlio Alacevich", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "plumbing concern in New York",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Italian merchant marine", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: "OSS Board of Officers Report on OSS, Allied Armies in Italy",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://digitalcollections.hoover.org/internal/media/dispatcher/331573/full",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("T-3");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);
});

test("Batch 062 publishes Albarranc's qualified identity evidence and preserves ten archival employer gaps", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["e5d72093-b123-55f9-aba8-d9af1c62bfdd", "Adrien Albarranc"],
    ["d82519a0-b83e-5445-b0da-81dcecb34349", "Dorothy O Albaugh"],
    ["06fb1712-7f09-5eb9-b12d-1afebc411f0b", "Esten E Albaugh"],
    ["442cbb88-4bf5-59b7-afcd-a7535e88c8b1", "Louis G Albee"],
    ["77e3312f-c038-5100-89b4-b92130d7e0b5", "Strone F Albee"],
    ["0158c622-2129-5b00-aa5b-5b570e2acea7", "George E Albers"],
    ["d91f908a-1172-53ec-95c8-d9ce69b92128", "Allen D Albert"],
    ["3860d895-8a4d-5c8b-af05-6577c01b4a72", "Daniel L Albert"],
    ["52ed887a-ca4c-5c60-946a-8a3e7787c0d0", "Joseph H Albert"],
    ["252af520-cd0a-551a-8cf6-6109043a6275", "Paul Albertis"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("7", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/e5d72093-b123-55f9-aba8-d9af1c62bfdd/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "very likely the French resistance member",
  );
  await expect(
    page.getByRole("link", {
      name: "Dossiers des agents des réseaux de renseignement et d'évasion de la France combattante",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/2019-10/SHDGR_INV_28P4_DOSSIERS_DES_AGENTS_DES_RESEAUX_0.pdf",
  );
  await expect(
    page.getByRole("link", {
      name: "Liste des membres des Forces françaises libres (18 juin 1940 - 31 juillet 1943)",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://genealomaniac.fr/wp-content/uploads/2022/12/Liste-des-membres-des-Forces-francaises-libres-18-juin-1940-31-juillet-1943-.pdf",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("Capt");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText("Not printed");
});

test("Batch 063 publishes Albrecht's documented law-firm role while preserving nine archival pathways", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["279b4039-5923-592a-b7b1-8d6ea1b473d6", "Cecil V Albertsen", "7"],
    ["e962edf9-0d6e-54ae-97b8-280b423ba703", "Glen H Albertsen", "7"],
    ["a18dbffe-b1eb-5a6d-9879-c3655ddfac9f", "Esther M Albertus", "7"],
    ["22c74862-09a5-5164-83a5-cbef06415b6d", "Roy R Albin", "7"],
    ["6d30ca3c-3d2c-5448-b977-ed5bf4b06237", "Marion L Albinson", "7"],
    ["58432fd4-bec7-561d-a3a0-71fdf04f65e1", "Eric Albrecht", "7"],
    ["823cb958-8c06-5f9a-bb58-0efe08212ca1", "William T Albrecht", "8"],
    ["e7392c33-f858-5d66-b1c3-2c1a2e084ab7", "Walter B Albright", "8"],
    ["200fa6cd-d394-5224-8583-44d8fddfcf15", "William D Albright", "8"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/279b4039-5923-592a-b7b1-8d6ea1b473d6/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "probably represents the man of that exact name listed on a Ritchie Boys roster",
  );
  await expect(
    page.getByRole("link", {
      name: "The Ritchie Boys: A-C (Surnames)",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.theritchieboys.com/complete-roster/a-c-surnames",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("T/Sgt");

  await page.goto("./people/ba7fd863-ee1b-5753-b44f-c0df874bb178/");
  await expect(
    page.getByRole("heading", { name: "Ralph G Albrecht", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Peaslee, Brigham & Albrecht",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Office of Naval Intelligence",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "does not resolve whether the ONI assignment preceded or overlapped OSS service",
  );
  await expect(
    page.getByRole("link", { name: "In re Koch", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.leagle.com/decision/1940359116f2d2431297",
  );
  await expect(
    page.getByRole("link", {
      name: "Radio Warfare: OSS and CIA Subversive Propaganda",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.worldradiohistory.com/BOOKSHELF-ARH/History/Radio-Warfare-L-Soley-1989.pdf",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("LT COM");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText("Not printed");
});

test("Batch 064 separates four named employers, one occupation-only result, and five archival pathways", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["78230ad0-b028-5893-84d5-645fe419c705", "Leonard Alchevesky"],
    ["660601f4-86cc-5cba-97b5-636e35876491", "Romolo Alcini"],
    ["4a5be002-d66a-5b68-9de1-623febe1f094", "Joseph E Alderdice"],
    ["050102ea-9c92-5aa5-a46c-3cb55bb46692", "James A Alderman"],
    ["ac33ddf0-ee04-562a-aacf-fabba483cf1e", "Eleanor B Aldrich"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("8", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/660601f4-86cc-5cba-97b5-636e35876491/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: "Romolo (Ray) Alcini January 13, 1915 – August 7, 2012",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://gilroydispatch.com/romolo-ray-alcini-january-13-1915-august-7-2012/",
  );

  await page.goto("./people/8da17ef3-ba34-5295-bd70-7b96c7be0d4f/");
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Office of U.S. Representative William Miller",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Westminster School", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Deaths", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://archive.dartmouthalumnimagazine.com/article/1980/6/deaths",
  );

  await page.goto("./people/0454f7bb-99f3-53b8-9e60-b2b833da1e55/");
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Station WLW", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "China Press", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Station XMHA", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Radio: Radio and Asia", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://time.com/archive/6770516/radio-radio-and-asia/",
  );

  await page.goto("./people/1530dd3a-9413-5429-9812-2d4e51168aac/");
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "worked as a Spanish teacher at an unnamed high school",
  );
  await expect(
    page.getByRole("link", { name: "Espías vascas", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.euskonews.eus/zbk/262/espias-vascas/ar-0262001001C/",
  );

  await page.goto("./people/13bce197-4080-5012-b684-8c7f98887102/");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army Air Corps", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Texas Technological College", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: "Scholar, War Hero Gets French Highest Honor",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://scholar.lib.vt.edu/VA-news/VA-Pilot/issues/1995/vp951022/10220065.htm",
  );

  await page.goto("./people/4a5be002-d66a-5b68-9de1-623febe1f094/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: "Instructing for Dangerous Missions",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );

  await page.goto("./people/fea7a8f5-e743-5408-b18d-d324e6c481ff/");
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Aldis and Company", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("medium", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: "Board of Trustees Portraits, University of Chicago",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://photoarchive.lib.uchicago.edu/db.xqy?show=browse9.xml%7C233",
  );
});

test("Batch 065 documents Aldrich's Army pathway and routes nine unresolved profiles to Box 8", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["8a2af14d-c52b-5f88-a566-314cccf7b638", "Mary Aldrich"],
    ["5de49930-d55b-52cc-a7f5-316c7610083b", "Wilson H Aldrich"],
    ["1c7e6e19-bcc5-5b33-9f54-e470c0701439", "Thomas J Aldridge"],
    ["b2cce279-49d7-5a70-8bba-296a9287aaf6", "Arlene V Ale"],
    ["4d805c52-0062-56a9-801c-3d0f91712eaf", "Janice H Ale"],
    ["0e5e37d5-e2d7-58e9-a41c-83f604397785", "Albert W Alessi"],
    ["40598a68-9418-5fc7-8227-5987ac471891", "Frank J Alessi"],
    ["53b28c63-9a49-5ca2-a60d-bfe3e9042f05", "Humbert Alessi"],
    ["84348760-0c46-58bd-bdb5-77ccd79ef645", "Alexander Alexander"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("8", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/40ae0d59-f11e-5df2-ad1f-3777571f3195/");
  await expect(
    page.getByRole("heading", { name: "Harry S Aldrich", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "American Military Mission to China",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "United States Army Coast Artillery Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "served first in Army intelligence and then in the Office of Strategic Services in 1944",
  );
  await expect(
    page.getByRole("link", {
      name: "A Preliminary Who's Who of U.S. Army Military Intelligence",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.yumpu.com/en/document/view/30019693/a-preliminary-whos-who-of-us-army-military-intelligence",
  );
  await expect(
    page.getByRole("link", {
      name: "Congressional Record, 76th Congress, 3d Session, Volume 86, Part 8",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.govinfo.gov/content/pkg/GPO-CRECB-1940-pt8-v86/pdf/GPO-CRECB-1940-pt8-v86-12-1.pdf",
  );
});

test("Batch 066 routes the next ten Alexander profiles to Boxes 8 and 9 without promoting namesakes", async ({
  page,
}) => {
  const terminalProfiles = [
    ["a5a553a2-4f53-58c5-84f7-e19cdcb62526", "Arthur Alexander", "8"],
    ["f3f07a74-be28-552f-bde2-6e8fa018e55f", "Charles T Alexander", "8"],
    ["c2bf4f25-fb59-57de-a0b9-1d9e9e52683d", "Cletus S Alexander", "8"],
    ["36722c7e-159f-5147-ad5a-fc69e9e2d796", "Edna S Alexander", "8"],
    ["7d7f7acb-0ad1-5ef4-8c16-75dee09b3e03", "Eileen Alexander", "9"],
    ["5cd72df8-2e4a-5463-9d6a-8bfb58cb7043", "Guy Alexander", "9"],
    ["eb621a9e-cb52-590c-8562-80d19a9a0278", "Hubert Alexander", "9"],
    ["15dd449d-9819-5e2a-91fb-5cecca9532e6", "Jean E Alexander", "9"],
    ["0ebfbbc5-4711-5fd3-8ec5-46b5f2621f87", "Lawrence Alexander", "9"],
    ["09730c59-5bee-5e27-8abd-0a58d0340232", "Leonard Alexander", "9"],
  ];

  for (const [personId, displayName, box] of terminalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/f3f07a74-be28-552f-bde2-6e8fa018e55f/");
  await expect(page.locator("body")).toContainText(
    "commissioned naval officer",
  );
  await expect(page.locator("body")).toContainText("LT USN");

  await page.goto("./people/c2bf4f25-fb59-57de-a0b9-1d9e9e52683d/");
  await expect(page.locator("body")).toContainText(
    "Federal Works Agency lead",
  );
  await expect(page.locator("body")).toContainText(
    "before accepting or rejecting",
  );

  await page.goto("./people/09730c59-5bee-5e27-8abd-0a58d0340232/");
  await expect(page.locator("body")).toContainText(
    "test but do not assume the Texas candidate",
  );
});

test("Batch 067 confirms Spencer Alexander's OSS identity while preserving eight archival cases and Sidney Alexander's earlier research", async ({
  page,
}) => {
  const terminalProfiles = [
    ["73bad0d2-a349-56c8-a7fd-ccd9a2ce7065", "Leroy W Alexander"],
    ["130adbd1-17a1-517b-ab84-99b53681b2b7", "Leslie A Alexander"],
    ["e4d69062-21d2-55f7-ad26-e37ca4c71c8f", "Lynford T Alexander"],
    ["7d2032b6-01aa-5ed5-bea9-63ab7edc7698", "Michael R Alexander"],
    ["7da810bf-2fa6-5788-9e3e-05ac5ec0ac06", "Paul J Alexander"],
    ["46641654-7361-5500-bc78-0eaaed159310", "Peter Alexander"],
    ["0df6c0b2-292f-5441-a920-f30f1c2e8e4e", "Phyllis E Alexander"],
    ["eef40eb3-27c7-556d-8e20-afcd9b14e62f", "Thomas B Alexander"],
  ];

  for (const [personId, displayName] of terminalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("9", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/98755eac-69c3-5152-9878-3af3ebd73826/");
  await expect(
    page.getByRole("heading", { name: "Spencer L Alexander", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("high confidence");
  await expect(page.locator("body")).toContainText(
    "January 1945 OSS transfer request",
  );
  await expect(page.locator("body")).toContainText(
    "internal OSS assignment but not a pre-OSS affiliation",
  );
  await expect(
    page.getByRole("link", {
      name: "Request for Transfer of Personnel from SO-EF to SO-CBI",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://www.archives.gov/files/research/jfk/releases/104-10165-10134.pdf",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);

  await page.goto("./people/d38ec240-05df-5155-abc9-3ed54484ff5f/");
  await expect(
    page.getByRole("heading", { name: "Sidney S Alexander", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "National Bureau of Economic Research",
  );
  await expect(page.locator("body")).toContainText(
    "United States Office of Price Administration",
  );
});

test("Batch 068 confirms Alexatos's qualified Greek Battalion pathway and routes nine unresolved profiles to Box 9", async ({
  page,
}) => {
  const terminalProfiles = [
    ["259061e7-af4d-55f4-8cc3-d642397cbfa9", "Indigo Alfalfa"],
    ["e738b33c-db68-5d62-ad38-f22dcd32eb71", "Indalicico Alfaro"],
    ["81059752-a755-5fd0-9c0e-1d44fa9ce75b", "Guiseppe Alfieri"],
    ["de8da4dc-6d73-56bb-8b86-c6dd5e56ec12", "Marie L Alfonsi"],
    ["e634d38f-7008-5ce7-bb64-1e21028adf6d", "Everett P Alford"],
    ["5dbddf45-b7c6-52e1-a175-fd7cf633b3e1", "Howard Alford"],
    ["d184456c-4cf2-5c17-9529-dac765f2045f", "Hudson Alford"],
    ["84d4ff8a-59dd-5ab1-9a33-f982df196e08", "Mary I Alford"],
    ["a3477668-6677-5bfc-899f-d0e58b532058", "Hugh S Alger"],
  ];

  for (const [personId, displayName] of terminalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("9", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/b966a9bd-4588-52ea-bee6-053c0b7ac1bb/");
  await expect(
    page.getByRole("heading", { name: "James K Alexatos", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "122nd Infantry Battalion (Separate)",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "best-supported immediate pre-OSS assignment",
  );
  await expect(page.locator("body")).toContainText(
    "same-private-identifier James Kalexatos file in Box 388",
  );
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS civilian employer has yet been identified",
  );
  await expect(
    page.getByRole("link", {
      name: "10th Mountain Division Name Index",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://history.denverlibrary.org/sites/history/files/10th%20Mountain%20Division%20Name%20Index%20%281%29.pdf",
  );
  await expect(
    page.getByRole("link", {
      name: "OSS Behind the Lines in Greece",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://dokumen.pub/after-the-battle-behind-the-scenes-with-the-oss-in-greece-186.html",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);

  await page.goto(
    "./organizations/2405baa3-705e-5fce-9a65-25d343587817/",
  );
  await expect(
    page.getByRole("heading", {
      name: "122nd Infantry Battalion (Separate)",
      exact: true,
    }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Greek Battalion");
  await expect(
    page.getByRole("link", { name: "James K Alexatos", exact: true }),
  ).toBeVisible();
});

test("Batch 069 publishes Algrant's qualified 1941 Kolynos evidence and routes nine profiles to archival review", async ({
  page,
}) => {
  const terminalProfiles = [
    ["5eabdf31-e4d4-5ce9-bd1d-f24631fd62c9", "Emma L Allan", "9"],
    ["14a93520-0b1e-5ce4-b2f8-ec656b47741f", "Lorna A Allan", "9"],
    ["4a9a5643-ea1d-5172-bf07-15d379ac9996", "Willard Allan", "9"],
    ["b7013b65-d071-5302-a00a-c6462f3b9be3", "William J Allanson", "10"],
    ["66d373cf-5524-5bfc-90a8-3246d7337423", "Albert Allart", "10"],
    ["bc64e5ec-65bb-5106-8d84-ec5824990c0e", "Lewis G Allbee", "10"],
    ["f1e663cc-0fa8-594c-a2f8-d19bd1a202a8", "Roy J Allemand", "10"],
    ["4faac446-39d3-59a4-99c4-ee0184a290c3", "Alice L Allen", "10"],
    ["24d61c71-72ab-503f-86a3-42b41395401f", "Amory L Allen", "10"],
  ];

  for (const [personId, displayName, box] of terminalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/14a93520-0b1e-5ce4-b2f8-ec656b47741f/");
  await expect(page.locator("body")).toContainText(
    "intended 'see also' cross-reference",
  );

  await page.goto("./people/bc64e5ec-65bb-5106-8d84-ec5824990c0e/");
  await expect(page.locator("body")).toContainText("commissioned naval officer");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);

  await page.goto("./people/5a520c84-b6d7-510a-ae97-8882b7fa8d4c/");
  await expect(
    page.getByRole("heading", { name: "Victor Algrant", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "The Kolynos Company", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "senior employee, export department",
  );
  await expect(page.locator("body")).toContainText(
    "Kolynos is not yet established as the immediate or last civilian pre-service employer",
  );
  await expect(
    page
      .getByRole("link", { name: "Bohemia, April 13, 1941", exact: true })
      .first(),
  ).toHaveAttribute("href", "https://ufdc.ufl.edu/UF00029010/00395");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText("Not printed");

  await page.goto(
    "./organizations/46c9d843-7983-5c67-9973-aa358dbb44d2/",
  );
  await expect(
    page.getByRole("heading", { name: "The Kolynos Company", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("The Kolynos Co.");
  await expect(
    page.getByRole("link", { name: "Victor Algrant", exact: true }),
  ).toBeVisible();
});

test("Batch 070 routes the contiguous Carol F Allen through Hanceford D Allen sequence to Box 10 review", async ({
  page,
}) => {
  const terminalProfiles = [
    ["ac953480-aeef-5daa-b318-0ed49e90bfda", "Carol F Allen"],
    ["6903433c-6412-51d1-8b84-88d7a6b269d1", "Charles L Allen"],
    ["b51d7472-5509-59cb-96ee-a8a14e9ea496", "Desrae M Allen"],
    ["cf662ef0-3af6-5ed1-92a6-41e27c53f901", "Edward W Allen"],
    ["6e22c576-df04-58db-9715-43870771cbab", "Elisa M Allen"],
    ["a6cad3a2-9054-5f90-886a-2c4da6ca6c61", "Everett T Allen"],
    ["a1f013a2-738f-5583-91f5-33886216ca4b", "Franklin G Allen"],
    ["0315f576-4256-5bef-b6e2-4e660f141d71", "Gilbert Allen"],
    ["e0574e79-7c5f-5fda-aae2-f0f3ed1fe53f", "Guy D Allen"],
    ["861237a0-e5a8-5de0-8bf6-cf6669844519", "Hanceford D Allen"],
  ];

  for (const [personId, displayName] of terminalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("10", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/a6cad3a2-9054-5f90-886a-2c4da6ca6c61/");
  await expect(page.locator("body")).toContainText("commissioned army officer");
  await expect(page.locator("body")).toContainText(
    "official officer records for Everett T. Allen",
  );

  await page.goto("./people/a1f013a2-738f-5583-91f5-33886216ca4b/");
  await expect(page.locator("body")).toContainText("commissioned army officer");
  await expect(page.locator("body")).toContainText(
    "test the 9th Infantry Division namesake",
  );

  await page.goto("./people/861237a0-e5a8-5de0-8bf6-cf6669844519/");
  await expect(page.locator("body")).toContainText(
    "distinguish the Florida namesakes",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);
});

test("Batch 071 publishes Hedvig Allen's qualified federal pathway and Keith Allen's corrected colonel identity while preserving eight archival cases", async ({
  page,
}) => {
  const archivalProfiles = [
    ["5b1182d0-87e7-5282-b1da-7d702acfd7cb", "Helen E Allen"],
    ["7058c510-df1f-5437-8043-34e0cf7d52a1", "Horace H Allen"],
    ["34ed1c86-e2d3-5d1f-a0cb-fdd1a11d682e", "Howard Allen"],
    ["0d87a330-3b5e-5b9d-a627-bdf1b474f916", "James L Allen"],
    ["cb6f0bb2-4361-5049-b9be-bfb375ee1560", "James T Allen"],
    ["61b9fdd4-e8c1-5772-8989-26ba67ac28c6", "Joel E Allen"],
    ["915fa417-f854-569a-87f1-53e37654247c", "Katherine E Allen"],
    ["e32db7e9-2c51-5e5f-ac37-8c207bfe940e", "Laura D Allen"],
  ];

  for (const [personId, displayName] of archivalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("10", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/5e239791-b869-5a67-86b1-35b10b2819f6/");
  await expect(
    page.getByRole("heading", { name: "Hedvig J Allen", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Bureau of Internal Revenue", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("explicit immediate");
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(
    page.getByRole("link", { name: "Washington DC", exact: true }),
  ).toHaveAttribute(
    "href",
    "https://libertyladybook.com/2009/10/25/washington-dc/",
  );

  await page.goto("./people/5daf22ac-a7cf-520a-bdd4-c8a638b49ea8/");
  await expect(
    page.getByRole("heading", { name: "Keith Allen", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("commissioned army officer");
  await expect(page.locator("body")).toContainText("Keith Nichols Allen");
  await expect(page.locator("body")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(
    page.getByRole("link", {
      name: "OSS Monthly Activity Reports – September 1944",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100140011-7.pdf",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("Not printed");

  await page.goto(
    "./organizations/03e209a5-4ba3-5968-bce1-2f403d5b3458/",
  );
  await expect(
    page.getByRole("heading", {
      name: "Bureau of Internal Revenue",
      exact: true,
    }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Internal Revenue Service");
  await expect(
    page.getByRole("link", { name: "Hedvig J Allen", exact: true }),
  ).toBeVisible();
});

test("Batch 072 preserves ten Marian Allen through Thomas Allen profiles as explicit Box 10 archival-review outcomes", async ({
  page,
}) => {
  const profiles = [
    ["2526e75c-ed1d-5c00-ba97-59f30697afaf", "Marian A Allen", "civilian professional or administrative grade"],
    ["c5278a89-89e5-542c-b5eb-295fd1aeecdb", "Mary T Allen", "civilian professional or administrative grade"],
    ["fe52d758-d6dd-5890-bf81-b66c092e7b5e", "Mary P Allen", "unknown or indeterminate"],
    ["a1522ad7-e908-5254-919f-1e60db5e7f4b", "Max R Allen", "enlisted army personnel"],
    ["896a06b3-4871-57d1-aad5-cfb6f3d48060", "Pauline R Allen", "civilian professional or administrative grade"],
    ["71a249d3-1164-5ecb-8eac-1f3d8c940d7d", "Richard Allen", "enlisted army personnel"],
    ["8ff69a04-8eeb-5413-8383-7de861620d5f", "Robert A Allen", "enlisted army personnel"],
    ["495aa9af-662a-50d7-8666-cec55c81327d", "Robert M Allen", "commissioned army officer"],
    ["bb6e1cc1-a1ea-59b0-ac73-d16052e61064", "Terrell A Allen", "civilian professional or administrative grade"],
    ["3c626d49-6a3c-5a67-8f07-e00f296201ba", "Thomas B Allen", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(personnelCategory);
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("10", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/2526e75c-ed1d-5c00-ba97-59f30697afaf/");
  await expect(page.locator("body")).toContainText("Atlanta educator");

  await page.goto("./people/8ff69a04-8eeb-5413-8383-7de861620d5f/");
  await expect(page.locator("body")).toContainText(
    "Review Box 10 and official Army records",
  );

  await page.goto("./people/3c626d49-6a3c-5a67-8f07-e00f296201ba/");
  await expect(page.locator("body")).toContainText(
    "wartime personnel status",
  );
});

test("Batch 073 preserves ten Vernon Allen through John Alley profiles as explicit Box 10 or Box 11 archival-review outcomes", async ({
  page,
}) => {
  const profiles = [
    ["1486f9df-c968-5690-bd5e-a662996aa5a2", "Vernon C Allen", "enlisted army personnel", "10"],
    ["a4d21520-3273-5bfa-87ab-e220a9409e22", "Walter P Allen", "enlisted army personnel", "10"],
    ["066f8af2-ba44-5e37-9593-9af30d53a1ec", "William H Allen", "enlisted army personnel", "10"],
    ["78096fef-2ff5-5b78-8027-fe72cdbd854d", "Carey W Allender", "enlisted army personnel", "11"],
    ["2b0d3006-83c8-5ff4-9b0b-3ab105391217", "Josephine S Allenovitch", "civilian professional or administrative grade", "11"],
    ["340937e8-bf68-502d-ae29-e5d0ea2388fe", "Clifford O Allenson", "unknown or indeterminate", "11"],
    ["a4672508-2a68-52eb-95f5-2e12b7284dcf", "Richard M Allenson", "unknown or indeterminate", "11"],
    ["434a8e57-51d1-5039-ac23-18e740e0486a", "Arthur J Alley", "enlisted army personnel", "11"],
    ["b3aeac1f-0def-5a9d-bcfd-7320be81696c", "Dorothy G Alley", "civilian professional or administrative grade", "11"],
    ["ef113512-d2aa-561b-a723-3e601295dd76", "John N Alley", "commissioned army officer", "11"],
  ];

  for (const [personId, displayName, personnelCategory, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(personnelCategory);
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/a4d21520-3273-5bfa-87ab-e220a9409e22/");
  await expect(page.locator("body")).toContainText(
    "compare the Walter Paul Allen candidate only",
  );

  await page.goto("./people/2b0d3006-83c8-5ff4-9b0b-3ab105391217/");
  await expect(page.locator("body")).toContainText(
    "compare the Pennsylvania namesake only",
  );

  await page.goto("./people/a4672508-2a68-52eb-95f5-2e12b7284dcf/");
  await expect(page.locator("body")).toContainText(
    "inspect the 1946 newspaper image only",
  );

  await page.goto("./people/ef113512-d2aa-561b-a723-3e601295dd76/");
  await expect(page.locator("body")).toContainText(
    "official officer records",
  );
});

test("Batch 074 confirms Harry B Allinsmith's OSS identity and qualified Bell System history while preserving nine archival cases", async ({
  page,
}) => {
  const archivalProfiles = [
    ["3cf38fb5-59e8-5b24-8808-394a54226546", "Roy Alley", "enlisted army personnel"],
    ["a7e8c27f-73ad-5244-96f0-957e2f130d8a", "Vernon C Alley", "unknown or indeterminate"],
    ["adbd10c3-391c-560c-b0d1-db01770218c1", "William S Alley", "commissioned naval officer"],
    ["9937e6a3-4d8f-5cec-99a6-cfa4760255cc", "John E Allgood", "unknown or indeterminate"],
    ["10284525-45a3-5e62-afe4-89083d568249", "William E Allgrunn", "unknown or indeterminate"],
    ["9c363103-92ac-5105-832b-80c58ab200e6", "Jack B Allin", "unknown or indeterminate"],
    ["92314f9e-9ff9-54d9-a519-c11aa27af9da", "Dale D Allison", "commissioned army officer"],
    ["12f8a6a3-903e-5525-85df-4647ad0662ec", "George R Allison", "enlisted army personnel"],
    ["14e5d2da-f303-5736-9c2b-1579edaa08db", "James S Allison", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of archivalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(personnelCategory);
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("11", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/3cf38fb5-59e8-5b24-8808-394a54226546/");
  await expect(page.locator("body")).toContainText(
    "conflicting-identifier candidate",
  );

  await page.goto("./people/9c363103-92ac-5105-832b-80c58ab200e6/");
  await expect(page.locator("body")).toContainText("CSP P T");
  await expect(page.locator("body")).toContainText(
    "interpret the printed",
  );

  await page.goto("./people/13a8b947-166a-56ce-877b-8cad0e236f48/");
  await expect(
    page.getByRole("heading", { name: "H B Allinsmith", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Harry Bryan Allinsmith");
  await expect(page.locator("body")).toContainText(
    "chief of the Radio Intelligence Division",
  );
  await expect(page.locator("body")).toContainText("Bell System");
  await expect(page.locator("body")).toContainText("documented prewar");
  await expect(page.locator("body")).toContainText(
    "which Bell System subsidiary",
  );
  await expect(
    page.getByRole("link", { name: "OSS Orders, April 1944", exact: true }),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/readingroom/docs/CIA-RDP13X00001R000100140007-2.pdf",
  );
  await expect(
    page.getByRole("link", {
      name: "International Television Almanac 1956",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://www.worldradiohistory.com/Archive-International-Television-Almanac/1956/International-Television-Almanac-1956-1-Whos-Who.pdf",
  );

  await page.goto(
    "./organizations/4c98ac2c-db09-503d-8549-ecd3dfe83a23/",
  );
  await expect(
    page.getByRole("heading", { name: "Bell System", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "H B Allinsmith", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "does not silently merge or sequence the subsidiaries",
  );
});

test("Batch 075 publishes two qualified student pathways while preserving conflicting, ambiguous, and unresolved Ames-area identities", async ({
  page,
}) => {
  const archivalProfiles = [
    ["dd877ae4-0ab2-58d9-9fbc-a3339fdf278a", "Dadus I Ambrose", "unresolved", "12"],
    ["86b5d7e1-81bb-50c2-8cb3-c2f1096893b6", "Peter Ambrose", "conflicting", "12"],
    ["0c2bb8b9-2238-5808-ad7d-bcc97bf6657b", "Charles J Amedia", "unresolved", "12"],
    ["9d245ea6-597a-502f-8d66-2ffd2f624e4b", "Ben Ames", "ambiguous", "13"],
    ["6c0947f8-3912-5967-84a4-c6d6d1bd1fa2", "Carlisle B Ames", "unresolved", "13"],
    ["94f06424-a050-5e59-ae18-6df7dfd717b8", "Mary F Ames", "unresolved", "13"],
    ["bcc28a15-416e-58b9-afb6-cf431cc454d9", "Robert Ames", "unresolved", "13"],
    ["5f372a4f-8d9e-5d63-834b-84c7fb9d770e", "Robert L Ames", "unresolved", "13"],
  ];

  for (const [personId, displayName, identityStatus, box] of archivalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText(identityStatus, { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/86b5d7e1-81bb-50c2-8cb3-c2f1096893b6/");
  await expect(page.locator("body")).toContainText(
    "private identifiers conflict",
  );
  await expect(page.locator("body")).toContainText(
    "do not merge",
  );

  await page.goto("./people/9d245ea6-597a-502f-8d66-2ffd2f624e4b/");
  await expect(page.locator("body")).toContainText(
    "common-name candidate cannot be linked without additional evidence",
  );

  await page.goto("./people/9edc4107-39d3-548a-bef0-71190419c03a/");
  await expect(
    page.getByRole("heading", { name: "Ruth G Amende", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Ruth Amende Rosa");
  await expect(page.locator("body")).toContainText("Brown University");
  await expect(page.locator("body")).toContainText("documented prewar");
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(
    page.getByRole("link", {
      name: "World Politics, Volume I, Number 4: The Contributors",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F68D0AEA3780085C3F7F6B7D3F935D26/S0043887100006493a.pdf/wpo_volume_1_issue_4_front_matter.pdf",
  );

  await page.goto("./people/f7bc5d97-4adb-513b-a38a-0c8c31c90588/");
  await expect(
    page.getByRole("heading", { name: "Harry T Ameredes", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Harry Theodore Ameredes");
  await expect(page.locator("body")).toContainText("Weir High School");
  await expect(page.locator("body")).toContainText(
    "undated start of his Weirton Steel career is not treated as pre-OSS employment",
  );
  await expect(
    page.getByRole("link", {
      name: "Harry Ameredes among 2014 inductees",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.weirtondailytimes.com/news/local-news/2014/04/harry-ameredes-among-2014-inductees/",
  );

  await page.goto(
    "./organizations/08d9f092-ff0b-5e6b-89d8-61c35e4ae90b/",
  );
  await expect(
    page.getByRole("heading", { name: "Weir High School", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Harry T Ameredes", exact: true }),
  ).toBeVisible();

  await page.goto(
    "./organizations/dfc9e35b-88f9-593d-874e-01edd9a69d7a/",
  );
  await expect(
    page.getByRole("heading", { name: "Brown University", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Ruth G Amende", exact: true }),
  ).toBeVisible();
});

test("Batch 076 preserves the Amigdalitis spelling variant and keeps all ten Ames-through-Amon employer outcomes unresolved", async ({
  page,
}) => {
  const profiles = [
    ["8f3dc2a1-afcf-5eb3-b86c-a001f55ee981", "Ruth Ames", "unresolved"],
    ["8b7493df-4959-5ab7-9485-5a2251c4f57a", "Redja B Ameyund", "unresolved"],
    ["c6628679-01ec-53ea-9919-ed1e737710d2", "William A Amick", "unresolved"],
    ["50c098e1-673c-5c26-b576-ee29807a78ef", "Paul Amico", "ambiguous"],
    [
      "b8ab801d-d4ac-536a-a32e-0364c1e4925e",
      "Nick J Amigdalitis",
      "high confidence",
    ],
    ["a08535b4-3957-5c75-b8cd-6df280044d0f", "Elizabeth W Amis", "unresolved"],
    ["4754d09e-877f-5023-96ab-c0b6e61530f7", "James Ammerman", "unresolved"],
    [
      "20d22be1-5c58-52ea-b0b9-fa595245be9d",
      "Richard C Ammerman",
      "unresolved",
    ],
    [
      "f4c82dd9-7c8c-5cd3-a080-ee22d32cefe4",
      "William R Ammon Jr.",
      "unresolved",
    ],
    ["004513db-369d-5f1f-8ba6-7b5c47fd3a6d", "Phillip J Amon", "unresolved"],
  ];

  for (const [personId, displayName, identityStatus] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText(identityStatus, { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("13", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/b8ab801d-d4ac-536a-a32e-0364c1e4925e/");
  await expect(page.locator("body")).toContainText("Nick J Amigdalitsis");
  await expect(page.locator("body")).toContainText(
    "Greek Operational Group",
  );
  await expect(page.locator("body")).toContainText(
    "does not itself establish a pre-OSS affiliation",
  );
  await expect(
    page.getByRole("link", {
      name: "Office of Strategic Services Operational Groups",
      exact: true,
    }),
  ).toHaveAttribute("href", "https://ossog.info/personnel.html");
  await expect(
    page.getByRole("link", { name: "Amigdalitsis Nick J.", exact: true }),
  ).toHaveAttribute(
    "href",
    "https://www.uswarmemorials.org/html/people_details.php?PeopleID=24636",
  );

  await page.goto("./people/50c098e1-673c-5c26-b576-ee29807a78ef/");
  await expect(page.locator("body")).toContainText(
    "candidates are not merged",
  );
  await expect(page.locator("body")).toContainText(
    "Do not publish the diner chronology without a unique linkage",
  );
});

test("Batch 077 separates Amoss's COI assignment from his last civilian employer and keeps weaker candidates qualified", async ({
  page,
}) => {
  const archivalProfiles = [
    ["aec91c5a-3a6d-5639-9278-6d2f0ae83254", "Vittorio Amoruso", "13", "ambiguous"],
    ["021dc894-630c-58fb-b4c8-0bab2db0e2ad", "[fnu] Amory", "13", "unresolved"],
    ["2c20b6e1-a163-5748-8e6d-9b5296f7645b", "John F Amory", "13", "unresolved"],
    ["215cd073-9134-567d-9f20-9d62baec8a59", "Harry A Amos", "13", "unresolved"],
    ["95330480-b981-5dc4-bd07-6953abe0b294", "Joseph D Amott", "13", "unresolved"],
    ["c2493a28-346b-5c4b-b6c9-6b53974f273e", "Emille W Amram", "14", "unresolved"],
    ["496f2f82-b44d-5d63-b04e-f9d71087d649", "Earl S Amspacher", "14", "ambiguous"],
    ["80353f69-feb0-54ca-b21f-daafb1dcb125", "Millicent V Amstrutz", "14", "unresolved"],
    ["8aaa698b-e4a7-56f8-b303-4ac0f06af8e2", "Sever B Amunrud", "14", "unresolved"],
  ];

  for (const [personId, displayName, box, identityStatus] of archivalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText(identityStatus, { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/aec91c5a-3a6d-5639-9278-6d2f0ae83254/");
  await expect(page.locator("body")).toContainText(
    "different grade",
  );
  await expect(page.locator("body")).not.toContainText("Ginny I working party");

  await page.goto("./people/2c0d50b2-1dfe-54fe-9310-cac56094b7a4/");
  await expect(
    page.getByRole("heading", { name: "Uliuss L Amoss", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Ulius Louis Amoss");
  await expect(page.locator("body")).toContainText(
    "Coordinator of Information",
  );
  await expect(page.locator("body")).toContainText(
    "Gramtrade International Corporation",
  );
  await expect(page.locator("body")).toContainText("government assignment");
  await expect(page.locator("body")).toContainText(
    "Last civilian employer before service",
  );
  await expect(
    page.getByRole("link", {
      name: "South Eastern European Section SA/B - SI: Review of Period December 1941 - March 1943",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /elia\.org\.gr\/userfiles\/pdf_archieve\//);
  await expect(
    page.getByRole("link", { name: "OSS Records", exact: true }),
  ).toHaveAttribute("href", "https://www.archives.gov/research/military/ww2/oss");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••[A-Z0-9]{4}$/);

  await page.goto(
    "./organizations/7717ee63-f94b-59b6-a06e-5b0f44350338/",
  );
  await expect(
    page.getByRole("heading", {
      name: "Coordinator of Information",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Uliuss L Amoss", exact: true }),
  ).toBeVisible();

  await page.goto(
    "./organizations/e7cfb64d-3379-5091-99c2-537478ef7726/",
  );
  await expect(
    page.getByRole("heading", {
      name: "Gramtrade International Corporation",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Uliuss L Amoss", exact: true }),
  ).toBeVisible();
});

test("Batch 078 publishes Anastos and Anbender's bounded pre-OSS evidence without promoting unresolved candidates", async ({
  page,
}) => {
  const archivalProfiles = [
    ["d8209b92-fafd-5c8a-a1e4-7639f4f1d114", "Richard P Amy", "unresolved"],
    ["50c86aa3-171d-5a70-b8d5-1d785ebfabb9", "John S Anacab", "unresolved"],
    [
      "48254a06-bcc0-52f8-b133-9790596ee101",
      "Christian B Anagnostis",
      "unresolved",
    ],
    ["8c55cdf4-03d1-5280-ab5b-30cca64404ef", "Ettore Anamia", "unresolved"],
    ["837eb17f-fd7d-57af-bd7b-f1b9e098e841", "Angelo Anastasio", "ambiguous"],
    ["654b9db0-c854-5423-8a0e-10c1a57b6de3", "Peter J Anastasio", "unresolved"],
    ["add9ec59-1846-5dbb-8f81-f680e774cd7a", "Stella Anastos", "unresolved"],
  ];

  for (const [personId, displayName, identityStatus] of archivalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText(identityStatus, { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("14", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/837eb17f-fd7d-57af-bd7b-f1b9e098e841/");
  await expect(page.locator("body")).not.toContainText("Camp Shelby");

  await page.goto("./people/831906a8-758d-5b32-b486-89321efda28e/");
  await expect(
    page.getByRole("heading", { name: "Milton V Anastos", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Harvard Divinity School Library",
  );
  await expect(page.locator("body")).toContainText(
    "Dumbarton Oaks Research Library and Collection",
  );
  await expect(page.locator("body")).toContainText("professional affiliation");
  await expect(
    page.getByRole("link", { name: "Librarians", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://library.hds.harvard.edu/about/mission-and-history/librarians",
  );
  await expect(
    page.getByRole("link", {
      name: "Saving the World, Part I: Dumbarton Oaks to Monuments Men",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://icfadumbartonoaks.wordpress.com/2014/02/10/saving-the-world-part-i-dumbarton-oaks-to-monuments-men/",
  );

  await page.goto("./people/c1e004f0-a1bb-5b4a-ad5a-83fbb0e6c883/");
  await expect(
    page.getByRole("heading", { name: "Harry H Anbender", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Office of Maurice Sugar, UAW counsel",
  );
  await expect(page.locator("body")).toContainText("professional affiliation");
  await expect(page.locator("body")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
  await expect(
    page.getByRole("link", {
      name: "United automobile worker (Detroit, Mich.), May 15, 1941",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.loc.gov/resource/42047197/1941-05-15/ed-1/?sp=5",
  );
  await expect(
    page.getByRole("link", {
      name: "Harry H. Anbender, Attorney, Dies at 46",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://digital.bentley.umich.edu/djnews/djn.1962.06.22.001/30",
  );

  await page.goto(
    "./organizations/4bdfb9fb-0342-504d-b2be-884706acd53a/",
  );
  await expect(
    page.getByRole("heading", {
      name: "Harvard Divinity School Library",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Milton V Anastos", exact: true }),
  ).toBeVisible();

  await page.goto(
    "./organizations/0fea8763-a2e6-5c1e-8fde-79545d8629b5/",
  );
  await expect(
    page.getByRole("heading", {
      name: "Dumbarton Oaks Research Library and Collection",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Milton V Anastos", exact: true }),
  ).toBeVisible();

  await page.goto(
    "./organizations/91537f19-0c8c-5805-a655-8a90cf625b43/",
  );
  await expect(
    page.getByRole("heading", {
      name: "Office of Maurice Sugar, UAW counsel",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Harry H Anbender", exact: true }),
  ).toBeVisible();

  await page.goto("./people/b9907bf8-4544-55fe-85a2-e99e9530df73/");
  await expect(
    page.getByRole("heading", { name: "Etienne Ancergues", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
});

test("Batch 079 keeps student affiliations, probable roster matches, and unresolved names in their evidentiary lanes", async ({
  page,
}) => {
  await page.goto("./people/f587a8be-f249-5625-8a4a-3f59fa90fefc/");
  await expect(
    page.getByRole("heading", { name: "Calhoun Ancrum Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Duke University");
  await expect(page.locator("body")).toContainText("student");
  await expect(page.locator("body")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
  await expect(
    page.getByRole("link", { name: "The Chanticleer, 1935", exact: true }).first(),
  ).toHaveAttribute("href", "https://lib.digitalnc.org/record/28578?ln=en");

  await page.goto("./people/0e45834f-eb80-5260-86f9-f290b7f429f9/");
  await expect(
    page.getByRole("heading", { name: "Donald E Anderegg", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Willamette University");
  await expect(page.locator("body")).toContainText("student");
  await expect(page.locator("body")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
  await expect(
    page.getByRole("link", { name: "Donald Anderegg Obituary", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.legacy.com/us/obituaries/seattletimes/name/donald-anderegg-obituary?id=28968382",
  );

  for (const [personId, displayName] of [
    ["672032f6-d1a1-5c3c-81a0-ad2ebf130713", "Harold Andersen"],
    ["720428a0-4b35-5db9-9be3-272eefce5c36", "Jorgen F Andersen"],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
    await expect(page.locator("body")).toContainText("Norwegian Operations");
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  const unresolvedProfiles = [
    ["e58d345c-cd2d-52f8-931b-165e4b07e824", "James T Ander", "ambiguous"],
    [
      "ea113558-ec12-5cd4-b403-b25235b4fb2e",
      "Frederick C Anderegg",
      "unresolved",
    ],
    ["edaa58b1-c9e6-5fcf-970b-94f1d1125ea4", "Ora V Anders", "unresolved"],
    ["930c290f-a194-5a8b-a2ae-d68e665e297e", "Erik J Andersen", "unresolved"],
    ["20129c34-8eef-5eb5-9160-3fc5666ce7d0", "Robert E Andersen", "ambiguous"],
    ["bfe9c69e-8a22-54c1-a855-b7baf79b2859", "Albert C Anderson", "unresolved"],
  ];

  for (const [personId, displayName, identityStatus] of unresolvedProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText(identityStatus, { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("14", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/e58d345c-cd2d-52f8-931b-165e4b07e824/");
  await expect(page.locator("body")).not.toContainText("AncientFaces");
  await page.goto("./people/20129c34-8eef-5eb5-9160-3fc5666ce7d0/");
  await expect(page.locator("body")).not.toContainText("Embassy Stockholm");

  for (const [organizationId, organizationName, personName] of [
    [
      "9b16d4bc-f90d-511c-b531-b39122733efe",
      "Duke University",
      "Calhoun Ancrum Jr.",
    ],
    [
      "58906d40-c25a-52a9-9459-2f09267c1857",
      "Willamette University",
      "Donald E Anderegg",
    ],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText("student");
  }
});

test("Batch 080 preserves ten Anderson records as distinct archival-review profiles without promoting namesakes", async ({
  page,
}) => {
  const profiles = [
    ["5911bece-15bb-53b4-9d5f-ef215827baf6", "Allen A Anderson", "14"],
    ["60ba20fe-adbd-56a4-83c2-01c0153ec7fd", "Alvina S Anderson", "14"],
    ["0819b0b8-6531-5e6b-9f1f-3c7a868d81c0", "Beatrice M Anderson", "14"],
    ["4cb42fa5-db79-55f3-ad4b-892d5cb31293", "Betty A Anderson", "14"],
    ["344df1b5-5f03-5c5f-914d-90ce51d3f02c", "Bruce I Anderson", "14"],
    ["636a515b-f1f4-52ed-9de5-b8152b7d0eba", "David F Anderson", "14"],
    ["86872e9e-9a0c-5c5d-933d-2b3a6a9d7d5d", "Donald Anderson", "15"],
    ["2a96a2c2-bd5c-5bc2-bebb-e31e0e9b7acc", "Dorothy M Anderson", "15"],
    ["86259d38-bb5c-5614-adc1-eb5972f21530", "Duane M Anderson", "15"],
    ["fe1acd6f-492c-5131-a843-b23aa7179ca8", "Erik J Anderson", "15"],
  ];

  for (const [personId, displayName, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/86259d38-bb5c-5614-adc1-eb5972f21530/");
  await expect(page.locator("body")).toContainText("C8M");
  await expect(page.locator("body")).toContainText("unknown or indeterminate");

  await page.goto("./people/636a515b-f1f4-52ed-9de5-b8152b7d0eba/");
  await expect(page.locator("body")).toContainText("commissioned army officer");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText(
    "Army Service Forces",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText(
    "Army Service Forces",
  );

  await page.goto("./people/2a96a2c2-bd5c-5bc2-bebb-e31e0e9b7acc/");
  await expect(page.locator("body")).not.toContainText("Artigas");
});

test("Batch 081 preserves the next ten Anderson records, classifications, and rejected namesakes", async ({
  page,
}) => {
  const profiles = [
    ["7b34674e-5b92-5b2e-9094-9a2f1824462b", "Eugene N Anderson"],
    ["2eaca631-8c19-5cc8-bc2b-ab158c650ebb", "Frederick F Anderson"],
    ["aa3d6bce-9b02-5c22-a4e6-3ba5b8518e9a", "George W Anderson"],
    ["49498285-8dcd-55af-b982-6a4638c5542d", "George H Anderson"],
    ["ad75ca9b-bf15-5822-9caa-dffa5a54b821", "Gordon Anderson"],
    ["9ee20707-4b4c-58c9-938c-2fecebb8c295", "Harold Anderson"],
    ["0933c1a8-4969-5651-9aec-779c495fdac7", "Henry A Anderson"],
    ["c19deb55-c954-579b-8c49-b6adcaec1617", "Henry J Anderson"],
    ["ed7968ad-9146-5129-b5ae-71257711b993", "Howard M Anderson"],
    ["1906df50-2028-51c5-b243-a6feaee8b94c", "Howard B Anderson"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("15", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/7b34674e-5b92-5b2e-9094-9a2f1824462b/");
  await expect(page.locator("body")).toContainText(
    "civilian professional or administrative grade",
  );
  await expect(page.locator("body")).not.toContainText(
    "Division of Cultural Cooperation",
  );

  await page.goto("./people/c19deb55-c954-579b-8c49-b6adcaec1617/");
  await expect(page.locator("body")).toContainText(
    "commissioned naval officer",
  );
  await expect(page.locator("body")).toContainText("Lt USNR");

  await page.goto("./people/9ee20707-4b4c-58c9-938c-2fecebb8c295/");
  await expect(page.locator("body")).not.toContainText("Ghost Army");
});

test("Batch 082 preserves ten common-name Anderson records without promoting rejected candidates", async ({
  page,
}) => {
  const profiles = [
    ["8fd5567f-d023-5d87-8b4c-7338aab9d14b", "Howell W Anderson"],
    ["a58cabcc-6d90-588c-985c-fc4356bdab32", "Jack W Anderson"],
    ["4b7f7799-a20f-5d06-a781-2f4fd2c45c71", "James F Anderson"],
    ["fc8904c4-0d17-5edc-aa9f-91571f7b0d67", "James R Anderson"],
    ["22bd3dcb-04fe-56b9-acb5-cff3962bb26d", "James T Anderson"],
    ["3a635a7a-518c-5a72-97dd-22a48b363316", "James W Anderson"],
    ["770688b5-266e-55bc-9999-6ad5edbc0cbe", "Jean R Anderson"],
    ["146c2532-3009-5bb8-ac4f-a2bcdd79c021", "Jean C Anderson"],
    ["c32c4c59-ef99-5d11-ad08-39d31af01d20", "John W Anderson"],
    ["3da80bac-7b92-5894-a711-94fb3c1c6151", "John H Anderson"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("15", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/4b7f7799-a20f-5d06-a781-2f4fd2c45c71/");
  await expect(page.locator("body")).toContainText(
    "civilian professional or administrative grade",
  );

  for (const personId of [
    "22bd3dcb-04fe-56b9-acb5-cff3962bb26d",
    "c32c4c59-ef99-5d11-ad08-39d31af01d20",
    "3da80bac-7b92-5894-a711-94fb3c1c6151",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "commissioned army officer",
    );
  }

  for (const [personId, rejectedOrganization] of [
    [
      "a58cabcc-6d90-588c-985c-fc4356bdab32",
      "Tennessee Valley Authority",
    ],
    [
      "fc8904c4-0d17-5edc-aa9f-91571f7b0d67",
      "1st Armored Division",
    ],
    [
      "3a635a7a-518c-5a72-97dd-22a48b363316",
      "8th Photographic Reconnaissance Group",
    ],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).not.toContainText(
      rejectedOrganization,
    );
  }
});

test("Batch 083 preserves ten Anderson records, unfamiliar grade text, and rejected namesake pathways", async ({
  page,
}) => {
  const profiles = [
    ["6724f419-1447-57f7-957c-fcfc21ec1f5d", "John K Anderson", "15"],
    ["b0e1a78b-9d87-5b75-b4e2-a7000d81b2c5", "Karl A Anderson", "15"],
    ["faa2bc5d-1631-57f6-acdd-13bbd1483775", "Katherine G Anderson", "15"],
    ["21bfae21-b3c8-5506-8a35-99e942a2de3e", "Kenneth A Anderson", "16"],
    ["b7895528-b8ff-5e9e-a1c4-02c9ddba82be", "Kermit W Anderson", "16"],
    ["baf854d8-3dab-54bf-8829-af5b98ca9def", "Kirk T Anderson", "16"],
    [
      "f9c40101-eaf0-523c-9782-45ef1ea7b997",
      "Lawrence A Anderson Jr.",
      "16",
    ],
    ["f5687802-0385-5e7a-82de-d0927d9c3a0d", "Leonard W Anderson", "16"],
    ["25b3753c-8804-50fc-a130-3c7c54e9f3db", "Loma J Anderson", "16"],
    ["241ec312-97e4-5ede-b096-311373b91d6a", "Margaret J Anderson", "16"],
  ];

  for (const [personId, displayName, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/6724f419-1447-57f7-957c-fcfc21ec1f5d/");
  await expect(page.locator("body")).toContainText("warrant officer");

  for (const personId of [
    "b0e1a78b-9d87-5b75-b4e2-a7000d81b2c5",
    "faa2bc5d-1631-57f6-acdd-13bbd1483775",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "civilian professional or administrative grade",
    );
  }

  await page.goto("./people/b7895528-b8ff-5e9e-a1c4-02c9ddba82be/");
  await expect(page.locator("body")).toContainText(
    "commissioned army officer",
  );

  await page.goto("./people/25b3753c-8804-50fc-a130-3c7c54e9f3db/");
  await expect(page.locator("body")).toContainText("WAE");
  await expect(page.locator("body")).toContainText(
    "unknown or indeterminate",
  );

  for (const [personId, rejectedOrganization] of [
    [
      "6724f419-1447-57f7-957c-fcfc21ec1f5d",
      "Polaroid Corporation",
    ],
    [
      "21bfae21-b3c8-5506-8a35-99e942a2de3e",
      "Seattle-Tacoma Shipbuilding",
    ],
    [
      "f5687802-0385-5e7a-82de-d0927d9c3a0d",
      "90th Infantry",
    ],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).not.toContainText(
      rejectedOrganization,
    );
  }
});

test("Batch 084 confirms Odd A Anderson while preserving nine unresolved common-name records", async ({
  page,
}) => {
  const unresolvedProfiles = [
    ["c4ca578f-411e-5804-8e5f-84c80eea84da", "Margaret M Anderson"],
    ["462f8ecf-692d-54d6-ae28-cab34d6c6a3e", "Marie J Anderson"],
    ["17b153ea-9da3-531e-b84d-85f78b47c508", "Marvin Anderson"],
    ["e350b6a5-8138-511f-a483-465c60e8e13b", "Merle G Anderson"],
    ["88d2b8a3-dba7-5b36-8b94-60b378a89385", "Naomi Anderson"],
    ["4132f822-0f77-5836-8fcb-205c2e97ad36", "Neal B Anderson"],
    ["4519ec54-2651-56c8-997d-ea0f49e34d0b", "Noel L Anderson"],
    ["97f1eefa-e5b6-53b4-889e-84bc86ad31b0", "Norbert P Anderson"],
    ["56964077-e79f-5d1e-9496-96661cf2d3f5", "Orval W Anderson"],
  ];

  for (const [personId, displayName] of unresolvedProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("16", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/4132f822-0f77-5836-8fcb-205c2e97ad36/");
  await expect(page.locator("body")).toContainText(
    "commissioned army officer",
  );

  for (const personId of [
    "e350b6a5-8138-511f-a483-465c60e8e13b",
    "88d2b8a3-dba7-5b36-8b94-60b378a89385",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "civilian professional or administrative grade",
    );
  }

  await page.goto("./people/255119c1-5c15-56f2-9d06-2681e1b2bfe3/");
  await expect(
    page.getByRole("heading", { name: "Odd A Anderson", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  const immediateSection = page.locator(
    'section[aria-labelledby="immediate-affiliation"]',
  );
  await expect(immediateSection).toContainText("Purdue University");
  await expect(immediateSection).toContainText("engineering student");
  await expect(immediateSection).toContainText("medium");
  await expect(immediateSection).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(page.locator("body")).toContainText(
    "Purdue is an educational affiliation, not an employer",
  );
  await expect(page.locator("body")).toContainText(
    "Masked serial suffixes assist orientation without publishing full service numbers",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••[A-Z0-9]{4}$/);

  for (const [personId, rejectedOrganization] of [
    ["17b153ea-9da3-531e-b84d-85f78b47c508", "Minnesota Legislature"],
    ["88d2b8a3-dba7-5b36-8b94-60b378a89385", "Fidelity National Bank"],
    ["4132f822-0f77-5836-8fcb-205c2e97ad36", "Fort Snelling"],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).not.toContainText(
      rejectedOrganization,
    );
  }
});

test("Batch 085 keeps ten Anderson identities unresolved and separates the two Robert J records", async ({
  page,
}) => {
  const profiles = [
    ["62f6a3cb-412a-596f-9f6a-e63358164d1c", "Otto E Anderson"],
    ["c57f322a-e173-5676-a59d-37414758707d", "Paul R Anderson"],
    ["790ea751-912f-588a-86b3-778909cb1232", "Pauline M Anderson"],
    ["5623a296-5f1f-50e0-9c7b-d0fd24031f71", "Ralph J Anderson"],
    ["cdb32c7c-0d49-5bba-973b-d7626961584f", "Richard F Anderson"],
    ["8ad974bf-1e49-5978-b01a-6ddde5995bed", "Robert J Anderson"],
    ["7053bcc8-262c-5ad1-b723-c34a44759e66", "Robert J Anderson"],
    ["8d30ac3c-8f49-527f-8fa5-45bc86dda44c", "Robert N Anderson"],
    ["ec0021ac-0d33-5ca5-b5b7-281fcd2ea799", "Robert E Anderson Jr."],
    ["8761a4bd-4465-5796-bc7b-e4563a84bd69", "Shirley J Anderson"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("16", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/cdb32c7c-0d49-5bba-973b-d7626961584f/");
  await expect(page.locator("body")).toContainText(
    "commissioned army officer",
  );

  for (const personId of [
    "790ea751-912f-588a-86b3-778909cb1232",
    "8761a4bd-4465-5796-bc7b-e4563a84bd69",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "civilian professional or administrative grade",
    );
  }

  await page.goto("./people/5623a296-5f1f-50e0-9c7b-d0fd24031f71/");
  await expect(page.locator("body")).toContainText(
    "unknown or indeterminate",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••[A-Z0-9]{4}$/);

  await page.goto("./people/8ad974bf-1e49-5978-b01a-6ddde5995bed/");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("M/Sgt");
  await expect(page.locator("body")).toContainText(
    "separately from the adjacent Technical Sergeant file",
  );

  await page.goto("./people/7053bcc8-262c-5ad1-b723-c34a44759e66/");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("T/Sgt");
  await expect(page.locator("body")).toContainText(
    "separately from the adjacent Master Sergeant file",
  );

  await page.goto("./people/c57f322a-e173-5676-a59d-37414758707d/");
  await expect(page.locator("body")).toContainText(
    "later second-lieutenant OSS claimant",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 086 preserves unresolved cases, carries Andrade forward, and publishes Andreasen occupation only", async ({
  page,
}) => {
  const profiles = [
    ["89178551-82de-54a4-ab90-8f43dabc4543", "Stanley E Anderson"],
    ["89e4aa38-6be8-5d96-b2d6-904c021dfd6a", "Tom L Anderson"],
    ["94e8c1d6-c12f-550c-bdd8-4107e697e999", "Walter Anderson"],
    ["55dbb385-d33e-5c9e-969b-64eda93d560f", "William M Anderson"],
    ["d9e04433-fe98-5d2b-8326-7d98089f9a69", "Russell W Anderton"],
    ["d814bb3e-9a94-5d9f-b9d6-2f38767762fe", "Anna B Andes"],
    ["a3108672-b09f-554b-84ef-fb5fb6287d70", "Jean J Andoire"],
    ["2201ee7c-3d64-5672-b519-0aad4625d185", "Edna W Andrade"],
    ["a4193027-1c25-5bd7-8ba3-20dc32e68529", "George Andreas"],
    ["cc9f004b-27eb-50ab-9611-deadb51db884", "Knut Andreasen"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(/^(16|17)$/, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "89178551-82de-54a4-ab90-8f43dabc4543",
    "89e4aa38-6be8-5d96-b2d6-904c021dfd6a",
    "94e8c1d6-c12f-550c-bdd8-4107e697e999",
    "55dbb385-d33e-5c9e-969b-64eda93d560f",
    "d814bb3e-9a94-5d9f-b9d6-2f38767762fe",
    "a4193027-1c25-5bd7-8ba3-20dc32e68529",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/d9e04433-fe98-5d2b-8326-7d98089f9a69/");
  await expect(
    page.getByText("ambiguous", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No employer claim is published from the current lead",
  );

  await page.goto("./people/a3108672-b09f-554b-84ef-fb5fb6287d70/");
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Postwar publishing work is not treated as pre-OSS evidence",
  );

  await page.goto("./people/2201ee7c-3d64-5672-b519-0aad4625d185/");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Hecht Company");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Hecht Company");

  await page.goto("./people/cc9f004b-27eb-50ab-9611-deadb51db884/");
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("first mate");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 087 preserves ten unresolved Andrews-area records and the French rank abbreviation", async ({
  page,
}) => {
  const profiles = [
    ["041497c0-ebff-56a2-bbd2-fd76dadb3883", "Antony Andreopoulos"],
    ["887b87a9-6696-5bdd-a03e-2f4bc4dbe419", "Andre Andreu"],
    ["40d28dc3-09cf-54ff-ad8d-70db69fc853f", "Ethel N Andrew"],
    ["5e91eb71-2d51-50ae-9262-4d26ff6ace3f", "Edward W Andrews"],
    ["5597ea6a-21d0-573c-9049-8819c980170c", "Ernest F Andrews"],
    ["2e1561e3-b2ee-5b35-afac-e9c0f3f5cf5c", "Evelyn Andrews"],
    ["9e7a6428-3fc5-592a-bb4b-c4aa1c261efb", "George H Andrews"],
    ["f5d04df5-edb0-5f28-b942-b50df9bb8990", "Graydon L Andrews"],
    ["f3d6b186-44a8-5ce9-bcba-84c11539c7c8", "Horace Andrews"],
    ["8ef462f5-0ba0-5f60-91b1-7a3a1c64e031", "Lewis W Andrews Jr."],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("17", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/887b87a9-6696-5bdd-a03e-2f4bc4dbe419/");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("S/Lt");
  await expect(page.locator("body")).toContainText(
    "foreign or allied military personnel",
  );
  await expect(page.locator("body")).toContainText("French");
  await expect(page.locator("body")).toContainText(
    "the meaning of S/Lt in this record",
  );

  await page.goto("./people/40d28dc3-09cf-54ff-ad8d-70db69fc853f/");
  await expect(page.locator("body")).toContainText(
    "civilian professional or administrative grade",
  );

  await page.goto("./people/5e91eb71-2d51-50ae-9262-4d26ff6ace3f/");
  await expect(page.locator("body")).toContainText(
    "commissioned naval officer",
  );

  for (const personId of [
    "5597ea6a-21d0-573c-9049-8819c980170c",
    "9e7a6428-3fc5-592a-bb4b-c4aa1c261efb",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "commissioned army officer",
    );
  }

  for (const personId of [
    "f5d04df5-edb0-5f28-b942-b50df9bb8990",
    "8ef462f5-0ba0-5f60-91b1-7a3a1c64e031",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "enlisted army personnel",
    );
  }

  for (const personId of [
    "041497c0-ebff-56a2-bbd2-fd76dadb3883",
    "2e1561e3-b2ee-5b35-afac-e9c0f3f5cf5c",
    "f3d6b186-44a8-5ce9-bcba-84c11539c7c8",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "unknown or indeterminate",
    );
  }
});

test("Batch 088 separates Army pathways, student status, documented employment, and unresolved Andrews records", async ({
  page,
}) => {
  const profiles = [
    ["dcf4c9e2-e6fd-593b-904e-bb04214b46bf", "May E Andrews"],
    ["6acb10b5-d6dc-55fb-b237-eca5823d2a7f", "Reuben K Andrews"],
    ["a2f71631-f97a-52d5-a5cc-81dd5949053e", "Robert A Andrews"],
    ["ced21977-cb09-5555-9c9f-7fd3dea2735c", "Schofield Andrews Jr."],
    ["89894fa3-c88b-503e-bb1b-622eaad54beb", "Thomas K Andrews"],
    ["e313514c-a222-5bfd-bd94-44c6a33b341e", "Virgil Andrews"],
    ["33d953c6-10f0-51d6-ad3f-aa23c5fb7599", "William C Andrews"],
    ["600c12c5-1644-584c-a4ca-494bbaafc50e", "Mortimer Andron"],
    ["00af6aea-fe0a-5eb4-aedc-0cba4eb7c365", "Nicholas Andronovitch"],
    ["53933f8b-20ec-5302-9e84-66d324dbf69b", "Anthony N Andros"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(/^(17|18)$/, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "dcf4c9e2-e6fd-593b-904e-bb04214b46bf",
    "6acb10b5-d6dc-55fb-b237-eca5823d2a7f",
    "a2f71631-f97a-52d5-a5cc-81dd5949053e",
    "89894fa3-c88b-503e-bb1b-622eaad54beb",
    "e313514c-a222-5bfd-bd94-44c6a33b341e",
    "33d953c6-10f0-51d6-ad3f-aa23c5fb7599",
    "53933f8b-20ec-5302-9e84-66d324dbf69b",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/ced21977-cb09-5555-9c9f-7fd3dea2735c/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Harvard University");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("student");
  await expect(page.locator("body")).toContainText(
    "Harvard is not classified as his employer",
  );

  await page.goto("./people/600c12c5-1644-584c-a4ca-494bbaafc50e/");
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("University of Illinois Urbana-Champaign");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Assistant in Economics");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/00af6aea-fe0a-5eb4-aedc-0cba4eb7c365/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army G-2");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Military Liaison Officer in Jerusalem");
  await expect(page.locator("body")).toContainText(
    "military assignment, not a civilian employer",
  );
});

test("Batch 089 preserves ten unresolved Box 18 records and recognizes the printed S2 C naval grade", async ({
  page,
}) => {
  const profiles = [
    ["c0864814-5041-5f39-9df7-a1e2b8124362", "James H Andros"],
    ["e2fb1057-fef4-50a9-9ef9-2719b13a6ba8", "Frank J Androvich"],
    ["e308f5f9-02c2-5edc-b810-e22f98ef7bda", "Victor L Anduso"],
    ["370fb3f1-322a-5b56-b546-6ff48bd4b8c6", "Andrew A Anganes"],
    ["ad826d3d-a9aa-59eb-87fa-df13acc5b2ba", "Charles F Angell"],
    ["6801930e-1a9a-5b64-9175-d6ccc5463b48", "James B Angell"],
    ["c303f8d2-0b12-51f1-b619-2b2869f1ca5b", "Joseph Angello"],
    ["0772e56b-5951-5ad2-8a81-b202c4169bda", "Anthony G Angelo"],
    ["b309c520-72fe-570c-9380-419c077ca31d", "Nick Angelo"],
    ["2f0f6e2e-0ecf-5993-bb96-7a362c526e26", "Anthony G Angelos"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("18", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "c0864814-5041-5f39-9df7-a1e2b8124362",
    "e2fb1057-fef4-50a9-9ef9-2719b13a6ba8",
    "370fb3f1-322a-5b56-b546-6ff48bd4b8c6",
    "0772e56b-5951-5ad2-8a81-b202c4169bda",
    "b309c520-72fe-570c-9380-419c077ca31d",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "enlisted army personnel",
    );
  }

  await page.goto("./people/6801930e-1a9a-5b64-9175-d6ccc5463b48/");
  await expect(page.locator("body")).toContainText(
    "civilian professional or administrative grade",
  );

  await page.goto("./people/c303f8d2-0b12-51f1-b619-2b2869f1ca5b/");
  await expect(page.locator("body")).toContainText(
    "commissioned army officer",
  );

  for (const personId of [
    "e308f5f9-02c2-5edc-b810-e22f98ef7bda",
    "ad826d3d-a9aa-59eb-87fa-df13acc5b2ba",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(
      "unknown or indeterminate",
    );
  }

  await page.goto("./people/2f0f6e2e-0ecf-5993-bb96-7a362c526e26/");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("S2 C");
  await expect(page.locator("body")).toContainText(
    "enlisted naval personnel",
  );
});

test("Batch 090 publishes direct pathways, corrects status semantics, and preserves the Aglione duplicate review", async ({
  page,
}) => {
  const profiles = [
    ["e9a2525c-92be-5beb-a273-9ba91c872305", "Michael T Angelos"],
    ["700951e0-9c87-5832-bea6-1c36099236bb", "Nicholas A Angelos"],
    ["b45249d9-d982-5010-9ef8-7186544935f9", "Bert W Anger"],
    ["c7c7786a-a6e7-5f23-acd0-4223b21a94af", "Damiamo Angione"],
    ["2f189352-aabb-5d3e-899c-ffaafef19aad", "James Angleton"],
    ["577a8037-dac8-53f1-80ff-b79b4c9519c6", "James H Angleton"],
    ["858188bc-468f-5032-a857-b8575690d4db", "Frank E Anglim"],
    ["894a80ae-3c80-53da-b217-9599c8b524f6", "Peter M Anglione"],
    ["14964895-e765-57e5-a4e9-5269c341c49e", "Carlos J Angulo"],
    ["8d41903e-c9de-5390-8945-0be696dc465f", "Manuel R Angulo"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("18", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  await page.goto("./people/e9a2525c-92be-5beb-a273-9ba91c872305/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Petty Officer Michael Angelos");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/c7c7786a-a6e7-5f23-acd0-4223b21a94af/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Damiano Angione");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");

  await page.goto("./people/2f189352-aabb-5d3e-899c-ffaafef19aad/");
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).not.toContainText("verified employer found");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/577a8037-dac8-53f1-80ff-b79b4c9519c6/");
  await expect(page.getByText("verified employer found", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("National Cash Register Company");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("School of Military Government");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("American Chamber of Commerce in Italy");
  await expect(page.locator("body")).toContainText(
    "Have been connected with the National Cash Register Company",
  );

  for (const personId of [
    "700951e0-9c87-5832-bea6-1c36099236bb",
    "14964895-e765-57e5-a4e9-5269c341c49e",
    "8d41903e-c9de-5390-8945-0be696dc465f",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
  }

  for (const personId of [
    "b45249d9-d982-5010-9ef8-7186544935f9",
    "858188bc-468f-5032-a857-b8575690d4db",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  for (const personId of [
    "35afb022-93c2-532d-a08b-60ac54c81b9f",
    "894a80ae-3c80-53da-b217-9599c8b524f6",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.locator(".profile-aside").getByText(/^duplicate-/),
    ).toBeVisible();
  }

  await page.goto("./people/894a80ae-3c80-53da-b217-9599c8b524f6/");
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Preserve both source records",
  );

  await page.goto("./organizations/35f60594-c068-5fe5-8fbb-2f356b7b7df4/");
  await expect(
    page.getByRole("heading", { name: "National Cash Register Company", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "James H Angleton", exact: true }),
  ).toBeVisible();
});

test("Batch 091 publishes Antell's bounded civilian and naval pathways while preserving nine archival cases", async ({
  page,
}) => {
  const profiles = [
    ["8b09a2fc-7f0f-5197-b6dc-c91b68a6ba46", "Richard J Ankeny"],
    ["ffe784de-054b-5f9e-a6ed-832e3cb842c6", "Dorothy S Annan"],
    ["60d51c45-8202-5610-8b88-1d95ba6ff8a7", "Charles S Annell"],
    ["b549b41b-2786-57b4-a7c8-0b31393c67e2", "Jayne L Annis"],
    ["988dc29a-ccd4-51ee-b414-3362f507597e", "Juliet K Ansperry"],
    ["de6c72ba-ecff-5855-be19-29ea41e6f610", "Robert M Anstett"],
    ["af17890d-d914-590b-b814-a325f9c28525", "Bertel W Antell"],
    ["69ac8c22-d653-5010-b3cf-a3b256a33f86", "Earl K Anthony"],
    ["ed6e70be-3f3b-5e3e-8f0e-7c11884b9d7d", "Fred D Anthony"],
    ["e058c0a8-6c57-58a0-a3c3-98a6127677ae", "Kelly Anthony"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(/^(18|19)$/, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    expect(await page.locator("body").innerText()).not.toMatch(/\b\d{6,8}\b/);
  }

  await page.goto("./people/af17890d-d914-590b-b814-a325f9c28525/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "commissioned naval officer",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("U.S. Naval Training School at Cornell University");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Chemical Construction Company");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Personnel director");
  await expect(page.locator("body")).toContainText(
    "the exact employment end date is not stated",
  );
  await expect(page.locator("body")).not.toContainText(
    "Chemical Construction Corporation",
  );

  await page.goto("./people/de6c72ba-ecff-5855-be19-29ea41e6f610/");
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Coast Artillery Corps officer",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");

  await page.goto("./people/60d51c45-8202-5610-8b88-1d95ba6ff8a7/");
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  for (const personId of [
    "8b09a2fc-7f0f-5197-b6dc-c91b68a6ba46",
    "ffe784de-054b-5f9e-a6ed-832e3cb842c6",
    "60d51c45-8202-5610-8b88-1d95ba6ff8a7",
    "b549b41b-2786-57b4-a7c8-0b31393c67e2",
    "988dc29a-ccd4-51ee-b414-3362f507597e",
    "de6c72ba-ecff-5855-be19-29ea41e6f610",
    "69ac8c22-d653-5010-b3cf-a3b256a33f86",
    "ed6e70be-3f3b-5e3e-8f0e-7c11884b9d7d",
    "e058c0a8-6c57-58a0-a3c3-98a6127677ae",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./organizations/bfee0756-c3ee-5d48-a001-8d70a14ccc46/");
  await expect(
    page.getByRole("heading", { name: "Chemical Construction Company", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Bertel W Antell", exact: true }),
  ).toBeVisible();
});

test("Batch 092 publishes three bounded Greek Battalion pathways and preserves seven identity or archival-review cases", async ({
  page,
}) => {
  const profiles = [
    ["65677c39-0808-5010-96e3-32ddc1f55523", "Robert Anthony"],
    ["734d742c-a97a-5a3f-9e48-c86f97448d9d", "Ante E Antic"],
    ["5b905dae-587e-5d02-b97a-f7ae0ec69f81", "John F Antico"],
    ["52960160-a468-5dec-9c53-adc1d1e0272b", "Alan A Antik"],
    ["ee32afee-f301-5e06-aacd-fce55cf1f4b9", "Charles P Antinopoulos"],
    ["706754b3-4c4c-5357-8058-459a43e950cf", "Laurens L Antley"],
    ["51229779-a805-5c45-af79-06beb3d2ba25", "Grace R Antoinette"],
    ["192a8818-01c8-53a2-9e61-cf2e26a3fe5a", "Hannah Antolik"],
    ["36a2a3c0-7c97-5b0b-81f6-8cf59d53862f", "Peter G Anton"],
    ["1db6492d-92d0-552b-bf67-68a481339b9b", "James Antonakis"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("19", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    expect(await page.locator("body").innerText()).not.toMatch(/\b\d{6,8}\b(?!-)/);
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "65677c39-0808-5010-96e3-32ddc1f55523",
    "734d742c-a97a-5a3f-9e48-c86f97448d9d",
    "5b905dae-587e-5d02-b97a-f7ae0ec69f81",
    "706754b3-4c4c-5357-8058-459a43e950cf",
    "51229779-a805-5c45-af79-06beb3d2ba25",
    "192a8818-01c8-53a2-9e61-cf2e26a3fe5a",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./people/52960160-a468-5dec-9c53-adc1d1e0272b/");
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "probably the film technician credited by the American Film Institute",
  );
  await expect(page.locator("body")).toContainText(
    "do not supply the middle initial, an OSS personnel-file link, or a pre-OSS chronology",
  );

  for (const [personId, identityStatus] of [
    ["ee32afee-f301-5e06-aacd-fce55cf1f4b9", "confirmed"],
    ["36a2a3c0-7c97-5b0b-81f6-8cf59d53862f", "high confidence"],
    ["1db6492d-92d0-552b-bf67-68a481339b9b", "confirmed"],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText(identityStatus, { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("verified employer found", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "enlisted army personnel",
    );
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("122nd Infantry Battalion (Separate)");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("military assignment");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("strongly date bounded");
    await expect(page.locator("body")).toContainText(
      "does not state his personal transfer date",
    );
  }

  await page.goto("./organizations/2405baa3-705e-5fce-9a65-25d343587817/");
  await expect(
    page.getByRole("heading", { name: "122nd Infantry Battalion (Separate)", exact: true }),
  ).toBeVisible();
  for (const displayName of [
    "Charles P Antinopoulos",
    "Peter G Anton",
    "James Antonakis",
  ]) {
    await expect(
      page.getByRole("link", { name: displayName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 093 separates confirmed, qualified, occupational, military, and unresolved pathways", async ({
  page,
}) => {
  const profiles = [
    ["18861fa8-e7c8-5515-a8cc-7d61204107ca", "Charlote Antonelli", "19"],
    ["fef6c271-c8c8-5687-abd8-711bab4e3e71", "Anargyros Antonopoulos", "19"],
    ["231d2f77-05bb-59d4-b074-3dfb7730d1f6", "Anthony Antony", "19"],
    ["923a5ed8-6d70-58d7-8452-cbf3fbd05dc0", "Ivo Antunovic", "19"],
    ["038cb77b-0343-5a08-a616-7351308cd4ba", "Rudolf Anzbock", "19"],
    ["7611975b-3f56-50cf-929e-99252df7490f", "Dominic J Anzevino", "19"],
    ["eeffff8e-eb5b-5cc0-8636-70d7475fad63", "Kukuji Aoki", "20"],
    ["55597bcd-bb94-5723-b3de-1799e59ab107", "Harry E Apaar", "20"],
    ["af0b35d6-5d84-5a83-856e-357eb126d1a5", "Zumruth Apcar", "20"],
    ["3c406464-880e-58ad-8078-c1448ce0e41d", "Antranig Apkarian", "20"],
  ];

  for (const [personId, displayName, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "18861fa8-e7c8-5515-a8cc-7d61204107ca",
    "231d2f77-05bb-59d4-b074-3dfb7730d1f6",
    "eeffff8e-eb5b-5cc0-8636-70d7475fad63",
    "55597bcd-bb94-5723-b3de-1799e59ab107",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
  }

  for (const [personId, evidenceText] of [
    [
      "7611975b-3f56-50cf-929e-99252df7490f",
      "probably the Army veteran and OSS member described in a Vindicator family-history article",
    ],
    [
      "af0b35d6-5d84-5a83-856e-357eb126d1a5",
      "probably Ruth (Zumruth) Apcar",
    ],
    [
      "3c406464-880e-58ad-8078-c1448ce0e41d",
      "probably the military-age Fresno registrant",
    ],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("probable", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(evidenceText);
  }

  await page.goto("./people/038cb77b-0343-5a08-a616-7351308cd4ba/");
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("85th Mountain Infantry Regiment");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("strongly date bounded");
  await expect(page.locator("body")).toContainText(
    "busboy, screw-factory machinist, and hatmaker",
  );

  await page.goto("./people/fef6c271-c8c8-5687-abd8-711bab4e3e71/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("122nd Infantry Battalion (Separate)");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");

  await page.goto("./people/923a5ed8-6d70-58d7-8452-cbf3fbd05dc0/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "merchant sea captain commanding the steamship Sveti Duje",
  );
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Yugoslav Seamen's Club (New York)");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("professional affiliation");

  for (const [organizationId, organizationName, personName] of [
    [
      "03496176-10b8-5ed6-bd73-d96782f0107f",
      "85th Mountain Infantry Regiment",
      "Rudolf Anzbock",
    ],
    [
      "a2c18964-b826-5795-9ce3-1119c9b4e939",
      "Yugoslav Seamen's Club (New York)",
      "Ivo Antunovic",
    ],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 094 preserves indexed names while separating military, civilian, and unresolved pathways", async ({
  page,
}) => {
  const profiles = [
    ["ab3bebd4-2972-5c36-9c8c-c75b8f0ec8cd", "George F Apolito"],
    ["4895eddb-a4f5-5d9c-9ef0-ca255d1e0222", "Garcia E Aponte"],
    ["6e6e127e-360e-5073-90fb-07d33dcbd1e6", "Rache S Apostoi"],
    ["f903ff0f-5956-59ca-9087-ec9abcec8c66", "Jerry Apostolatos"],
    ["423e735c-ef0e-5bc0-b5da-96fe457fb4c2", "James M Apostolopoulo"],
    ["e7c1f891-9325-5fe4-b83c-b8c7c7e3fc29", "Timothy Apostolos"],
    ["2543f97c-c12d-54dd-b145-759d44d5e881", "Leonard Appel"],
    ["287101f3-3eb6-551a-b849-bd8f795648c3", "Donald A Appetrad"],
    ["feefe0b5-18ba-5834-bfa3-6381cee1f755", "Harold N Applebaum"],
    ["714aaa6a-f151-5038-812c-deb282cfbd36", "William Applebaum"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("20", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "4895eddb-a4f5-5d9c-9ef0-ca255d1e0222",
    "e7c1f891-9325-5fe4-b83c-b8c7c7e3fc29",
    "287101f3-3eb6-551a-b849-bd8f795648c3",
    "feefe0b5-18ba-5834-bfa3-6381cee1f755",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/ab3bebd4-2972-5c36-9c8c-c75b8f0ec8cd/");
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("OSS Lafayette team");
  await expect(page.locator("body")).toContainText(
    "no middle initial, private identifier, hometown, or civilian chronology",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/6e6e127e-360e-5073-90fb-07d33dcbd1e6/");
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Rache S Apostol");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("explicit immediate");
  await expect(page.locator("body")).toContainText(
    "entered the U.S. Army in September 1942",
  );
  await expect(page.locator("body")).toContainText(
    "assigned from Army service to OSS in September 1943",
  );

  for (const [personId, identityStatus, variant] of [
    [
      "f903ff0f-5956-59ca-9087-ec9abcec8c66",
      "high confidence",
      "Gerasimos Apostolatos",
    ],
    [
      "423e735c-ef0e-5bc0-b5da-96fe457fb4c2",
      "confirmed",
      "James M Apostolopoulos",
    ],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText(identityStatus, { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(variant);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("122nd Infantry Battalion (Separate)");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("military assignment");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("strongly date bounded");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/2543f97c-c12d-54dd-b145-759d44d5e881/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("explicit immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("National Labor Relations Board");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("strongly date bounded");

  await page.goto("./people/714aaa6a-f151-5038-812c-deb282cfbd36/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "commissioned marine corps officer",
  );
  for (const sectionId of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page.locator(`section[aria-labelledby="${sectionId}"]`),
    ).toContainText("Economy Grocery Stores Corporation");
  }
  await expect(page.locator("body")).toContainText(
    "1914 Economy Grocery Store founding and 1942 adoption of the Stop & Shop, Inc. company name",
  );

  await page.goto("./people/923a5ed8-6d70-58d7-8452-cbf3fbd05dc0/");
  await expect(page.locator("body")).toContainText(
    "Immediately before entering OSS, Antunovic was a captain in Yugoslavia's merchant marine",
  );
  await expect(page.locator("body")).toContainText(
    "the official record does not name his employer",
  );

  for (const [organizationId, organizationName, personName] of [
    [
      "ff44a1b8-3794-5839-bf93-0471ce4d5578",
      "National Labor Relations Board",
      "Leonard Appel",
    ],
    [
      "aa61a0c6-ad0a-51ab-9ba2-87f92a93794b",
      "Economy Grocery Stores Corporation",
      "William Applebaum",
    ],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
    if (organizationName === "Economy Grocery Stores Corporation") {
      await expect(page.locator("body")).toContainText(
        "the modern name is documented as a historical relationship, not substituted as Applebaum's employer",
      );
    }
  }
});

test("Batch 095 preserves printed grades and routes unsupported Appleton-through-Arbucci identities to archival review", async ({
  page,
}) => {
  const profiles = [
    ["576aa158-a1be-56a6-96fc-c6c536de6381", "Rex Applegate"],
    ["2be8dce7-b974-5b11-b996-57dc46527584", "John B Appleton"],
    ["f036030a-6d1f-5c89-8e55-2854b46ed497", "Margaret E Appleton"],
    ["a7636e46-c351-511c-bf45-a0f41b0c69e4", "Sabri Appolini"],
    ["b63ca3f5-ca5f-532c-bb7d-0addd15a29b9", "Carlo E Aprato"],
    ["ebabf95c-780b-53e5-b149-6b6def8dee4a", "Helene A Apt"],
    ["60c19781-302d-5f8a-8cde-853fcde15540", "Samuel P Aquilina"],
    ["11b358de-dab6-5ef5-875e-2abea9e9402e", "Joseph J Aquino Jr."],
    ["9e8a4cda-76de-5785-a59c-30458ebd585d", "Pedro J Aquirre"],
    ["caa2dfb6-d8bb-566b-bc98-5992b7049b05", "Louis F Arbucci"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("20", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of profiles.slice(1).map(([personId]) => personId)) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  for (const [personId, rankText, categoryText] of [
    [
      "ebabf95c-780b-53e5-b149-6b6def8dee4a",
      "Caf-3",
      "civilian professional or administrative grade",
    ],
    [
      "60c19781-302d-5f8a-8cde-853fcde15540",
      "Sgt USM",
      "unknown or indeterminate",
    ],
    [
      "11b358de-dab6-5ef5-875e-2abea9e9402e",
      "Pvt",
      "enlisted army personnel",
    ],
    [
      "9e8a4cda-76de-5785-a59c-30458ebd585d",
      "2nd Lt",
      "commissioned army officer",
    ],
    [
      "caa2dfb6-d8bb-566b-bc98-5992b7049b05",
      "T-5",
      "enlisted army personnel",
    ],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(rankText);
    await expect(page.locator("body")).toContainText(categoryText);
  }

  await page.goto("./people/9e8a4cda-76de-5785-a59c-30458ebd585d/");
  await expect(
    page.getByRole("heading", { name: "Pedro J Aquirre", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Pedro J Aguirre (search variant only)",
  );

  await page.goto("./people/a7636e46-c351-511c-bf45-a0f41b0c69e4/");
  await expect(page.locator("body")).toContainText(
    "basis for inclusion in the personnel index",
  );
  await expect(page.locator("body")).not.toContainText("Espionage");
  await expect(page.locator("body")).not.toContainText("Vittorio");

  await page.goto("./people/576aa158-a1be-56a6-96fc-c6c536de6381/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
});

test("Batch 096 separates Archbold's civilian livelihood from naval service and preserves unresolved Archer identities", async ({
  page,
}) => {
  const profiles = [
    ["20c1c1ab-1d97-5f48-9665-e1d1b64b53e8", "Carmela E Arcaro"],
    ["4527b433-85d2-5b00-817b-d16b85609454", "John D Archbold"],
    ["7db33a77-adc9-58d0-9132-9ebe72aa3297", "Alford Archer"],
    ["6afd61a6-8ad0-5e90-8547-d2148cf57141", "Flton W Archer"],
    ["ddab11a7-066e-52d9-960f-469c451d128b", "Harold F Archer"],
    ["7898f2ba-7a38-5945-9f27-a675d85ec097", "Raymond Archer"],
    ["8e4882b1-598a-5731-a290-3bd4083409f6", "William L Archer"],
    ["e6017cc9-1539-556c-abc6-7cd9952efcd1", "Robert Archibald"],
    ["77a9350e-8c58-5229-8660-04e1f08a087c", "Anthony A Archuleta Jr."],
    ["d9dd5779-296e-5bdf-a05a-b7a653e0b991", "Eugene F Archuleta"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("20", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "20c1c1ab-1d97-5f48-9665-e1d1b64b53e8",
    "7db33a77-adc9-58d0-9132-9ebe72aa3297",
    "6afd61a6-8ad0-5e90-8547-d2148cf57141",
    "ddab11a7-066e-52d9-960f-469c451d128b",
    "7898f2ba-7a38-5945-9f27-a675d85ec097",
    "8e4882b1-598a-5731-a290-3bd4083409f6",
    "e6017cc9-1539-556c-abc6-7cd9952efcd1",
    "d9dd5779-296e-5bdf-a05a-b7a653e0b991",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  for (const [personId, rankText, categoryText] of [
    [
      "20c1c1ab-1d97-5f48-9665-e1d1b64b53e8",
      "Caf-5",
      "civilian professional or administrative grade",
    ],
    [
      "6afd61a6-8ad0-5e90-8547-d2148cf57141",
      "1st Lt",
      "commissioned army officer",
    ],
    [
      "ddab11a7-066e-52d9-960f-469c451d128b",
      "Sgt",
      "enlisted army personnel",
    ],
    [
      "8e4882b1-598a-5731-a290-3bd4083409f6",
      "Capt",
      "commissioned army officer",
    ],
    [
      "d9dd5779-296e-5bdf-a05a-b7a653e0b991",
      "S/Sgt",
      "enlisted army personnel",
    ],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator("body")).toContainText(rankText);
    await expect(page.locator("body")).toContainText(categoryText);
  }

  await page.goto("./people/6afd61a6-8ad0-5e90-8547-d2148cf57141/");
  await expect(
    page.getByRole("heading", { name: "Flton W Archer", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).not.toContainText("Fulton W Archer");
  await expect(page.locator("body")).not.toContainText("Elton W Archer");

  await page.goto("./people/7db33a77-adc9-58d0-9132-9ebe72aa3297/");
  await expect(page.locator("body")).toContainText(
    "before evaluating the Ohio State namesake",
  );

  await page.goto("./people/4527b433-85d2-5b00-817b-d16b85609454/");
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Naval Reserve");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("strongly date bounded");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Springfield Plantation");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("self employment");
  await expect(page.locator("body")).toContainText(
    "last documented civilian livelihood",
  );

  await page.goto("./people/77a9350e-8c58-5229-8660-04e1f08a087c/");
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("body")).toContainText(
    "Civil Life is a status, not an employer",
  );

  for (const [organizationId, organizationName, personName] of [
    [
      "1b90fcf6-604d-588b-8a30-7bb08c930c6f",
      "United States Naval Reserve",
      "John D Archbold",
    ],
    [
      "4d5e1a65-d52f-563c-baba-ee4a0ac2b3b4",
      "Springfield Plantation",
      "John D Archbold",
    ],
    [
      "28a26f92-78af-5a1a-9c09-a843eb5975b4",
      "United States Army",
      "Anthony A Archuleta Jr.",
    ],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 097 publishes Arensberg and Argyropais in distinct evidence lanes while preserving seven archival cases", async ({
  page,
}) => {
  const profiles = [
    ["1d67bdcc-9f3f-509a-a3ef-b3863cbe4055", "Oliver W Arden", "20"],
    ["2b0c15bf-22b1-5141-b5d1-3c175e8e87f9", "Joseph F Ardinger", "20"],
    ["82d0c2da-14d4-5d90-b605-57da5a928978", "John G Ardon", "20"],
    ["363c7ba5-99c0-548e-b1f5-eb1e8a57941f", "Phillip J Arengi", "21"],
    ["97a70dce-399d-536b-bba9-efa7d76f42a1", "Conrad Arensberg", "21"],
    ["bd0eb8e5-edf6-5a2b-9433-6395c59b8f50", "Julius Arensteim", "21"],
    ["fba157a4-9abc-5fcf-99c0-655b5b1eaaaf", "Florence T Arft", "21"],
    ["d6683ada-a492-5dc4-b546-cf39918ccdf8", "Christian A Argyris", "21"],
    ["a21b2937-f993-5cb1-91e4-a7d85eef14ee", "Lemonis J Argyropais", "21"],
    ["79f86e73-77b8-510e-803e-c963d7b83872", "Edward Arida", "21"],
  ];

  for (const [personId, displayName, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "1d67bdcc-9f3f-509a-a3ef-b3863cbe4055",
    "2b0c15bf-22b1-5141-b5d1-3c175e8e87f9",
    "82d0c2da-14d4-5d90-b605-57da5a928978",
    "bd0eb8e5-edf6-5a2b-9433-6395c59b8f50",
    "fba157a4-9abc-5fcf-99c0-655b5b1eaaaf",
    "d6683ada-a492-5dc4-b546-cf39918ccdf8",
    "79f86e73-77b8-510e-803e-c963d7b83872",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  await page.goto("./people/d6683ada-a492-5dc4-b546-cf39918ccdf8/");
  await expect(page.locator("body")).toContainText(
    "before reconsidering any namesake",
  );
  await expect(page.locator("body")).not.toContainText(
    "authority on organizational behavior",
  );

  await page.goto("./people/363c7ba5-99c0-548e-b1f5-eb1e8a57941f/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("medium");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/97a70dce-399d-536b-bba9-efa7d76f42a1/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Brooklyn College");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Massachusetts Institute of Technology");
  await expect(page.locator("body")).toContainText(
    "dates Arensberg's Brooklyn College appointment from 1941 to 1946",
  );

  await page.goto("./people/a21b2937-f993-5cb1-91e4-a7d85eef14ee/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Clark University");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("University of Athens");
  await expect(page.locator("body")).toContainText(
    "disagree whether the master's degree was recorded in 1942 or 1943",
  );

  for (const [organizationId, organizationName, personName] of [
    [
      "8f419f2a-9478-5d6d-944c-1949855cf8c5",
      "Brooklyn College",
      "Conrad Arensberg",
    ],
    [
      "c254b90a-52af-5598-a9f9-9ac1d4406f16",
      "Massachusetts Institute of Technology",
      "Conrad Arensberg",
    ],
    [
      "10d9d453-94cc-59e5-a1ca-c337fe5ddc76",
      "Clark University",
      "Lemonis J Argyropais",
    ],
    [
      "31f32f7f-e7dc-5c4b-a43f-38432dbcca53",
      "National and Kapodistrian University of Athens",
      "Lemonis J Argyropais",
    ],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 098 publishes Arluck and Armandi pathways while preserving six archival cases and two identity-only outcomes", async ({
  page,
}) => {
  const profiles = [
    ["2fc6b15e-a70b-53b1-8cb7-fccc6576f305", "Salvatoroe Arlotta"],
    ["3711f377-5ab5-54da-8599-2ead535e07fb", "Edward W Arluck"],
    ["6fc5aae3-7381-5bb2-b9fa-641901a94657", "Joseph O Armandariz"],
    ["c2d19474-9028-5b38-bcac-8d3824b65a70", "Raymond Armandi"],
    ["a0776531-ae02-50b1-acb7-1e4246a300f0", "Virgile C Armaos"],
    ["aef22be7-52c9-53ae-ba5a-5a411501b82b", "Mary C Armato"],
    ["9858d093-e0b6-53b7-9130-c42e4cd4990b", "William E Armband"],
    ["95768589-c254-58da-8083-3867a475c528", "George E Armbruster"],
    ["a6c677da-8464-557d-ba74-5731563db6da", "Andrew R Armentor"],
    ["9ca18abd-a751-549e-9a03-b9b9a9759179", "John E Armer"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("21", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "2fc6b15e-a70b-53b1-8cb7-fccc6576f305",
    "6fc5aae3-7381-5bb2-b9fa-641901a94657",
    "a0776531-ae02-50b1-acb7-1e4246a300f0",
    "aef22be7-52c9-53ae-ba5a-5a411501b82b",
    "9858d093-e0b6-53b7-9130-c42e4cd4990b",
    "95768589-c254-58da-8083-3867a475c528",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/2fc6b15e-a70b-53b1-8cb7-fccc6576f305/");
  await expect(
    page.getByRole("heading", { name: "Salvatoroe Arlotta", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).not.toContainText("Salvatore Arlotta");

  await page.goto("./people/9858d093-e0b6-53b7-9130-c42e4cd4990b/");
  await expect(
    page.getByRole("heading", { name: "William E Armband", exact: true }),
  ).toBeVisible();
  await expect(page.locator(".index-record").first()).toContainText("Caf-11");

  await page.goto("./people/3711f377-5ab5-54da-8599-2ead535e07fb/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Columbia University");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/c2d19474-9028-5b38-bcac-8d3824b65a70/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("explicit immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).not.toContainText("International Paper");

  for (const [personId, identityText] of [
    [
      "a6c677da-8464-557d-ba74-5731563db6da",
      "The indexed Staff Sergeant Andrew R. Armentor",
    ],
    [
      "9ca18abd-a751-549e-9a03-b9b9a9759179",
      "The indexed Corporal John E. Armer",
    ],
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
    await expect(page.locator("body")).toContainText(identityText);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const [organizationId, organizationName, personName] of [
    [
      "87e3d52a-9ace-512a-9677-e966b7fbd5e5",
      "Columbia University",
      "Edward W Arluck",
    ],
    [
      "28a26f92-78af-5a1a-9c09-a843eb5975b4",
      "United States Army",
      "Raymond Armandi",
    ],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 099 publishes Lester Armour's naval pathway without turning board roles into employment", async ({
  page,
}) => {
  const profiles = [
    ["96940f0e-3817-5c23-b36e-28ef8a5dacc5", "M E Armistead"],
    ["45dcedfa-2833-5535-8c73-9880621609ae", "Stanley N Armitage"],
    ["bac8222f-9ef3-5981-a1a8-b36529eb55f3", "Lester Armour"],
    ["bb7abead-a3d2-58b0-bb3e-9e37d2719b73", "Albert L Armstrong"],
    ["0744050f-188a-59da-8e6d-d2e019389c6d", "Claude C Armstrong Jr."],
    ["4546300f-0612-5e26-96be-a87a7fd69ac2", "Delton V Armstrong"],
    ["59c80068-e66f-5767-a1d8-b828597e4d55", "Elizabeth H Armstrong"],
    ["be4a7e93-66f9-546d-9111-e8154477a0ec", "Frank E Armstrong"],
    ["c96b4cd7-046d-52e2-9f8e-56e2fe968896", "Herbert E Armstrong Jr."],
    ["a89a1112-c099-54e1-b5e4-638e089d6cf1", "Howard H Armstrong"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("21", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "96940f0e-3817-5c23-b36e-28ef8a5dacc5",
    "45dcedfa-2833-5535-8c73-9880621609ae",
    "bb7abead-a3d2-58b0-bb3e-9e37d2719b73",
    "0744050f-188a-59da-8e6d-d2e019389c6d",
    "4546300f-0612-5e26-96be-a87a7fd69ac2",
    "59c80068-e66f-5767-a1d8-b828597e4d55",
    "be4a7e93-66f9-546d-9111-e8154477a0ec",
    "c96b4cd7-046d-52e2-9f8e-56e2fe968896",
    "a89a1112-c099-54e1-b5e4-638e089d6cf1",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/96940f0e-3817-5c23-b36e-28ef8a5dacc5/");
  await expect(
    page.getByRole("heading", { name: "M E Armistead", exact: true }),
  ).toBeVisible();
  await expect(page.locator(".index-record").first()).toContainText("Lt");

  await page.goto("./people/bb7abead-a3d2-58b0-bb3e-9e37d2719b73/");
  await expect(page.locator(".index-record").first()).toContainText("CPC-6");

  await page.goto("./people/59c80068-e66f-5767-a1d8-b828597e4d55/");
  await expect(page.locator(".index-record").first()).toContainText("P-3");

  await page.goto("./people/bac8222f-9ef3-5981-a1a8-b36529eb55f3/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator(".profile-aside")).toContainText(
    "commissioned naval officer",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Navy");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("strongly date bounded");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier).toContainText("Field Museum of Natural History");
  await expect(earlier).toContainText("Armour and Company");
  await expect(earlier).toContainText("General Stockyards Corporation");
  await expect(earlier).toContainText(
    "City National Bank and Trust Company of Chicago",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).not.toContainText("General Stockyards");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).not.toContainText("City National");
  await expect(
    page.getByRole("link", { name: "Lester Armour papers", exact: true }).first(),
  ).toHaveAttribute("href", /digitalcollections\.hoover\.org/);
  await expect(
    page
      .getByRole("link", { name: "Lester Armour: Legion of Merit", exact: true })
      .first(),
  ).toHaveAttribute("href", /valor\.militarytimes\.com/);

  for (const [organizationId, organizationName] of [
    ["3960fa8e-a551-56cf-8305-b2b9e4961b9d", "United States Navy"],
    ["d2fa6694-018a-5667-84e1-103802fdc3a6", "Armour and Company"],
    ["50a938e5-be9b-54d4-b30e-5a200218ab3c", "General Stockyards Corporation"],
    [
      "45cc7128-6b61-5b9a-9d5a-fcf0f56956ae",
      "City National Bank and Trust Company of Chicago",
    ],
    ["34f0b784-e740-56ea-aa08-2bc0f41a722f", "Field Museum of Natural History"],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: "Lester Armour", exact: true }),
    ).toBeVisible();
  }
});

test("Batch 100 preserves qualified Armstrong pathways and the confirmed Arnault attachment", async ({
  page,
}) => {
  const profiles = [
    ["bd592469-9834-589c-82ee-c27b210672e1", "James H Armstrong", "21"],
    ["2cf0ea26-a270-5523-b4f1-bf9d70948273", "Jay W Armstrong", "21"],
    ["49f8525e-c07b-5adf-a0ea-ee03273a7c9f", "Lena V Armstrong", "22"],
    ["d4066095-526a-5228-9ae8-cf7ff378b08c", "Mary H Armstrong", "22"],
    ["fa355673-ac0b-50d9-a7d6-b0285c311725", "Raymond A Armstrong", "22"],
    ["865541d6-c404-58ed-ab40-0ee67a7971da", "Robert P Armstrong", "22"],
    ["22e0ef05-0a08-5bfb-90a6-472bfdd22135", "Robert W Armstrong Jr.", "22"],
    ["8db28d8f-76bc-57d4-b99f-c745ba6c7d52", "Sinclair Armstrong", "22"],
    ["5d6ed3b0-1984-5ca3-8aa1-6ea7aea622ea", "Claude G Arnault", "22"],
    ["86ef493c-62ff-59b6-87b3-4fec4552975f", "George C Arnberg", "22"],
  ];

  for (const [personId, displayName, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "2cf0ea26-a270-5523-b4f1-bf9d70948273",
    "49f8525e-c07b-5adf-a0ea-ee03273a7c9f",
    "d4066095-526a-5228-9ae8-cf7ff378b08c",
    "fa355673-ac0b-50d9-a7d6-b0285c311725",
    "865541d6-c404-58ed-ab40-0ee67a7971da",
    "22e0ef05-0a08-5bfb-90a6-472bfdd22135",
    "86ef493c-62ff-59b6-87b3-4fec4552975f",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/865541d6-c404-58ed-ab40-0ee67a7971da/");
  await expect(page.locator(".profile-aside")).toContainText(
    "enlisted naval personnel",
  );
  await expect(page.locator(".index-record").first()).toContainText("RM2/c");

  await page.goto("./people/bd592469-9834-589c-82ee-c27b210672e1/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army Air Forces, 19th Weather Squadron");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("explicit immediate");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("medium");
  await expect(
    page.getByRole("link", { name: "The Yugoslavia Caper", exact: true }).first(),
  ).toHaveAttribute("href", "https://greyberet.org/hight");

  await page.goto("./people/8db28d8f-76bc-57d4-b99f-c745ba6c7d52/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Isham, Lincoln & Beale");
  await expect(
    page.getByRole("link", {
      name: "A Sense of Securities: J. Sinclair Armstrong '41",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /hls\.harvard\.edu/);

  await page.goto("./people/5d6ed3b0-1984-5ca3-8aa1-6ea7aea622ea/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(page.locator(".profile-aside")).toContainText(
    "foreign or allied military personnel",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("French Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("explicit immediate");
  await expect(
    page.getByRole("link", {
      name: "Claude Arnault: Distinguished Service Cross",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /valor\.militarytimes\.com/);

  for (const [organizationId, organizationName, personName] of [
    [
      "122fdabe-af12-596c-9c76-b3c09a522887",
      "United States Army Air Forces, 19th Weather Squadron",
      "James H Armstrong",
    ],
    [
      "902e4135-6c35-56e5-aa62-c2129e2c8361",
      "Isham, Lincoln & Beale",
      "Sinclair Armstrong",
    ],
    [
      "f61aed47-47ad-5e11-82be-3835d1bc4365",
      "French Army",
      "Claude G Arnault",
    ],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 101 confirms Arnesen's qualified Army pathway while preserving archival uncertainty", async ({
  page,
}) => {
  const profiles = [
    ["f8ad75b2-c1e6-5482-a266-7a616dc8dc91", "Clifford H Arndt"],
    ["3e4999fa-bd44-5300-b1f0-ad2537af049a", "Miriam I Arndt"],
    ["3156f1ce-ab52-5e4a-b2fd-35a79fe3e993", "Alf G Arnesen"],
    ["15854cf9-9dc9-546f-9218-30618f650064", "Reider Arnesen"],
    ["7c477047-2696-5bac-a1ea-d5c5b17e5b61", "Homer E Arnett"],
    ["16cc3b9b-ec35-5204-baaf-f49e58a16d28", "Lucy V Arnett"],
    ["fe87f961-64ba-5034-a271-0180451ed3ac", "Maynard C Arney"],
    ["46bc841b-578f-5007-807a-7733295de70b", "George A Arnold"],
    ["e3f8d84c-d5b1-5243-91bf-9f94cd68f3e0", "Glenn E Arnold"],
    ["50cd9e33-505c-51de-a9f0-aed4ec096c72", "Harry K Arnold"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("22", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "f8ad75b2-c1e6-5482-a266-7a616dc8dc91",
    "3e4999fa-bd44-5300-b1f0-ad2537af049a",
    "15854cf9-9dc9-546f-9218-30618f650064",
    "7c477047-2696-5bac-a1ea-d5c5b17e5b61",
    "16cc3b9b-ec35-5204-baaf-f49e58a16d28",
    "46bc841b-578f-5007-807a-7733295de70b",
    "e3f8d84c-d5b1-5243-91bf-9f94cd68f3e0",
    "50cd9e33-505c-51de-a9f0-aed4ec096c72",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/15854cf9-9dc9-546f-9218-30618f650064/");
  await expect(page.locator(".index-record").first()).toContainText("possibly");
  await expect(page.locator("main")).toContainText(
    "conflicting 99th Infantry candidate",
  );

  await page.goto("./people/3156f1ce-ab52-5e4a-b2fd-35a79fe3e993/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army, 99th Infantry Battalion (Separate)");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("medium");
  await expect(
    page.getByRole("link", {
      name: "Headquarters Operational Group Command, Special Orders Number 9",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /archives\.gov\/files\/research\/jfk\/releases/);

  await page.goto("./people/fe87f961-64ba-5034-a271-0180451ed3ac/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(page.locator("main")).toContainText("PFC. MAYNARD C. ARNEY");
  await expect(
    page.getByRole("link", {
      name: "Honor Roll Album of Bayfield County Men and Women Who Served in World War II",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /worldwartwoveterans\.org/);

  await page.goto("./organizations/a520c0e7-81d8-5aea-90d7-ddb0b2ce5eff/");
  await expect(
    page.getByRole("heading", {
      name: "United States Army, 99th Infantry Battalion (Separate)",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.locator("h3").getByRole("link", { name: "Alf G Arnesen", exact: true }),
  ).toBeVisible();
});

test("Batch 102 qualifies Arnoldy's Army film pathway and preserves common-name uncertainty", async ({
  page,
}) => {
  const profiles = [
    ["a877ba31-3831-5c65-ac31-def45df2b8e3", "Howard W Arnold", "22"],
    ["cada8583-a8fa-513f-90ff-e0517b94b62a", "James S Arnold", "22"],
    ["0c66ae1c-cd45-5cf9-9396-1bb966c11add", "Paul B Arnold", "22"],
    ["9a8d55a2-19fc-59bc-8622-63c39e306da2", "Robert W Arnold", "22"],
    ["33e7124a-106f-590b-89bc-c40e80c9e60d", "Virginia W Arnold", "22"],
    ["2a3a5ee1-91e8-5948-b2d8-3fa793923110", "Wilfred Arnold Jr.", "22"],
    ["04aa0bcc-f27f-5182-a2a1-bac4f1e3485f", "William E Arnold", "22"],
    ["b5c889e5-13d7-5a47-bb1d-f8536f24be22", "Richard G Arnold-Baker", "22"],
    ["f0fb97e4-95f9-5646-99e9-0dc750846d89", "Francis N Arnoldy", "22"],
    ["d8336ef8-0a06-5a0d-ae03-4472b62d8ed3", "Raymond Arnone", "23"],
  ];

  for (const [personId, displayName, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "a877ba31-3831-5c65-ac31-def45df2b8e3",
    "cada8583-a8fa-513f-90ff-e0517b94b62a",
    "0c66ae1c-cd45-5cf9-9396-1bb966c11add",
    "9a8d55a2-19fc-59bc-8622-63c39e306da2",
    "33e7124a-106f-590b-89bc-c40e80c9e60d",
    "2a3a5ee1-91e8-5948-b2d8-3fa793923110",
    "04aa0bcc-f27f-5182-a2a1-bac4f1e3485f",
    "d8336ef8-0a06-5a0d-ae03-4472b62d8ed3",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/f0fb97e4-95f9-5646-99e9-0dc750846d89/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army, Film Branch, Special Service Division");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Technical adviser on Russian films");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("medium");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.getByRole("link", { name: "They Fight with Film", exact: true }).first(),
  ).toHaveAttribute("href", /indianamilitary\.org/);
  await expect(
    page.getByRole("link", {
      name: "Communist Stardom in the Cold War: Josip Broz Tito in Western and Yugoslav Photography, 1943-1980",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /bac-lac\.gc\.ca/);

  await page.goto("./people/b5c889e5-13d7-5a47-bb1d-f8536f24be22/");
  await expect(page.locator("main")).toContainText("British A");
  await expect(page.locator("main")).toContainText("Intelligence Corps");
  await expect(page.locator("main")).toContainText("temporal relation uncertain");

  await page.goto("./organizations/f67d5945-8f5b-5ad6-b7f1-cd4d7a80fccc/");
  await expect(
    page.getByRole("heading", {
      name: "United States Army, Film Branch, Special Service Division",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.locator("h3").getByRole("link", { name: "Francis N Arnoldy", exact: true }),
  ).toBeVisible();
});

test("Batch 103 identifies Aromando and qualifies Aronson's Navy photographic pathway", async ({
  page,
}) => {
  const profiles = [
    ["e8a31fb3-f988-5c48-8369-dc464be5eeed", "Anetta S Arnston"],
    ["9ab706fc-6359-5402-8913-f49a2110ae06", "Carmine Aromando"],
    ["64182fed-b317-5648-b179-9942fb3852fd", "Emanuel L Aronhime"],
    ["64bdd50d-0f34-5d6e-aa14-8cb33231b319", "Ernest G Arons"],
    ["b590af61-6c94-573b-a214-d05cf4ded19a", "Bernard Aronson"],
    ["00148465-dea9-5aff-bae1-95f8dcd77ad6", "Naomi T Arp"],
    ["617d5450-4e60-5e52-a9e8-def807b02705", "Manuel R Arpanjian"],
    ["1febdbb0-2f64-5d15-94c4-b848cf003090", "Burton Arrington"],
    ["6ac6ffa5-23d5-5612-9d18-9d4c694fb48b", "John E Arrington"],
    ["b6e6e221-3dab-58d5-b7c1-c46c6b009fd4", "Mabel I Arrington"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("23", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "e8a31fb3-f988-5c48-8369-dc464be5eeed",
    "64182fed-b317-5648-b179-9942fb3852fd",
    "64bdd50d-0f34-5d6e-aa14-8cb33231b319",
    "00148465-dea9-5aff-bae1-95f8dcd77ad6",
    "617d5450-4e60-5e52-a9e8-def807b02705",
    "1febdbb0-2f64-5d15-94c4-b848cf003090",
    "6ac6ffa5-23d5-5612-9d18-9d4c694fb48b",
    "b6e6e221-3dab-58d5-b7c1-c46c6b009fd4",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/9ab706fc-6359-5402-8913-f49a2110ae06/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(page.locator("main")).toContainText("Operation Ginny I");
  await expect(
    page.getByRole("link", {
      name: "Ex pluribus unum. Come l'Office of Strategic Service ha rivoluzionato il sistema d'intelligence statunitense",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /unire\.unige\.it/);

  await page.goto("./people/b590af61-6c94-573b-a214-d05cf4ded19a/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("SP P 2/c");
  await expect(page.locator("main")).toContainText("enlisted naval personnel");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Navy");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Specialist (Photographic), second class");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("medium");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.getByRole("link", { name: "Bernard Aronson Obituary", exact: true }).first(),
  ).toHaveAttribute("href", /legacy\.com/);
  await expect(
    page.getByRole("link", {
      name: "Abbreviations Used for Navy Enlisted Ratings",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /history\.navy\.mil/);

  await page.goto("./organizations/3960fa8e-a551-56cf-8305-b2b9e4961b9d/");
  await expect(
    page.getByRole("heading", { name: "United States Navy", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator("h3").getByRole("link", { name: "Bernard Aronson", exact: true }),
  ).toBeVisible();
});

test("Batch 104 distinguishes Arrowood, Asbury, and Aserinsky pathways", async ({
  page,
}) => {
  const profiles = [
    ["13b9ab82-15f5-5dce-927f-23d27ba7acb9", "Mable O Arrington"],
    ["23aac3de-4dd9-584f-9da3-f5c6cb770493", "Anita Arrow"],
    ["14688d75-99d2-5fba-afa9-d6ae14f3cc78", "Buford B Arrowood"],
    ["1066bbac-2fe9-5db0-b13c-6cfac3fd54e4", "Arthur J Arruda"],
    ["fbb425d3-d6be-50a2-bbf0-364c0ead6ebc", "Leonard J Arsenault"],
    ["0afca4c2-5577-5d15-a9db-3a3796742b64", "Paul E Arther"],
    ["58f05d67-24fd-5f11-9a13-262ed8ceedb4", "Paul Artisst"],
    ["419911d8-f090-5a3a-95e6-dc1e17794350", "Carmelo Aruta"],
    ["309cd4b5-1372-58ee-8a8e-ee0752e52e79", "Willard C Asbury"],
    ["abcb4fb7-5825-5ded-a51c-447530af0d38", "Eugene Aserinsky"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("23", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "13b9ab82-15f5-5dce-927f-23d27ba7acb9",
    "1066bbac-2fe9-5db0-b13c-6cfac3fd54e4",
    "fbb425d3-d6be-50a2-bbf0-364c0ead6ebc",
    "58f05d67-24fd-5f11-9a13-262ed8ceedb4",
    "419911d8-f090-5a3a-95e6-dc1e17794350",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/23aac3de-4dd9-584f-9da3-f5c6cb770493/");
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Anita Arrow Summers");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/0afca4c2-5577-5d15-a9db-3a3796742b64/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Army from 1943 to 1945");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");

  await page.goto("./people/14688d75-99d2-5fba-afa9-d6ae14f3cc78/");
  await expect(
    page.getByText("confirmed", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("U.S. Army Forces in the Middle East");
  await expect(page.locator("main")).toContainText("Rayon mill work");
  await expect(
    page.getByRole("link", {
      name: "Proceedings of the board appointed by director of OSS by secret letter dated Washington 7 March 1944",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /digitalcollections\.hoover\.org/);

  await page.goto("./people/309cd4b5-1372-58ee-8a8e-ee0752e52e79/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText(
    "Standard Oil Development Company",
  );
  await expect(page.locator("main")).toContainText("documented prewar");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");

  await page.goto("./people/abcb4fb7-5825-5ded-a51c-447530af0d38/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable immediate");
  await expect(page.locator("main")).toContainText("Brooklyn College");
  await expect(page.locator("main")).toContainText("University of Maryland");

  await page.goto("./organizations/2f509b33-cf0b-51a8-a09c-549c9f23cc69/");
  await expect(
    page.getByRole("heading", {
      name: "U.S. Army Forces in the Middle East",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.locator("h3").getByRole("link", { name: "Buford B Arrowood", exact: true }),
  ).toBeVisible();

  await page.goto("./organizations/14816dbb-d382-525d-b265-8278f97cd819/");
  await expect(
    page.getByRole("heading", {
      name: "Standard Oil Development Company",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.locator("h3").getByRole("link", { name: "Willard C Asbury", exact: true }),
  ).toBeVisible();
});

test("Batch 105 preserves the ten Ash-through-Ashcraft unresolved pathways", async ({
  page,
}) => {
  const profiles = [
    ["0172547d-eef7-50aa-85c4-474feec785c6", "Charles H Ash", "civilian professional or administrative grade"],
    ["853f570e-b590-59b3-95dc-175f9b349416", "Frank S Ash", "enlisted army personnel"],
    ["3aeccd2e-4fd3-53f3-bfe2-e5a819f980a1", "Gladys Ash", "civilian professional or administrative grade"],
    ["34f72504-8550-58a9-b411-31b1ee60ad30", "Mckinley Ash", "commissioned army officer"],
    ["c6f75eab-e145-5a6b-9ee3-01aabdf5d39c", "Nelson E Ash", "enlisted army personnel"],
    ["06919b70-a83a-511f-a8f7-8d52f3e40fbe", "Loris W Ashby", "enlisted army personnel"],
    ["e94b9aca-5a70-5cd8-a004-e13e48378139", "Lylie H Ashby", "unknown or indeterminate"],
    ["7f8c75e4-e3b7-5af9-83d4-e3d52c077724", "Mary J Ashby", "civilian professional or administrative grade"],
    ["c205acb5-4610-54a1-9362-3f85d6629a4f", "Harold F Ashcraft", "unknown or indeterminate"],
    ["26520e38-3b27-51af-882c-aa5f467f7d56", "John J Ashcraft Jr.", "commissioned army officer"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("23", { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/34f72504-8550-58a9-b411-31b1ee60ad30/");
  await expect(page.locator("main")).toContainText("Major McKinley Ash Jr.");

  await page.goto("./people/26520e38-3b27-51af-882c-aa5f467f7d56/");
  await expect(page.locator("main")).toContainText("John W. Ashcraft Jr.");
  await expect(page.locator("main")).toContainText("died in 1929");
});

test("Batch 106 separates Ashin and Ashley pathways from unresolved namesakes", async ({
  page,
}) => {
  const profiles = [
    ["7382ae26-2e40-524e-a919-0bfc6bdeee35", "Wanda T Ashcraft", "23", "unknown or indeterminate"],
    ["97a55104-5418-54cc-9edb-dcdc8761048d", "William C Ashcraft", "24", "commissioned army officer"],
    ["e5940ac0-eb51-59dc-ab83-ceb1b99e0058", "Wiliam B Asher", "24", "enlisted army personnel"],
    ["4f5db04d-52d3-588c-ba4b-11735775169f", "Mark Ashin", "24", "commissioned army officer"],
    ["68115a33-d5b9-5f8f-bff7-2005b1f457d0", "Alfred B Ashley", "24", "unknown or indeterminate"],
    ["ec559cf3-d57b-59ad-bb97-a99305a4fe6f", "Belva L Ashley", "24", "unknown or indeterminate"],
    ["be29e9b1-fea8-5401-b4bd-4b894241487f", "Ira Ashley", "24", "commissioned army officer"],
    ["a61918bd-cd62-5871-bd12-f130ebdef75a", "Richard Ashley", "24", "enlisted army personnel"],
    ["f4177419-d9b3-5ebf-907e-a45e48e85c07", "Margaret Ashton", "24", "civilian professional or administrative grade"],
    ["01e5ee6c-bf6e-53c6-bd7c-249d6bc4e938", "James M Ashworth", "24", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, box, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "7382ae26-2e40-524e-a919-0bfc6bdeee35",
    "97a55104-5418-54cc-9edb-dcdc8761048d",
    "e5940ac0-eb51-59dc-ab83-ceb1b99e0058",
    "68115a33-d5b9-5f8f-bff7-2005b1f457d0",
    "ec559cf3-d57b-59ad-bb97-a99305a4fe6f",
    "a61918bd-cd62-5871-bd12-f130ebdef75a",
    "f4177419-d9b3-5ebf-907e-a45e48e85c07",
    "01e5ee6c-bf6e-53c6-bd7c-249d6bc4e938",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/e5940ac0-eb51-59dc-ab83-ceb1b99e0058/");
  await expect(page.locator("main")).toContainText(
    "William B Asher (search alias; not a correction)",
  );

  await page.goto("./people/4f5db04d-52d3-588c-ba4b-11735775169f/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("University of Chicago");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("strongly date bounded");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Michigan State College");
  await expect(
    page.getByRole("link", { name: "Obituary: Mark Ashin", exact: true }).first(),
  ).toHaveAttribute("href", /chronicle\.uchicago\.edu/);
  await expect(
    page.getByRole("link", {
      name: "Minutes of the Meeting of the State Board of Agriculture, September 15, 1939",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /onthebanks\.msu\.edu/);

  await page.goto("./people/be29e9b1-fea8-5401-b4bd-4b894241487f/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Lambert & Feasley");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("documented prewar");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Stage Door Canteen (CBS radio program)");
  await expect(
    page.getByRole("link", {
      name: "Now It Can Be Told: The Story of the Soldatensender",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /ajr\.org\.uk/);
  await expect(
    page.getByRole("link", { name: "Producer in the Army", exact: true }).first(),
  ).toHaveAttribute("href", /worldradiohistory\.com/);

  for (const [organizationId, organizationName, personName] of [
    ["6d308576-4b9f-581f-b5fd-7f63d742e1e3", "Lambert & Feasley", "Ira Ashley"],
    ["d37718c1-1acf-5c35-9d9d-2be5a1de1dd6", "Stage Door Canteen (CBS radio program)", "Ira Ashley"],
    ["f2c878b0-ee44-573d-ab30-7e4282bc85e5", "University of Chicago", "Mark Ashin"],
    ["24ac156d-62e6-5107-a412-646391d990a2", "Michigan State College", "Mark Ashin"],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 107 preserves Askew-through-Aste identity and temporal boundaries", async ({
  page,
}) => {
  const profiles = [
    ["5f9bafc9-adbc-5a7d-a7cb-3ada6e844f5c", "Leo G Askew", "unknown or indeterminate"],
    ["ccc8941b-2ab3-5fc7-9a73-2936da041412", "Milton C Askew", "enlisted army personnel"],
    ["1031ef2c-9d05-53e4-8ea8-b8f55296bcd5", "Monroe P Askins", "enlisted naval personnel"],
    ["894e1ad1-74cc-583f-b464-8a0d26800f33", "A. W Asmuth Jr.", "unknown or indeterminate"],
    ["4b71c845-36d9-5fa9-85eb-e3a12ae242c0", "Lea T Aspinwall", "unknown or indeterminate"],
    ["ceaf422b-0462-55b6-9990-09f49474aa30", "James D Assaf", "commissioned army officer"],
    ["27f3030a-180b-51b3-b463-a6ae1cebd003", "Gerard R Asselin", "enlisted army personnel"],
    ["dee9b236-903d-5235-aac8-3301657a4eaf", "Graziella Asselin", "civilian professional or administrative grade"],
    ["fee6be23-0065-5712-901a-aac10a8b02f3", "Jean R Assemat", "foreign or allied military personnel"],
    ["a0f44de1-fa6c-52ed-aa23-9b27672ad9d9", "John Aste", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("24", { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "5f9bafc9-adbc-5a7d-a7cb-3ada6e844f5c",
    "ccc8941b-2ab3-5fc7-9a73-2936da041412",
    "894e1ad1-74cc-583f-b464-8a0d26800f33",
    "4b71c845-36d9-5fa9-85eb-e3a12ae242c0",
    "ceaf422b-0462-55b6-9990-09f49474aa30",
    "dee9b236-903d-5235-aac8-3301657a4eaf",
    "a0f44de1-fa6c-52ed-aa23-9b27672ad9d9",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/1031ef2c-9d05-53e4-8ea8-b8f55296bcd5/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("John Ford Field Photo Unit");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.getByRole("link", { name: "Thanks to ASC Veterans", exact: true }).first(),
  ).toHaveAttribute("href", /normalexposure\.com/);

  await page.goto("./people/27f3030a-180b-51b3-b463-a6ae1cebd003/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("H. P. Hood & Sons");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("documented prewar");
  await expect(
    page.getByRole("link", { name: "Gerard R. Asselin Obituary", exact: true }).first(),
  ).toHaveAttribute("href", /tylunasfuneralhome\.com/);

  await page.goto("./people/fee6be23-0065-5712-901a-aac10a8b02f3/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Jean Assémat");
  await expect(page.locator("main")).toContainText("Jacques Bauer");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Bureau Central de Renseignements et d'Action");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("explicit immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.getByRole("link", {
      name: "Archives photographiques du capitaine Jean Assémat (1919-2003). Le 1er régiment de chasseurs parachutistes en 1956",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /imagesdefense\.gouv\.fr/);

  for (const [organizationId, organizationName, personName] of [
    ["06f143a6-5bea-50f7-88c0-b1af2708abd1", "H. P. Hood & Sons", "Gerard R Asselin"],
    ["3056684e-4315-514a-b18b-27462862a489", "Bureau Central de Renseignements et d'Action", "Jean R Assemat"],
  ]) {
    await page.goto(`./organizations/${organizationId}/`);
    await expect(
      page.getByRole("heading", { name: organizationName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator("h3").getByRole("link", { name: personName, exact: true }),
    ).toBeVisible();
  }
});

test("Batch 108 preserves Aston-through-Athens identity and predecessor boundaries", async ({
  page,
}) => {
  const profiles = [
    ["a9de39d3-7bcc-5f88-afb7-8b63923bd322", "Stanley C Aston", "enlisted army personnel"],
    ["26e8b192-660c-5f34-8856-b0956a386c6e", "Theodore F Astrella", "commissioned army officer"],
    ["70b03b39-e056-5bf4-a522-d4e37bc27f94", "James B Aswell", "civilian professional or administrative grade"],
    ["54a3eb06-95fb-5acb-83db-0bfe5cef57e8", "Prayoon Atachinda", "unknown or indeterminate"],
    ["ee7e6786-ebb2-5d2b-992d-b4157add9114", "Ethel M Atchison", "civilian professional or administrative grade"],
    ["717a5917-0ebb-5f76-8cfa-8479c808baf6", "James J Atchison", "enlisted army personnel"],
    ["e452475b-d5cf-51a5-94a3-327d30d10260", "Peter S Athanasakos", "enlisted army personnel"],
    ["c1e3483a-6cd2-5058-b916-bcb1571d3295", "Peter J Atheneos", "enlisted army personnel"],
    ["1f9ace73-691d-5b96-8349-203d8c7594f4", "Everett J Athens", "commissioned naval officer"],
    ["808ca937-d656-5ca0-a005-d75ffd68364e", "John S Athens", "civilian professional or administrative grade"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("24", { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "a9de39d3-7bcc-5f88-afb7-8b63923bd322",
    "ee7e6786-ebb2-5d2b-992d-b4157add9114",
    "717a5917-0ebb-5f76-8cfa-8479c808baf6",
    "e452475b-d5cf-51a5-94a3-327d30d10260",
    "c1e3483a-6cd2-5058-b916-bcb1571d3295",
    "808ca937-d656-5ca0-a005-d75ffd68364e",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/26e8b192-660c-5f34-8856-b0956a386c6e/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Theodore Fox Astrella");
  await expect(page.locator("main")).toContainText("Fort Belvoir");
  await expect(
    page.getByRole("link", { name: "Congressional Record—Senate", exact: true }).first(),
  ).toHaveAttribute("href", /govinfo\.gov/);

  await page.goto("./people/70b03b39-e056-5bf4-a522-d4e37bc27f94/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("James Benjamin Aswell Jr.");
  await expect(page.locator("main")).toContainText("World War II: OSS, head of Morale Operations");
  await expect(
    page.getByRole("link", {
      name: "Dictionary of Louisiana Biography: Aswell, James Benjamin, Jr.",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /lahistory\.org/);

  await page.goto("./people/54a3eb06-95fb-5acb-83db-0bfe5cef57e8/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Free Th");
  await expect(page.locator("main")).toContainText("Prayun Atthachinda");
  await expect(
    page.getByRole("link", {
      name: "Thailand's Secret War: The Free Thai, OSS, and SOE during World War II — Index",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /cambridge\.org/);

  await page.goto("./people/1f9ace73-691d-5b96-8349-203d8c7594f4/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Everette J. Athens");
  await expect(page.locator("main")).toContainText("Chicago Mission");
  await expect(
    page.getByRole("link", { name: "Final Report of the Evros Mission", exact: true }).first(),
  ).toHaveAttribute("href", /elia\.org\.gr/);

  for (const personId of [
    "26e8b192-660c-5f34-8856-b0956a386c6e",
    "70b03b39-e056-5bf4-a522-d4e37bc27f94",
    "54a3eb06-95fb-5acb-83db-0bfe5cef57e8",
    "1f9ace73-691d-5b96-8349-203d8c7594f4",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 109 preserves Atherton-through-Atkisson identity and predecessor boundaries", async ({
  page,
}) => {
  const profiles = [
    ["1905bba1-001d-5c4f-8d18-02e2b28bdbc2", "David Atherton", "enlisted army personnel", "24"],
    ["3025dd53-45f3-50ee-b0a0-d54fc245a63a", "Carl A Atkins", "commissioned army officer", "24"],
    ["6f6aa669-64c4-558c-9fcf-7a5ab4bf7d08", "Earl J Atkins", "unknown or indeterminate", "24"],
    ["82f21d35-4cce-56ae-a497-06c7e38c97f4", "Frank J Atkins", "unknown or indeterminate", "24"],
    ["9c8259bd-4289-5e19-bd0a-58ac386a592b", "Geoffroy Atkinson", "unknown or indeterminate", "25"],
    ["d0ac0ab0-8537-5924-b2b4-98bc609ed353", "John W Atkinson", "unknown or indeterminate", "25"],
    ["032010b7-1c43-5d40-a18b-c81f40fe85dd", "Katrhryn C Atkinson", "civilian professional or administrative grade", "25"],
    ["f81a7caa-0332-5aef-a6d8-e02cacd1397a", "Marion Atkinson", "unknown or indeterminate", "25"],
    ["ef123141-2e98-516e-8c47-4af50f0e4f8f", "William H Atkinson", "enlisted army personnel", "25"],
    ["002fe575-acc6-5612-a7c1-9d1524961703", "Kathryne J Atkisson", "civilian professional or administrative grade", "25"],
  ];

  for (const [personId, displayName, personnelCategory, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of profiles.slice(1).map(([personId]) => personId)) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByText("unresolved", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./people/1905bba1-001d-5c4f-8d18-02e2b28bdbc2/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Operational Group Emily");
  await expect(
    page.getByRole("link", {
      name: "American Woman Donates WWII Photos to French Resistance Museum in Cahors",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /connexionfrance\.com/);
});

test("Batch 110 preserves Atkisson-through-Atwood evidence and temporal boundaries", async ({
  page,
}) => {
  const profiles = [
    ["4d7d2b14-6715-5338-8afd-f725ab266f72", "Russell E Atkisson", "civilian professional or administrative grade"],
    ["7fdfa5e3-d825-5a3d-a79a-88b477c09add", "Leslie H Atlass Jr.", "commissioned army officer"],
    ["e8a7f198-6324-5057-ad45-d9c1194b094b", "Ben C Attardi", "enlisted army personnel"],
    ["9440d21c-04bc-5d5d-bf91-5edc726f5414", "Aldon N Attayer", "commissioned army officer"],
    ["f9c7fe00-b8a8-5599-beb8-8de55f7ca5d4", "Paul R Attix", "enlisted army personnel"],
    ["23631912-560a-5a1e-8263-b55f0a9fd608", "Roy B Attride Sr.", "enlisted army personnel"],
    ["5332cfbd-681e-5236-92f2-d327953a131f", "Allen R. Atwater Jr.", "enlisted army personnel"],
    ["eb303a39-db05-55d0-8323-099373bf643e", "Amariah G Atwater", "commissioned naval officer"],
    ["3a2ea6f1-7c4f-55eb-9a27-66acff22d7fe", "Bert Atwater Jr.", "enlisted army personnel"],
    ["31ef0147-71d8-5268-bed7-70332491f5af", "Donald F Atwood", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("25", { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "4d7d2b14-6715-5338-8afd-f725ab266f72",
    "e8a7f198-6324-5057-ad45-d9c1194b094b",
    "5332cfbd-681e-5236-92f2-d327953a131f",
    "3a2ea6f1-7c4f-55eb-9a27-66acff22d7fe",
    "31ef0147-71d8-5268-bed7-70332491f5af",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./people/7fdfa5e3-d825-5a3d-a79a-88b477c09add/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("promoted to major");
  await expect(
    page.getByRole("link", {
      name: "Promotion to Major for H. Leslie Atlass, Jr.",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /worldradiohistory\.com/);

  await page.goto("./people/f9c7fe00-b8a8-5599-beb8-8de55f7ca5d4/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Ninth Army");

  await page.goto("./people/23631912-560a-5a1e-8263-b55f0a9fd608/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("bookkeeper");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("International Grenfell Association");
  await expect(page.locator("main")).toContainText("winter 1936-37");
  await expect(
    page.getByRole("link", { name: "X-2 Branch - 3 (BCCM continued)", exact: true }).first(),
  ).toHaveAttribute("href", /archives\.gov/);

  await page.goto("./people/eb303a39-db05-55d0-8323-099373bf643e/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Amariah George Cox Atwater Sr.");
  await expect(page.locator("main")).toContainText("undated Wrigley role");

  await page.goto("./organizations/c281a125-2c46-5240-8c9f-7a0cd123ea54/");
  await expect(
    page.getByRole("heading", { name: "International Grenfell Association", exact: true }),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Grenfell Mission");
  await expect(page.getByRole("link", { name: "Roy B Attride Sr.", exact: true })).toBeVisible();
});

test("Batch 111 preserves Atwood-through-Aubrey evidence and predecessor boundaries", async ({
  page,
}) => {
  const profiles = [
    ["1bde5214-0093-5448-81a6-dd27a57f13dd", "Elmer E Atwood", "enlisted army personnel"],
    ["3c8b5ecc-8146-5395-b2d6-01d722df4acb", "John L Atwood", "enlisted army personnel"],
    ["89cb9405-29e3-513b-9578-5c807f1a630f", "Margaret Atwood", "civilian professional or administrative grade"],
    ["5f286125-32d8-503c-b0dd-a001cc4171e3", "Robert D Atwood", "enlisted army personnel"],
    ["53dc459d-f622-5178-a94d-e52b92a081cd", "Samuel J Atwood", "enlisted army personnel"],
    ["f6dbf762-c90e-58b2-9843-7849cc2844bb", "Wallace W Atwood Jr.", "commissioned army officer"],
    ["a7306ebb-2f20-564e-abb9-aaa43fa55fb8", "Arthur S Aubrey Jr.", "enlisted army personnel"],
    ["70f9b762-17f1-58ad-9ca7-2bacba4c9566", "August O Aubrey", "enlisted army personnel"],
    ["f9b04d68-af1d-5aa4-8046-41eaed3b03da", "Jules W Aubrey", "commissioned army officer"],
    ["e182fde8-163f-5961-b000-55d868e64aa4", "Leland K Aubrey", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("25", { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  for (const personId of profiles
    .filter(([personId]) => personId !== "f6dbf762-c90e-58b2-9843-7849cc2844bb")
    .map(([personId]) => personId)) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/f6dbf762-c90e-58b2-9843-7849cc2844bb/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Clark University");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("United States National Park Service");
  await expect(page.locator("main")).toContainText("Atcorob");
  await expect(page.locator("main")).toContainText("immediate pre-OSS affiliation remains unresolved");
  await expect(
    page.getByRole("link", { name: "Largest Map in World Near End", exact: true }).first(),
  ).toHaveAttribute("href", /loc\.gov/);
  await expect(
    page.getByRole("link", { name: "Wallace Atwood Jr. map collection", exact: true }).first(),
  ).toHaveAttribute("href", /findingaids\.loc\.gov/);

  await page.goto("./organizations/10d9d453-94cc-59e5-a1ca-c337fe5ddc76/");
  await expect(
    page.getByRole("heading", { name: "Clark University", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Wallace W Atwood Jr.", exact: true })).toBeVisible();

  await page.goto("./organizations/8fe17c91-fbcd-5761-bc76-17ce4cb65434/");
  await expect(
    page.getByRole("heading", { name: "United States National Park Service", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Wallace W Atwood Jr.", exact: true })).toBeVisible();
});

test("Batch 112 preserves Aubuchon-through-Auerbach uncertainty and civilian-employer boundaries", async ({
  page,
}) => {
  const profiles = [
    ["8691269b-967c-5b03-8da4-307a0f1cde37", "Joseph A Aubuchon", "unknown or indeterminate", "25"],
    ["4471b6a1-3ab5-5928-bc03-1150a334e6dd", "Roy A Aubuchon", "enlisted army personnel", "25"],
    ["38e649ef-ff97-5b9d-aab8-79f8cf86efd4", "Gordon Auchincloss II", "commissioned army officer", "25"],
    ["07d71c22-1379-5f77-b609-e12a7cb6c1c8", "John W Auchincloss", "commissioned army officer", "25"],
    ["14775c1b-5c54-58cf-9022-b1de8afe6bef", "Joseph P Auclair", "unknown or indeterminate", "25"],
    ["ccdb1aec-7b04-510f-9783-047c94190730", "William S Aud", "unknown or indeterminate", "25"],
    ["d36072df-ff9a-5364-8bce-a9e696085e22", "Rene E Audet", "enlisted army personnel", "26"],
    ["0e04730f-3b25-52e5-88a3-b41ec5a12d6f", "Marie Audibert", "civilian professional or administrative grade", "26"],
    ["a3667542-502b-5ce0-b4e9-bb8d806e31ba", "Joseph J Audie", "enlisted army personnel", "26"],
    ["2feecffb-498b-5d87-b611-f67eea6073df", "Carl A Auerbach", "commissioned army officer", "26"],
  ];

  for (const [personId, displayName, personnelCategory, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText(box, { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  for (const personId of profiles
    .filter(([personId]) => personId !== "2feecffb-498b-5d87-b611-f67eea6073df")
    .map(([personId]) => personId)) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/38e649ef-ff97-5b9d-aab8-79f8cf86efd4/");
  await expect(page.locator("main")).toContainText("CIA-RDP13X00001R000100410005-4");
  await expect(page.locator("main")).toContainText("discovery lead only");

  await page.goto("./people/2feecffb-498b-5d87-b611-f67eea6073df/");
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("United States Office of Price Administration");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("U.S. Department of Labor");
  await expect(page.locator("main")).toContainText("intervening Army assignment");
  await expect(
    page.getByRole("link", { name: "In Memoriam: Carl Auerbach", exact: true }).first(),
  ).toHaveAttribute("href", /ali\.org/);
  await expect(
    page.getByRole("link", {
      name: "Law School Mourns the Passing of Former Dean Carl Auerbach",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /law\.umn\.edu/);

  await page.goto("./organizations/a37403a5-5878-511c-9413-dd7054848aa0/");
  await expect(
    page.getByRole("heading", { name: "United States Office of Price Administration", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Carl A Auerbach", exact: true })).toBeVisible();

  await page.goto("./organizations/feacdeca-7391-5e30-a968-6c29d8b43039/");
  await expect(
    page.getByRole("heading", { name: "U.S. Department of Labor", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Carl A Auerbach", exact: true })).toBeVisible();
});

test("Batch 113 preserves Auerbach-through-Ault military pathways and unresolved boundaries", async ({
  page,
}) => {
  const profiles = [
    ["fcf3aabf-d3dd-52e8-b8aa-a918bae73451", "Herbert Auerbach", "enlisted army personnel"],
    ["f8821c43-616c-5e80-85e2-fc736e4d9416", "Meyer Auerbach", "unknown or indeterminate"],
    ["f8e971e4-5dd2-5986-8885-a4d9ec7bc5ce", "William Auerbach", "enlisted army personnel"],
    ["fc948772-1195-5ce6-b0a7-12b9d487762a", "Douglas B Auffmordt", "unknown or indeterminate"],
    ["125e45ce-1765-5dc3-9470-e6832be7fb35", "Joseph R Augello", "commissioned army officer"],
    ["fced10b3-b738-5979-95f4-f41d3efb80fc", "Duplius P Auguste", "unknown or indeterminate"],
    ["2ed53e12-86c6-5c97-8deb-27b8d6857e54", "James R Augustine", "enlisted army personnel"],
    ["820ad771-7780-574f-86fd-38f514731d73", "Mary Augustine", "civilian professional or administrative grade"],
    ["18c2ce06-32ba-5b7c-8611-56541941d648", "Richard N Auld", "commissioned army officer"],
    ["ccd5b3f7-183d-5e5a-a23e-dad540d9c21a", "Lawrence Ault Jr.", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: displayName, exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".profile-aside").getByText("26", { exact: true }),
    ).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of profiles
    .filter(([personId]) =>
      ![
        "fcf3aabf-d3dd-52e8-b8aa-a918bae73451",
        "f8821c43-616c-5e80-85e2-fc736e4d9416",
      ].includes(personId),
    )
    .map(([personId]) => personId)) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/fcf3aabf-d3dd-52e8-b8aa-a918bae73451/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("V Force");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("United States Army Signal Corps");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("OSS Detachment 101");
  await expect(
    page.getByRole("link", { name: "Auerbach, Herbert", exact: true }).first(),
  ).toHaveAttribute("href", /ww2online\.org/);
  await expect(
    page.getByRole("link", { name: "Bonus Episode: Voices of the Secret WWII", exact: true }).first(),
  ).toHaveAttribute("href", /nationalww2museum\.org/);

  await page.goto("./people/f8821c43-616c-5e80-85e2-fc736e4d9416/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Meyer Morton Auerbach");
  await expect(page.locator("main")).toContainText("identity evidence only");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(
    page.getByRole("link", { name: "Meyer Auerbach Collection", exact: true }).first(),
  ).toHaveAttribute("href", /findingaids\.csun\.edu/);

  await page.goto("./organizations/b6a7166d-9e98-5448-adc0-a6015356676c/");
  await expect(
    page.getByRole("heading", { name: "V Force", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Herbert Auerbach", exact: true })).toBeVisible();

  await page.goto("./organizations/37fe0e48-9745-5a0a-8e04-6be9bc7c5c91/");
  await expect(
    page.getByRole("heading", { name: "United States Army Signal Corps", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Herbert Auerbach", exact: true })).toBeVisible();
});

test("Batch 114 preserves Ault-through-Austreng occupations, conflicts, and unresolved boundaries", async ({
  page,
}) => {
  const profiles = [
    ["9665418d-f004-5ef3-8246-45a217d67fb4", "Lee A Ault", "unknown or indeterminate"],
    ["4a26e08e-f14f-542e-9cdf-7fd379c2ca2c", "Otis L Ausen", "enlisted army personnel"],
    ["aeac723c-2097-5fd4-a649-fc8abcfbad46", "Gino Austi", "enlisted army personnel"],
    ["699d44e4-f048-5bb3-96c3-248bb0b56127", "Benton M Austin", "commissioned army officer"],
    ["7e304805-4dce-5d46-85c9-1e2976e8bfe1", "James W Austin", "enlisted army personnel"],
    ["44440ddd-93bf-5fc3-be31-b32b9c85f97b", "Kenneth P Austin", "enlisted army personnel"],
    ["28e1f4a4-a42a-5f39-9c38-968e25184e3c", "Merry A Austin", "civilian professional or administrative grade"],
    ["7d63c31c-3898-550a-8beb-28bf2e4c438e", "Nancy R Austin", "civilian professional or administrative grade"],
    ["cb5a2541-7eef-53b7-9229-bef9e13e8282", "Robert W Austin", "enlisted army personnel"],
    ["e17d6efc-d488-52a6-99e7-5bc9a6759f7b", "Vernon L Austreng", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("26", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "9665418d-f004-5ef3-8246-45a217d67fb4",
    "aeac723c-2097-5fd4-a649-fc8abcfbad46",
    "699d44e4-f048-5bb3-96c3-248bb0b56127",
    "28e1f4a4-a42a-5f39-9c38-968e25184e3c",
    "7d63c31c-3898-550a-8beb-28bf2e4c438e",
    "cb5a2541-7eef-53b7-9229-bef9e13e8282",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/4a26e08e-f14f-542e-9cdf-7fd379c2ca2c/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("OSS Norwegian Operational Group");
  await expect(page.locator("main")).toContainText(
    "strongly matched to the Otis Ausen listed with the OSS Norwegian Operational Group",
  );

  await page.goto("./people/7e304805-4dce-5d46-85c9-1e2976e8bfe1/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "student",
  );
  await expect(page.locator("main")).toContainText("the institution is not identified");

  await page.goto("./people/44440ddd-93bf-5fc3-be31-b32b9c85f97b/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("P/R middle-initial discrepancy");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "student",
  );
  await expect(page.locator("main")).toContainText("the institution is not identified");

  await page.goto("./people/e17d6efc-d488-52a6-99e7-5bc9a6759f7b/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "farm hand",
  );
  await expect(page.locator("main")).toContainText("no employing farm is identified");
  await expect(page.locator("main")).toContainText("middle-initial and Army-entry-day conflicts");
  await expect(
    page.getByRole("link", { name: "Register of North Dakota Veterans", exact: false }).first(),
  ).toHaveAttribute("href", /veterans\.nd\.gov/);
});

test("Batch 115 preserves Autotte-through-Axelrad pathways, variants, and conflicts", async ({
  page,
}) => {
  const profiles = [
    ["f6ef76a8-7c17-5077-90dc-ebf46d6850c7", "Joseph R Autotte", "26"],
    ["0e6f5000-5210-54c5-b6b2-cbd625fd9ea6", "Mary E Autrey", "27"],
    ["b3c5ad2c-deef-5f8f-934b-5a0f67a7f812", "Cleveland E Autry", "27"],
    ["78836845-ed90-5c21-9f17-41708b95f818", "Herbert Avedon", "27"],
    ["bc3d9e4a-0ef0-50ea-a344-65b7f595499b", "Crazia R Avitabile", "27"],
    ["9ef36456-344c-5668-9279-c7b2fb952d85", "Stella Avner", "27"],
    ["aa0b9ccb-7967-54a7-83b2-643f5e960eff", "Jacob D Avshalonoff", "27"],
    ["fc719b01-ceb0-532f-b85b-7a96be2f5e6b", "James H Awad", "27"],
    ["b1ec388e-e453-5a2b-88bb-3e4b80062a3a", "Nabit Awad", "27"],
    ["f9aa1435-7ad3-51dd-ac6e-47bcd7b5fa5a", "Gerald Axelrad", "27"],
  ];

  for (const [personId, displayName, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
  }

  for (const personId of [
    "0e6f5000-5210-54c5-b6b2-cbd625fd9ea6",
    "9ef36456-344c-5668-9279-c7b2fb952d85",
    "b1ec388e-e453-5a2b-88bb-3e4b80062a3a",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/f6ef76a8-7c17-5077-90dc-ebf46d6850c7/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("European Theater battle-participation roster");

  await page.goto("./people/b3c5ad2c-deef-5f8f-934b-5a0f67a7f812/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Chance Island");

  await page.goto("./people/78836845-ed90-5c21-9f17-41708b95f818/");
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("4th Ranger Battalion");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("SS Birmingham City");
  await expect(
    page.getByRole("link", { name: "Captain Herbert Avedon", exact: false }).first(),
  ).toHaveAttribute("href", /arsof-history\.org/);

  await page.goto("./people/bc3d9e4a-0ef0-50ea-a344-65b7f595499b/");
  await expect(page.locator("main")).toContainText("Grazia Avitabile");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Wheaton College");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Wheaton College");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Bryn Mawr College");
  await expect(
    page.getByRole("link", { name: /Wheaton College Board of Trustees Minutes/i }).first(),
  ).toHaveAttribute("href", /s3\.amazonaws\.com/);

  await page.goto("./people/aa0b9ccb-7967-54a7-83b2-643f5e960eff/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Jacob David Avshalomov");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Eastman School of Music");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "three different Chinese factories",
  );

  await page.goto("./people/fc719b01-ceb0-532f-b85b-7a96be2f5e6b/");
  await expect(page.getByText("conflicting", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("conflicting sources", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText(
    "does not corroborate the OSS index's private identifier",
  );

  await page.goto("./people/f9aa1435-7ad3-51dd-ac6e-47bcd7b5fa5a/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText(
    "civilian occupation code maps to multiple possible occupations",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 116 preserves Axelrod-through-Aznavourian occupations, conflicts, and unresolved outcomes", async ({
  page,
}) => {
  const profiles = [
    ["ef3e12dc-9f18-5acc-937a-54fe6172a60e", "Kermit Axelrod", "enlisted army personnel"],
    ["2a0370a1-4036-5d60-8fa7-421e5ac17f26", "R A Axlund", "civilian professional or administrative grade"],
    ["4bc411ac-75eb-5f5f-a881-42af3469c0b6", "Morris E Aycock", "enlisted army personnel"],
    ["f626df86-e8ce-5a4c-a5f8-8edd6dee0c36", "Forrest R Ayers", "enlisted army personnel"],
    ["346e0d33-5f8f-5531-80d6-30721a352f7b", "Frank W Ayers", "unknown or indeterminate"],
    ["183f6730-bfbc-5073-b667-af9b5f760bb9", "Henry C Ayers", "enlisted army personnel"],
    ["ae0e2726-54ea-55db-8d2b-d73fc683c89b", "John F Ayers", "enlisted army personnel"],
    ["820ea4f6-82c8-518a-a9e1-466336563342", "Barbara F Aylesworth", "civilian professional or administrative grade"],
    ["c3dc5b26-2ab3-57ef-8860-9f2649099181", "John M Ayshford", "unknown or indeterminate"],
    ["515752da-0978-5cc7-91e6-c9e98157a341", "Margaret Aznavourian", "civilian professional or administrative grade"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("27", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText(
      /No (reviewed claim currently meets the publication threshold|reliable pre-OSS employer has yet been identified)/,
    );
  }

  for (const personId of [
    "2a0370a1-4036-5d60-8fa7-421e5ac17f26",
    "346e0d33-5f8f-5531-80d6-30721a352f7b",
    "820ea4f6-82c8-518a-a9e1-466336563342",
    "c3dc5b26-2ab3-57ef-8860-9f2649099181",
    "515752da-0978-5cc7-91e6-c9e98157a341",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  for (const personId of [
    "ef3e12dc-9f18-5acc-937a-54fe6172a60e",
    "4bc411ac-75eb-5f5f-a881-42af3469c0b6",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("conflicting", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("conflicting sources", { exact: true }).first()).toBeVisible();
    await expect(page.locator("main")).toContainText(
      "does not corroborate the OSS index's private identifier",
    );
  }

  await page.goto("./people/f626df86-e8ce-5a4c-a5f8-8edd6dee0c36/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("general office clerk");

  await page.goto("./people/183f6730-bfbc-5073-b667-af9b5f760bb9/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
    await expect(page.locator("main")).toContainText("occupation code is undefined");

  await page.goto("./people/ae0e2726-54ea-55db-8d2b-d73fc683c89b/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("sales clerk");
});

test("Batch 117 preserves Aznone-through-Babberle occupations, unit context, and unresolved identities", async ({
  page,
}) => {
  const profiles = [
    ["9f334c9a-29ab-5663-905a-3cb6147d9342", "James W Aznone", "27", "unknown or indeterminate"],
    ["93b02d0d-d68e-5a81-8a00-416d2b567ea7", "Matthew F Azzarone", "27", "enlisted army personnel"],
    ["2b353d00-f2ec-57df-bcde-8d9278ceff9b", "Josephine Azzolina", "27", "commissioned army officer"],
    ["0a0fddcf-bc32-5755-81f6-eb42f77f3ee3", "Philip Azzolina", "27", "enlisted army personnel"],
    ["3e2607ec-b3db-51f6-9585-c2326eca351a", "Knud Baagoe", "28", "unknown or indeterminate"],
    ["84f902a8-4e02-59f1-af9c-e48b8ad4fa6b", "Mike Baarsvik", "28", "enlisted army personnel"],
    ["9f88e86c-8e55-5b33-ab89-af4985d8bf0a", "Thomas T Baba", "28", "enlisted army personnel"],
    ["98b44ae8-de39-5cf7-b4b5-f7722ee9d1de", "Gust J Babalis", "28", "enlisted army personnel"],
    ["5dace43d-c78f-556d-9b4a-3ee1f341e88f", "John E Babb", "28", "commissioned army officer"],
    ["feaf1259-dbda-50fa-aebd-b0ce8c55ad0c", "Stanley L Babberle", "28", "enlisted army personnel"],
  ];

  for (const [personId, displayName, box, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "9f334c9a-29ab-5663-905a-3cb6147d9342",
    "2b353d00-f2ec-57df-bcde-8d9278ceff9b",
    "3e2607ec-b3db-51f6-9585-c2326eca351a",
    "9f88e86c-8e55-5b33-ab89-af4985d8bf0a",
    "5dace43d-c78f-556d-9b4a-3ee1f341e88f",
    "feaf1259-dbda-50fa-aebd-b0ce8c55ad0c",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/93b02d0d-d68e-5a81-8a00-416d2b567ea7/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("semiskilled machine-shop occupation");

  await page.goto("./people/0a0fddcf-bc32-5755-81f6-eb42f77f3ee3/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("metal-products fabrication occupation");
  await expect(page.locator("main")).toContainText("1890-born Meriden bandmaster namesake");

  await page.goto("./people/84f902a8-4e02-59f1-af9c-e48b8ad4fa6b/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("fireman other than process fireman");
  await expect(page.locator("main")).toContainText("Company A, 99th Infantry");
  await expect(
    page.getByRole("link", { name: "10th Mountain Division Name Index", exact: true }).first(),
  ).toHaveAttribute("href", /denverlibrary\.org/);

  await page.goto("./people/98b44ae8-de39-5cf7-b4b5-f7722ee9d1de/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("OSS Greek Group VII");
  await expect(page.locator("main")).toContainText("occupation code is undefined");
});

test("Batch 118 preserves Babcock-through-Babyak identity thresholds and occupation-only evidence", async ({
  page,
}) => {
  const profiles = [
    ["838b1019-92ca-5a2f-873e-1fc57ca6e3b3", "George H Babcock", "enlisted army personnel"],
    ["2b7136ca-64e9-5595-a77d-dc2ac261ffaa", "Merrill Babcock", "civilian professional or administrative grade"],
    ["aecb7f9d-a24c-5ffd-8326-075fb010afa8", "Richard Babcock", "unknown or indeterminate"],
    ["3a81418e-d2e2-5ed9-8472-10f0da9f99dc", "Mike Babich", "enlisted naval personnel"],
    ["ac85983d-371b-5da5-85ea-8a63525c76c2", "Milan Babich", "unknown or indeterminate"],
    ["277ec46f-71e7-56b0-b366-ca7f1f9c9bb5", "Millard A Babin Jr.", "enlisted army personnel"],
    ["a5e4b2af-6c97-5c0b-b678-5837327e3495", "Thomas Babin", "unknown or indeterminate"],
    ["109c88d7-47cc-58b9-a08a-c78217da239f", "Raymond P Babineau", "commissioned army officer"],
    ["6f8d5426-4180-5d99-b153-f4292973ebaf", "Arthur A Babst", "enlisted naval personnel"],
    ["2340e205-3f27-5f47-982c-8fbcfdba9782", "Andrew H Babyak", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("28", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "2b7136ca-64e9-5595-a77d-dc2ac261ffaa",
    "aecb7f9d-a24c-5ffd-8326-075fb010afa8",
    "3a81418e-d2e2-5ed9-8472-10f0da9f99dc",
    "ac85983d-371b-5da5-85ea-8a63525c76c2",
    "277ec46f-71e7-56b0-b366-ca7f1f9c9bb5",
    "6f8d5426-4180-5d99-b153-f4292973ebaf",
    "2340e205-3f27-5f47-982c-8fbcfdba9782",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/838b1019-92ca-5a2f-873e-1fc57ca6e3b3/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("occupation code is undefined");

  await page.goto("./people/a5e4b2af-6c97-5c0b-b678-5837327e3495/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("longshoreman in Hoboken");
  await expect(page.locator("main")).toContainText("occupation with uncertain sequence");
  await expect(page.getByRole("link", { name: /GRU agent Thomas Babin is going to Cairo/ }).first()).toHaveAttribute("href", /nsa\.gov/);
  await expect(page.getByRole("link", { name: "Venona: Decoding Soviet Espionage in America", exact: true }).first()).toHaveAttribute("href", /jstor\.org/);

  await page.goto("./people/109c88d7-47cc-58b9-a08a-c78217da239f/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("probable, not confirmed");
  await expect(page.locator("main")).toContainText("postwar Michigan State Vietnam Project records");
  await expect(page.getByRole("link", { name: "Vietnam Project Records UA.2.9.5.5", exact: true }).first()).toHaveAttribute("href", /msu\.edu/);

  await page.goto("./people/2b7136ca-64e9-5595-a77d-dc2ac261ffaa/");
  await expect(page.locator("main")).toContainText("Caf-4");
  await page.goto("./people/3a81418e-d2e2-5ed9-8472-10f0da9f99dc/");
  await expect(page.locator("main")).toContainText("SK 3/c");
  await expect(page.locator("main")).toContainText("steelworker namesake");
  await page.goto("./people/6f8d5426-4180-5d99-b153-f4292973ebaf/");
  await expect(page.locator("main")).toContainText("BM2/c T");
});

test("Batch 119 preserves Bachand-through-Backus identity thresholds and withholds unsupported affiliations", async ({
  page,
}) => {
  const profiles = [
    ["dfcbff26-7581-5857-9c23-accd043b188a", "Albert E Bachand", "enlisted army personnel"],
    ["8e607803-bc87-55b3-8b24-fc43d26869ba", "Walter F Bachelder", "commissioned army officer"],
    ["99747044-53c6-54a1-8cfd-407b3b53159a", "Robert J Bachman", "unknown or indeterminate"],
    ["b59a4ab1-e194-5240-a720-cb0814d8e57c", "Albert V Bacik", "enlisted army personnel"],
    ["addae8c4-4269-5ea3-bac0-6c0744088869", "Ross E Backenstoss Jr.", "enlisted army personnel"],
    ["21c1e081-60b4-5a46-a8f9-bd7f41c6e088", "Mary E Backle", "unknown or indeterminate"],
    ["b7854fe9-538f-5bca-a32c-d7b09cbf8464", "Gilbert O Backman", "commissioned army officer"],
    ["bbcace2e-c73f-5769-91d5-ffadeadd9714", "Rose M Backman", "civilian professional or administrative grade"],
    ["f1b2aa73-74aa-58bd-a631-31b952b13fe2", "Alice C Backus", "civilian professional or administrative grade"],
    ["97acbe69-3d25-59da-a57e-641ec2e0e250", "Emmett F Backus", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("28", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "dfcbff26-7581-5857-9c23-accd043b188a",
    "99747044-53c6-54a1-8cfd-407b3b53159a",
    "bbcace2e-c73f-5769-91d5-ffadeadd9714",
    "f1b2aa73-74aa-58bd-a631-31b952b13fe2",
    "97acbe69-3d25-59da-a57e-641ec2e0e250",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/8e607803-bc87-55b3-8b24-fc43d26869ba/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("declassified 1944 personnel-interview index");
  await expect(
    page.getByRole("link", {
      name: "Index of personnel interviewed in the North African theater of operations",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /digitalcollections\.hoover\.org/);
  await expect(page.locator("main")).toContainText("Testing Machines Inc. began in 1947");

  await page.goto("./people/b7854fe9-538f-5bca-a32c-d7b09cbf8464/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("second lieutenant stationed at Bari");

  await page.goto("./people/b59a4ab1-e194-5240-a720-cb0814d8e57c/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Team Arthur");
  await expect(page.locator("main")).toContainText("roster is secondary and lacks the private identifier");

  await page.goto("./people/addae8c4-4269-5ea3-bac0-6c0744088869/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Ross Elwood Backenstoss, Jr.");
  await expect(
    page.getByRole("link", {
      name: "Figures of speech in the dramas of Heinrich von Kleist: An investigation into Kleist's style",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /drum\.lib\.umd\.edu/);

  await page.goto("./people/21c1e081-60b4-5a46-a8f9-bd7f41c6e088/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("civilian secretary documented in a 1946 Strategic Services Unit successor record");
  await expect(page.locator("main")).toContainText("post-OSS identity evidence only");

  await page.goto("./people/bbcace2e-c73f-5769-91d5-ffadeadd9714/");
  await expect(page.locator("main")).toContainText("Caf-3");
  await page.goto("./people/f1b2aa73-74aa-58bd-a631-31b952b13fe2/");
  await expect(page.locator("main")).toContainText("Caf-4");
});

test("Batch 120 separates qualified employment, occupation-only findings, Allied identity, and unresolved names", async ({
  page,
}) => {
  const profiles = [
    ["87d86f1e-1bf0-52e1-ab62-49f1b280cb53", "Samuel D Backus", "enlisted army personnel"],
    ["2feacabe-6765-5fa7-b461-4cf5cbd58961", "Charles A Bacon Jr.", "enlisted army personnel"],
    ["59e0bb4f-5401-5fa9-b29a-23f9fae4a094", "Elizabeth E Bacon", "civilian professional or administrative grade"],
    ["7b21a9d1-d92f-5c68-ad6c-df3e1a38835e", "Greta Bacon", "unknown or indeterminate"],
    ["a080d69e-3897-5017-b0f8-46f1a7288c5a", "Gwendel Bacote", "unknown or indeterminate"],
    ["77c2ed93-890a-5fb2-b026-740b764821fb", "Albert E Bacquet", "foreign or allied military personnel"],
    ["dffaed52-359a-546e-8eff-be1020f52aa4", "Steve Bacsik", "enlisted army personnel"],
    ["b5f9a9e0-af69-587f-b337-0268526c42b2", "Michael Baczynski", "unknown or indeterminate"],
    ["c59d3b95-016e-530f-9407-17f99c6ca304", "Nate A Badami", "enlisted army personnel"],
    ["806ef924-35cf-55e5-9209-45ee594c1953", "James W Bader", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("28", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  for (const personId of profiles.map(([personId]) => personId).filter(
    (personId) => personId !== "59e0bb4f-5401-5fa9-b29a-23f9fae4a094",
  )) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const personId of [
    "7b21a9d1-d92f-5c68-ad6c-df3e1a38835e",
    "a080d69e-3897-5017-b0f8-46f1a7288c5a",
    "dffaed52-359a-546e-8eff-be1020f52aa4",
    "b5f9a9e0-af69-587f-b337-0268526c42b2",
    "806ef924-35cf-55e5-9209-45ee594c1953",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/87d86f1e-1bf0-52e1-ab62-49f1b280cb53/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("occupation code is undefined");

  await page.goto("./people/2feacabe-6765-5fa7-b461-4cf5cbd58961/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("semiskilled photographic-process occupation");

  await page.goto("./people/59e0bb4f-5401-5fa9-b29a-23f9fae4a094/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("documented prewar employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("University of Washington");
  await expect(page.locator("main")).toContainText("Instructor in Far Eastern Studies");
  await expect(page.locator("main")).toContainText("immediate transition is not established");
  await expect(
    page.getByRole("link", { name: "University of Washington General Catalog, 1944-1945", exact: true }).first(),
  ).toHaveAttribute("href", /washington\.edu/);

  await page.goto("./people/a080d69e-3897-5017-b0f8-46f1a7288c5a/");
  await expect(page.locator("main")).toContainText("Gwendolyn Bacote (search alias only)");

  await page.goto("./people/77c2ed93-890a-5fb2-b026-740b764821fb/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("Commissioned officer", { exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("French Army sous-lieutenant");
  await expect(page.locator("main")).toContainText("Jean Coulombel");
  await expect(page.getByRole("link", { name: "Albert Bacquet: Silver Star", exact: true }).first()).toHaveAttribute("href", /militarytimes\.com/);

  await page.goto("./people/c59d3b95-016e-530f-9407-17f99c6ca304/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("textile-products fabrication occupation");
  await expect(page.locator("main")).toContainText("Valentine-Livingston Shore Party");

  await page.goto("./people/dffaed52-359a-546e-8eff-be1020f52aa4/");
  await expect(page.locator("main")).toContainText("Do not assign the cemetery candidate");
  await expect(page.locator("main")).toContainText("without a second corroborating identifier");
});

test("Batch 121 preserves an identifier conflict, occupation-only evidence, a withheld namesake, and qualified Baerwald pathways", async ({
  page,
}) => {
  const profiles = [
    ["aa4e55e6-7df0-507b-a569-a7cb95a40391", "Daniel E Badia", "28", "unknown or indeterminate"],
    ["8adef22b-921c-5312-bbd0-d484f4b12076", "Leo P Badia", "28", "commissioned army officer"],
    ["fbfe354a-5c57-5332-9999-756dffd65792", "Edna Badinger", "28", "civilian professional or administrative grade"],
    ["5c4a673c-b96b-51de-b199-62615a23945f", "Joseph T Badzik", "28", "enlisted army personnel"],
    ["61699b2c-cb14-5a6c-8166-10a85ac2ef52", "Robert E Baehr", "29", "commissioned army officer"],
    ["6c2adeb2-d2b4-5fc6-acb4-900401950437", "Barbara Baer", "29", "civilian professional or administrative grade"],
    ["99182302-f039-5cb9-b850-8e7eeddc4464", "Edwin I Baer", "29", "enlisted army personnel"],
    ["641f0708-19cc-5cef-92d4-dceb54e9cc8a", "Ralph H Baer", "29", "unknown or indeterminate"],
    ["38c74198-8d92-5c42-a1ca-27825f318f80", "Vivian L Baer", "29", "enlisted army personnel"],
    ["e8d8e303-f72c-54a4-b3fb-3134865690a0", "Ernest D Baerwald", "29", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, box, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••[A-Z0-9]{4})$/);
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold");
  }

  for (const personId of [
    "aa4e55e6-7df0-507b-a569-a7cb95a40391",
    "8adef22b-921c-5312-bbd0-d484f4b12076",
    "fbfe354a-5c57-5332-9999-756dffd65792",
    "61699b2c-cb14-5a6c-8166-10a85ac2ef52",
    "6c2adeb2-d2b4-5fc6-acb4-900401950437",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/5c4a673c-b96b-51de-b199-62615a23945f/");
  await expect(page.getByText("conflicting", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("conflicting sources", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("belongs to William R. Brandes");
  await expect(page.locator("main")).toContainText("Do not assign William R. Brandes's occupation");
  await expect(page.locator("main")).not.toContainText("unskilled machine-shop occupation");

  await page.goto("./people/99182302-f039-5cb9-b850-8e7eeddc4464/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("general-office clerk occupation");
  await expect(page.locator("main")).toContainText("but no employer");

  await page.goto("./people/38c74198-8d92-5c42-a1ca-27825f318f80/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Women's Army Corps");
  await expect(page.locator("main")).toContainText("stenographer and typist occupation");

  await page.goto("./people/641f0708-19cc-5cef-92d4-dceb54e9cc8a/");
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("famous biography is withheld");
  await expect(page.getByRole("link", { name: "Ralph H. Baer Papers", exact: true })).toHaveCount(0);

  await page.goto("./people/e8d8e303-f72c-54a4-b3fb-3134865690a0/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("documented prewar employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Doitsu Senryo Gomei Kaisha");
  await expect(page.locator("main")).toContainText("not established as his immediate pre-OSS employer");
  await expect(page.locator("main")).toContainText("American Jewish Joint Distribution Committee");
  await expect(page.locator("main")).toContainText("professional affiliation");
  await expect(
    page.getByRole("link", { name: "Japanese-American Applications", exact: true }).first(),
  ).toHaveAttribute("href", /digicoll\.lib\.berkeley\.edu/);
  await expect(
    page.getByRole("link", { name: "JDC Digest, October 1952", exact: true }).first(),
  ).toHaveAttribute("href", /americanjewisharchives\.org/);
});

test("Batch 122 preserves occupation-only evidence, a spelling variant, film-profession limits, and Box 29 review paths", async ({
  page,
}) => {
  const profiles = [
    ["2c346890-fb26-5a92-b5a4-b251881e3e94", "Philip H Bagby", "enlisted army personnel"],
    ["8ba31ed6-ab93-5be9-816e-17e5e0e77fc6", "Percy A Bagge", "unknown or indeterminate"],
    ["5b974ba7-02d8-5215-a43c-ab3742916fb5", "Robert K Baggot", "unknown or indeterminate"],
    ["3afb0f7d-09b2-5e73-9137-a6f70372ddd7", "Douglas W Bagier", "unknown or indeterminate"],
    ["2246cbd8-47f5-512a-a83f-ce147833ba8a", "Helene B Baginski", "civilian professional or administrative grade"],
    ["dcc6d19d-6cc9-5040-ac4b-ca1d330a081b", "Irving J Bagle", "enlisted army personnel"],
    ["1bbd4776-c3e1-5845-9022-95ac13c6bcfa", "David J Bagley", "civilian professional or administrative grade"],
    ["99fd7c45-e5e4-5095-9b88-eb01859ff071", "Merrill B Bahnson", "enlisted army personnel"],
    ["dfde6e18-5e77-5a72-bcbe-359f96c47a24", "Sidney Bah-Oh", "unknown or indeterminate"],
    ["6fd46b84-860f-5373-b7b1-6bf1f7e60112", "Frank P Bahor", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("29", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
  }

  for (const personId of [
    "8ba31ed6-ab93-5be9-816e-17e5e0e77fc6",
    "5b974ba7-02d8-5215-a43c-ab3742916fb5",
    "2246cbd8-47f5-512a-a83f-ce147833ba8a",
    "1bbd4776-c3e1-5845-9022-95ac13c6bcfa",
    "dfde6e18-5e77-5a72-bcbe-359f96c47a24",
    "6fd46b84-860f-5373-b7b1-6bf1f7e60112",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/2c346890-fb26-5a92-b5a4-b251881e3e94/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("general-office clerk occupation");
  await expect(page.locator("main")).toContainText("but no employer");

  await page.goto("./people/3afb0f7d-09b2-5e73-9137-a6f70372ddd7/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Wolfgang Loë-Bagier");
  await expect(page.locator("main")).toContainText("No production company is inferred as an employer from film credits alone");
  await expect(page.locator('a[href*="filmportal.de"]', { hasText: "Wolfgang Loë-Bagier" }).first()).toHaveAttribute(
    "href",
    /filmportal\.de/,
  );

  await page.goto("./people/dcc6d19d-6cc9-5040-ac4b-ca1d330a081b/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Irving J Eagle");
  await expect(page.locator("main")).toContainText("sailor or deckhand occupation");
  await expect(page.locator("main")).toContainText("but no employer or vessel");

  await page.goto("./people/99fd7c45-e5e4-5095-9b88-eb01859ff071/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("motor-vehicle mechanic and repairer occupation");
  await expect(page.locator("main")).toContainText("but no employer");

  await page.goto("./people/2246cbd8-47f5-512a-a83f-ce147833ba8a/");
  await expect(page.locator("main")).toContainText("personnel file exists in Record Group 226, Box 29, and is not digitized");
  await expect(
    page.getByRole("link", { name: "Seeking OSS Asset File on Zygfryd Baginski", exact: true }).first(),
  ).toHaveAttribute("href", /openhistoryhub\.com/);
});

test("Batch 123 publishes two bounded occupation findings and preserves eight Box 29 review paths", async ({
  page,
}) => {
  const profiles = [
    ["559309fa-88a8-550b-8c95-c085e8b83037", "Bodizar Bahoric", "unknown or indeterminate"],
    ["fa91697c-5bb9-570b-a94d-3c547c19a12d", "Robert J Bahr", "unknown or indeterminate"],
    ["1978b14a-7988-5fc3-9bf0-84da6ecd7900", "E J Bailey", "civilian professional or administrative grade"],
    ["40d5ef96-f9ca-53d6-b900-0a46cdde5577", "Fay I Bailey", "civilian professional or administrative grade"],
    ["282d962b-81b5-5f7d-a342-92f03e4e1605", "Georgia M Bailey", "civilian professional or administrative grade"],
    ["29732da1-3828-50ab-8939-6b5694205d20", "Guy B Bailey", "enlisted army personnel"],
    ["0ca2a771-004b-587e-b948-36940731973b", "Harry F Bailey", "enlisted army personnel"],
    ["b8152325-2736-5d8b-be59-beabbab1de84", "Irving S Bailey", "commissioned army officer"],
    ["a26b5aa7-2648-51fe-95e4-e0d141c6ef93", "Jason S Bailey", "commissioned army officer"],
    ["a423f081-063b-5b30-86f8-2e1a86fee602", "Jay E Bailey", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("29", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
  }

  for (const personId of [
    "559309fa-88a8-550b-8c95-c085e8b83037",
    "fa91697c-5bb9-570b-a94d-3c547c19a12d",
    "1978b14a-7988-5fc3-9bf0-84da6ecd7900",
    "40d5ef96-f9ca-53d6-b900-0a46cdde5577",
    "282d962b-81b5-5f7d-a342-92f03e4e1605",
    "b8152325-2736-5d8b-be59-beabbab1de84",
    "a26b5aa7-2648-51fe-95e4-e0d141c6ef93",
    "a423f081-063b-5b30-86f8-2e1a86fee602",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/559309fa-88a8-550b-8c95-c085e8b83037/");
  await expect(page.locator("main")).toContainText("aka Boz");
  await expect(page.locator("main")).toContainText("Bozidar Bahoric remains a search candidate only");

  await page.goto("./people/29732da1-3828-50ab-8939-6b5694205d20/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("dairy farm-hand occupation category");
  await expect(page.locator("main")).toContainText("November 1945 Army entry or recall");
  await expect(page.locator("main")).toContainText("but names no farm or employer");

  await page.goto("./people/0ca2a771-004b-587e-b948-36940731973b/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("bus, taxi, truck, or tractor driver occupation category");
  await expect(page.locator("main")).toContainText("but no employer");

  for (const personId of [
    "29732da1-3828-50ab-8939-6b5694205d20",
    "0ca2a771-004b-587e-b948-36940731973b",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
  }
});

test("Batch 124 publishes four bounded occupation findings and preserves six Box 29-30 review paths", async ({
  page,
}) => {
  const profiles = [
    ["32b39a22-46a3-58da-ac3e-2ebac9b8b041", "Kenneth R Bailey", "29", "enlisted army personnel"],
    ["261108f5-ad5e-59d8-8bd3-eaf921ebb2b5", "Marcella D Bailey", "29", "unknown or indeterminate"],
    ["f5e03503-cedd-5521-b9c9-ba03bdebc35e", "Morris F Bailey", "29", "enlisted army personnel"],
    ["5e88f040-b80c-5b3b-8aad-db6c1263a76b", "Robert C Bailey", "29", "enlisted army personnel"],
    ["6299bf2d-05ad-58d0-b843-5eb78921c785", "Stephen K Bailey", "29", "commissioned army officer"],
    ["3bbd389e-5d2a-5f0d-9d62-67d47df29282", "Thomas H Bailey", "30", "enlisted army personnel"],
    ["c3ebcc15-2b6b-5cec-ac5d-d4116d02ba38", "Urcle G Bailey", "30", "unknown or indeterminate"],
    ["bf479992-9db8-5c6f-b295-ae8392d85e27", "Waldo E Bailey", "30", "enlisted army personnel"],
    ["bd08c2d0-6865-52b7-b687-275c2fd3b0a7", "Walter H Bailey", "30", "enlisted army personnel"],
    ["d49fcf33-5991-5ae9-a553-1fee9d476bef", "Walter L Bailey", "30", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, box, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const personId of [
    "261108f5-ad5e-59d8-8bd3-eaf921ebb2b5",
    "5e88f040-b80c-5b3b-8aad-db6c1263a76b",
    "6299bf2d-05ad-58d0-b843-5eb78921c785",
    "c3ebcc15-2b6b-5cec-ac5d-d4116d02ba38",
    "bf479992-9db8-5c6f-b295-ae8392d85e27",
    "d49fcf33-5991-5ae9-a553-1fee9d476bef",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  const occupationProfiles = [
    ["32b39a22-46a3-58da-ac3e-2ebac9b8b041", "occupation category students"],
    ["f5e03503-cedd-5521-b9c9-ba03bdebc35e", "semiskilled routeman occupation category"],
    ["3bbd389e-5d2a-5f0d-9d62-67d47df29282", "photographer occupation category"],
    ["bd08c2d0-6865-52b7-b687-275c2fd3b0a7", "college presidents, professors, and instructors"],
  ];
  for (const [personId, claimText] of occupationProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
    await expect(page.locator("main")).toContainText(claimText);
  }

  await page.goto("./people/c3ebcc15-2b6b-5cec-ac5d-d4116d02ba38/");
  await expect(page.locator("main")).toContainText("compare those identifiers with the 1937-1938 Montana laundry-work candidate");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Batch 125 publishes two bounded occupations, one qualified opera pathway, and preserves Box 30 review", async ({
  page,
}) => {
  const profiles = [
    ["12464bf5-aa0b-5557-9516-3327d31f35d8", "Wilbur A Bailey", "unknown or indeterminate"],
    ["dc098456-c914-58ff-a062-a9d698f8afa3", "William M Bailey", "unknown or indeterminate"],
    ["05927d43-6d23-512f-a833-926c92131485", "William H Bailey", "enlisted army personnel"],
    ["415a002f-d297-5b62-ad6f-f70f75932278", "William J Bailey", "enlisted army personnel"],
    ["b6332ea3-da17-5971-a20e-ea824f27123d", "James Bain Jr.", "commissioned army officer"],
    ["4b9159e8-fff6-5eb5-97aa-98e169d29387", "John R Baine", "commissioned army officer"],
    ["3e469244-4c57-51ab-ab17-8af519d26039", "Raymond Baine", "unknown or indeterminate"],
    ["d80f34a4-c1ed-5c35-aca7-ef5ceddc87ff", "Ruth E Bains", "civilian professional or administrative grade"],
    ["83c7ce46-9c54-57f9-be58-a16939694686", "Charles A Bair", "unknown or indeterminate"],
    ["37845f5b-64e1-52fe-9f26-9c55342be68c", "William D Bair", "commissioned army officer"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("30", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const personId of [
    "12464bf5-aa0b-5557-9516-3327d31f35d8",
    "dc098456-c914-58ff-a062-a9d698f8afa3",
    "05927d43-6d23-512f-a833-926c92131485",
    "415a002f-d297-5b62-ad6f-f70f75932278",
    "b6332ea3-da17-5971-a20e-ea824f27123d",
    "3e469244-4c57-51ab-ab17-8af519d26039",
    "d80f34a4-c1ed-5c35-aca7-ef5ceddc87ff",
    "83c7ce46-9c54-57f9-be58-a16939694686",
    "37845f5b-64e1-52fe-9f26-9c55342be68c",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
  }

  for (const personId of [
    "12464bf5-aa0b-5557-9516-3327d31f35d8",
    "dc098456-c914-58ff-a062-a9d698f8afa3",
    "3e469244-4c57-51ab-ab17-8af519d26039",
    "d80f34a4-c1ed-5c35-aca7-ef5ceddc87ff",
    "83c7ce46-9c54-57f9-be58-a16939694686",
    "37845f5b-64e1-52fe-9f26-9c55342be68c",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/05927d43-6d23-512f-a833-926c92131485/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("floormen and floor managers, stores");
  await expect(page.locator("main")).toContainText("names no store or employer");

  await page.goto("./people/415a002f-d297-5b62-ad6f-f70f75932278/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("stock-clerk occupation category");
  await expect(page.locator("main")).toContainText("names no business, warehouse, retailer, or other employer");

  await page.goto("./people/b6332ea3-da17-5971-a20e-ea824f27123d/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("later official Regular Army appointment record");

  await page.goto("./people/4b9159e8-fff6-5eb5-97aa-98e169d29387/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "Philadelphia Lyric Opera",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "member and opera tenor",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("medium");
  await expect(page.locator("main")).toContainText("professional affiliation");

  for (const personId of [
    "4b9159e8-fff6-5eb5-97aa-98e169d29387",
    "3e469244-4c57-51ab-ab17-8af519d26039",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.locator(".profile-aside")).toContainText("duplicate-649706dcfb20");
  }
});

test("Batch 126 separates two occupations, an Army-to-OSS pathway, student status, and six archival cases", async ({
  page,
}) => {
  const profiles = [
    ["acb63214-0135-5fba-a4a3-5bc38462855a", "Alexander W Baird", "enlisted army personnel"],
    ["f111ddba-4bf2-5a3c-8dca-4830d6da4432", "Beverly B Baird", "unknown or indeterminate"],
    ["1f6291a3-ca19-50b2-a2eb-0f76b84a0dcb", "John W Baird", "unknown or indeterminate"],
    ["4b243752-8c80-566d-91f8-17a5915ef158", "Kenneth W Baird", "commissioned army officer"],
    ["f84c2c75-0f0d-5535-897a-5574671c6d47", "Louis R Baird", "enlisted army personnel"],
    ["85a3ea5b-ca9f-53c1-b4f9-035909346204", "Robert R Baird Jr.", "enlisted army personnel"],
    ["2ecc388d-2765-54e7-9bf2-c6e7d389120a", "Virginia C Baird", "civilian professional or administrative grade"],
    ["0f9120d1-e0b4-500d-95f7-e0eee88ef40e", "Michael Bakalar", "civilian professional or administrative grade"],
    ["1848de15-d820-55e9-b17c-ed55c32edf2f", "Andrew H Baker", "enlisted army personnel"],
    ["1bb25e1f-4ec9-5b0b-a966-8ce9c3e1ea46", "Arthur Baker III", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("30", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const personId of [
    "f111ddba-4bf2-5a3c-8dca-4830d6da4432",
    "1f6291a3-ca19-50b2-a2eb-0f76b84a0dcb",
    "4b243752-8c80-566d-91f8-17a5915ef158",
    "f84c2c75-0f0d-5535-897a-5574671c6d47",
    "2ecc388d-2765-54e7-9bf2-c6e7d389120a",
    "0f9120d1-e0b4-500d-95f7-e0eee88ef40e",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
  }

  await page.goto("./people/acb63214-0135-5fba-a4a3-5bc38462855a/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("commercial artists");
  await expect(page.locator("main")).toContainText("names no studio, agency, company, or other employer");

  await page.goto("./people/85a3ea5b-ca9f-53c1-b4f9-035909346204/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("skilled food-production occupation category");
  await expect(page.locator("main")).toContainText("names no manufacturer or other employer");

  await page.goto("./people/1848de15-d820-55e9-b17c-ed55c32edf2f/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("occupation field is an undefined code");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );

  await page.goto("./people/1bb25e1f-4ec9-5b0b-a966-8ce9c3e1ea46/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "United States Army",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "Camp Hale",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "military assignment",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "Wesleyan University",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "student",
  );
  await expect(page.locator("main")).toContainText(
    "Following this training he volunteered for the U.S. Army Office of Strategic Services",
  );
});

test("Batch 127 preserves ten unresolved Baker profiles and the LT COM naval classification", async ({
  page,
}) => {
  const profiles = [
    ["c03d80bb-50e5-5e7a-b6d6-4c8c23d6cdb3", "Ben Baker", "enlisted army personnel", "30"],
    ["0abb9bc6-e6ab-5608-95a0-81de145f109c", "Bonnie T Baker", "unknown or indeterminate", "30"],
    ["02a0b270-7beb-5b2c-a104-e8ef8d9bdc54", "Charles E Baker", "enlisted army personnel", "30"],
    ["8637c2ee-116a-5ec8-9da1-583675ed95be", "Charles W Baker", "enlisted army personnel", "30"],
    ["9d478406-0195-5938-80e4-ca2d8f57e110", "Clarence L Baker", "enlisted army personnel", "30"],
    ["76f7de96-0540-5535-aac4-90ebc7ff9dcd", "Donald S Baker", "enlisted army personnel", "30"],
    ["52a5cc22-3ccc-55aa-90e7-379b85a522b6", "Douglas H Baker", "commissioned army officer", "30"],
    ["77ed90e4-bb4e-569d-afdb-b1a3ea2dc17c", "Dwight C Baker", "commissioned naval officer", "30"],
    ["7f082c51-dac2-52b6-85c4-ad6b001fd200", "Evan D Baker", "enlisted army personnel", "31"],
    ["c9226b5a-6af6-5565-825a-e3001284dd2d", "Ford P Baker", "enlisted army personnel", "31"],
  ];

  for (const [personId, displayName, personnelCategory, box] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/77ed90e4-bb4e-569d-afdb-b1a3ea2dc17c/");
  await expect(page.locator("main")).toContainText("LT COM");
  await expect(page.locator("dt", { hasText: "Commissioned officer" }).locator("+ dd")).toHaveText(
    "Yes",
  );

  await page.goto("./people/52a5cc22-3ccc-55aa-90e7-379b85a522b6/");
  await expect(page.locator("main")).toContainText("605th Field Artillery candidate");
  await expect(page.locator("main")).toContainText("only if the file supplies matching identifiers");
});

test("Batch 128 qualifies Gibbs Baker's law practice and preserves nine unresolved Box 31 profiles", async ({
  page,
}) => {
  const unresolvedProfiles = [
    ["1c3617ff-b86f-58d4-9cf6-126172babe81", "George S Baker", "unknown or indeterminate"],
    ["29a3041c-cab4-5fbe-87c1-77a6260c3ec8", "Harold L Baker", "enlisted army personnel"],
    ["ac091ddd-5202-54a0-843f-731dd3ea6232", "Jack Baker", "enlisted army personnel"],
    ["0f54ce63-d8ef-5486-92cd-fc65dd9cd8bb", "Jamems A Baker", "enlisted army personnel"],
    ["ef0c10c2-e3c0-5253-bec1-1993aca8c86d", "Jane Baker", "unknown or indeterminate"],
    ["5421b053-c062-5c17-9908-d201167e4def", "John B Baker", "commissioned army officer"],
    ["dfb244bf-ec41-5e93-9540-a8356c16a40c", "John S Baker", "unknown or indeterminate"],
    ["901e6f33-9d7f-5451-b4cf-79f7d00ce712", "Joseph R Baker", "enlisted army personnel"],
    ["3ab54057-45fd-5bfb-827e-4c2246f80ef9", "Joseph A Baker", "enlisted army personnel"],
  ];

  for (const [personId, displayName, personnelCategory] of unresolvedProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("31", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/fb97a7ef-7e57-5d16-84c1-e45470dca992/");
  await expect(page.getByRole("heading", { name: "Gibbs L Baker", exact: true })).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("commissioned naval officer");
  await expect(page.locator("main")).toContainText("LT JG");
  await expect(page.locator("dt", { hasText: "Commissioned officer" }).locator("+ dd")).toHaveText(
    "Yes",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "general-practice lawyer",
  );
  await expect(page.locator("main")).toContainText(
    "practiced general law in Washington from the mid-1930s",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(page.locator("main")).toContainText(
    "Gibbs L. Baker to Harris, Pouch Letter #3, 24 September 1943",
  );
  await expect(page.locator("main")).toContainText(
    "The 1910 Douglas, Baker & Sherrill record belongs to an older namesake and must remain excluded",
  );
});

test("Batch 129 documents Baker's Ohio State and Library of Congress pathways while qualifying the weather candidate", async ({
  page,
}) => {
  const unresolvedProfiles = [
    ["56e95210-bf70-5342-afc5-b511d84a05c2", "Levi J Baker", "commissioned army officer"],
    ["1540e189-7b4c-5528-a9fa-754c14db44db", "Marvin D Baker", "enlisted army personnel"],
    ["a84ef72a-98e1-5b1e-a9d7-d3f404afebb2", "Nicholas J Baker", "enlisted army personnel"],
    ["a1d3990a-5804-52bf-a4af-9c223b242ec9", "Ralph P Baker", "commissioned army officer"],
    ["5c919a2d-8039-53c2-909d-d3abb6cb19ea", "Rosalie M Baker", "civilian professional or administrative grade"],
    ["ffb2ae03-c09b-5f0f-ab80-a7ba36325a6b", "William A Baker", "enlisted army personnel"],
    ["f7ec0950-934f-56ed-bc52-52155fbf64f2", "William H Baker", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, personnelCategory] of unresolvedProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("31", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/2490f5eb-b7f6-567b-8e4f-a1ae385d4d4d/");
  await expect(page.getByRole("heading", { name: "Kenneth H Baker", exact: true })).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("verified employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "Ohio State University",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Ohio State University",
  );
  await expect(page.locator("main")).toContainText("Kenneth Hammond Baker");
  await expect(page.locator("main")).toContainText("assistant professor of psychology");

  await page.goto("./organizations/de52c90c-62bc-532e-a99e-a7d9ca019c09/");
  await expect(page.getByRole("heading", { name: "The Ohio State University", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Kenneth H Baker");

  await page.goto("./people/179dfadc-1686-5c3c-a22a-ad401b10d959/");
  await expect(page.getByRole("heading", { name: "Richard B Baker", exact: true })).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "Library of Congress",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "government assignment",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "The Providence Journal",
  );
  await expect(page.locator("main")).toContainText("Richard Brown Baker");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/1abbbf6f-6165-5224-86bc-a3aaf7272693/");
  await expect(page.getByRole("heading", { name: "Ralph C Baker", exact: true })).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("needs identity review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("19th Weather Squadron");
  await expect(page.locator("main")).toContainText("identity is not yet resolved");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Batch 130 preserves ten source rows, resolves Ballachey's employer, and qualifies Balasy and the duplicate", async ({
  page,
}) => {
  const archivalProfiles = [
    ["825e2153-d4bc-57d7-9f27-a8dd08c54219", "Dorothy J Bakewell", "civilian professional or administrative grade"],
    ["f68ced73-7fb5-587a-8014-a2fb8ae43948", "John J Bakey", "civilian professional or administrative grade"],
    ["7199f8ea-c7ae-5fbf-bd15-2f736f872436", "John G Bakirdgis", "enlisted army personnel"],
    ["1388b08c-f412-527c-bdd7-288791239792", "Romeo Balaguer", "unknown or indeterminate"],
    ["d52dd821-1ff5-5e1e-a9bd-1eac3e74f6d7", "Duane H Balasty", "unknown or indeterminate"],
    ["6fbec944-2c27-5115-84d4-e830c1fac290", "William E Balazs", "commissioned army officer"],
    ["784a9be5-53b6-5529-af73-91c334772d47", "Wambley Bald", "unknown or indeterminate"],
    ["543edc0e-58a2-571a-a738-df7901b87829", "Stephen W Baldanza", "unknown or indeterminate"],
  ];

  for (const [personId, displayName, personnelCategory] of archivalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("31", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/5672d792-8da0-53b3-890f-e1b432c2ff25/");
  await expect(page.getByRole("heading", { name: "Anthony I Balasy", exact: true })).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("needs temporal review", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "Royal Hungarian Legation",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "government assignment",
  );
  await expect(page.locator("main")).toContainText("Anthony de Balasy");
  await expect(page.locator("main")).toContainText("middle initial I remains unexplained");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );

  await page.goto("./organizations/f59ecdd8-3587-5864-9304-940fab721e8e/");
  await expect(
    page.getByRole("heading", { name: "Royal Hungarian Legation in Washington", exact: true }),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Anthony I Balasy");

  await page.goto("./people/4306b544-8cf8-5651-a935-529961b7d516/");
  await expect(page.getByRole("heading", { name: "Egerton L Baldachey", exact: true })).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("needs identity review", { exact: true }).first()).toBeVisible();
  await expect(page.locator(".profile-aside")).toContainText(/duplicate-[a-f0-9]{12}/);
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );

  await page.goto("./people/4cf8ea80-6bb8-59f5-891f-4f4a9ec12b63/");
  await expect(page.getByRole("heading", { name: "Egerton L Ballachey", exact: true })).toBeVisible();
  await expect(page.locator(".profile-aside").getByText("33", { exact: true })).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("verified employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "Michigan State College",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Michigan State College",
  );
  await expect(page.locator("main")).toContainText("faculty member");
  await expect(page.locator("main")).toContainText("Chief Psychologist in the O.S.S.");

  await page.goto("./organizations/24ac156d-62e6-5107-a412-646391d990a2/");
  await expect(page.getByRole("heading", { name: "Michigan State College", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Egerton L Ballachey");
});

test("Batch 131 separates lend-lease, civilian publishing, Army, advertising, and archival-review pathways", async ({
  page,
}) => {
  const archivalProfiles = [
    ["10a2227d-a411-5247-a1c0-88f745808cc9", "Arthur L Baldwin", "31", "enlisted army personnel"],
    ["f85118a1-f6cc-5dc3-83b5-b899a0e72461", "Philip Baldwin", "32", "unknown or indeterminate"],
    ["7f4bdb55-078d-5aa4-8c46-11425e639461", "Robert L Baldwin", "32", "unknown or indeterminate"],
    ["8942315d-aa6c-57c4-9574-6bb67eadf881", "Robert M Baldwin", "32", "commissioned army officer"],
    ["827226d2-c076-59cf-9324-197ed1ea20ea", "William H Baldwin", "32", "commissioned army officer"],
    ["c578a107-15e2-5333-a298-a2ec2b2a86ef", "Robert N Baldy", "32", "enlisted army personnel"],
    ["ff136d64-7385-52eb-a0ba-76712dff9450", "Dominick Balei", "31", "enlisted army personnel"],
  ];

  for (const [personId, displayName, box, personnelCategory] of archivalProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(personnelCategory);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/95ef5b00-a344-56f8-bd3a-e9253663c53d/");
  await expect(page.getByRole("heading", { name: "Elbert Baldwin", exact: true })).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("verified employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "United States government lend-lease work",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "government assignment",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Research International",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "self employment",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "Business Week",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "United States Department of Commerce",
  );

  await page.goto("./organizations/9cdf3d9c-9512-5c14-9598-52fdfb1b9db7/");
  await expect(page.getByRole("heading", { name: "Research International", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Elbert Baldwin");

  await page.goto("./people/867223c8-19c0-55aa-a36b-d6ed2205a79a/");
  await expect(page.getByRole("heading", { name: "Howard Baldwin", exact: true })).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("worked in advertising before the war");
  await expect(page.locator("main")).toContainText("Do not assign The New Yorker or J. Walter Thompson");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/8d87eb94-a5f8-5d60-92f8-431454346be6/");
  await expect(page.getByRole("heading", { name: "Thomas Baldwin", exact: true })).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "United States Army",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "military assignment",
  );
  await expect(page.locator("main")).toContainText("OSS Detachment 101");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 132 preserves seven unresolved identities and qualifies the three supported Ball identities", async ({
  page,
}) => {
  const allProfiles = [
    ["1cf10caf-6e59-5fc5-b278-cbf615980a5b", "Francis A Balfour"],
    ["0bc6ba50-1e66-5a28-ae1b-be39391fa475", "Nina Balfour"],
    ["b788c7df-4878-5dc7-919e-8b522de27aaa", "Julius M Balick"],
    ["261d6884-1594-526e-b26e-b15e566f6db3", "Joseph A Balint"],
    ["549c77e3-70e8-5d00-88bf-12ffc83f9851", "Dorothy L Balkam"],
    ["ffe506ac-7aa6-5586-808a-05d346e4a2a7", "John Balko"],
    ["2b76d6fd-c67f-540f-9001-f2085cf36dcc", "Berkley C Ball"],
    ["8fcf8786-1fb8-5c27-92b1-d96d355c3f79", "Frank L Ball Jr."],
    ["2ac60374-2c37-5ce7-9d68-926110f51678", "John J Ball Jr."],
    ["d3503752-d5de-5051-8877-bb516c708a58", "Leon F Ball"],
  ];

  for (const [personId, displayName] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("32", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("PDF page");
    await expect(page.locator("main")).toContainText("Page 20");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
  }

  const unresolvedProfiles = [
    "1cf10caf-6e59-5fc5-b278-cbf615980a5b",
    "0bc6ba50-1e66-5a28-ae1b-be39391fa475",
    "b788c7df-4878-5dc7-919e-8b522de27aaa",
    "261d6884-1594-526e-b26e-b15e566f6db3",
    "549c77e3-70e8-5d00-88bf-12ffc83f9851",
    "ffe506ac-7aa6-5586-808a-05d346e4a2a7",
    "2ac60374-2c37-5ce7-9d68-926110f51678",
  ];

  for (const personId of unresolvedProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/2b76d6fd-c67f-540f-9001-f2085cf36dcc/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Berkley Clark Ball");
  await expect(
    page.getByRole("link", { name: "The Evening Star, May 28, 1944", exact: true }).first(),
  ).toHaveAttribute("href", /loc\.gov/);
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );

  await page.goto("./people/8fcf8786-1fb8-5c27-92b1-d96d355c3f79/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("progression from lieutenant in 1942 to major in 1944");
  await expect(
    page.getByRole("link", { name: "The Evening Star, October 8, 1944", exact: true }).first(),
  ).toHaveAttribute("href", /loc\.gov/);
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/d3503752-d5de-5051-8877-bb516c708a58/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Niveau");
  await expect(page.locator("main")).toContainText("lard salesman");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "Centre américain de secours",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "professional affiliation",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./organizations/463def8b-1633-5a8d-8c1a-af710fc29b9a/");
  await expect(
    page.getByRole("heading", { name: "Centre américain de secours", exact: true }),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("Leon F Ball");
});

test("Batch 133 preserves nine unresolved profiles and qualifies the probable Frank Ballante identity", async ({
  page,
}) => {
  const allProfiles = [
    ["415d6298-53ca-54f3-bb18-0a1638020c8e", "Maurice Ball", "32"],
    ["7164ae21-d569-5590-b13a-767c8e2627a7", "Mildred G Ball", "32"],
    ["cc7c2228-a272-51ab-a776-f8a62b4d0ffa", "Ned B Ball", "32"],
    ["4fcc4224-509e-5abe-9eba-9e1dd27d0b97", "Robert O Ball", "33"],
    ["4be91334-488a-5af2-aba4-53ca4a908b30", "Rubye L Ball", "33"],
    ["6a16d42b-5589-58c7-a971-f7526850b0a1", "Tellison F Ball", "33"],
    ["ed6d5e37-fb64-5b79-a504-e113598ff64f", "Ernest L Ballachino", "33"],
    ["69f37d9c-91bc-5e29-b87d-1fb822871dca", "Frank L Ballante", "33"],
    ["d619dfc4-251f-5ba7-b33f-33b50a5b79e1", "Adele Ballantine", "33"],
    ["770e1e8f-307d-5057-8333-23ff1f3b1fc0", "Harry W Ballard", "33"],
  ];

  for (const [personId, displayName, box] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("PDF page");
    await expect(page.locator("main")).toContainText("Page 20");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  const unresolvedProfiles = allProfiles
    .filter(([personId]) => personId !== "69f37d9c-91bc-5e29-b87d-1fb822871dca")
    .map(([personId]) => personId);

  for (const personId of unresolvedProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/69f37d9c-91bc-5e29-b87d-1fb822871dca/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Choctaw and Alpha Operational Groups");
  await expect(page.locator("main")).toContainText("T/5 Frank L. Ballante");
  await expect(
    page.getByRole("link", {
      name: "Office of Strategic Services Operational Groups: Personnel",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /ossog\.info\/personnel\.html/);
});

test("Batch 134 preserves employer gaps while qualifying the Balliet sisters and Bennie Ballone", async ({
  page,
}) => {
  const allProfiles = [
    ["544ee467-9ab2-5dcf-921a-c7781b946e34", "Mary J Ballew", "20"],
    ["c0ca7518-d359-55fd-a591-ebe6a48cfbc2", "Bette Balliet", "20"],
    ["3f60f485-127d-582e-82ff-f74f7d8f600b", "Ellin M Balliet", "20"],
    ["d7287f85-2724-50a4-a2f2-894caad6cb6f", "Robert H Balliet", "20"],
    ["59dbb455-d337-5a14-a474-9f7fa9cc939e", "Dorman L Ballinger", "20"],
    ["c4b7d2b4-6f49-587e-8a9c-66f955a82bf6", "Bennie Ballone", "20"],
    ["c651c5be-78ca-5c28-8712-55341867f0dc", "Harold E Ballou", "20"],
    ["df3378ba-6498-589c-b870-a4420cf3072b", "May L Ballou", "21"],
    ["e3e7d7eb-69a0-5041-a2fb-5ed9a3f34faa", "Lyle B Balluf", "21"],
    ["f5fbce96-479c-567f-8017-77b633886b8f", "Georges S Bally", "21"],
  ];

  for (const [personId, displayName, pdfPage] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("33", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(`Page ${pdfPage}`);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  const unresolvedProfiles = allProfiles
    .filter(
      ([personId]) =>
        ![
          "c0ca7518-d359-55fd-a591-ebe6a48cfbc2",
          "3f60f485-127d-582e-82ff-f74f7d8f600b",
          "c4b7d2b4-6f49-587e-8a9c-66f955a82bf6",
        ].includes(personId),
    )
    .map(([personId]) => personId);

  for (const personId of unresolvedProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/c0ca7518-d359-55fd-a591-ebe6a48cfbc2/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Bette Balliet Grefe");
  await expect(page.locator("main")).toContainText("declined Red Cross offer");
  await expect(
    page.getByRole("link", { name: /Wonderful Wizards of OSS/ }).first(),
  ).toHaveAttribute("href", /washingtonpost\.com/);

  await page.goto("./people/3f60f485-127d-582e-82ff-f74f7d8f600b/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Lin Balliet Gregory");
  await expect(page.locator("main")).toContainText("probably");

  await page.goto("./people/c4b7d2b4-6f49-587e-8a9c-66f955a82bf6/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Operational Group Santee");
  await expect(page.locator("main")).toContainText("B-24 Queenie");
  await expect(
    page.getByRole("link", { name: /Resti del bombardiere statunitense/ }).first(),
  ).toHaveAttribute("href", /cssav\.it/);
});

test("Batch 135 keeps publishing associations and student status distinct from employers", async ({
  page,
}) => {
  const allProfiles = [
    ["88323445-9718-518e-8268-b5403d0a988a", "Charles Balog", "33"],
    ["d658f57d-0d81-5787-ac7e-f9dc3b53850f", "Leslie S Balogh", "33"],
    ["8099bead-3a61-5282-9d5d-61552d657c22", "James J Balopitos", "33"],
    ["b2e83412-fbb5-5fec-b74d-039ea93ea22a", "Henry H Balos", "33"],
    ["669e2e02-425e-5797-a096-497403783e60", "Ferdinand A Balsamo", "33"],
    ["2ae252cc-7164-560c-b4b9-d8e91d49e05d", "John M Balsamo", "33"],
    ["f2c77a46-cfc1-506f-b675-5845863205e4", "Hugh C Balsinger", "34"],
    ["32e33816-b058-5a54-8abb-83e5c8d33764", "Henry H Balter", "34"],
    ["0b37db50-d085-5ce9-a731-404df2580dcc", "James H Baltzell", "34"],
    ["b8598812-9310-535e-96ff-75d6d993a7da", "Harold J Balvott", "34"],
  ];

  for (const [personId, displayName, box] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 21");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const personId of [
    "88323445-9718-518e-8268-b5403d0a988a",
    "d658f57d-0d81-5787-ac7e-f9dc3b53850f",
    "8099bead-3a61-5282-9d5d-61552d657c22",
    "669e2e02-425e-5797-a096-497403783e60",
    "f2c77a46-cfc1-506f-b675-5845863205e4",
    "b8598812-9310-535e-96ff-75d6d993a7da",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/b2e83412-fbb5-5fec-b74d-039ea93ea22a/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Bruce Humphries, Inc.");
  await expect(page.locator("main")).toContainText("United Publishers Association, Inc.");
  await expect(page.locator("main")).toContainText("professional affiliation");
  await expect(
    page.getByRole("link", { name: /Congressional Record/ }).first(),
  ).toHaveAttribute("href", /govinfo\.gov/);

  await page.goto("./people/32e33816-b058-5a54-8abb-83e5c8d33764/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Wharton School student");
  await expect(page.locator("main")).toContainText("student");
  await expect(page.getByRole("link", { name: "The Jewish Criterion", exact: true }).first()).toHaveAttribute(
    "href",
    /iiif\.library\.cmu\.edu/,
  );

  await page.goto("./people/0b37db50-d085-5ce9-a731-404df2580dcc/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("University of Illinois student in November 1941");
  await expect(page.locator("main")).toContainText("student");
  await expect(page.getByRole("link", { name: "The Nuntius", exact: true }).first()).toHaveAttribute(
    "href",
    /esparchives\.org/,
  );

  await page.goto("./people/2ae252cc-7164-560c-b4b9-d8e91d49e05d/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("occupation only");
  await expect(page.locator("main")).toContainText("Wall Street telegrapher");
});

test("Batch 136 preserves index spelling and qualifies COI, radio, and student evidence", async ({
  page,
}) => {
  const allProfiles = [
    ["9b42fdab-5f39-5314-ac80-8ed189adbb75", "Louis Balzarini"],
    ["8b8ffa4b-9bba-57c2-ae17-23920a882137", "William G Balzer"],
    ["75283faa-d73f-5442-a443-d9249f11a082", "Ivan A Ban"],
    ["28f1a44b-f3cc-5634-9b32-a2215d91a1f6", "Wesley G Banbury"],
    ["156c2910-530a-5b6f-9ce3-6ad12b421a5b", "John P Banchiu"],
    ["1213df7f-24c7-5e50-9637-954c9125fcc6", "Hubert H Bancroft"],
    ["14989add-3bea-5c75-9f23-8067c7e7f0ac", "Kenneth G Bandelier"],
    ["abb37bec-7398-528b-a2a1-5db68469c5eb", "Cahrles A Bane"],
    ["7f08ebdd-5fb8-5221-b00c-1ff4feda25d1", "Edward A Banek"],
    ["79b9df22-bf7e-5ec3-b01b-decd5b90b066", "Margaret M Banfill"],
  ];

  for (const [personId, displayName] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("34", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 21");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const personId of [
    "9b42fdab-5f39-5314-ac80-8ed189adbb75",
    "8b8ffa4b-9bba-57c2-ae17-23920a882137",
    "75283faa-d73f-5442-a443-d9249f11a082",
    "28f1a44b-f3cc-5634-9b32-a2215d91a1f6",
    "1213df7f-24c7-5e50-9637-954c9125fcc6",
    "14989add-3bea-5c75-9f23-8067c7e7f0ac",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/156c2910-530a-5b6f-9ce3-6ad12b421a5b/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Yugoslavian Operational Group");
  await expect(page.getByRole("link", { name: "Personnel of the Operational Groups", exact: true }).first()).toHaveAttribute(
    "href",
    /ossog\.info/,
  );

  await page.goto("./people/abb37bec-7398-528b-a2a1-5db68469c5eb/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Charles A. Bane");
  await expect(page.locator("main")).toContainText("Coordinator of Information");
  await expect(page.locator("main")).toContainText("government assignment");
  await expect(page.locator("main")).toContainText("service branch");
  await expect(page.getByRole("link", { name: /Radio Warfare/ }).first()).toHaveAttribute(
    "href",
    /device\.report/,
  );

  await page.goto("./people/7f08ebdd-5fb8-5221-b00c-1ff4feda25d1/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("commercial radio");
  await expect(page.locator("main")).toContainText("S.S. Catherine");
  await expect(page.getByRole("link", { name: "Communications, November 1945", exact: true }).first()).toHaveAttribute(
    "href",
    /americanradiohistory\.com/,
  );

  await page.goto("./people/79b9df22-bf7e-5ec3-b01b-decd5b90b066/");
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("University of Maryland");
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).not.toContainText("University of Maryland — employer");
  await expect(page.getByRole("link", { name: /Crescent of Gamma Phi Beta/ }).first()).toHaveAttribute(
    "href",
    /gpbarchives\.org/,
  );
});

test("Batch 137 preserves ten Box 34 rows and separates Bangsboll's military path from occupation", async ({
  page,
}) => {
  const allProfiles = [
    ["675258e8-bfa4-582b-a4db-6a629fbc6767", "Robert B Bangs"],
    ["a0a56884-8b58-58fd-b9b6-9511c915cdad", "Leif Bangsboll"],
    ["aba5eb49-454a-56a2-b06c-0626e38fd239", "Clarence Banister"],
    ["5e148586-fd1d-5963-9b3e-9ec5f19758b6", "Harold J Banker"],
    ["154aab22-6b38-5701-9221-40e05bd1b409", "Clayton F Banks Jr."],
    ["46203234-2e48-5d6a-9f78-a01d85cbe923", "Elmer C Banks"],
    ["355fdf38-9fbc-5946-8966-563de6e603a0", "Isabel E Banks"],
    ["a6016289-6929-569b-b54e-085a4d5012ab", "John M Banks"],
    ["b60de010-276d-5de6-8ea9-ab43583fd005", "Samuel L Banks"],
    ["add11dce-91f7-5419-8afd-29861c6ba91e", "John J Bann"],
  ];

  for (const [personId, displayName] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("34", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 21");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const personId of [
    "675258e8-bfa4-582b-a4db-6a629fbc6767",
    "aba5eb49-454a-56a2-b06c-0626e38fd239",
    "5e148586-fd1d-5963-9b3e-9ec5f19758b6",
    "154aab22-6b38-5701-9221-40e05bd1b409",
    "46203234-2e48-5d6a-9f78-a01d85cbe923",
    "355fdf38-9fbc-5946-8966-563de6e603a0",
    "a6016289-6929-569b-b54e-085a4d5012ab",
    "b60de010-276d-5de6-8ea9-ab43583fd005",
    "add11dce-91f7-5419-8afd-29861c6ba91e",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
  }

  await page.goto("./people/a0a56884-8b58-58fd-b9b6-9511c915cdad/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "United States Army",
  );
  await expect(page.locator("main")).toContainText("Norwegian Air Force in Exile");
  await expect(page.locator("main")).toContainText("flight sergeant");
  await expect(page.locator("main")).toContainText("merchant marine");
  await expect(page.locator("main")).toContainText("occupation only");
  await expect(
    page.getByRole("link", {
      name: "The Office of Strategic Services (OSS) Influence on Special Forces",
      exact: true,
    }).first(),
  ).toHaveAttribute("href", /arsof-history\.org/);
});

test("Batch 138 preserves ten page 21 rows and qualifies Baranski's Army and student pathways", async ({
  page,
}) => {
  const allProfiles = [
    ["52eba111-7f81-53cd-a270-3e12f64a17d4", "Rita E Bannan", "34"],
    ["615b02ef-cf69-51ff-9df2-20c58da7989f", "Ramon A Bannister", "35"],
    ["052df7a2-d724-5789-85ec-b40ec8a7b37a", "Bill B Bantz", "35"],
    ["b59ade96-9be3-5d2b-a27c-72c9250b0fc4", "Louise Banville", "35"],
    ["de06eaef-8d63-5a96-8378-efca882d9420", "Elizabeth Barack", "35"],
    ["10dcf598-5d33-501b-ab94-4571e3164371", "Joseph J Baran", "35"],
    ["37fcd0dc-b987-53ef-9934-7f6038b8aacc", "James A Baranosky", "35"],
    ["638c05ba-7226-56de-93dd-8e61334258e0", "Hilary L Baranowski", "35"],
    ["0111384b-dda8-532f-b560-2f065869fc44", "Edward V Baranski", "35"],
    ["4fc4061a-0f29-5754-b8b8-eb32f92537ea", "George Barb", "35"],
  ];

  for (const [personId, displayName, box] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 21");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
  }

  for (const personId of allProfiles
    .map(([personId]) => personId)
    .filter((personId) => personId !== "0111384b-dda8-532f-b560-2f065869fc44")) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
  }

  await page.goto("./people/615b02ef-cf69-51ff-9df2-20c58da7989f/");
  await expect(page.getByText("warrant officer", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("WO JG");

  await page.goto("./people/0111384b-dda8-532f-b560-2f065869fc44/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "United States Army",
  );
  await expect(page.locator("main")).toContainText("mess sergeant");
  await expect(page.locator("main")).toContainText("University of Illinois");
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).not.toContainText("University of Illinois — employer");
  await expect(page.getByRole("link", { name: /Edward Victor Baranski/ }).first()).toHaveAttribute(
    "href",
    /uiaa\.org/,
  );
});

test("Batch 139 preserves ten page 22 rows and documents Barbati's Army and Ford pathways", async ({
  page,
}) => {
  const allProfiles = [
    ["c3294217-fc9c-546d-a003-69ceaa30e62b", "Paul F Barb"],
    ["50f128c4-b940-5fcb-a44d-26c63268a8d7", "Geno Barbati"],
    ["1ab179fa-6130-5a87-8fc5-45a025991a49", "Audrey E Barber"],
    ["0ce4b78a-355e-5e1b-9352-f31731db70c0", "C E Barber"],
    ["e3a137ee-281f-545b-a67a-e4ad9b211178", "Eleanor M Barber"],
    ["0a9236e2-454f-5c54-b75d-7f6bf03c5690", "Martha Barber"],
    ["d0bb3f39-8187-5fa9-9271-22464f8f95b1", "William Barber"],
    ["66eff858-099c-5539-9c8b-634373b74446", "Roger W Barbey"],
    ["e50199fe-62d3-54ba-ab89-ceb37f826f91", "Lawrence I Barbier"],
    ["9c1c261a-3284-57a6-8364-cb72666af1cc", "Louis J Barbieri"],
  ];

  for (const [personId, displayName] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("35", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 22");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
  }

  for (const personId of allProfiles
    .map(([personId]) => personId)
    .filter((personId) => personId !== "50f128c4-b940-5fcb-a44d-26c63268a8d7")) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/50f128c4-b940-5fcb-a44d-26c63268a8d7/");
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("verified employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "United States Army",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Ford Motor Company",
  );
  await expect(page.locator("main")).toContainText("press operator and spot welder");
  await expect(page.locator("main")).toContainText("Air Corps basic training");
  await expect(
    page.getByRole("link", { name: /Office of Strategic Services Board Proceedings/ }).first(),
  ).toHaveAttribute("href", /digitalcollections\.hoover\.org/);
});

test("Batch 140 preserves ten page 22 rows and rejects unsupported Barbour through Bardenhagen matches", async ({
  page,
}) => {
  const allProfiles = [
    ["80235d1b-f96b-523c-92fb-ac5eae68bcd6", "Bruce R Barbour"],
    ["5195a285-f5ec-5612-9123-0968784c5d01", "Dana M Barbour"],
    ["0a7b8dbf-23b4-5c29-989f-d0e955240767", "Thomas Barbour"],
    ["82b14b53-d1d5-54ec-9f8f-7efe8bb3835c", "George W Barclay"],
    ["2cf510df-b2a3-5991-aa6a-135796be9403", "Walter S Barclay"],
    ["cd4cc9b3-b211-5113-8e02-cf518fef9b77", "Edward I Barcroft"],
    ["94ae58e4-f67d-5238-92c8-1bd9e0d9f515", "Andrew Bard"],
    ["f91c3a6e-9677-5096-8c97-33d934f0671a", "Charles L Bard"],
    ["d7ef5a0c-6afd-5ade-8f7d-5c0b338b7a1c", "Michael Bardaro"],
    ["c046fea7-9b7a-5113-80aa-fbf0efc8c5db", "Christopher T Bardenhagen"],
  ];

  for (const [personId, displayName] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("35", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 22");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/5195a285-f5ec-5612-9123-0968784c5d01/");
  await expect(page.locator("main")).toContainText("federal-publication namesake");
  await expect(page.locator("main")).not.toContainText("Temporary National Economic Committee — employer");

  await page.goto("./people/0a7b8dbf-23b4-5c29-989f-d0e955240767/");
  await expect(page.locator("main")).toContainText("Harvard zoologist");

  await page.goto("./people/c046fea7-9b7a-5113-80aa-fbf0efc8c5db/");
  await expect(page.locator("main")).toContainText("younger Vietnam-era namesake");
});

test("Batch 141 preserves Barders through Barker rows and qualifies Harold Barger's Columbia pathway", async ({
  page,
}) => {
  const allProfiles = [
    ["7b58b991-86e7-5ab0-9781-c77140261080", "Iva H Barders", "35"],
    ["5c29b80c-489d-569f-b686-0a381c84e58d", "Beverly A Baresh", "35"],
    ["aff50616-0cd2-5c24-8672-071ca7db3a21", "Harold Barger", "35"],
    ["e6b8cfc7-3f6d-5b62-893e-5fc3fab6f389", "Kenneth E Baringer", "35"],
    ["4408a0db-c12d-5f02-9d11-f03f4348b0a0", "Salvatore R Barisano", "35"],
    ["2dcda0ed-e1aa-52e4-8a09-431021dc8091", "Samuel N Barish", "36"],
    ["bbc0fe3f-2d0b-52d7-89b2-5106a6f9ef28", "Gabriel J Barkate", "36"],
    ["7fb79e9c-6648-5568-9299-17dc91ac5908", "Burk O Barker", "36"],
    ["891f46ba-f06d-583b-a272-134dff363ae1", "Francis M Barker", "36"],
    ["c7c2b26b-c20e-53cd-bf6c-375bf20c961f", "George B Barker", "36"],
  ];

  for (const [personId, displayName, box] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 22");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
  }

  for (const personId of allProfiles
    .map(([personId]) => personId)
    .filter((personId) => personId !== "aff50616-0cd2-5c24-8672-071ca7db3a21")) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/aff50616-0cd2-5c24-8672-071ca7db3a21/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("verified employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Columbia University",
  );
  await expect(page.locator("main")).toContainText("Assistant Professor of Economics");
  await expect(page.locator("main")).toContainText("rank variation");
  await expect(
    page.getByRole("link", { name: /Annual Report of the President and Treasurer/ }).first(),
  ).toHaveAttribute("href", /wikimedia\.org/);
  await expect(page.getByRole("link", { name: /Report #3: Transportation/ }).first()).toHaveAttribute(
    "href",
    /cia\.gov\/readingroom/,
  );

  await page.goto("./people/2dcda0ed-e1aa-52e4-8a09-431021dc8091/");
  await expect(page.locator("main")).toContainText("White Plains attorney");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText(
    "attorney",
  );

  await page.goto("./people/bbc0fe3f-2d0b-52d7-89b2-5106a6f9ef28/");
  await expect(page.locator("main")).toContainText("Louisiana educator candidate");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText(
    "educator",
  );
});

test("Batch 142 preserves Barker through Barkley rows and qualifies Mayno and Wilson Barker evidence", async ({
  page,
}) => {
  const allProfiles = [
    ["6dba8057-553d-5518-89e2-e46cbec48ac8", "James M Barker"],
    ["bd734136-02dc-5b8c-a39f-e019fdcac9e2", "John C Barker"],
    ["a88fa973-77f3-5a45-a108-e89e7407ceee", "Lavern P Barker"],
    ["5a15a701-641f-57e2-b8aa-672094fdb4fb", "Mayno W Barker"],
    ["9c942b44-cf4f-5b1f-92a2-5b18ba3947af", "Pauline M Barker"],
    ["94954f0a-0c95-596d-a948-1780cf03de47", "Robert G Barker"],
    ["db0663e4-e71e-5f43-b373-3827d37cac34", "Warren Barker"],
    ["703da672-7ff2-53ca-aab6-174fd9b47815", "Wilson Barker"],
    ["5852bc04-99ea-5c0c-8460-fe287fe62cb9", "Richard Barkhorn"],
    ["6f587914-2396-5988-825f-88b13b72d9e9", "Archie R Barkley"],
  ];

  for (const [personId, displayName] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("36", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 22");
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
  }

  for (const personId of allProfiles
    .map(([personId]) => personId)
    .filter(
      (personId) =>
        personId !== "5a15a701-641f-57e2-b8aa-672094fdb4fb" &&
        personId !== "703da672-7ff2-53ca-aab6-174fd9b47815",
    )) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/5a15a701-641f-57e2-b8aa-672094fdb4fb/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("documented prewar employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(page.locator("main")).toContainText("Postal Telegraph-Cable Company");
  await expect(page.locator("main")).toContainText("printer operator");
  await expect(page.locator("main")).toContainText("documented prewar");
  await expect(
    page.getByRole("link", { name: /Hill's Charlotte.*City Directory, 1941/ }).first(),
  ).toHaveAttribute("href", /digitalnc\.org/);

  await page.goto("./people/703da672-7ff2-53ca-aab6-174fd9b47815/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("occupation only found", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Boyd County farmhand");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(page.locator("main")).not.toContainText("farm — employer");
  await expect(
    page.getByRole("link", { name: /Congressional Gold Medal Ceremony/ }).first(),
  ).toHaveAttribute("href", /republicanleader\.senate\.gov/);

  await page.goto("./people/94954f0a-0c95-596d-a948-1780cf03de47/");
  await expect(page.locator("main")).toContainText("different officer identifier");
  await expect(page.locator("main")).not.toContainText("69th Infantry Division — employer");

  await page.goto("./people/db0663e4-e71e-5f43-b373-3827d37cac34/");
  await expect(page.locator("main")).toContainText("composer and Army Air Forces bandleader");

  await page.goto("./people/5852bc04-99ea-5c0c-8460-fe287fe62cb9/");
  await expect(page.locator("main")).toContainText("Dartmouth/Army Air Forces candidate");

  await page.goto("./people/6f587914-2396-5988-825f-88b13b72d9e9/");
  await expect(page.locator("main")).toContainText("CPC-5");
});

test("Batch 143 preserves Barkley through Barnabe rows and separates Barmine's civilian and military pathways", async ({
  page,
}) => {
  const allProfiles = [
    ["e148d0b2-1c39-5024-b5ca-2a659cbbf2d3", "Mabel Barkley", "Page 22"],
    ["c1c5716f-cc6c-5ca8-b36c-8ea9a0ff2aa9", "Merle C Barkley", "Page 22"],
    ["da7c225f-8f79-5de5-a567-75b6a14ad220", "William M Barlet", "Page 22"],
    ["bfb71f5d-e0e1-589f-aef0-92bb257dc22b", "Angelo Barlotta", "Page 22"],
    ["fb6387af-592c-5b94-9103-70e46c77bd49", "Alice D Barlow", "Page 22"],
    ["2c5b7758-3a35-5c90-b19e-d8e51975c44f", "William H Barlow", "Page 22"],
    ["d47671fd-a1ad-5246-bec6-11f9915f509c", "Hyman A Barmack", "Page 23"],
    ["e0892485-de88-5018-9b8a-aa5aa61a00ed", "Howard W Barmes", "Page 23"],
    ["d7c214c1-914d-5725-b947-943ca4ece775", "Alexander Barmine", "Page 23"],
    ["1feb8610-3057-519e-8bea-196e61bd1d6a", "Camille A Barnabe", "Page 23"],
  ];

  for (const [personId, displayName, sourcePage] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText("36", { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(sourcePage);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
  }

  for (const personId of allProfiles
    .map(([personId]) => personId)
    .filter((personId) => personId !== "d7c214c1-914d-5725-b947-943ca4ece775")) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  await page.goto("./people/d7c214c1-914d-5725-b947-943ca4ece775/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("verified employer found", { exact: true }).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "United States Army",
  );
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
    "military assignment",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "National Broadcasting Company",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "medium",
  );
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(
    "Self-employed",
  );
  await expect(page.locator("main")).toContainText("freelance writer");
  await expect(page.locator("main")).toContainText("dates the OSS service from 1943");
  await expect(page.locator("main")).not.toContainText("Voice of America — employer");
  await expect(
    page.getByRole("link", { name: /Summary of Information: Alexander Barmine/ }).first(),
  ).toHaveAttribute("href", /cia\.gov\/readingroom/);
  await expect(
    page.getByRole("link", { name: /A Counterintelligence Reader/ }).first(),
  ).toHaveAttribute("href", /irp\.fas\.org/);
});

test("Batch 144 preserves Barnard through Barnes rows and keeps Barner's undated education out of pre-OSS claims", async ({
  page,
}) => {
  const allProfiles = [
    ["74d7fe16-57ac-5126-b88f-64a63df27282", "Frances W Barnard", "36", "WAE"],
    ["356f7818-1544-5f94-ae6b-c770ff5a31d5", "Ralph N Barnard", "36", "1st Lt"],
    ["437ed836-faaf-5021-8d05-7438679d88ae", "Leroy E Barner", "36", "1st Lt"],
    ["d3bd8a0b-e6ff-501a-9890-34439cca316d", "Cecil W Barnes", "36", "Caf-13"],
    ["6a17dc69-e913-5a84-8a89-f869092b2706", "Charles D Barnes", "37", "Capt"],
    ["1bafa050-b590-5b9d-b5d5-42ab491d6a2d", "Charles T Barnes", "37", "Capt"],
    ["ab0d973b-ab94-5b07-86de-7b1dad635649", "Clarence I Barnes", "37", "Not printed"],
    ["e83d089f-9fc5-555b-860d-805597a10ffe", "Edward E Barnes", "37", "Not printed"],
    ["ea109b43-14e7-580e-ae4b-4419c9f1cd37", "Edward O Barnes", "37", "1st Lt"],
    ["3a2aa744-8294-5ca5-803d-ebea8c835517", "Eric W Barnes", "37", "Not printed"],
  ];

  for (const [personId, displayName, box, rank] of allProfiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.locator(".profile-aside").getByText(box, { exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 23");
    await expect(page.locator(".index-record").first().locator("dd").nth(1)).toHaveText(rank);
    await expect(page.locator(".index-record").first().locator("dd").nth(2)).toHaveText(
      /^(Not printed|••••[A-Z0-9]{4})$/,
    );
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }

  for (const personId of allProfiles
    .map(([personId]) => personId)
    .filter((personId) => personId !== "437ed836-faaf-5021-8d05-7438679d88ae")) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("unresolved", { exact: true }).first()).toBeVisible();
  }

  await page.goto("./people/437ed836-faaf-5021-8d05-7438679d88ae/");
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText("Leroy Elwood Barner");
  await expect(page.locator("main")).toContainText("University of Pittsburgh degree");
  await expect(page.locator("main")).toContainText("no pre-OSS affiliation is published");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toHaveCount(0);
  await expect(
    page.getByRole("link", { name: /Leroy Barner Obituary/ }).first(),
  ).toHaveAttribute("href", /dignitymemorial\.com/);
  await expect(
    page.getByRole("link", { name: /Cambria County Veterans Honor Roll/ }).first(),
  ).toHaveAttribute("href", /pagenweb\.org/);
});
