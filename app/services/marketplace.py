from typing import List
from app.database import get_db
from app.models import Order
from sqlalchemy.orm import Session
from app.models import Order, OrderStatus


from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.order import Order, OrderStatus
from app.utils import db

# 1. Centralized Status Transition Logic
VALID_TRANSITIONS = {
        OrderStatus.PENDING: [OrderStatus.CONFIRMED, OrderStatus.CANCELLED],
            OrderStatus.CONFIRMED: [OrderStatus.PROCESSING, OrderStatus.CANCELLED],
                OrderStatus.PROCESSING: [OrderStatus.SHIPPED],
                    OrderStatus.SHIPPED: [OrderStatus.DELIVERED, OrderStatus.RETURNED],
                        OrderStatus.DELIVERED: [],
                            OrderStatus.CANCELLED: [],
                                OrderStatus.RETURNED: []
}

def fetch_new_orders(db: Session) -> List[Order]:
        """Fetch orders that are marked as 'new'."""    
        return db.query(Order).filter(Order.status == "new").all()

def mark_order_processed(db: Session, order_id: int):
                """Mark order as processed after workflow execution."""
                order = db.query(Order).filter(Order.id == order_id).first()
                if not order:
                                return None
                                    
                order.status = "processed"
                db.commit()
                db.refresh(order)
                return order

def update_order_status(db: Session, order_id: int, new_status: OrderStatus):
                                                        """Updates status only if the transition is valid."""
                                                        order = db.query(Order).filter(Order.id == order_id).first()
                                                                
                                                        if not order:
                                                                            return None

                                                        current_status = order.status

                                                                                    # Validate the transition
                                                        if new_status not in VALID_TRANSITIONS.get(current_status, []):
                                                                                                raise ValueError(f"Invalid transition from {current_status} to {new_status}")

                                                        order.status = new_status
                                                        db.commit()
                                                        db.refresh(order)
                                                        return order
