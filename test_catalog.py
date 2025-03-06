from page_catalog import Base


def test_01_page_catalog(browser):
    catalog = Base(browser)
    catalog.open_page()
    catalog.open_catalog_page()
    catalog.check_catalog_url("https://antcar.ru/catalog")
    catalog.choose_random_brand_car()
    catalog.choose_random_model_car()
    catalog.choose_random_car_location()
    catalog.choose_random_price_from()