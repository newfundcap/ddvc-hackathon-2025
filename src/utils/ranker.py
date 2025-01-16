import os, wave, struct
import openai
from openai import OpenAI
from dotenv import load_dotenv
from dotenv import find_dotenv

import prompts
import logging
import requests
import prompts
import json
from models import db, Company, Filter, Ranker, FilterCompany, RankerCompany, People, CompanyPeople
from config import config

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def process_json(filename):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    f = open(file_path)
    data = json.load(f)
    f.close()
    return json.dumps(data)


def generate_file(filename, info):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    f = open(os.path.join(script_dir, "match-info.json"), "w")
    f.write(info)


def rank_company(company: Company, people: People):

    company_details = company.__dict__
    people_details = people.__dict__
    rankers = []

    for ranker in Ranker.select():
        rankers.append(ranker.__dict__)
        

    logging.info("OPENAI CALLED...")

    completion = client.chat.completions.create(
        model = "gpt-4o",
        messages=[
            {"role": "developer",
            "content": prompts.startup_matching + "\nStartup Information:\n" + company_details + "\nPeople Information:\n" + people_details + "\nRankers:\n" + rankers},
            {"role": "user",
            "content": "Generate an output as requested by the developer role."}
        ]
    )

    print(completion.choices[0].message.content.strip())

    startup_match_info = completion.choices[0].message.content.strip()

    ranker_company = RankerCompany.select().where(RankerCompany.company.id == startup_match_info.get("startup-id")).get()
    ranker_company.score = int(startup_match_info.get("score"))
    ranker_company.category = startup_match_info.get("category")

    ranker_company.save()


def openai_api_calculate_cost(usage, model: str) -> float:
    pricing = {
        "gpt-3.5": {
            "prompt": 0.0015,
            "completion": 0.002,
        },

        "gpt-4": {
            "prompt": 0.03,
            "completion": 0.06,
        },

        "gpt-4o": {
            "prompt": 0.0045,
            "completion": 0.0135,
        },

        "gpt-4o-mini": {
            "prompt": 0.0015,
            "completion": 0.006,
        }
    }

    try:
        model_pricing = pricing[model]
    except KeyError:
        raise ValueError("Invalid model specified")
    
    prompt_cost = usage.prompt_tokens * model_pricing["prompt"] / 1000
    completion_cost = usage.completion_tokens * model_pricing["completion"] / 1000

    total_cost = prompt_cost + completion_cost
    # round to 6 decimals
    total_cost = round(total_cost, 6)

    logging.info(
        f"Tokens used:  {usage.prompt_tokens:,} prompt + {usage.completion_tokens:,} completion = {usage.total_tokens:,} tokens"
    )
    logging.info(f"Total cost [{model}]: ${total_cost:.4f}\n")

    print(f"Tokens used:  {usage.prompt_tokens:,} prompt + {usage.completion_tokens:,} completion = {usage.total_tokens:,} tokens")
    print(f"Total cost [{model}]: ${total_cost:.4f}\n")

    return total_cost


def delete_all_files():
    files_list = client.files.list()
    files_list = [file.id for file in files_list.data]

    if files_list == []:
        logging.info("No files to delete")
        return
    i = 0
    for file in files_list:
        client.files.delete(file)
        i += 1
        logging.info(f"({i}) Deleted file {file}")


def delete_all_assistants():
    my_assistants = client.beta.assistants.list(
        order="desc",
        limit=50,
    )
    if my_assistants.data == []:
        logging.info("No assistants to delete")
        return
    i = 0
    for assistant in my_assistants.data:
        client.beta.assistants.delete(assistant.id)
        i += 1
        logging.info(f"({i}) Deleted assistant {assistant.id}")


def delete_all():
    delete_all_files()
    delete_all_assistants()
