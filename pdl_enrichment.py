import json
from peopledatalabs import PDLPY

from config import config
from models import Company, People, Education, Experience


def enrich(people: People, company: Company):
    # Create a client, specifying your API key
    pdl_client = PDLPY(api_key=config.pdl_api_key)

    # Build the Elasticsearch query
    ES_QUERY = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"experience.company.name": company.name}},  # Match specific company
                    {"match": {"first_name": people.first_name}},  # Match first name
                    {"match": {"last_name": people.last_name}}  # Match last name
                ]
            }
        }
    }

    # Create parameters for the API call
    PARAMS = {
        "query": ES_QUERY,
        "size": 10,
        "pretty": True,
    }

    # Call the People Data Labs API
    response = pdl_client.person.search(**PARAMS).json()

    # Check for a successful response
    if response["status"] == 200:
        data = response["data"]
        # Save results to a file
        with open("filtered_pdl_search.jsonl", "w") as out:
            for record in data:
                out.write(json.dumps(record) + "\n")
        print(f"Successfully retrieved {len(data)} records.")
        print(f"{response['total']} total records exist matching the query.")
    else:
        print("Error:", response)

    person_data = data[0] if len(data) > 0 else None
    if person_data:
        people.update(
            pdl_id=people.person_id or person_data.get("person_id"),
            sex=people.sex or person_data.get("sex"),
            linkedin=people.linkedin_url or person_data.get("linkedin_url"),
            # facebook_url=people.facebook_url or person_data.get("facebook_url"),
            twitter_url=people.twitter_url or person_data.get("twitter_url"),
            github=people.github_url or person_data.get("github_url"),
            work_email=people.work_email or person_data.get("work_email"),
            personal_emails=people.personal_emails or person_data.get("personal_emails"),
            industry=people.industry or person_data.get("industry"),
            job_title=people.job_title or person_data.get("job_title"),
            location_country=people.location_country or person_data.get("location_country"),
            linkedin_connections=people.linkedin_connections or person_data.get("linkedin_connections"),
            inferred_years_experience=people.inferred_years_experience or person_data.get("inferred_years_experience"),
            summary=people.summary or person_data.get("summary"),
            interests=people.interests or person_data.get("interests")
        )

        # Add experience data using provided ID
        for exp in person_data["experience"]:
            Experience.create(
                people=people,  # Foreign key to `People`
                company_name=exp["company"]["name"],
                industry=exp["company"].get("industry"),
                start_date=exp.get("start_date"),
                end_date=exp.get("end_date"),
                title=(exp.get("title") or dict()).get("name"),
                summary=exp.get("summary")
            )

        # Add education data using provided ID
        for edu in person_data["education"]:
            Education.create(
                people=people,  # Foreign key reference to People model
                school_name=edu["school"]["name"],  # School name
                school_type=edu["school"]["type"],  # School type (e.g., university)
                degrees=edu.get("degrees"),  # Degrees obtained
                start_date=edu.get("start_date"),  # Start date
                end_date=edu.get("end_date"),  # End date
                majors=edu("majors"),  # Majors studied
                summary=edu("summary")
            )
