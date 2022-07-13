# Created by ahmadshah at 7/11/22
Feature: Tests for GetTop logo

  Scenario: Verify that GetTop logo is clickable and takes to the home page
    Given Open GetTop page
    When click the logo sign
    Then verify GetTop logo is clickable and takes to the home page

  Scenario: Verify that the page gives a 404 error message
    Given Open GetTop page
    When Hover over Accessories
    And Click on Cases & Protection from the drop-down menu
    Then Verify the product page is appear with 404 error message
