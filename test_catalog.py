from page_catalog import Base
import pytest

expected_url = "https://antcar.ru/catalog"
@pytest.mark.smoke
def test_01_page_catalog(browser):
    catalog = Base(browser)
    catalog.open_page()
    catalog.open_catalog_page()
    catalog.check_catalog_url(expected_url)
    catalog.choose_random_brand_car()
    catalog.choose_random_model_car()
    #catalog.choose_random_car_location()
    catalog.choose_random_price_from()
    catalog.choose_random_price_to()
    catalog.choose_years_from_car("1")
    catalog.choose_years_to_car('10')