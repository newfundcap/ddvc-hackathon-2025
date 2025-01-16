from http.client import HTTPException

from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

from models import Ranker

router = APIRouter(
    prefix='/rankers',
    tags=['rankers']
)
# TODO implement the correct endpoint

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
        raise HTTPException(status_code=404, detail="Filter not found")
    ranker_obj.delete_instance()
    return {"detail": "Filter deleted"}
