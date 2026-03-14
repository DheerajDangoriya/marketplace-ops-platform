from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.order import Order, OrderStatus
from app.auth.security import oauth2_scheme

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float


@router.post("/")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    new_order = Order(
        customer_name=order.customer_name,
        total_amount=order.total_amount,
        status="pending"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


@router.get("/")
def get_all_orders(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    return db.query(Order).all()


@router.get("/pending")
def get_pending_orders(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    return db.query(Order).filter(Order.status == "pending").all()


@router.put("/{order_id}/status")
def update_order_status(
    order_id: int,
    status: OrderStatus,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status
    db.commit()
    db.refresh(order)

    return order