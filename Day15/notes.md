# Day 15 Notes

## Synchronization

Synchronization means waiting until the application is ready before interacting with elements.

---

## Implicit Wait

driver.implicitly_wait(10)

Applies globally to all element lookups.

---

## Explicit Wait

wait = WebDriverWait(driver, 10)

Recommended for specific elements.

---

## Fluent Wait

Allows customization of timeout, polling interval, and ignored exceptions.

---

## Expected Conditions

visibility_of_element_located()

element_to_be_clickable()

presence_of_element_located()

title_contains()

url_contains()

alert_is_present()

---

## Best Practices

Avoid time.sleep()

Use Explicit Waits whenever possible.

Do not mix Implicit and Explicit Waits.

Wait for meaningful conditions like visibility or clickability instead of arbitrary delays.