# Day 16 - Web Element Interactions

## Objective

Learn how to interact with common web elements using Selenium.

Topics covered:

* click()
* send_keys()
* clear()
* text
* get_attribute()
* is_displayed()
* is_enabled()
* is_selected()
* Text fields
* Dropdowns
* Radio buttons
* Checkboxes
* Submit buttons
* Assertions
* Explicit waits

Practice website:

https://demoqa.com/automation-practice-form

---

# 1. click()

The `click()` method is used to click an element.

It can be used with:

* Buttons
* Links
* Radio buttons
* Checkboxes

Example:

```python
element.click()
```

Example:

```python
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()
```

---

# 2. send_keys()

The `send_keys()` method is used to enter text into input fields.

Example:

```python
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("Deepti")
```

For a text field:

```python
username.send_keys("admin")
```

For a password field:

```python
password.send_keys("Password123")
```

---

# 3. clear()

The `clear()` method removes existing text from an input field.

Example:

```python
username.clear()
```

Complete example:

```python
username.send_keys("Old Value")

username.clear()

username.send_keys("New Value")
```

---

# 4. text

The `text` property returns the visible text of an element.

Example:

```html
<h1>Student Registration Form</h1>
```

Python:

```python
heading = driver.find_element(By.TAG_NAME, "h1")

print(heading.text)
```

Output:

```text
Student Registration Form
```

Important:

```python
element.text
```

Correct.

Do not use:

```python
element.text()
```

because `text` is a property, not a method.

---

# 5. get_attribute()

The `get_attribute()` method is used to retrieve the value of an HTML attribute.

Example HTML:

```html
<input id="username"
       placeholder="Enter username"
       value="Deepti">
```

Python:

```python
username = driver.find_element(By.ID, "username")

print(username.get_attribute("id"))

print(username.get_attribute("placeholder"))

print(username.get_attribute("value"))
```

Output:

```text
username
Enter username
Deepti
```

Common attributes:

```python
element.get_attribute("id")

element.get_attribute("class")

element.get_attribute("value")

element.get_attribute("placeholder")

element.get_attribute("href")

element.get_attribute("type")
```

---

# 6. text vs get_attribute("value")

This is a common interview question.

## text

Returns the visible text of an element.

Example:

```html
<button>Login</button>
```

Python:

```python
button.text
```

Result:

```text
Login
```

---

## get_attribute("value")

Used mainly for input fields.

Example:

```html
<input value="Deepti">
```

Python:

```python
input_field.get_attribute("value")
```

Result:

```text
Deepti
```

For input fields, use:

```python
element.get_attribute("value")
```

to validate entered text.

---

# 7. is_displayed()

The `is_displayed()` method checks whether an element is visible on the page.

Example:

```python
element = driver.find_element(By.ID, "firstName")

assert element.is_displayed()
```

If the element is visible:

```text
True
```

Example:

```python
assert first_name.is_displayed(), "First Name field is not visible"
```

---

# 8. is_enabled()

The `is_enabled()` method checks whether an element is enabled and can be interacted with.

Example:

```python
submit = driver.find_element(By.ID, "submit")

assert submit.is_enabled()
```

Example:

```python
if submit.is_enabled():
    submit.click()
```

---

# 9. is_selected()

The `is_selected()` method is mainly used with:

* Checkboxes
* Radio buttons

Example:

```python
checkbox.click()

assert checkbox.is_selected()
```

---

# 10. Text Fields

Example:

```python
first_name = driver.find_element(By.ID, "firstName")

assert first_name.is_displayed()

assert first_name.is_enabled()

first_name.send_keys("Deepti")

assert first_name.get_attribute("value") == "Deepti"
```

This is a good automation pattern:

1. Find the element.
2. Verify it is displayed.
3. Verify it is enabled.
4. Perform the action.
5. Verify the result.

---

# 11. Dropdowns

There are two main types of dropdowns:

1. Native HTML dropdown
2. Custom dropdown

---

# Native HTML Dropdown

A native dropdown uses:

```html
<select>
```

Example:

```html
<select id="country">
    <option value="IN">India</option>
    <option value="US">USA</option>
</select>
```

Use Selenium's `Select` class:

```python
from selenium.webdriver.support.ui import Select

country = driver.find_element(By.ID, "country")

select = Select(country)
```

---

## select_by_visible_text()

```python
select.select_by_visible_text("India")
```

---

## select_by_value()

```python
select.select_by_value("IN")
```

---

## select_by_index()

```python
select.select_by_index(0)
```

Important:

The `Select` class works only with native:

```html
<select>
```

elements.

---

# Custom Dropdown

Custom dropdowns are usually created using:

```html
<div>
```

or:

```html
<ul>
```

or:

```html
<span>
```

For custom dropdowns, the Selenium `Select` class does not work.

Example approach:

```python
dropdown.click()

option = driver.find_element(
    By.XPATH,
    "//div[text()='India']"
)

option.click()
```

---

# 12. Radio Buttons

Radio buttons allow the user to select one option from a group.

Example:

```python
gender = driver.find_element(
    By.XPATH,
    "//label[text()='Female']"
)

gender.click()
```

Then validate the selection:

```python
assert gender.is_selected()
```

Sometimes the actual input is hidden and the label is visible.

Example:

```html
<input type="radio" id="female">

<label for="female">Female</label>
```

In this case:

```python
driver.find_element(
    By.XPATH,
    "//label[@for='female']"
).click()
```

---

# 13. Checkboxes

Checkboxes allow multiple selections.

Example:

```python
hobby = driver.find_element(
    By.XPATH,
    "//label[text()='Sports']"
)

hobby.click()
```

Then verify:

```python
assert hobby.is_selected()
```

A safer approach is:

```python
if not hobby.is_selected():
    hobby.click()
```

Why?

If the checkbox is already selected and you click it again, it will become unselected.

---

# 14. Submit Button

Before clicking the submit button, verify that it is displayed and enabled.

```python
submit = driver.find_element(By.ID, "submit")

assert submit.is_displayed()

assert submit.is_enabled()

submit.click()
```

After clicking, validate the result.

Example:

```python
confirmation = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "example-modal-sizes-title-lg")
    )
)

assert confirmation.text == "Thanks for submitting the form"
```

---

# 15. Explicit Wait

Instead of using:

```python
time.sleep(5)
```

Use:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

Create a wait:

```python
wait = WebDriverWait(driver, 10)
```

Wait for an element to be visible:

```python
element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "firstName")
    )
)
```

Wait for an element to be clickable:

```python
button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)
```

---

# 16. Complete Interaction Pattern

A good Selenium interaction follows this pattern:

```python
element = driver.find_element(By.ID, "username")

assert element.is_displayed()

assert element.is_enabled()

element.clear()

element.send_keys("Deepti")

assert element.get_attribute("value") == "Deepti"
```

This makes the test more reliable.

---

# 17. Complete Multi-Field Form Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_practice_form():

    driver = webdriver.Chrome()

    try:

        driver.maximize_window()

        driver.get(
            "https://demoqa.com/automation-practice-form"
        )

        wait = WebDriverWait(driver, 10)

        # First Name

        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "firstName")
            )
        )

        assert first_name.is_displayed()

        assert first_name.is_enabled()

        first_name.send_keys("Deepti")

        assert first_name.get_attribute(
            "value"
        ) == "Deepti"


        # Last Name

        last_name = driver.find_element(
            By.ID,
            "lastName"
        )

        last_name.send_keys("Patel")

        assert last_name.get_attribute(
            "value"
        ) == "Patel"


        # Email

        email = driver.find_element(
            By.ID,
            "userEmail"
        )

        email.send_keys(
            "deepti@test.com"
        )

        assert email.get_attribute(
            "value"
        ) == "deepti@test.com"


        # Gender

        gender = driver.find_element(
            By.XPATH,
            "//label[text()='Female']"
        )

        gender.click()


        # Mobile Number

        mobile = driver.find_element(
            By.ID,
            "userNumber"
        )

        mobile.send_keys(
            "9876543210"
        )

        assert mobile.get_attribute(
            "value"
        ) == "9876543210"


        # Hobby Checkbox

        hobby = driver.find_element(
            By.XPATH,
            "//label[text()='Sports']"
        )

        hobby.click()


        # Current Address

        address = driver.find_element(
            By.ID,
            "currentAddress"
        )

        address.send_keys(
            "Hyderabad, India"
        )

        assert address.get_attribute(
            "value"
        ) == "Hyderabad, India"


        # Submit

        submit = driver.find_element(
            By.ID,
            "submit"
        )

        assert submit.is_displayed()

        assert submit.is_enabled()

        submit.click()


        # Confirmation

        confirmation = wait.until(
            EC.visibility_of_element_located(
                (
                    By.ID,
                    "example-modal-sizes-title-lg"
                )
            )
        )

        assert confirmation.text == (
            "Thanks for submitting the form"
        )

    finally:

        driver.quit()
```

---

# 18. Important Selenium Element Methods

| Method / Property | Purpose               |
| ----------------- | --------------------- |
| `click()`         | Clicks an element     |
| `send_keys()`     | Enters text           |
| `clear()`         | Clears input text     |
| `text`            | Gets visible text     |
| `get_attribute()` | Gets HTML attribute   |
| `is_displayed()`  | Checks visibility     |
| `is_enabled()`    | Checks enabled state  |
| `is_selected()`   | Checks selected state |

---

# 19. Best Practice: Validate After Every Important Action

Do not write:

```python
username.send_keys("Deepti")

checkbox.click()

submit.click()
```

without validation.

Better:

```python
username.send_keys("Deepti")

assert username.get_attribute("value") == "Deepti"
```

```python
checkbox.click()

assert checkbox.is_selected()
```

```python
submit.click()

assert confirmation.is_displayed()
```

This prevents silent failures.

---

# 20. Common Exceptions

## ElementNotInteractableException

The element exists but cannot currently be interacted with.

Possible reasons:

* Element is hidden
* Element is disabled
* Element is not ready

Solution:

```python
wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)
```

---

## ElementClickInterceptedException

Another element is blocking the click.

Possible reasons:

* Popup
* Advertisement
* Overlay
* Sticky header

Possible solution:

```python
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    element
)
```

Then:

```python
element.click()
```

---

## NoSuchElementException

Selenium cannot find the element.

Check:

* Locator
* Page URL
* Element availability
* Whether a wait is required

---

# 21. Interview Questions

## Q1. What is the difference between `text` and `get_attribute("value")`?

### Answer

`text` retrieves the visible text of an element, while `get_attribute("value")` retrieves the value attribute of an HTML element.

For input fields, entered text is usually validated using:

```python
element.get_attribute("value")
```

---

## Q2. How do you handle a dropdown in Selenium?

### Answer

For a native HTML `<select>` element, I use Selenium's `Select` class:

```python
select.select_by_visible_text("India")
```

Other options are:

```python
select.select_by_value("IN")
```

and:

```python
select.select_by_index(0)
```

For custom dropdowns, I click the dropdown and then locate and click the required option manually.

---

## Q3. Can the Select class be used for every dropdown?

### Answer

No. The `Select` class works only with native HTML `<select>` elements. For custom dropdowns implemented using `div`, `li`, or other elements, I use normal Selenium locators and click the required option.

---

## Q4. How do you handle a checkbox that may already be selected?

```python
if not checkbox.is_selected():
    checkbox.click()
```

This avoids accidentally unselecting it.

---

## Q5. How do you validate an action?

### Answer

I validate the resulting state after important actions. For example:

* After entering text, I validate the `value` attribute.
* After selecting a checkbox, I validate `is_selected()`.
* Before clicking a button, I validate `is_displayed()` and `is_enabled()`.
* After submitting a form, I validate the confirmation message or URL.

---

# Key Takeaway

The best automation tests do not just perform actions.

They follow:

```text
Locate
   ↓
Verify State
   ↓
Perform Action
   ↓
Verify Result
```

Example:

```text
Find Username Field
        ↓
Verify Visible and Enabled
        ↓
Enter Username
        ↓
Verify Entered Value
```

This is the foundation of reliable Selenium automation.
