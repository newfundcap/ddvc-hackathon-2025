import json
from peopledatalabs import PDLPY

from config import config
from models import Company, People, CompanyPeople


def enrich(company: Company):
    company_data = {}
    team_data = [{}, {}]

    team = []
    company.update(...)
    for people in team_data:
        people = People.create(...)
        CompanyPeople.create(company=company, people=people)
        team.append(people)

    return company, team
