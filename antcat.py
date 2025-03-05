from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time
import random
from locators_catalog import LocatorsCatalog as loc


class Base:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://antcar.ru/")
    wait = WebDriverWait(browser, 10)

    catalog = wait.until(
        EC.presence_of_all_elements_located((loc.catalog_loc))
    )[8].click()


    brand_car = wait.until(EC.presence_of_element_located((loc.brand_car_loc))).click()
    brand_list = wait.until(
        EC.presence_of_all_elements_located(
            (loc.brand_list_loc)
        )
    )
    chosen_brand = random.choice(brand_list).click()


    model_car = wait.until(EC.presence_of_element_located((loc.model_car_loc))).click()
    model_list = wait.until(
        EC.presence_of_all_elements_located(
            (loc.model_list_loc)
        )
    )
    chosen_model = random.choice(model_list).click()

    car_location = browser.find_element(loc.car_location_loc).click()
    time.sleep(0.5)
    location_list = wait.until(
        EC.presence_of_all_elements_located(
            (loc.location_list_loc)
        )
    )
    chosen_location = random.choice(location_list).click()
    time.sleep(1)

    car_price_from = browser.find_element(loc.car_price_from_loc).click()
    car_price_list = wait.until(
        EC.presence_of_all_elements_located(
            (loc.car_price_list_loc)
        )
    )
    chosen_price_from = random.choice(car_price_list).click()


    car_price_to = browser.find_element(loc.car_price_to_loc).click()
    car_price_list = wait.until(
        EC.presence_of_all_elements_located(
            (loc.car_price_list_loc)
        )
    )
    chosen_price_to = random.choice(car_price_list).click()

    time.sleep(0.5)
    car_years_from = browser.find_element(loc.car_years_from_loc).send_keys(1)
    car_years_to = browser.find_element(loc.car_years_to_loc).send_keys(10)

    owners = browser.find_elements(loc.owners_loc)[2].click()
    car_owners_from = wait.until(
        EC.presence_of_element_located((loc.car_owners_from_loc))
    ).send_keys(1)
    car_owners_to = browser.find_element(loc.car_owners_to_loc).send_keys(10)

    car_mileage_from = browser.find_element(loc.car_mileage_from_loc).send_keys(1)
    car_mileage_to = browser.find_element((loc.car_mileage_to_loc)).clear()
    car_mileage_to = browser.find_element(loc.car_mileage_to_loc).send_keys(100000000)














time.sleep(3)
