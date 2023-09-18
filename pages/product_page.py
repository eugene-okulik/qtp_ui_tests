from pages.base_page import BasePage
from pages.locators import product_page_loc as loc


class ProductPage(BasePage):
    page_url = None

    def __init__(self, driver, product_url=None):
        super().__init__(driver)
        self.product_url = product_url

    def open(self,):
        if self.product_url:
            self.driver.get(f'{self.base_url}{self.product_url}')
        else:
            raise NotImplementedError('Product URL should be passed to object be able to open the page by URL')

    def add_to_cart_button_is_enabled(self):
        return self.find(loc.add_to_cart_button).is_enabled()
