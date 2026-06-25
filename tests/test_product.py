from src.axentx_product.product import Product

def test_product_init():
    product = Product("Test Product", 0.8)
    assert product.name == "Test Product"
    assert product.demand_score == 0.8

def test_product_is_high_demand():
    product = Product("Test Product", 0.8)
    assert product.is_high_demand()

def test_product_is_not_high_demand():
    product = Product("Test Product", 0.2)
    assert not product.is_high_demand()
