Test Framework for www.kpmg.nl

Introduction:
This test framework is designed to automate the testing of the www.kpmg.nl website using Selenium and Behave. The framework is built in Python and includes Gherkin-style test scenarios.
This framework is specifically designed to test the kpmg.nl - Netherlands(NL) site, it uses keywords from the site that are in Dutch.

Prerequisites:
Before running the test framework, please ensure that the following software is installed:

Python 3.10.8
pip (Python package manager)
Allure (https://docs.qameta.io/allure/)

Setup:
Install the Python dependencies by running 'pip install -r requirements.txt'.

Running the Tests:
To run the test framework, open a command prompt or terminal window and navigate to the root directory of the repository. Then run the following command:
behave

Test Results:
After running the tests, Behave will generate a report in the reports directory that includes detailed information about each test scenario, including the status (passed or failed), duration, and any errors or warnings encountered.

Additionally, an html report can be generated by the following command
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% 
allure serve %allure_result_folder%

Details of testcases included :

1. Verifying changing the language - The language of the site is changed to Global(EN) using this feature, the changed language is verified and afterwards, the language is changed back to
Netherlands (NL)
2. Verifying the upper drop down menus - There are drop down menus at the top pertaining to 'Trending', 'Sectoren', 'Services', 'Over ons' etc. 
In this test, the two topics 'Trending' and 'Sectoren' are tested, after clicking on the topics the drop down menu is verified by name and the links are also verified to be working correctly.
3. Verifying the links for ESG & Sustainability, De energietransitie, Corporate Sustainability Reporting Directive,
  Onze mensen, KPMG: vier Nederlandse grootbanken financieel gezond in 2022, Laadpaalfiles dreigen voor Nederlandse wintersporters,
  Jaarcijfers KPMG Nederland: bedrijf groeit sterk in veranderende wereld, KPMG scherpt accountantscontrole klimaatverantwoording aan - all these are sections in the kpmg.nl site. The availability of all the above elements are verified and the hyper link is also verified to be working.
4. Verifying the search feature - A text is entered after clicking on the search button at the top right corner, the resulting page is also verified to be correct.
5. Verified the presence of the KPMG logo
