from http.client import HTTPException

from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

from models import Company, RankerCompany

router = APIRouter(
    prefix='/companies',
    tags=['companies']
)


@router.post("/")
async def create_company(company: dict):
    try:
        company_obj = Company.create(**company)
        # trigger the background job for enriching and stuff
        return model_to_dict(company_obj)
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
