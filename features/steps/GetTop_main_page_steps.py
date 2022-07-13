from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep
from selenium.webdriver.common.keys import Keys

LOGO = (By.XPATH, "//div[@id='logo']/a")


@given('Open GetTop page')
def open_GetTop(context):
    # context.driver.get('https://gettop.us/')
    context.app.main_page.open_GetTop()


@when('click the logo sign')
def click_logo(context):
    # context.driver.find_element(*LOGO).click()
    context.app.header.click_logo()


@when('Hover over Accessories')
def hover_access(context):
    context.app.header.hover_access()


@when('Click on Cases & Protection from the drop-down menu')
def click_cases_protection(context):
    context.app.header.click_cases_protection()


@then('verify GetTop logo is clickable and takes to the home page')
def clickable_logo(context):
    # context.driver.wait.until(EC.url_contains('https://gettop.us/'))
    context.app.header.verify_url_contains_clickable_logo('https://gettop.us/')



