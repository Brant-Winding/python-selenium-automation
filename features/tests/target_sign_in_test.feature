# Created by brand at 2/20/2024
Feature: Target.com sign in check

  Scenario: User can sign in to Target account
    Given Open Target main page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened