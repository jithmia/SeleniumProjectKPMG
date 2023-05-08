Feature: Verifying the upper drop down menus

  Scenario: Trending is present on the KPMG home page
    Given user is on the home page
    And selects Trending on home page
    Then a drop down menu should appear under Trending
    Then links should work

  Scenario: Sectoren is present on the KPMG home page
    And selects Sectoren on home page
    Then a drop down menu should appear under Sectoren
    Then links should work


