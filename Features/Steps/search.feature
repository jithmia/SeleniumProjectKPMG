Feature: Verifying the search feature

  Scenario: Search functionality is working
    Given user is on the home page
    And selects Search button on home page
    And enters 'blogs'
    Then a page with search items should appear
