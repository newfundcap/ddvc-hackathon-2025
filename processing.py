import harmonic_enrichment
import pdl_enrichment
from models import Company
import ranker, prompts

def enrich_company(company: Company):
    print('Enriching stuff from harmonic')
    company, team = harmonic_enrichment.enrich(company)

    print('Enriching stuff from PDL')
    enriched_team = []
    for people in team:
        print(f"Enriching for {people.first_name}")
        enriched_people = pdl_enrichment.enrich(people, company)
        enriched_team.append(enriched_people)
    return company, enriched_team

def apply_filters(company: Company):
    print('Applying filters')
    return

def apply_rankers(company: Company):
    print('Applying rankers')
    ranker.rank_company(company)
    return 


def process_company(company: Company):
    print(f"Processing company {company.name}")
    company = enrich_company(company)
    apply_filters(company)
    apply_rankers(company)
    print(f"Done processing {company.name}")
    return