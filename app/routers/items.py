from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import get_database
from services.items_service import ItemService
from schemas.items_schemas import Items, ItemRequest

router = APIRouter()


@router.get('/items', tags=['items'], response_model=List[Items])
def get_items(db: Session = Depends(get_database)) -> JSONResponse:
    items = ItemService(db).get_all_items()
    return JSONResponse(content=jsonable_encoder(items))


@router.post('/items', tags=['items'], response_model=Items)
def create_item(item: ItemRequest, db: Session = Depends(get_database)) -> JSONResponse:
    result = ItemService(db).create_item(item)
    return JSONResponse(content=jsonable_encoder(result))
