from datetime import datetime


class Company:
    def __init__(
        self,
        name,
        country,
        sector,
        team,
        contact,
        funding_stage,
        creation_date,
        investors,
        revenue,
        revenue_growth,
        total_amount_raised,
        description,
        website,
        linkedin,
        harmonic_id,
        pdl_id,
        full_time_employees,
        full_time_employees_growth,
    ):
        self.name = name
        self.country = country
        self.sector = sector
        self.team = team
        self.contact = contact
        self.funding_stage = funding_stage
        self.creation_date = creation_date
        self.investors = investors
        self.revenue = revenue
        self.revenue_growth = revenue_growth
        self.total_amount_raised = total_amount_raised
        self.description = description
        self.website = website
        self.linkedin = linkedin
        self.harmonic_id = harmonic_id
        self.pdl_id = pdl_id
        self.full_time_employees = full_time_employees
        self.full_time_employees_growth = full_time_employees_growth


## team sera un json data
## refaire le teams pour ameliorer la recherche

settings = {
    "country": ["France", "italy"],
    "sector": ["Health", "Food", "Tech", "Energy", "Finance", "Education", "Transport"],
    "funding_stage": ["Pre-seed ", "Seed", "Series A"],
    "min_creation_date": "2020-01-01",
    "team_size": "2",
    "total_amount_raised": "1000000",
    "revenue": "1000000",
}


def filterOneCompany(company: Company, settings: dict):
    if "country" in settings and len(settings["country"]) > 0:
        valid_values = [v.lower() for v in settings["country"]]
        country = company.country.lower()
        if country not in valid_values:
            return False

    if "sector" in settings and len(settings["sector"]) > 0:
        valid_values = [v.lower() for v in settings["sector"]]
        sector = company.sector.lower()
        if sector not in valid_values:
            return False

    if "funding_stage" in settings and len(settings["funding_stage"]) > 0:
        valid_values = [v.lower() for v in settings["funding_stage"]]
        funding_stage = company.funding_stage.lower()
        if funding_stage not in valid_values:
            return False

    if "min_creation_date" in settings:
        min_creation_date = settings["min_creation_date"]
        creation_date = company.creation_date
        minCreation_date = datetime.strptime(min_creation_date, "%Y-%m-%d")
        creationDate = datetime.strptime(creation_date, "%Y-%m-%d")
        if creationDate < minCreation_date:
            return False

    if "team_size" in settings and len(settings["team_size"]) > 0:
        team = len(company.team)
        if team < int(settings["team_size"]):
            return False

    if "total_amount_raised" in settings:
        total_amount_raised = settings["total_amount_raised"]
        total_amount_raised = company.total_amount_raised
        if int(total_amount_raised) < int(settings["total_amount_raised"]):
            return False

    if "revenue" in settings:
        revenue = settings["revenue"]
        revenue = company.revenue
        if int(revenue) < int(settings["revenue"]):
            return False

    return True


# def filterCompanies(companies: list, settings: dict):
#     res = []
#     for company in companies:
#         if filterOneCompany(company, settings):
#             res.append(company)
#     return res


def main():
    company = Company(
        "name",
        "France",
        "Health",
        ["frf", "gfgf", "rgrg"],
        "contact",
        "seed",
        "2025-01-01",
        "investors",
        "1000000000",
        "0.1",
        "100000000",
        "description",
        "website",
        "linkedin",
        "harmonic_id",
        "pdl_id",
        "10",
        "0.1",
    )

    res = filterOneCompany(company, settings)

    print(res)

    print("Hello from filter.py")


if __name__ == "__main__":
    main()
