from behave import *
from selenium.webdriver.common.by import By
from Features.Steps.common_functions import select_icon, enter_text, select_lang


@given('selects the icon of the world at the top right corner')
def select_icon1(context):
    select_icon(context)


@given('enters "{lang}" in text box')
def enter_text1(context, lang):
    enter_text(context, lang)


@given('selects "{lang}" in drop down menu')
def enter_text1(context, lang):
    select_lang(context, lang)


@then('the page should refresh in selected language')
def change_language(context):
    html_element = context.driver.find_element(By.TAG_NAME, 'html')
    lang_value = html_element.get_attribute('lang')

    expected_value = 'en-US'  # works for English
    assert lang_value == expected_value, f'Error: Language is {lang_value}, but expected {expected_value}'
