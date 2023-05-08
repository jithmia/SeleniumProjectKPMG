from behave import *
from selenium.webdriver.common.by import By


@then('the KPMG logo is visible')
def logo(context):
    image_element = context.driver.find_element(By.XPATH, "//img[@alt='KPMG']")
    assert image_element.is_displayed()
