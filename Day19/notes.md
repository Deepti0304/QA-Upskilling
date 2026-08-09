# Day 19 - Advanced Actions

## 1. ActionChains

## 2. Mouse Actions

### click()
### double_click()
### context_click()
### move_to_element()
### click_and_hold()
### release()

## 3. Keyboard Actions

### key_down()
### key_up()
### send_keys()

## 4. Drag and Drop

## 5. JavaScript Executor

### execute_script()

## 6. Scrolling

## 7. Working with Hidden Elements

## 8. Reading Attributes Using JavaScript

## 9. When to Use JavaScript

## 10. Common Selenium Exceptions

## 11. Interview Questions and Answers

## 12. Best Practices

| Action       | Selenium Python                                          |
| ------------ | -------------------------------------------------------- |
| Click        | `element.click()`                                        |
| Double click | `actions.double_click(element).perform()`                |
| Right click  | `actions.context_click(element).perform()`               |
| Hover        | `actions.move_to_element(element).perform()`             |
| Click & hold | `actions.click_and_hold(element)`                        |
| Release      | `actions.release(element)`                               |
| Drag/drop    | `actions.drag_and_drop(source, target).perform()`        |
| Key down     | `actions.key_down(Keys.CONTROL)`                         |
| Key up       | `actions.key_up(Keys.CONTROL)`                           |
| Scroll       | `driver.execute_script()`                                |
| JS click     | `driver.execute_script("arguments[0].click()", element)` |


