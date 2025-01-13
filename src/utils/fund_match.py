import os, wave, struct
import openai
from openai import OpenAI
from dotenv import load_dotenv
from dotenv import find_dotenv

import prompts
from dataclasses_config import OpenAIResponse
import logging
import requests
import prompts
import json

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
    return f


def call_model():
    model_prompt: str
    user_prompt: str
    limit: int

    logging.info("OPENAI CALLED...")

    completion = client.chat.completions.create(
        model = "gpt-4o",
        messages=[
            {"role": "developer",
            "content": prompts.fund_matching + process_json("funds.json") + process_json("startup.json") + process_json("investor-preferences.json")}, # investor preferences can link to the investor's account or something like that
            {"role": "user",
            "content": "Generate an output as requested by the developer role."}
        ]
    )

    generate_file("match-info.json", completion.choices[0].message.content.strip())

    print(completion.choices[0].message.content.strip())
    

    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens

    return OpenAIResponse(
        body=completion.choices[0].message.content,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
    )



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
