from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: int = Field(gt=1)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ItemRequest(ItemBase):
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Un producto asombroso para crear",
                "price": 10000,
                "created_at": "2024-01-01T12:34:56"
            }
        }


class Item(ItemBase):
    updated_at: datetime | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Un producto asombroso",
                "price": 10000,
                "created_at": "2024-07-01T00:00:00",
                "updated_at": "2024-07-01T00:00:00",
            }
        }
