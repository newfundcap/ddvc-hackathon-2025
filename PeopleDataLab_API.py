#!/usr/bin/env python
# coding: utf-8

# In[104]:


import json
from peopledatalabs import PDLPY

# Create a client, specifying your API key
CLIENT = PDLPY(
    api_key="19def2a487c108856614ed041a9a670daa5e58cf29eafa4898908d401f26f53c",
)

# Extract startup names from the Harmonic AI response
startup_name = "OpenAI"
first_name = "Daniela"
last_name = "Amodei"
#[entry["startup_name"] for entry in harmonic_data]

# Build the Elasticsearch query
ES_QUERY = {
    "query": {
        "bool": {
            "must": [
                {"match": {"experience.company.name": startup_name}},  # Match specific company
                {"match": {"first_name": first_name}},                # Match first name
                {"match": {"last_name": last_name}}                   # Match last name
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
response = CLIENT.person.search(**PARAMS).json()

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


# In[105]:


data


# In[109]:


person_table = []
experience_table = []
education_table = []

for person in data:
    person_id = person["id"]
    
    # Add person data
    person_table.append({
        "person_id": person_id,
        "full_name": person["full_name"],
        "sex": person["sex"],
        "linkedin_url": person["linkedin_url"],
        "facebook_url": person["facebook_url"],
        "twitter_url": person["twitter_url"],
        "github_url": person["github_url"],
        "work_email": person["work_email"],
        "personal_emails": person["personal_emails"],
        "industry": person["industry"],
        "job_title": person["job_title"],
        "location_country": person["location_country"],
        "linkedin_connections": person["linkedin_connections"],
        "inferred_years_experience": person["inferred_years_experience"],
        "summary": person["summary"],
        "interests": person["interests"]
    })
    
    # Add experience data using provided ID
    for exp in person["experience"]:
        experience_table.append({
            "experience_id": exp.get("company", {}).get("id", "unknown_id"),
            "person_id": person_id,
            "company_name": exp["company"]["name"],
            "industry": exp["company"]["industry"],
            "start_date": exp["start_date"],
            "end_date": exp["end_date"],
            "title": exp["title"]["name"],
            "summary": exp["summary"]
        })
    
    # Add education data using provided ID
    for edu in person["education"]:
        education_table.append({
            "education_id": edu.get("school", {}).get("id", "unknown_id"),
            "person_id": person_id,
            "school_name": edu["school"]["name"],
            "school_type": edu["school"]["type"],
            "degrees": edu["degrees"],
            "start_date": edu["start_date"],
            "end_date": edu["end_date"],
            "majors": edu["majors"],
            "summary": edu["summary"]
        })

df_deduplicated = df.drop_duplicates(subset=['linkedin_url'], keep='first') ## Delete Duplicates based on LinkedIn URL
        
        
# Convert to DataFrames
person_df = pd.DataFrame(person_table)
experience_df = pd.DataFrame(experience_table)
education_df = pd.DataFrame(education_table)


# In[111]:


experience_df


# 
