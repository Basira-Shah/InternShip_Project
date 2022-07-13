from pages.main_page import MainPage
from pages.header import Header
from pages.product_page import Product


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.product_page = Product(self.driver)
