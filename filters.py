from datetime import datetime
from typing import List

from models import Company, People

## team sera un json data
## refaire le teams pour ameliorer la recherche

'''
Example of the settings for filters

settings = {
    "country": ["France", "Italy"],
    "sector": ["Health", "Food", "Tech", "Energy", "Finance", "Education", "Transport"],
    "funding_stage": ["Pre-seed ", "Seed", "Series A"],
    "min_creation_date": "2020-01-01",
    "team_size": "2",
    "total_amount_raised": "1000000",
    "revenue": "1000000",
}
'''


def apply_filters(company: Company, settings: dict, team: List[People]):
    if "country" in settings and len(settings["country"]) > 0:
        valid_values = [v.lower().strip() for v in settings["country"]]
        country = company.country.lower().strip()
        if country not in valid_values:
            return False

    if "sector" in settings and len(settings["sector"]) > 0:
        valid_values = [v.lower().strip() for v in settings["sector"]]
        sector = company.sector.lower().strip()
        if sector not in valid_values:
            return False

    if "funding_stage" in settings and len(settings["funding_stage"]) > 0:
        valid_values = [v.lower().strip() for v in settings["funding_stage"]]
        funding_stage = company.funding_stage.lower().strip()
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
        if len(team) < int(settings["team_size"]):
            return False

    if "total_amount_raised" in settings:
        if float(company.total_amount_raised) < float(settings["total_amount_raised"]):
            return False

    if "revenue" in settings:
        if int(company.revenue) < int(settings["revenue"]):
            return False

    return True


# def filterCompanies(companies: list, settings: dict):
#     res = []
#     for company in companies:
#         if filterOneCompany(company, settings):
#             res.append(company)
#     return res


def main():


if __name__ == "__main__":
    main()
