from typing import Tuple, List

import requests

from config import config
from models import Company, People, CompanyPeople


def enrich(company: Company) -> Tuple[Company, List[People]]:
    if company.harmonic_id is None:
        print('Enriching from harmonic')
        team = []
        URL = "https://api.harmonic.ai/graphql"
        body = """
        mutation($identifiers: CompanyEnrichmentIdentifiersInput!) {
            enrichCompanyByIdentifiers(identifiers: $identifiers) {
                companyFound
                company {
                    id
                    name
                    entityUrn
                    logoUrl
                    website { url }
                    socials { linkedin { url } }
                    contact { phoneNumbers emails }
                    description
                    funding { fundingStage fundingTotal }
                    foundingDate { date }
                    location { city country }
                    tags { type displayValue }
                    tagsV2 { displayValue type }
                    stage
                    employees {
                        id
                        firstName
                        lastName
                        about
                        socials {
                            linkedin { url followerCount }
                            twitter { url }
                        }
                        experience {title isCurrentPosition }
                        location { country }
                    }
                }
            }
        }
        """
        headers = {
            "Content-Type": "application/json",
            "apikey": config.harmonic_api_key
        }

        variables = {"identifiers": {"websiteUrl": f"{company.website}"}}

        response = requests.post(
            url=URL,
            json={"query": body, "variables": variables},
            headers=headers)
        company_data = response.json()
        if response.ok and company_data['data'] != None:
            company_data = company_data["data"]["enrichCompanyByIdentifiers"]["company"]

            company.name = company_data.get("name")
            company.harmonic_id = company_data.get("id")
            company.logo_url = company_data.get("logoUrl")
            company.country = company_data.get("location", {}).get("country")
            company.sector = ', '.join(
                [tag.get('displayValue') for tag in (company_data.get("tagsV2") or company_data.get("tags") or [])])
            company.contact = company_data.get("contact", {}).get("emails")
            company.funding_stage = company_data.get("funding", {}).get("fundingStage")
            company.creation_date = company_data.get("fundingDate")
            company.total_amount_raised = company_data.get("funding", {}).get("fundingTotal")
            company.description = company_data.get("description")
            company.website = company_data.get("website", {}).get("url")
            company.linkedin = company_data.get("socials", {}).get("linkedin", {}).get("url")
            company.full_time_employees = len(company_data.get("employees", []))
            company.save()

            # Préparer les données de l'équipe
            team_data = company_data.get("employees", [])

            # Créer les employés et les relations avec l'entreprise
            for person_data in team_data:
                if person_data.get("firstName") and person_data.get("lastName"):
                    xp = person_data.get("experience")
                    title = xp[0].get("title") if len(xp) > 0 else None
                    people = People.create(
                        first_name=person_data.get("firstName"),
                        last_name=person_data.get("lastName"),
                        linkedin=person_data.get("socials", {}).get("linkedin", {}).get("url"),
                        harmonic_id=person_data.get("id"),
                        personal_emails=person_data.get("contact", {}).get("emails"),
                        job_title=title,
                        linkedin_connections=person_data.get("socials", {}).get("linkedin", {}).get("followerCount"),
                        # twitter_url=person_data.get("socials", {}).get("twitter", {}).get("url"),
                        location_country=person_data.get("location").get("country"),
                        summary=person_data.get("about")
                    )
                    CompanyPeople.create(company=company, people=people)
                    team.append(people)
    else:
        print('Harmonic enrichment already done, not retrying')
        team = [people.people for people in company.employees]
    return company, team


def test_module(company_id: Company):
    company = Company.get(Company.id == company_id)
    company, team = enrich(company)
    return company, team
