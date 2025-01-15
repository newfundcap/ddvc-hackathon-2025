from http.client import HTTPException

from fastapi import FastAPI
from playhouse.shortcuts import model_to_dict
from models import db, Company, Filter, Ranker, FilterCompany, RankerCompany, People
from contextlib import asynccontextmanager

def initialize_database():
    db.connect()
    db.create_tables([Company, People, Filter, FilterCompany, Ranker, RankerCompany])


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield
    if not db.is_closed():
        db.close()


app = FastAPI(lifespan=lifespan)

@app.post("/companies")
async def create_company(company: dict):
    try:
        company_obj = Company.create(**company)
        return model_to_dict(company_obj)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/filters")
async def create_filter(filter_data: dict):
    try:
        filter_obj = Filter.create(**filter_data)
        return model_to_dict(filter_obj)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/filters/{filter_id}")
async def delete_filter(filter_id: int):
    filter_obj = Filter.get_or_none(id=filter_id)
    if not filter_obj:
        raise HTTPException(status_code=404, detail="Filter not found")
    filter_obj.delete_instance()
    return {"detail": "Filter deleted"}

@app.get("/companies")
async def list_companies(sort_by: str = None, ranker_score: float = None):
    query = Company.select()
    if ranker_score:
        query = query.join(RankerCompany).where(RankerCompany.score == ranker_score)
    if sort_by:
        query = query.order_by(getattr(Company, sort_by))
    return [model_to_dict(company) for company in query]