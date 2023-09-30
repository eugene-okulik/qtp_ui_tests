from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.login_page import LoginPage
from pages.sale_page import SalePage
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from time import sleep
import random


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    sleep(3)
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.save_screenshot(f'{str(random.randint(100, 10000))}.png')


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def category_page(driver):
    return CategoryPage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)
