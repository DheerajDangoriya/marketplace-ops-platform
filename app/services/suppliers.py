def get_supplier_cost(product_id: str) -> float:
    """
    Retrieves the cost price for a specific product from the supplier database.
    """
    # Placeholder: In a real app, this would query a database or CSV
    supplier_data = {
        "PROD-001": 45.50,
        "PROD-002": 120.00,
        "PROD-003": 15.75
    }
    return supplier_data.get(product_id, 0.0)

def list_available_suppliers():
    return ["Global Logistics", "Direct Wholesale", "Local Hub"]
def get_supplier_info(product_id: str):
    """
    Returns the cost price and supplier name for a given product ID.
    """
    # In a real app, this would query a database.
    database = {
        "SKU-001": {"cost_price": 50.0, "supplier": "TechWholesale"},
        "SKU-002": {"cost_price": 120.0, "supplier": "GlobalParts"},
    }
    
    return database.get(product_id, {"cost_price": 0.0, "supplier": "Unknown"})