from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def select_icon(context):
    wait = WebDriverWait(context.driver, 10)
    language_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-toggle='dropdown' and "
                                                                       "@aria-label='Site Selector']")))
    language_select.click()


def enter_text(context, lang):
    language_txt = context.driver.find_element(By.ID, "country-site-selector-search")
    language_txt.send_keys(lang)


def select_lang(context, lang):
    language_global = context.driver.find_element(By.LINK_TEXT, f"{lang}")
    language_global.click()
