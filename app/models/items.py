from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Sequence
from config.database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, Sequence('item_id_seq'), primary_key=True, index=True)
    name = Column(String(50), nullable=False, index=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=None, onupdate=datetime.utcnow, nullable=True)
