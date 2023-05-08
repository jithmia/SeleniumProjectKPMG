from selenium.webdriver.common.by import By
from behave import *


@given('selects the links for the above topics')
def selects_links(context):
    link_elements = context.driver.find_elements(By.XPATH, '//a[@class="inner-section chrome"][@data-title]')
    link_text = [link.get_attribute("data-title").strip() for link in link_elements]
    context.links = link_elements  # to be used in link_working()

    # all the following topics will be checked in the home page
    expected_values = ["ESG & Sustainability", "De energietransitie", "Corporate Sustainability Reporting Directive",
                       "Onze mensen", "KPMG: vier Nederlandse grootbanken financieel gezond in 2022",
                       "Laadpaalfiles dreigen voor Nederlandse wintersporters",
                       "Jaarcijfers KPMG Nederland: bedrijf groeit sterk in veranderende wereld",
                       "KPMG scherpt accountantscontrole klimaatverantwoording aan"]

    # check if all the expected values are in the links
    # this will work in the Dutch site only
    for expected_value in expected_values:
        assert expected_value in link_text, f'{expected_value} not found in links'
