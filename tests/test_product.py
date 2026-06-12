import pytest
from src.product import Product

def test_product_creation():
    product = Product("Test Product", 10.99)
    assert product.name == "Test Product"
    assert product.price == 10.99

def test_product_equality():
    product1 = Product("Test Product", 10.99)
    product2 = Product("Test Product", 10.99)
    assert product1 == product2

def test_product_inequality():
    product1 = Product("Test Product", 10.99)
    product2 = Product("Different Product", 10.99)
    assert product1 != product2
