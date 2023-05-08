from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


@given('Chrome browser is launched')
def setup(context):
    context.driver = webdriver.Chrome()


@when('user opens the KPMG home page')
def go_to_browser(context):
    context.driver.get('https://kpmg.com/nl/nl/home.html')
    context.driver.maximize_window()


@given('accepts cookies')
def accept_cookie(context):
    wait = WebDriverWait(context.driver, 10)
    btn_cookie = wait.until(EC.element_to_be_clickable((By.XPATH, "// button[ @ id = 'onetrust-accept-btn-handler']")))
    btn_cookie.click()


@then('links should work')
def link_working(context):
    links = context.links
    for link in links:
        response = requests.get(link.get_attribute('href'))
        assert response.status_code == 200, f"Link {link.get_attribute('href')} is broken \
                                            with status code {response.status_code} "


@then('close browser')
def step_impl(context):
    context.driver.close()
