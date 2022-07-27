from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Product(Page):
    PRODUCT_PAGE = (By.CSS_SELECTOR, "h1.page-title")
    MAC_IMG = (By.CSS_SELECTOR, "img[src='https://gettop.us/wp-content/uploads/2013/08/mc13-1-1536x1510-1-600x590.jpg']")

    def verify_product_page(self, expected_text):
        self.verify_text(expected_text, *self.PRODUCT_PAGE)

    def verify_img(self):
        self.wait.until(EC.presence_of_element_located(self.MAC_IMG))
