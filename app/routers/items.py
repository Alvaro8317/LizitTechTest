from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import get_database
from services.items_service import ItemService
from schemas.items_schemas import Item, ItemRequest

router = APIRouter()


@router.get('/items', tags=['items'], response_model=List[Item])
def get_items(db: Session = Depends(get_database)) -> JSONResponse:
    items = ItemService(db).get_all_items()
    return JSONResponse(content=jsonable_encoder(items), status_code=status.HTTP_200_OK)


@router.post('/items', tags=['items'], response_model=Item)
def create_item(item: ItemRequest, db: Session = Depends(get_database)) -> JSONResponse:
    result = ItemService(db).create_item(item)
    if isinstance(result, dict):
        return JSONResponse(content=result, status_code=status.HTTP_409_CONFLICT)
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_201_CREATED)
