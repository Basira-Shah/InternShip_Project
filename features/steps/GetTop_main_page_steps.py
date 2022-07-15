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

# Code for TMTN-125
@when('click the logo sign')
def click_logo(context):
    # context.driver.find_element(*LOGO).click()
    context.app.header.click_logo()

# For TMTN-194
@when('Hover over Accessories')
def hover_access(context):
    context.app.header.hover_access()

# For TMTN-194
@when('Click on Cases & Protection from the drop-down menu')
def click_cases_protection(context):
    context.app.header.click_cases_protection()

# For TMNT-195
@when('Hover over iPhone')
def hover_iphone(context):
    context.app.header.hover_iphone()

# For TMNT-195
@when('Click on iPhone 12 option from the drop-down menu')
def click_iphone12(context):
    context.app.header.click_iphone12()

# Code for TMTN-197
@when('Hover over Mac')
def hover_mac(context):
    context.app.header.hover_mac()

# Code for TMTN-197
@when('Click on MacBook Pro 13-inch from the drop-down menu')
def click_mac_13(context):
    context.app.header.click_mac_13()


# Code for TMTN-125
@then('verify GetTop logo is clickable and takes to the home page')
def clickable_logo(context):
    # context.driver.wait.until(EC.url_contains('https://gettop.us/'))
    context.app.header.verify_url_contains_clickable_logo('https://gettop.us/')

# Code for TMNT-195
@then('Verify the iPhone 12 option is un clickable')
def un_clickable_iphone(context):
    context.app.header.un_clickable_iphone()







