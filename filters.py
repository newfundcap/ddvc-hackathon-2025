from datetime import datetime
from typing import List

from models import Company, People, Filter, FilterCompany, CompanyPeople

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
    "min_revenue": "1000000",
}
'''


def filter_company(company: Company, team: List[People]):
    applied = []
    for myfilter in Filter.select():
        if not apply_filter(company, myfilter.settings, team):
            applied.append(FilterCompany.create(filter=myfilter, company=company))
    return applied


def apply_filter(company: Company, settings: dict, team: List[People]):
    if settings.get("country"):
        valid_values = [v.lower().strip() for v in settings["country"]]
        country = company.country.lower().strip()
        if country not in valid_values:
            return False

    if settings.get("sector"):
        valid_values = [v.lower().strip() for v in settings["sector"]]
        sector = company.sector.lower().strip()
        if sector not in valid_values:
            return False

    if settings.get("funding_stage"):
        valid_values = [v.lower().strip() for v in settings["funding_stage"]]
        funding_stage = company.funding_stage.lower().strip()
        if funding_stage not in valid_values:
            return False

    if settings.get("min_creation_date"):
        min_creation_date = settings["min_creation_date"]
        creation_date = company.creation_date
        minCreation_date = datetime.strptime(min_creation_date, "%Y-%m-%d")
        creationDate = datetime.strptime(creation_date, "%Y-%m-%d")
        if creationDate < minCreation_date:
            return False

    if settings.get("team_size", 0) > 0:
        if len(team) < int(settings["team_size"]):
            return False

    if settings.get("total_amount_raised", 0) > 0:
        if float(company.total_amount_raised) < float(settings["total_amount_raised"]):
            return False

    if settings.get("min_revenue", 0):
        if int(company.revenue) < settings["min_revenue"]:
            return False


    return True


def test_module(company_id):
    company = Company.get(company_id)
    filters_applied = filter_company(company, [people.people for people in company.employees])
    return filters_applied
