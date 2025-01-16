import json
from http.client import HTTPException
from typing import Optional

from fastapi import APIRouter, BackgroundTasks
from peewee import JOIN, prefetch
from playhouse.shortcuts import model_to_dict

import json_utils
import processing

from models import Company, RankerCompany, Filter, FilterCompany
from pydantic import BaseModel


router = APIRouter(
    prefix='/companies',
    tags=['companies']
)

class CreateCompanyRequest(BaseModel):
    name: str
    creation_date: str
    country: Optional[str] = None
    sector: Optional[str] = None
    contact: Optional[str] = None
    funding_stage: Optional[str] = None
    investors: Optional[list] = None
    revenue: Optional[float] = None
    revenue_growth: Optional[float] = None

@router.post("/")
async def create_company(req: CreateCompanyRequest, background_tasks: BackgroundTasks):
    try:
        company = Company.create(**req.dict())
        # todo create the founders
        background_tasks.add_task(processing.process_company, company)
        return model_to_dict(company)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/")
async def list_companies():
    # companies_q = Company.select()
    # filter_company = FilterCompany.select()
    # ranker_company = RankerCompany.select()
    
    companies = Company.select().order_by(Company.created_at.desc())


    # query = query.join(RankerCompany).where(RankerCompany.score == ranker_score)
    # if sort_by:
    #     query = query.order_by(getattr(Company, sort_by))

    resp = []
    for company in companies:
        company_details = model_to_dict(company)
        team = [people.people for people in company.employees]
        people_details = [model_to_dict(t)for t in team]
        rankers_results = []
        filters = []
        company_details['team'] = people_details
        company_details['rankers'] = rankers_results
        company_details['filters'] = filters

        resp.append(company_details)

    return resp
