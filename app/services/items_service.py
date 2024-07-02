from sqlalchemy.orm import Session
from models.items import Item as ItemModel
from schemas.items_schemas import ItemRequest as ItemSchemaCreate
from repositories.item_repository import ItemRepository


class ItemService:
    def __init__(self, db: Session):
        self.item_repository = ItemRepository(db)

    def create_item(self, item: ItemSchemaCreate):
        item = ItemModel(**item.model_dump())
        result = self.item_repository.create_item(item)
        if not result:
            return {"message": "Item already exists"}
        return item

    def get_all_items(self):
        return self.item_repository.read_all()
