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

def add_ranker(ranker_name: str, ranker_description: str):
    new_ranker = Ranker.create(name=ranker_name, description=ranker_description)
    return new_ranker

def store_ranker(ranker: Ranker, name: str, description: str):
    ranker.name = ranker.name or name
    ranker.description = ranker.description or description
    ranker.save()

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

    #db.connect()

    ranker_company = RankerCompany.select().where(RankerCompany.company.id == startup_match_info.get("startup-id")).get()
    ranker_company.score = int(startup_match_info.get("score"))
    ranker_company.category = startup_match_info.get("category")
    ranker_company.justification = startup_match_info.get("justification")
    ranker_company.warnings = startup_match_info.get("warnings")

    ranker_company.save()

    #db.close()


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
