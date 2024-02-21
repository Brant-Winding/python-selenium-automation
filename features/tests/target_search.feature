# Created by brand at 2/20/2024
Feature: target.com search tests

  Scenario: user can search for product on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee is shown