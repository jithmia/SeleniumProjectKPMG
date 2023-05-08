from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given('selects Search button on home page')
def search(context):
    search_btn = context.driver.find_element(By.XPATH,
                                             "// header / div[ @ id = 'navigation-v2'] / div[1] / div[1] / nav[1] / div[2] / div[1] / button[1]")
    search_btn.click()


@given('enters \'blogs\'')
def enter_text(context):
    search_input = context.driver.find_element(By.ID, "desktop-search")
    search_input.send_keys('blogs', Keys.ENTER)


@then('a page with search items should appear')
def page_correct(context):
    expected_title = "Search results - KPMG Nederland"
    assert context.driver.title == expected_title, f"Expected title: '{expected_title}', but got '{context.driver.title}' "
