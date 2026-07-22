# Day 16 - Web Element Interaction Cheatsheet

## 1. Basic Selenium Setup

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")
```

---

# 2. Locate an Element

```python
element = driver.find_element(
    By.ID,
    "element_id"
)
```

Common locator strategies:

```python
By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.CSS_SELECTOR
By.XPATH
```

---

# 3. Click

```python
element.click()
```

Example:

```python
login_button.click()
```

Use for:

* Buttons
* Links
* Checkboxes
* Radio buttons

---

# 4. Enter Text

```python
element.send_keys("text")
```

Example:

```python
username.send_keys("Deepti")
```

---

# 5. Clear Text

```python
element.clear()
```

Example:

```python
username.clear()
username.send_keys("New Value")
```

---

# 6. Get Visible Text

```python
element.text
```

Example:

```python
message = driver.find_element(
    By.ID,
    "message"
)

print(message.text)
```

Important:

```python
element.text
```

Correct.

```python
element.text()
```

Incorrect.

---

# 7. Get HTML Attribute

```python
element.get_attribute("attribute_name")
```

Examples:

```python
element.get_attribute("value")

element.get_attribute("placeholder")

element.get_attribute("href")

element.get_attribute("class")

element.get_attribute("id")
```

For input validation:

```python
assert username.get_attribute(
    "value"
) == "Deepti"
```

---

# 8. Element State Methods

## is_displayed()

```python
assert element.is_displayed()
```

Checks whether the element is visible.

---

## is_enabled()

```python
assert element.is_enabled()
```

Checks whether the element is enabled.

---

## is_selected()

```python
assert checkbox.is_selected()
```

Used mainly for:

* Checkboxes
* Radio buttons

---

# 9. Text Field Interaction

```python
field = driver.find_element(
    By.ID,
    "firstName"
)

assert field.is_displayed()

assert field.is_enabled()

field.send_keys("Deepti")

assert field.get_attribute(
    "value"
) == "Deepti"
```

Best pattern:

```text
Locate
  ↓
Verify State
  ↓
Perform Action
  ↓
Verify Result
```

---

# 10. Native Dropdown

For:

```html
<select>
```

Use:

```python
from selenium.webdriver.support.ui import Select
```

Example:

```python
dropdown = Select(
    driver.find_element(
        By.ID,
        "country"
    )
)
```

## Select by visible text

```python
dropdown.select_by_visible_text(
    "India"
)
```

## Select by value

```python
dropdown.select_by_value(
    "IN"
)
```

## Select by index

```python
dropdown.select_by_index(0)
```

Important:

```text
Select class works only with HTML <select> elements.
```

---

# 11. Custom Dropdown

For dropdowns made with:

```html
<div>
<ul>
<li>
<span>
```

Do not use `Select`.

Example:

```python
dropdown.click()

option = driver.find_element(
    By.XPATH,
    "//div[text()='India']"
)

option.click()
```

---

# 12. Radio Button

```python
gender = driver.find_element(
    By.XPATH,
    "//label[text()='Female']"
)

gender.click()
```

For the actual input:

```python
radio = driver.find_element(
    By.ID,
    "female"
)

if not radio.is_selected():
    radio.click()

assert radio.is_selected()
```

---

# 13. Checkbox

```python
checkbox = driver.find_element(
    By.ID,
    "hobbies-checkbox-1"
)

if not checkbox.is_selected():
    checkbox.click()

assert checkbox.is_selected()
```

This prevents accidentally unchecking an already selected checkbox.

---

# 14. Submit Button

```python
submit = driver.find_element(
    By.ID,
    "submit"
)

assert submit.is_displayed()

assert submit.is_enabled()

submit.click()
```

After clicking:

```python
assert confirmation.is_displayed()
```

---

# 15. Explicit Wait

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

Create wait:

```python
wait = WebDriverWait(
    driver,
    10
)
```

---

## Wait for Visibility

```python
element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "firstName")
    )
)
```

---

## Wait for Clickability

```python
button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)
```

---

## Wait for Presence

```python
element = wait.until(
    EC.presence_of_element_located(
        (By.ID, "element")
    )
)
```

---

# 16. Common Expected Conditions

```python
EC.visibility_of_element_located()

EC.element_to_be_clickable()

EC.presence_of_element_located()

EC.invisibility_of_element_located()

EC.text_to_be_present_in_element()

EC.url_contains()

EC.title_contains()

EC.alert_is_present()
```

---

# 17. Common Exceptions

## NoSuchElementException

Element cannot be found.

Check:

```text
- Locator
- Page URL
- Frame
- Timing
```

---

## ElementNotInteractableException

Element exists but cannot be interacted with.

Use:

```python
wait.until(
    EC.element_to_be_clickable(
        locator
    )
)
```

---

## ElementClickInterceptedException

Another element is covering the target element.

Try:

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

If necessary:

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

Use JavaScript click as a workaround, not the first choice.

---

## StaleElementReferenceException

The DOM changed and the previously located element is no longer valid.

Solution:

```python
element = driver.find_element(
    By.ID,
    "element"
)
```

Locate the element again.

---

# 18. Scroll Element Into View

```python
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    element
)
```

Useful when:

* Element is below the visible screen
* Sticky headers cover the element
* Advertisements overlap the element

---

# 19. JavaScript Click

Normal approach:

```python
element.click()
```

Fallback:

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

Use only when normal Selenium click is blocked by the page layout.

---

# 20. Input Validation

For input fields:

```python
element.send_keys("Deepti")

assert element.get_attribute(
    "value"
) == "Deepti"
```

Do not use:

```python
assert element.text == "Deepti"
```

for most input fields.

---

# 21. Complete Interaction Pattern

```python
element = wait.until(
    EC.visibility_of_element_located(
        locator
    )
)

assert element.is_displayed()

assert element.is_enabled()

element.send_keys("Test Data")

assert element.get_attribute(
    "value"
) == "Test Data"
```

---

# 22. Interaction Quick Reference

| Action           | Selenium Code                     |
| ---------------- | --------------------------------- |
| Click            | `element.click()`                 |
| Enter text       | `element.send_keys("text")`       |
| Clear text       | `element.clear()`                 |
| Get visible text | `element.text`                    |
| Get attribute    | `element.get_attribute("value")`  |
| Check visible    | `element.is_displayed()`          |
| Check enabled    | `element.is_enabled()`            |
| Check selected   | `element.is_selected()`           |
| Native dropdown  | `Select(element)`                 |
| Scroll           | `execute_script()`                |
| Wait for visible | `visibility_of_element_located()` |
| Wait for click   | `element_to_be_clickable()`       |

---

# 23. Interview Formula

When asked how you interact with a web element:

```text
Find the element
       ↓
Wait for required state
       ↓
Verify element state
       ↓
Perform action
       ↓
Verify resulting state
```

Example:

```python
button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "submit")
    )
)

assert button.is_enabled()

button.click()

assert confirmation.is_displayed()
```

---

# Key Rule

## Do not perform actions silently.

Bad:

```python
checkbox.click()
```

Better:

```python
assert checkbox.is_displayed()

assert checkbox.is_enabled()

checkbox.click()

assert checkbox.is_selected()
```

Reliable automation means:

```text
Action + Validation = Stable Test
```
