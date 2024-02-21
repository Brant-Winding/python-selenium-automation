# Created by brand at 2/20/2024
Feature: target.com cart check

  Scenario: User can see empty cart
    Given Open Target main page
    When Click cart icon
    Then Verify “Your cart is empty” message is shown