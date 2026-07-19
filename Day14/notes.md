# Day 14 – Advanced Locators

## Objective

Learn advanced CSS Selectors and XPath techniques for locating web elements.

---

## CSS Selectors

### ID

#username

### Class

.login-btn

### Tag

input

### Attribute

input[type='text']

### Descendant

div input

### Child

div > input

### Adjacent Sibling

label + input

### General Sibling

label ~ input

### nth-child()

li:nth-child(3)

### not()

button:not(.disabled)

---

## XPath

### Relative XPath

//input

### By Attribute

//input[@id='username']

### contains()

//button[contains(@id,'login')]

### starts-with()

//button[starts-with(@id,'btn')]

### text()

//button[text()='Login']

### normalize-space()

//button[normalize-space()='Login']

---

## XPath Axes

Parent

//input/parent::div

Following Sibling

//label/following-sibling::input

Preceding Sibling

//input/preceding-sibling::label

Ancestor

//input/ancestor::form

Descendant

//form/descendant::button

---

## CSS vs XPath

CSS
- Faster
- Cleaner
- Preferred when possible

XPath
- More powerful
- Supports parent traversal
- Better for complex relationships

---

## Best Practices

✔ Prefer ID when available.

✔ Prefer CSS Selector over XPath for simple elements.

✔ Use XPath when parent/sibling relationships are needed.

✔ Avoid absolute XPath.

✔ Avoid index-based XPath whenever possible.

✔ Prefer meaningful attributes over positional indexes.