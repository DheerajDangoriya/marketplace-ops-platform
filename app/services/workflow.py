from app.services.marketplace import fetch_new_orders
from app.services.pricing import select_best_source
from app.logging_config import logger


def run_workflow(db=None):
    logger.info("Workflow started")

    orders = fetch_new_orders(db)

    for order in orders:
        logger.info(f"Processing order {order.id}")

        suppliers = [
            {"name": "Supplier A", "price": 120, "available": True},
            {"name": "Supplier B", "price": 110, "available": True},
            {"name": "Supplier C", "price": 130, "available": False},
        ]

        best_supplier = select_best_source(suppliers)

        if best_supplier:
            logger.info(f"Order {order.id} assigned to {best_supplier.get('name', 'unknown')}")
        else:
            logger.warning(f"No supplier available for order {order.id}")

    logger.info("Workflow completed")

    return {"processed_orders": len(orders)}