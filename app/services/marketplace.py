from typing import List
from sqlalchemy.orm import Session

from app.models.order import Order, OrderStatus
from app.logging_config import logger


# Valid state transitions for order lifecycle
VALID_TRANSITIONS = {
    OrderStatus.PENDING: [OrderStatus.CONFIRMED, OrderStatus.CANCELLED],
    OrderStatus.CONFIRMED: [OrderStatus.PROCESSING, OrderStatus.CANCELLED],
    OrderStatus.PROCESSING: [OrderStatus.SHIPPED],
    OrderStatus.SHIPPED: [OrderStatus.DELIVERED, OrderStatus.RETURNED],
    OrderStatus.DELIVERED: [],
    OrderStatus.CANCELLED: [],
    OrderStatus.RETURNED: [],
}


def fetch_new_orders(db: Session = None) -> List[Order]:
    """Fetch orders that are pending."""

    if db is None:
        logger.warning("No database session provided, returning empty order list")
        return []
    
    orders = db.query(Order).filter(Order.status == OrderStatus.PENDING).all()

    logger.info(f"Fetched {len(orders)} pending orders")

    return orders


def mark_order_processed(db: Session, order_id: int):
    """Mark order as processing after workflow execution."""

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        logger.warning(f"Order {order_id} not found")
        return None

    order.status = OrderStatus.PROCESSING

    db.commit()
    db.refresh(order)

    logger.info(f"Order {order_id} marked as PROCESSING")

    return order


def update_order_status(db: Session, order_id: int, new_status: OrderStatus):
    """Update order status if the transition is valid."""

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        logger.error(f"Order {order_id} not found")
        return None

    current_status = order.status

    # Validate transition
    if new_status not in VALID_TRANSITIONS.get(current_status, []):
        logger.error(f"Invalid transition from {current_status} to {new_status}")
        raise ValueError(f"Invalid transition from {current_status} to {new_status}")

    order.status = new_status

    db.commit()
    db.refresh(order)

    logger.info(
        f"Order {order_id} status updated from {current_status} to {new_status}"
    )

    return order