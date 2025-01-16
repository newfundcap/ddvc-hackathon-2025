import json
from http.client import HTTPException
from typing import Optional, Any, Dict, List

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


class PeopleResponse(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    previous_founded_companies_count: Optional[int]
    role: Optional[str]
    sex: Optional[str]
    twitter_url: Optional[str]
    work_email: Optional[str]
    personal_emails: Optional[Dict[str, Any]]
    industry: Optional[str]
    job_title: Optional[str]
    location_country: Optional[str]
    inferred_years_experience: Optional[int]
    summary: Optional[str]
    interests: Optional[Dict[str, Any]]
    pdl_id: Optional[str]
    harmonic_id: Optional[str]
    linkedin_connections: Optional[int]


class RankerCompanyResponse(BaseModel):
    id: int
    name: str
    description: str
    score: float
    category: str
    justification: str
    warnings: str


class CompanyResponse(BaseModel):
    id: int
    name: str
    website: Optional[str]
    linkedin: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    country: Optional[str]
    sector: Optional[str]
    logo_url: Optional[str]
    contact: Optional[str]
    funding_stage: Optional[str]
    creation_date: Optional[str]
    investors: Optional[Dict[str, Any]]
    revenue: Optional[float]
    revenue_growth: Optional[float]
    total_amount_raised: Optional[float]
    description: Optional[str]
    harmonic_id: Optional[str]
    pdl_id: Optional[str]
    full_time_employees: Optional[int]
    full_time_employees_growth: Optional[int]

    team: List[PeopleResponse]
    rankers: List[RankerResponse]

    class Config:
        orm_mode = True

class CreateCompanyRequest(BaseModel):
    name: str
    website: Optional[str]
    linkedin: Optional[str]

@router.post("/")
async def create_company(req: CreateCompanyRequest, background_tasks: BackgroundTasks) -> CompanyResponse:
    if (req.linkedin is None) and (req.website is None):
        raise HTTPException(status_code=400, detail="Require at least website or linkedin")
    try:
        company = Company.create(
            name=req.name,
            website=req.website,
            linkedin=req.linkedin,
        )
        background_tasks.add_task(processing.process_company, company)
        return model_to_dict(company)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/")
async def list_companies() -> list[CompanyResponse]:
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
