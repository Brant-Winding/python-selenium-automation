# Created by brand at 2/22/2024
Feature: target.com/circle check

  #Scenario: Verify there are correct amount benefit boxes
   # Given Open Target circle page
    #Then Verify there are 5 benefit boxes

  Scenario: User is able to navigate to Google Play Target page
    Given Open Target circle page
    And Store original window
    When Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current page
    And Return to original window