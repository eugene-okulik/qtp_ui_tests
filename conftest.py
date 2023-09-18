from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from pages.sale_page import SalePage
from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


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
