# Created by ahmadshah at 7/11/22
Feature: Tests for GetTop logo
# Code for TMTN-125
  Scenario: Verify that GetTop logo is clickable and takes to the home page
    Given Open GetTop page
    When click the logo sign
    Then verify GetTop logo is clickable and takes to the home page

  # Code for TMTN-194
  Scenario: Verify that the page gives a 404 error message
    Given Open GetTop page
    When Hover over Accessories
    And Click on Cases & Protection from the drop-down menu
    Then Verify the product page is appear with 404 error message

  # Code for TMTN-195
  Scenario: iPhone 12 option is un clickable from the drop-down menu under iPhone
    Given Open GetTop page
    When Hover over iPhone
    And Click on iPhone 12 option from the drop-down menu
    Then Verify the iPhone 12 option is un clickable

  # Code for TMTN-197
  Scenario: Verify that the image of MacBook Pro 13-inch is present properly
    Given Open GetTop page
    When Hover over Mac
    And Click on MacBook Pro 13-inch from the drop-down menu
    Then Verify the image is showing properly