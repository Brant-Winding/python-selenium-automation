# Created by brand at 2/22/2024
Feature: Adding item to cart check

  Scenario: User can add item to cart
    Given Open Target main page
    When Search for Pedigree Adult Complete
    And Click Add to cart
    And Click Add to cart from side nav
    And Open Cart page
    Then Verify cart has 1 item(s)
