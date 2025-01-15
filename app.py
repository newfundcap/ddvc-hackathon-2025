from http.client import HTTPException

from fastapi import FastAPI
from playhouse.shortcuts import model_to_dict

import filter_endpoint
import company_endpoint
import ranker_endpoint
from models import db, Company, Filter, Ranker, FilterCompany, RankerCompany, People, CompanyPeople
from contextlib import asynccontextmanager


# def initialize_database():
#     db.connect()
#     db.create_tables([Company, People, CompanyPeople, Filter, FilterCompany, Ranker, RankerCompany])


@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize_database()
    yield
    if not db.is_closed():
        db.close()


app = FastAPI(lifespan=lifespan)
app.include_router(company_endpoint.router)
app.include_router(filter_endpoint.router)
app.include_router(ranker_endpoint.router)

