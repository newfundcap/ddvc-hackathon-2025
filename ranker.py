import json
from typing import List

from openai import OpenAI
from playhouse.shortcuts import model_to_dict

import json_utils
import prompts
import logging
from models import Company, Ranker, RankerCompany, People
from config import config


def rank_company(company: Company, team: List[People]):
    print(f"Ranking company {company.name}")
    client = OpenAI(api_key=config.openai_api_key)
    company_details = json.dumps(model_to_dict(company), default=json_utils.json_serial)
    people_details = '\n'.join([json.dumps(model_to_dict(t), default=json_utils.json_serial) for t in team])
    results = []
    for ranker in Ranker.select():
        print(f"Ranking company {company.name} agains {ranker.name}")

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer",
                 "content": prompts.startup_matching + "\nStartup Information:\n" + company_details + "\nPeople Information:\n" + people_details + "\nRanker:\n" + ranker.description},
                {"role": "user",
                 "content": "Generate an output as requested by the developer role."}
            ]
        )

        startup_match_info = json.loads(completion.choices[0].message.content.strip())

        ranker_company = RankerCompany.create(
            ranker_id=ranker.id,
            company_id=company.id,
            score=int(startup_match_info.get("score")),
            category=startup_match_info.get("category"),
            justification=startup_match_info.get("justification"),
            warnings=startup_match_info.get("gaps"),
        )

        ranker_company.save()
        results.append(ranker_company)
    return results


def test_module(company_id):
    company = Company.get(company_id)
    team = [c_p.people for c_p in company.employees]
    results = rank_company(company, team)
    return results
