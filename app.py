from http.client import HTTPException

from fastapi import FastAPI
from playhouse.shortcuts import model_to_dict

import filter_endpoint
import company_endpoint
import ranker_endpoint
from config import config
from models import db, Company, Filter, Ranker, FilterCompany, RankerCompany, People, CompanyPeople
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    if not db.is_closed():
        db.close()


app = FastAPI(
    lifespan=lifespan, 
    port=config.api_port, 
    host=config.api_host,
)
app.include_router(company_endpoint.router)
app.include_router(filter_endpoint.router)
app.include_router(ranker_endpoint.router)

