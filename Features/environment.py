import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Features.Steps.common_functions import select_icon, enter_text, select_lang


def before_all(context):
    driver_path = os.path.join(os.getcwd(), "Drivers", "chromedriver.exe")
    context.driver = webdriver.Chrome(executable_path=driver_path)
    # context.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
    context.driver.get('https://kpmg.com/nl/nl/home.html')
    context.driver.maximize_window()
    wait = WebDriverWait(context.driver, 10)

    # accepts cookies, as the other elements aren't clickable until this dialog goes away
    try:
        btn_cookie = wait.until(EC.element_to_be_clickable((By.XPATH, "// button[ @ id = 'onetrust-accept-btn-handler']")))
        btn_cookie.click()
    except NoSuchElementException:
        print("No cookies pop up found")


def after_all(context):
    context.driver.quit()


# Change the language to Dutch after this feature
def after_feature(context, feature):
    if feature.name == 'Verifying changing the language':
        select_icon(context)
        enter_text(context, 'Netherlands (NL)')
        select_lang(context, 'Netherlands (NL)')
