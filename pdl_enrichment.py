from peopledatalabs import PDLPY

from config import config
from models import Company, People, Education, Experience, CompanyPeople


def parse_date(date_str: str):
    if date_str:
        if len(date_str) == 4:
            return f"{date_str}-01-01"
        elif len(date_str) == 7:
            return f"{date_str}-01"
        else:
            return date_str
    return date_str


def store_in_db(people: People, person_data: dict):
    people.pdl_id = person_data.get("id") if not people.pdl_id else people.pdl_id

    people.sex = person_data.get("sex") if not people.sex else people.sex
    people.linkedin = person_data.get("linkedin_url") if not people.linkedin else people.linkedin
    people.twitter_url = person_data.get("twitter_url") if not people.twitter_url else people.twitter_url
    people.github = person_data.get("github_url") if not people.github else people.github
    people.work_email = person_data.get("work_email") if not people.work_email else people.work_email
    people.personal_emails = person_data.get(
        "personal_emails") if not people.personal_emails else people.personal_emails
    people.industry = person_data.get("industry") if not people.industry else people.industry
    people.job_title = person_data.get("job_title") if not people.job_title else people.job_title
    people.location_country = person_data.get(
        "location_country") if not people.location_country else people.location_country
    people.linkedin_connections = person_data.get(
        "linkedin_connections") if not people.linkedin_connections else people.linkedin_connections
    people.inferred_years_experience = person_data.get(
        "inferred_years_experience") if not people.inferred_years_experience else people.inferred_years_experience
    people.summary = person_data.get("summary") if not people.summary else people.summary
    people.interests = person_data.get("interests") if not people.interests else people.interests
    people.save()

    # Add experience data using provided ID
    for exp in person_data["experience"]:
        Experience.create(
            people_id=people.id,  # Foreign key to `People`
            company_name=exp["company"]["name"],
            industry=exp["company"].get("industry"),
            start_date=parse_date(exp.get("start_date")),
            end_date=parse_date(exp.get("end_date")),
            title=(exp.get("title") or dict()).get("name"),
            summary=exp.get("summary")
        )

    # Add education data using provided ID
    for edu in person_data["education"]:
        Education.create(
            people_id=people.id,  # Foreign key reference to People model
            school_name=edu["school"]["name"],  # School name
            school_type=edu["school"]["type"],  # School type (e.g., university)
            degrees=edu.get("degrees"),  # Degrees obtained
            start_date=parse_date(edu.get("start_date")),  # Start date
            end_date=parse_date(edu.get("end_date")),  # End date
            majors=edu.get("majors"),  # Majors studied
            summary=edu.get("summary")
        )
    return people


def enrich(people: People, company: Company):
    if (people.pdl_id is not None):
        print(f"People id={people} already enriched with PDL, not calling API.")
    else:
        # Create a client, specifying your API key
        pdl_client = PDLPY(api_key=config.pdl_api_key)

        # Build the Elasticsearch query
        ES_QUERY = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"job_company_name": company.name}},  # Match specific company
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
            print(f"Successfully retrieved {len(data)} records.")
            print(f"{response['total']} total records exist matching the query.")
            person_data = data[0] if len(data) > 0 else None
            if person_data:
                people = store_in_db(people, person_data)
        else:
            print("Error:", response)

    return people


def test_module(company_id):
    company = Company.select(Company, People).join(CompanyPeople).join(People).switch(Company).where(
        Company.id == company_id).first()
    person = enrich(company.employees[0].people, company)
    return person
