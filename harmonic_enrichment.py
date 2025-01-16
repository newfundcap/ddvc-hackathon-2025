import json
import os
import requests
from peopledatalabs import PDLPY

from config import config
from models import Company, People, CompanyPeople


def enrich(company: Company):
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
                    firstName
                    lastName
                    socials {
                        linkedin {
                            url
                        }
                    }
                }
            }
        }
    }
    """
    headers = {
        "Content-Type": "application/json",
        "apikey": config.harmonic_api_key
    }

    variables = {"identifiers": {"websiteUrl": f"{company.website}" }}

    response = requests.post(
        url=URL, 
        json={"query": body, "variables": variables}, 
        headers=headers)

    company_data = response.json()["data"]["enrichCompanyByIdentifiers"]["company"]

    company.name = company_data.get("name")
    company.country = company_data.get("location", {}).get("country")
    company.sector = company_data.get("tagsV2")
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
    team = []
    for people in team_data:
        first_name = person_data.get("firstName")
        last_name = person_data.get("lastName")
        people = People.create(
            first_name=first_name,
            last_name=last_name,
        )
        CompanyPeople.create(company=company, people=people)
        team.append(people)

    return company, team
