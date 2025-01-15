from models import Company

def enrich_company(company: Company):
    print('Enriching stuff')
    return company

def apply_filters(company: Company):
    print('Applying filters')
    return

def apply_rankers(company: Company):
    print('Applying rankers')
    return


def process_company(company: Company):
    print(f"Processing company {company.name}")
    company = enrich_company(company)
    apply_filters(company)
    apply_rankers(company)
    print(f"Done processing {company.name}")
    return