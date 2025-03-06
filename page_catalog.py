from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time
import random
from locators_catalog import LocatorsCatalog as loc


BASE_URL = "https://antcar.ru/"

class Base:


    def __init__(self, browser):
        self.browser = browser
        wait = WebDriverWait(browser, 10)
        self.wait = wait

    def open_page(self):
        self.browser.get(BASE_URL)
    
    def open_catalog_page(self):
        """Opens the catalog page by clicking on the 8th element with class name rounded-xl"""
        catalog_button = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "rounded-xl"))
        )
        catalog_button[8].click()
        time.sleep(1)

    
    def check_catalog_url(self, expected_url):
        actual_url = self.browser.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    def choose_random_brand_car(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "car-brand"))).click()
        brand_list = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[data-testid='select-option']")
            )
        )
        random.choice(brand_list).click()

    def choose_random_model_car(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "car-model"))).click()
        model_list = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[data-testid='rc-select-item-option']")
            )
        )
        time.sleep(0.5)
        random.choice(model_list).click()

    def choose_random_car_location(self):
        self.wait.until(
            EC.presence_of_element_located((By. ID, "car-location"))
        ).click()
        time.sleep(0.5)
        location_list = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[data-testid='rc-select-item-option']")
            )
        )
        random.choice(location_list).click()
        time.sleep(1)

    def choose_random_price_from(self):
        self.browser.find_element(By.ID, "car-price-from").click()
        car_price_list = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[data-testid='select-option']")
            )
        )
        random.choice(car_price_list).click()















time.sleep(3)
