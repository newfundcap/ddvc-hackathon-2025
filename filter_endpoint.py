from http.client import HTTPException

from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict

from models import Filter

router = APIRouter(
    prefix='/filters',
    tags=['filters']
)


@router.post("/")
async def create_filter(filter_data: dict):
    try:
        filter_obj = Filter.create(**filter_data)
        return model_to_dict(filter_obj)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{filter_id}")
async def delete_filter(filter_id: int):
    filter_obj = Filter.get_or_none(id=filter_id)
    if not filter_obj:
        raise HTTPException(status_code=404, detail="Filter not found")
    filter_obj.delete_instance()
    return {"detail": "Filter deleted"}
