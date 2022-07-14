import time

from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class Header(Page):
    LOGO = (By.XPATH, "//div[@id='logo']/a")
    ACCESSORIES = (By.CSS_SELECTOR, "a[href='https://gettop.us/product-category/accessories/airpods/']")
    CASES_PROTECTION = (By.CSS_SELECTOR, "a[href='/cases']")
    IPHONE = (By.CSS_SELECTOR, "a.nav-top-link")
    IPHONE12 = (By.CSS_SELECTOR, "a[href='https://gettop.us/product-category/iphone/']")



    def click_logo(self):
        time.sleep(2)
        self.click(*self.LOGO)

    def verify_url_contains_clickable_logo(self, url):
        self.verify_url_contains_query(url)

    def hover_access(self):
        actions = ActionChains(self.driver)
        accessories = self.find_element(*self.ACCESSORIES)
        actions.move_to_element(accessories)
        actions.perform()

    def hover_iphone(self):
        actions = ActionChains(self.driver)
        iphone = self.find_element(*self.IPHONE)
        actions.move_to_element(iphone)
        actions.perform()

    def click_cases_protection(self):
        self.click(*self.CASES_PROTECTION)

    def click_iphone12(self):
        self.click(*self.IPHONE12)

    def un_clickable_iphone(self):
        self.click(*self.IPHONE12)