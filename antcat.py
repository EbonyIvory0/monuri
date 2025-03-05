from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time
import random
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://antcar.ru/")
wait = WebDriverWait(browser, 10)

catalog = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "rounded-xl"))
)[8].click()


brand_car = wait.until(EC.presence_of_element_located((By.ID, "car-brand"))).click()
brand_list = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[data-testid='select-option']")
    )
)
chosen_brand = random.choice(brand_list).click()


model_car = wait.until(EC.presence_of_element_located((By.ID, "car-model"))).click()
model_list = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[data-testid='rc-select-item-option']")
    )
)
chosen_model = random.choice(model_list).click()

car_location = browser.find_element(By.ID, "car-location").click()
time.sleep(0.5)
location_list = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[data-testid='rc-select-item-option']")
    )
)
chosen_location = random.choice(location_list).click()
time.sleep(1)

car_price_from = browser.find_element(By.ID, "car-price-from").click()
car_price_list = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[data-testid='select-option']")
    )
)
chosen_price_from = random.choice(car_price_list).click()


car_price_to = browser.find_element(By.ID, "car-price-to").click()
car_price_list = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[data-testid='select-option']")
    )
)
chosen_price_to = random.choice(car_price_list).click()

time.sleep(0.5)
car_years_from = browser.find_element(By.ID, "car-years-from").send_keys(1)
car_years_to = browser.find_element(By.ID, "car-years-to").send_keys(10)

owners = browser.find_elements(By. CLASS_NAME, "py-3")[2].click()
car_owners_from = wait.until(
    EC.presence_of_element_located((By. ID, "car-owners-from"))
).send_keys(1)
car_owners_to = browser.find_element(By. ID, "car-owners-to").send_keys(10)

car_mileage_from = browser.find_element(By. ID, "car-mileage-from").send_keys(1)
car_mileage_to = browser.find_element(By. ID, "car-mileage-to").clear()
car_mileage_to = browser.find_element(By. ID, "car-mileage-to").send_keys(100000000)













time.sleep(3)
