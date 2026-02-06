from app.services.pricing import select_best_source

def test_select_best_source():
    sources = [
            {"price": 100, "available": True},
                    {"price": 80, "available": True},
                            {"price": 120, "available": False},
                                ]

                                    result = select_best_source(sources)
                                        assert result["price"] == 80