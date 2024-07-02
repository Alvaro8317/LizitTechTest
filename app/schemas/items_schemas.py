from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    price: int = Field(gt=1)


class ItemRequest(ItemBase):
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Un producto asombroso para crear",
                "price": 10000,
                "created_at": "2024-01-01T12:34:56"
            }
        }


class Items(ItemBase):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Un producto asombroso",
                "price": 10000,
                "created_at": "2023-07-01T12:34:56",
                "updated_at": None,
            }
        }
