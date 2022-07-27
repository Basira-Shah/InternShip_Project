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
    MAC = (By.CSS_SELECTOR, "a[href='https://gettop.us/product-category/macbook/']")
    MAC13 = (By.XPATH, "//a[@href='https://gettop.us/product/macbook-pro-13/']")
    TOP_LINKS = (By.XPATH, "//ul[@class='header-nav header-nav-main nav nav-left  nav-uppercase']")

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
        time.sleep(2)
        actions = ActionChains(self.driver)
        iphone = self.find_element(*self.IPHONE)
        actions.move_to_element(iphone)
        actions.perform()

    def hover_mac(self):
        actions = ActionChains(self.driver)
        mac = self.find_element(*self.MAC)
        actions.move_to_element(mac)
        actions.perform()

    def click_cases_protection(self):
        self.click(*self.CASES_PROTECTION)

    def click_iphone12(self):
        self.click(*self.IPHONE12)

    def un_clickable_iphone(self):
        self.click(*self.IPHONE12)

    def click_mac_13(self):
        self.click(*self.MAC13)

    def verify_links(self, expected_links):
        time.sleep(3)
        actual_links = self.driver.find_elements(*self.TOP_LINKS)
        assert len(actual_links) == int(expected_links), \
            f' Expected {expected_links} links, but got {len(actual_links)}'
