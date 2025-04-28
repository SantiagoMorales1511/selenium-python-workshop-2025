Feature: Login Feature
  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user logs in with invalid credentials
    Then an error message should be displayed

  Scenario: Empty login credentials
    Given the user is on the login page
    When the user logs in with empty credentials
    Then an error message should be displayed
