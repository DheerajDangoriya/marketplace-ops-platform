from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Enum
from sqlalchemy.sql import func
import enum

from app.database import Base


class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"


class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    order_number = Column(String, unique=True, index=True, nullable=False)

    customer_email = Column(String, index=True, nullable=False)
    customer_name = Column(String, nullable=False)

    status = Column(
        Enum(OrderStatus, name="order_status"),
        default=OrderStatus.PENDING,
        nullable=False,
        index=True
    )

    total_amount = Column(Float, nullable=False)
    currency = Column(String, default="USD")

    shipping_address = Column(Text)
    billing_address = Column(Text)

    notes = Column(Text)

    tracking_number = Column(String, index=True)

    is_automated = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    def __repr__(self):
        return f"<Order id={self.id} order_number={self.order_number} status={self.status}>"