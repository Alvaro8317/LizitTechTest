from sqlalchemy.orm import Session
from models.items import Item as ItemModel


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def read_all(self):
        return self.db.query(ItemModel).all()

    def create_item(self, item: ItemModel) -> ItemModel:
        self.db.add(item)
        self.db.commit()
        return item
