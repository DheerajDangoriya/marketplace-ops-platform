from app.services.marketplace import fetch_new_orders

def test_fetch_orders_returns_orders():
    orders = fetch_new_orders()
    assert isinstance(orders, list)
    for order in orders:
        # Fixed: changed 'id' to 'order_id'
        assert 'order_id' in order 
        assert 'sku' in order