from page_catalog import Base
from page_catalog import BASE_URL
import pytest

@pytest.mark.smoke
def test_01_page_catalog(browser):
    catalog = Base(browser)
    catalog.open_page()
    catalog.open_catalog_page()
    catalog.check_catalog_url(BASE_URL)
    catalog.choose_random_brand_car()
    catalog.choose_random_model_car()
    catalog.choose_random_car_location()
    catalog.choose_random_price_from()