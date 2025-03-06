from selenium.webdriver.common.by import By


class LocatorsCatalog:
    #CATALOG
    CATALOG_LOCATOR = (By.CLASS_NAME, "rounded-xl")

    #BRAND
    BRAND_LOCATOR = (By.ID, "car-brand")
    BRAND_LIST_LOCATOR = (By.CSS_SELECTOR, "[data-testid='select-option']")

    #MODEL
    MODEL_LOCATOR = (By.ID, "car-model")
    MODEL_LIST_LOCATOR = (By.CSS_SELECTOR, "[data-testid='rc-select-item-option']")

    #LOCATION
    LOCATION_LOCATOR = (By.ID, "car-location")
    LOCATION_LIST_LOCATOR = (By.CSS_SELECTOR, "[data-testid='rc-select-item-option']")

    #PRICE
    PRICE_FROM_LOCATOR = (By.ID, "car-price-from")
    PRICE_LIST_LOCATOR = (By.CSS_SELECTOR, "[data-testid='select-option']")
    PRICE_TO_LOCATOR = (By.ID, "car-price-to")

    #YEARS
    YEARS_FROM_LOCATOR = (By.ID, "car-years-from")
    YEARS_LIST_LOCATOR = (By.CSS_SELECTOR, "[data-testid='select-option']")
    YEARS_TO_LOCATOR = (By.ID, "car-years-to")
    
    #OWNERS
    OWNERS_LOCATOR = (By.CLASS_NAME, "py-3")
    OWNERS_FROM_LOCATOR = (By.ID, "car-owners-from")
    OWNERS_TO_LOCATOR = (By.ID, "car-owners-to")
