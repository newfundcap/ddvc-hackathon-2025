from http.client import HTTPException
from typing import Optional

from fastapi import APIRouter, BackgroundTasks
from playhouse.shortcuts import model_to_dict

import processing

from models import Company, RankerCompany
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
async def list_companies(sort_by: str = None, ranker_score: float = None):
    query = Company.select()
    if ranker_score:
        query = query.join(RankerCompany).where(RankerCompany.score == ranker_score)
    if sort_by:
        query = query.order_by(getattr(Company, sort_by))
    return [model_to_dict(company) for company in query]
