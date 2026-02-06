from app.services.marketplace import fetch_new_orders
from app.services.pricing import select_best_source

def run_workflow():
    orders = fetch_new_orders()

        for order in orders:
                suppliers = [
                            {"name": "Supplier A", "price": 120, "available": True},
                                        {"name": "Supplier B", "price": 110, "available": True},
                                                    {"name": "Supplier C", "price": 130, "available": False},
                                                            ]

                                                                    best_supplier = select_best_source(suppliers)
                                                                            print(f"Order {order['order_id']} assigned to {best_supplier['name']}")