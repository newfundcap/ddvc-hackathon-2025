from http.client import HTTPException
from typing import Optional, Any, Dict, List

from fastapi import APIRouter, BackgroundTasks
from playhouse.shortcuts import model_to_dict

import processing

from models import Company, FilterCompany
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
    personal_emails: Optional[List[str]]
    industry: Optional[str]
    job_title: Optional[str]
    location_country: Optional[str]
    inferred_years_experience: Optional[int]
    summary: Optional[str]
    interests: Optional[List[str]]
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

class FilterCompanyResponse(BaseModel):
    id: int
    name: str


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
    rankers: List[RankerCompanyResponse]
    filters: List[FilterCompanyResponse]

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
    companies = Company.select().order_by(Company.created_at.desc())

    # query = query.join(RankerCompany).where(RankerCompany.score == ranker_score)
    # if sort_by:
    #     query = query.order_by(getattr(Company, sort_by))

    resp = []
    for company in companies:
        company_response = CompanyResponse(
            id=company.id,
            name=company.name,
            website=company.website,
            linkedin=company.linkedin,
            created_at=company.created_at.isoformat() if company.created_at else None,
            updated_at=company.updated_at.isoformat() if company.updated_at else None,
            country=company.country,
            sector=company.sector,
            logo_url=company.logo_url,
            contact=company.contact,
            funding_stage=company.funding_stage,
            creation_date=company.creation_date.isoformat() if company.creation_date else None,
            investors=company.investors,
            revenue=company.revenue,
            revenue_growth=company.revenue_growth,
            total_amount_raised=company.total_amount_raised,
            description=company.description,
            harmonic_id=company.harmonic_id,
            pdl_id=company.pdl_id,
            full_time_employees=company.full_time_employees,
            full_time_employees_growth=company.full_time_employees_growth,

            team=[PeopleResponse(**model_to_dict(person.people)) for person in company.employees],
            rankers=[],  # Assuming rankers data to populate here
            filters=[],  # Assuming rankers data to populate here
        )
        # company_details = model_to_dict(company)
        # team = [people.people for people in company.employees]
        # people_details = [model_to_dict(t) for t in team]
        # rankers_results = []
        # filters = []
        # company_details['team'] = people_details
        # company_details['rankers'] = rankers_results
        # company_details['filters'] = filters

        resp.append(company_response)

    return resp
