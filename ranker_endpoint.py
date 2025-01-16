from http.client import HTTPException
from typing import Optional, Any, Dict, List

from fastapi import APIRouter, BackgroundTasks
from peewee import prefetch
from playhouse.shortcuts import model_to_dict

from models import Ranker, RankerCompany
from pydantic import BaseModel

router = APIRouter(
    prefix='/rankers',
    tags=['rankers']
)
# TODO implement the correct endpoint

class RankerResponse(BaseModel):
    id: int
    name: str
    description: str

class RankerCompanyResponse(BaseModel):
    id: int
    name: str
    description: str
    score: float
    category: str
    justification: str
    warnings: str


class RankerResponse(BaseModel):
    id: int
    name: str
    description: str

    companies: List[RankerCompanyResponse]

    class Config:
        orm_mode = True


@router.post("/")
async def create_ranker(ranker_data: dict):
    # TODO implement the correct endpoint
    try:
        ranker_obj = Ranker.create(**ranker_data)
        return model_to_dict(ranker_obj)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{ranker_id}")
async def delete_ranker(ranker_id: int):
    ranker_obj = Ranker.get_or_none(id=ranker_id)
    if not ranker_obj:
        raise HTTPException(status_code=404, detail="Ranker not found")
    ranker_obj.delete_instance()
    return {"detail": "Ranker deleted"}


@router.get("/")
async def list_rankers() -> list[RankerResponse]:
    rankers = prefetch(
        Ranker.select().order_by(Ranker.created_at.desc()),
        RankerCompany.select(),
    )
    resp = []
    for ranker in rankers:
        ranker_response = RankerResponse(
            id=ranker.id,
            name=ranker.name,
            description=ranker.description,

            companies=[
                RankerCompanyResponse(
                    id=r_c.ranker.id,
                    name=r_c.ranker.name,
                    description=r_c.ranker.description,
                    score=r_c.score,
                    category=r_c.category,
                    justification=r_c.justification,
                    warnings=r_c.warnings,
                ) for r_c in ranker.rankers
            ],  # Assuming companies data to populate here
        )

        resp.append(ranker_response)

    return resp
    
@router.get("/")
async def get_all_rankers() -> list[RankerResponse]:
    rankers = Ranker.select()
    
    ranker_response_list = []
    for ranker in rankers:
        ranker_dict = model_to_dict(ranker)
        ranker_response = RankerResponse(
            id=ranker_dict['id'],
            name=ranker_dict['name'],
            description=ranker_dict['description']
        )
        ranker_response_list.append(ranker_response)
    return ranker_response_list

