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
        "apikey": f"{os.getenv("HARMONIC_KEY")}"
    }

    variables = {"identifiers": {"websiteUrl": f"{company.website}" }}

    response = requests.post(
        url=URL, 
        json={"query": body, "variables": variables}, 
        headers=headers)

    company_data = response.json()["data"]["enrichCompanyByIdentifiers"]["company"]

    company = {
        "name": company_data.get("name"),
        "country": company_data.get("location", {}).get("country"),
        "sector": company_data.get("sector"),
        "contact": company_data.get("contact", {}).get("emails"),
        "funding_stage": company_data.get("funding", {}).get("fundingStage"),
        "creation_date": company_data.get("fundingDate"),
        "total_amount_raised": company_data.get("funding", {}).get("fundingTotal"),
        "description": company_data.get("description"),
        "website": company_data.get("website", {}).get("url"),
        "linkedin": company_data.get("socials", {}).get("linkedin", {}).get("url"),
        "harmonic_id": company_data.get("id"),
        "full_time_employees": len(company_data.get("employees", []))
    }

    # Préparer les données de l'équipe
    team_data = company_data.get("employees", [])

    # Créer les employés et les relations avec l'entreprise
    team = []
    for people in team_data:
        # Vérifiez les données nécessaires pour éviter des erreurs
        first_name = person_data.get("firstName")
        last_name = person_data.get("lastName")
        people = People.create(
            first_name=first_name,
            last_name=last_name,
        )
        CompanyPeople.create(company=company, people=people)
        team.append(people)

    return company, team
