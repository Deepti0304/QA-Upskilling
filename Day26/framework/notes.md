# Day 25 - Reporting & Data Driven Testing

## Objective

Learn test reporting using:
- Allure
- Pytest HTML
- Screenshots
- Test steps
- Test severity
- Test features
- Data-driven testing

---

## Framework

- Python
- Selenium
- Pytest
- Allure
- Page Object Model
- JSON

---

## Data Driven Testing

Test data is stored externally in:

data/login_data.json

pytest.mark.parametrize() is used to execute
the same test with multiple datasets.

Example:

@pytest.mark.parametrize("test_data", data)

---

## Positive Test

Valid username and password should allow login.

Expected:

Login successful.

---

## Negative Tests

1. Invalid username
2. Invalid password
3. Empty username/password
4. Locked user

---

## Configuration Management

Application URL is stored in:

resources/config.ini

Example:

[environment]
base_url = https://www.saucedemo.com/

The URL is never hardcoded in test files.

---

## Page Object Model

LoginPage:
- Username
- Password
- Login button
- Error message

HomePage:
- Products title
- Menu
- Logout

---

## Allure

Generate results:

pytest --alluredir=reports/allure-results

Open report:

allure serve reports/allure-results

---

## Pytest HTML

Generate:

pytest --html=reports/report.html --self-contained-html

---

## Screenshots

Screenshots are captured automatically
when a test fails.

Screenshots are attached to Allure.

---

## Allure Annotations

@allure.feature("Login")

@allure.story("Data Driven Login")

@allure.step("Verify successful login")

---

## Important Interview Point

A good framework should separate:

Test logic
    ↓
Page objects
    ↓
Test data
    ↓
Configuration
    ↓
Reporting

This improves maintainability and reusability.