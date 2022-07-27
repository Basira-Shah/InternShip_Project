from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep
from selenium.webdriver.common.keys import Keys

PRODUCT_PAGE = (By.CSS_SELECTOR, "h1.page-title")


@then('Verify the product page is appear with 404 error message')
def verify_product_page(context):
    expected_text = 'Oops! That page can’t be found.'
    context.app.product_page.verify_product_page(expected_text)


# Code for TMTN-197
@then('Verify the image is showing properly')
def verify_img(context):
    context.app.product_page.verify_img()
