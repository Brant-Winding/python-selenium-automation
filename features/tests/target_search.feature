# Created by brand at 2/20/2024
Feature: target.com search tests

  Scenario: user can search for product on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee is shown
    Then Page URL has search term coffee


  Scenario: user can search for product on target
    Given Open Target main page
    When Search for mug
    Then Search results for mug is shown
    Then Page URL has search term mug


  Scenario: user can search for product on target
    Given Open Target main page
    When Search for dog food
    Then Search results for dog food is shown
    Then Page URL has search term dog+food
