import type { Organization } from "../types";

const oilCompanyTypes = new Set([
  "oil and gas company",
  "oil and refining company",
  "oil exploration company",
  "petroleum company",
  "petroleum research and development company",
]);

type OilCompanyEmployment = {
  organizationId: string;
  organizationName: string;
  role: string | null;
  confidence: string;
  qualified: boolean;
  relationshipType: "employment" | "self_employment";
};

export type OilCompanyEmployee = {
  personId: string;
  name: string;
  employers: OilCompanyEmployment[];
};

export function oilCompanyEmployees(organizations: Organization[]) {
  const people = new Map<string, OilCompanyEmployee>();
  const employerIds = new Set<string>();

  for (const organization of organizations) {
    if (!oilCompanyTypes.has(organization.organization_type ?? "")) continue;

    for (const person of organization.linked_people) {
      if (!["confirmed", "high_confidence"].includes(person.identity_status)) continue;

      for (const affiliation of person.affiliations) {
        if (
          affiliation.organization_id !== organization.organization_id ||
          !["employment", "self_employment"].includes(affiliation.relationship_type) ||
          !["published", "publish_qualified"].includes(affiliation.publication_status) ||
          !["confirmed", "high", "medium"].includes(affiliation.claim_confidence)
        ) continue;

        // Public category membership requires an inspectable work claim,
        // not just an organization name or a professional affiliation.
        const hasCitedClaim = person.claims.some((claim) =>
          claim.affiliation_id === affiliation.affiliation_id &&
          ["published", "publish_qualified"].includes(claim.publication_status) &&
          claim.sources.some((link) => link.support_type === "supports"),
        );
        if (!hasCitedClaim) continue;

        const entry = people.get(person.person_id) ?? {
          personId: person.person_id,
          name: person.display_name,
          employers: [],
        };
        if (!entry.employers.some((employer) =>
          employer.organizationId === organization.organization_id
        )) {
          entry.employers.push({
            organizationId: organization.organization_id,
            organizationName: organization.canonical_name,
            role: affiliation.role_title ?? affiliation.occupation,
            confidence: affiliation.claim_confidence,
            qualified: affiliation.publication_status === "publish_qualified",
            relationshipType: affiliation.relationship_type as "employment" | "self_employment",
          });
          employerIds.add(organization.organization_id);
        }
        people.set(person.person_id, entry);
      }
    }
  }

  const employees = [...people.values()].sort((left, right) =>
    left.name.localeCompare(right.name),
  );
  for (const employee of employees) {
    employee.employers.sort((left, right) =>
      left.organizationName.localeCompare(right.organizationName),
    );
  }

  return { employees, organizationCount: employerIds.size };
}
