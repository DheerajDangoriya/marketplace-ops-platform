from app.logging_config import logger


def select_best_source(suppliers):
    """
    Select the best supplier based on price and availability.
    """

    available_suppliers = [s for s in suppliers if s.get("available")]

    if not available_suppliers:
        logger.warning("No available suppliers found")
        return None

    best_supplier = min(available_suppliers, key=lambda s: s["price"])

    logger.info(
        f"Best supplier selected: {best_supplier.get('name', 'unknown')} "
        f"with price {best_supplier['price']}"
    )

    return best_supplier