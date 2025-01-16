import json
from peopledatalabs import PDLPY

from config import config
from models import Company, People, Education


def enrich(people: People, company: Company):
    # Create a client, specifying your API key
    pdl_client = PDLPY(api_key=config.pdl_api_key)

    # Build the Elasticsearch query
    ES_QUERY = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"experience.company.name": people.company.name}},  # Match specific company
                    {"match": {"first_name": people.first_name}},                # Match first name
                    {"match": {"last_name": people.last_name}}                   # Match last name
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

    person_table = []
    experience_table = []
    education_table = []
    person_data = data[0] if len(data) > 0 else None
    if person_data:
        people.update(
        person_id=people.person_id or person_data["person_id"],
        full_name=people.full_name or person_data["full_name"],
        sex=people.sex or person_data["sex"],
        linkedin_url=people.linkedin_url or person_data["linkedin_url"],
        facebook_url=people.facebook_url or person_data["facebook_url"],
        twitter_url=people.twitter_url or person_data["twitter_url"],
        github_url=people.github_url or person_data["github_url"],
        work_email=people.work_email or person_data["work_email"],
        personal_emails=people.personal_emails or person_data["personal_emails"],
        industry=people.industry or person_data["industry"],
        job_title=people.job_title or person_data["job_title"],
        location_country=people.location_country or person_data["location_country"],
        linkedin_connections=people.linkedin_connections or person_data["linkedin_connections"],
        inferred_years_experience=people.inferred_years_experience or person_data["inferred_years_experience"],
        summary=people.summary or person_data["summary"],
        interests=people.interests or person_data["interests"]
    )

        # Add experience data using provided ID
        for exp in person_data["experience"]:
            Experience.create(
            people=people,  # Foreign key to `People`
            experience_id=exp.get("company", {}).get("id", "unknown_id"),
            person_id=person_data["person_id"],
            company_name=exp["company"]["name"],
            industry=exp["company"]["industry"],
            start_date=exp["start_date"],
            end_date=exp["end_date"],
            title=exp["title"]["name"],
            summary=exp["summary"], )


        # Add education data using provided ID
        for edu in person_data["education"]:
            Education.create(
                people = people,                        # Foreign key reference to People model
                education_id= edu.get("school", {}).get("id", "unknown_id"),
                person_id=person_data["person_id"]
                school_name=edu["school"]["name"],       # School name
                school_type=edu["school"]["type"],       # School type (e.g., university)
                degrees=edu["degrees"],                  # Degrees obtained
                start_date=edu["start_date"],            # Start date
                end_date=edu["end_date"],                # End date
                majors=edu["majors"],                    # Majors studied
                summary=edu["summary"],                 )
           

