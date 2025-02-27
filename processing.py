from typing import List

import filters
import harmonic_enrichment
import pdl_enrichment
from models import Company, People
import ranker, prompts

def enrich_company(company: Company):
    print('Enriching stuff from harmonic')
    company, team = harmonic_enrichment.enrich(company)

    print('Enriching stuff from PDL')
    enriched_team = []
    for people in team[:4]:
        # only the first 4 of the team for rate limits on PDL
        print(f"Enriching for {people.first_name} {people.last_name}")
        enriched_people = pdl_enrichment.enrich(people, company)
        enriched_team.append(enriched_people)
    return company, enriched_team

def apply_filters(company: Company, team: List[People]):
    print('Applying filters')
    filters.filter_company(company, team)
    return

def apply_rankers(company: Company, team: List[People]):
    print('Applying rankers')
    results = ranker.rank_company(company, team)
    return results 


def process_company(company: Company):
    print(f"Processing company {company.name}")
    company, team = enrich_company(company)
    apply_filters(company, team)
    apply_rankers(company, team)
    print(f"Done processing {company.name}")
    return company, team

def test_module(company_id):
    company = Company.get(Company.id == company_id)
    return process_company(company)