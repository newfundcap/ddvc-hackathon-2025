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
async def get_all_rankers() -> list[RankerResponse]:
    rankers = Ranker.select()
    
    ranker_response_list = []
    for ranker in rankers:
        ranker_response = RankerResponse(
            id=ranker.id,
            name=ranker.name,
            description=ranker.description
        )
        ranker_response_list.append(ranker_response)
    return ranker_response_list

