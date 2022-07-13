from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class Product(Page):
    PRODUCT_PAGE = (By.CSS_SELECTOR, "h1.page-title")

    def verify_product_page(self, expected_text):
        self.verify_text(expected_text, *self.PRODUCT_PAGE)


