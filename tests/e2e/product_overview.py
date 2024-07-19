import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_search_interactions(browser):
    # Simulate user search interactions and verify product filtering
    browser.get('http://localhost:8000/products')
    search_input = browser.find_element_by_id('search-input')
    search_input.send_keys('shirt')
    search_input.submit()
    product_cards = browser.find_elements_by_css_selector('.product-card')
    assert len(product_cards) > 0
    for card in product_cards:
        assert 'shirt' in card.text.lower()

def test_edge_cases(browser):
    # Test network error
    browser.get('http://localhost:8000/products')
    browser.execute_script("window.stop();")
    assert 'Network error' in browser.page_source
