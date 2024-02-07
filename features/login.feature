Feature: login feature

  Background:
    Given I am on the login page

  @validCredentials
  Scenario: login with valid credentials
    When I enter a valid email
    And I enter a valid password
    And I click the login button
    Then I should be on the products page

  @invalidPassword
  Scenario: login with invalid password
    When I enter a valid email
    And I enter an invalid password
    And I click the login button
    Then I should see an error message

  @invalidEmail
  Scenario: login with invalid username
    When I enter an invalid email
    And I enter a valid password
    And I click the login button
    Then I should see an error message

  Scenario Outline: login with invalid credentials
    When I enter "<username>" as username
    And I enter "<password>" as password
    And I click the login button
    Then I should see an error message
    Examples:
      | username      | password     |
      | username1     | wrong        |
      | standard_user | wrong        |
      | username1     | secret_sauce |
