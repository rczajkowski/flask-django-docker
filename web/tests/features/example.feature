Feature: How to add new user
  Scenario: add new user
    When Im on /add
    And I fill username field username with testusername
    And I fill password field password with testpassword
    And I click add
    Then I should see success