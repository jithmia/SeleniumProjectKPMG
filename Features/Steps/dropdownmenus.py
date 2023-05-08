from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('user is on the home page')
def user(context):
    pass


@given('selects Trending on home page')
def trending(context):
    wait = WebDriverWait(context.driver, 10)
    dropdown_trending = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//body[1]/div[1]/header[1]/div[2]/div[1]/div[1]/nav[1]/ul[1]/li[1]/a[1]")))

    dropdown_trending.click()


@then('a drop down menu should appear under Trending')
def drop_down_trending(context):
    dropdown_menu = context.driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[2]/div[1]/div[1]/nav["
                                                          "1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/nav[1]")

    context.links = WebDriverWait(dropdown_menu, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

    # all the following topics will be checked under Trending drop down menu
    expected_values = ["ESG & Sustainability", "Digitale Transformatie",
                       "De Energietransitie", "Mobility 2030",
                       "Het Pensioenakkoord", "Risicobereidheid onder bestuurders", "Bekijk meer"]

    link_texts = {link.text for link in context.links}

    for expected_value in expected_values:
        assert expected_value in link_texts, f'{expected_value} not found in links'


@then('selects Sectoren on home page')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    txt_sector = wait.until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/header[1]/div[2]/div[1]/div["
                                                                  "1]/nav[1]/ul[1]/li[2]/a[1]")))
    txt_sector.click()


@then('a drop down menu should appear under Sectoren')
def drop_down_sector(context):
    dropdown_menu = context.driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[2]/div[1]/div[1]/nav["
                                                          "1]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]")
    context.links = WebDriverWait(dropdown_menu, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))

    expected_values = ["Consumentenmarkt & Retail", "Energy & Natural Resources",
                       "Financial services", "Gezondheidszorg",
                       "Publieke sector", "Technology, Media & Telecom", "Bekijk meer"]

    link_texts = {link.text for link in context.links}

    for expected_value in expected_values:
        assert expected_value in link_texts, f'{expected_value} not found in links'
