from sqlalchemy import (
       Column,
           Integer,
               String,
                   Text,
                       Boolean,
                           DateTime,
                               func
)
from app.database import Base

class Supplier(Base):
   __tablename__ = "suppliers"

   id = Column(Integer, primary_key=True, index=True)
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, unique=True, nullable=False, index=True)

   contact_person = Column(String)
   email = Column(String, index=True)
   phone = Column(String)
   address = Column(Text)
   city = Column(String)
   country = Column(String)

   api_key = Column(String)
   api_endpoint = Column(String)

   price = Column(Integer)
   available_qty = Column(Integer, default=0)

   is_active = Column(Boolean, default=True)
   notes = Column(Text)

   created_at = Column(DateTime, server_default=func.now())
   updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


   def __repr__(self):
                                                                               return f"<Supplier(id={self.id}, name='{self.name}')>"