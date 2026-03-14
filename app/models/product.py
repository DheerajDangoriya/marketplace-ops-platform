"""Product model for marketplace inventory management."""
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base


class Product(Base):
    """Product table for storing product information."""
    
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    category = Column(String, index=True)
    price = Column(Float, nullable=False)
    cost = Column(Float)
    quantity_available = Column(Integer, default=0)
    quantity_reserved = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Product(id={self.id}, sku='{self.sku}', name='{self.name}')>"