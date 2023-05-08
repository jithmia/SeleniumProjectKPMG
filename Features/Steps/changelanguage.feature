@last
Feature: Verifying changing the language

  Scenario Outline: Language can be changed
    Given user is on the home page
    And selects the icon of the world at the top right corner
    And enters "<Language>" in text box
    And selects "<Country>" in drop down menu
    And accepts cookies
    Then the page should refresh in selected language

    Examples:
    |Language     |Country          |
    |Global       |Global (EN)      |
    |Netherlands  |Netherlands (EN) |


