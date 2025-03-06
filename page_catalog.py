from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time
import random
import logging
from locators_catalog import LocatorsCatalog as loc


"""Логирование (запись событий в консоль)"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://antcar.ru/"


class Base:
    """
    Что делает? Инициализирует объект браузера и явное ожидание (WebDriverWait).

    Зачем? Чтобы все методы класса могли использовать браузер и ожидания.
    """

    def __init__(self, browser):    
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open_page(self):
        """Открытие домашней страницы, cтартовая точка для тестов."""

        try:
            self.browser.get(BASE_URL)
            logger.info(f"Открыта страница: {BASE_URL}")
        except Exception as e:
            logger.error(f"Ошибка при открытии страницы: {e}")
            self.browser.save_screenshot("error_open_page.png")
            raise

    def open_catalog_page(self):
        """Попадание на сайт каталога автомобилей с домашней страницы сайта
            Если страница не открылась в течение 10 секунд, то ошибка"""
        
        try:
            logger.info("Открытие страницы каталога")
            catalog_button = self.wait.until(
                EC.presence_of_all_elements_located(loc.CATALOG_LOCATOR)
            )
            catalog_button[8].click()
            logger.info("Клик по кнопке каталога")
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "[data-testid='catalog-filters-header']")
                )
            )
            logger.info("Страница каталога загружена")
        except Exception as e:
            logger.error(f"Ошибка при открытии каталога: {e}")
            self.browser.save_screenshot("error_open_catalog.png")
            raise

    def check_catalog_url(self, expected_url):
        """Проверка URL каталога автомобилей, сравнивает актуальный URL с ожидаемым,
        если не совпадают, то ошибка"""

        actual_url = self.browser.current_url
        assert (
            expected_url == actual_url
        ), f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    def choose_random_brand_car(self):
        """Выбор случайной марки автомобиля"""

        try:
            self.wait.until(EC.element_to_be_clickable(loc.BRAND_LOCATOR)).click()
            brand_list = self.wait.until(
                EC.presence_of_all_elements_located(loc.BRAND_LIST_LOCATOR)
            )
            if not brand_list:
                raise ValueError("Список марок автомобилей пуст")
            random.choice(brand_list).click()
            logger.info("Случайная марка автомобиля выбрана")
        except Exception as e:
            self.browser.save_screenshot("error_brand_selection.png")
            logger.error(f"Ошибка при выборе марки автомобиля: {e}")
            raise

    def choose_random_model_car(self):
        """Выбор случайной модели автомобиля"""

        try:
            self.wait.until(EC.element_to_be_clickable(loc.MODEL_LOCATOR)).click()
            model_list = self.wait.until(
                EC.presence_of_all_elements_located(loc.MODEL_LIST_LOCATOR)
            )
            if not model_list:
                raise ValueError("Список моделей автомобилей пуст")
            random.choice(model_list).click()
            logger.info("Случайная модель автомобиля выбрана")
        except Exception as e:
            self.browser.save_screenshot("error_model_selection.png")
            logger.error(f"Ошибка при выборе модели автомобиля: {e}")
            raise

    def choose_random_car_location(self):
        """Выбор случайной страны нахождения автомобиля"""

        try:
            location_dropdown = self.wait.until(
                EC.element_to_be_clickable(loc.LOCATION_LOCATOR)
            )
            location_dropdown.click()
            location_list = self.wait.until(
                EC.presence_of_all_elements_located(loc.LOCATION_LIST_LOCATOR)
            )
            if not location_list:
                raise ValueError("Список стран пуст")
            random.choice(location_list).click()
            logger.info("Случайная страна выбрана")
        except Exception as e:
            self.browser.save_screenshot("error_location_selection.png")
            logger.error(f"Ошибка при выборе страны: {e}")
            raise

    def choose_random_price_from(self):
        """Выбор случайной цены OT"""

        try:
            self.wait.until(EC.element_to_be_clickable(loc.PRICE_FROM_LOCATOR)).click()
            car_price_list = self.wait.until(
                EC.presence_of_all_elements_located(loc.PRICE_LIST_LOCATOR)
            )
            if not car_price_list:
                raise ValueError("Список цен пуст")
            random.choice(car_price_list).click()
            logger.info("Случайная цена выбрана")
        except Exception as e:
            self.browser.save_screenshot("error_price_selection.png")
            logger.error(f"Ошибка при выборе цены: {e}")
            raise

    def choose_random_price_to(self):

        try:
            self.wait.until(EC.element_to_be_clickable(loc.PRICE_TO_LOCATOR)).click()
            car_price_list = self.wait.until(
                EC.presence_of_all_elements_located(loc.PRICE_LIST_LOCATOR)
            )
            if not car_price_list:
                raise ValueError("Список цен пуст")
            random.choice(car_price_list).click()
            logger.info("Случайная цена выбрана")
        except Exception as e:
            self.browser.save_screenshot("error_price_selection.png")
            logger.error(f"Ошибка при выборе цены: {e}")
            raise