# Day 22 - Page Object Model (POM)

## 1. What is Page Object Model?

Page Object Model (POM) is a Selenium design pattern where each web page
or major component of an application is represented by a Python class.

The class contains:

- Locators
- Web element interactions
- Page-specific methods

The test file contains the actual test scenarios and assertions.

### Basic structure

Page = Class
Element = Locator
Action = Method
Test = Business scenario + Assertion

---

## 2. Why do we use POM?

Without POM, locators and Selenium actions are repeated inside test cases.

Example:

```python
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

If the locator changes, we may have to modify many test files.

With POM:

login_page.login("standard_user", "secret_sauce")


3. Advantages of POM
Maintainability

If the UI locator changes, update it in the page class.

Reusability

The same page methods can be reused by multiple tests.

Readability

Tests become easier to understand.

Example:

login_page.login(username, password)
home_page.verify_home_page()
Reduced duplication

Common Selenium code is kept inside page classes.

Easier debugging

Page-specific failures can be isolated.