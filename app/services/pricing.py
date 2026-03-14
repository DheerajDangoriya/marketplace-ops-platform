def select_best_source(sources):
    """
    Selects the cheapest available supplier.
    """
    available = [s for s in sources if s["available"]]
    if not available:
        return None
    return min(available, key=lambda x: x["price"])