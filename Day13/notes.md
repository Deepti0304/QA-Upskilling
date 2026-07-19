# Day 13 - Selenium Locators

## ID

Fastest and unique.

Example:

driver.find_element(By.ID, "username")

--------------------------------

## Name

Used when ID is unavailable.

driver.find_element(By.NAME, "password")

--------------------------------

## Class Name

driver.find_element(By.CLASS_NAME, "btn")

Avoid when multiple elements share the same class.

--------------------------------

## Tag Name

driver.find_elements(By.TAG_NAME, "button")

--------------------------------

## Link Text

driver.find_element(By.LINK_TEXT, "Login")

--------------------------------

## Partial Link Text

driver.find_element(By.PARTIAL_LINK_TEXT, "Log")

--------------------------------

Locator Preference

1. ID
2. Name
3. CSS Selector
4. XPath
5. Class Name
6. Tag Name