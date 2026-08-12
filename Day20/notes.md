# Day 20 - Advanced Selenium Interactions

## Topics

1. Shadow DOM
2. File Upload
3. Screenshots
4. Cookies

---

# 1. Shadow DOM

Shadow DOM is a web platform feature used to encapsulate
HTML, CSS and JavaScript inside a web component.

Example:

Host
    |
    +-- Shadow Root
          |
          +-- Button

Normal Selenium locators may not directly access elements
inside the shadow root.

## Selenium approach

```python
host = driver.find_element(
    By.CSS_SELECTOR,
    "my-component"
)

shadow_root = host.shadow_root

button = shadow_root.find_element(
    By.CSS_SELECTOR,
    "button"
)

button.click()