import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_product_overview_integration(client):
    # Test that the product overview page is properly integrated with Vue and backend API
    response = client.get('/products')
    assert response.status_code == 200
    assert b'<div id="app">' in response.data

def test_search_bar(client):
    # Test search bar functionality
    response = client.get('/products?search=shirt')
    assert b'<product-card v-for="product in filteredProducts"' in response.data

    # Test edge case: empty product list
    response = client.get('/products?search=invalidquery')
    assert b'No products found' in response.data

def test_product_filtering(client):
    # Test that product list is correctly filtered based on search input
    response = client.get('/products?search=shirt')
    product_data = response.get_json()
    for product in product_data:
        assert 'shirt' in product['name'].lower()
