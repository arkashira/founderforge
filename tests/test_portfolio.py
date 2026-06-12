from src.axentx_product.portfolio import Portfolio
from src.axentx_product.product import Product

def test_portfolio_add_product():
    portfolio = Portfolio()
    product = Product("Test Product", 100)
    portfolio.add_product(product)
    assert len(portfolio.products) == 1

    portfolio.add_product(product)
    assert len(portfolio.products) == 1

def test_portfolio_get_validated_products():
    portfolio = Portfolio()
    product1 = Product("Test Product 1", 100)
    product2 = Product("Test Product 2", 50)
    portfolio.add_product(product1)
    portfolio.add_product(product2)
    validated_products = portfolio.get_validated_products()
    assert len(validated_products) == 1
    assert validated_products[0].name == "Test Product 1"
