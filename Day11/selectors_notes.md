# Day 11 - CSS Selector Notes

## ID Selector

#username

Example:
<input id="username">

--------------------------------

## Class Selector

.form-control

Example:
<input class="form-control">

--------------------------------

## Tag Selector

button

--------------------------------

## Descendant Selector

form input

Targets:
Any input inside form

--------------------------------

## Child Selector

form > input

Targets:
Direct child only

--------------------------------

## Attribute Selector

input[type='email']

--------------------------------

## Multiple Classes

.btn.primary

--------------------------------

## Contains

input[id*='user']

--------------------------------

## Starts With

input[id^='user']

--------------------------------

## Ends With

input[id$='123']

--------------------------------

## DevTools Commands

$("button")

Returns first button

$$("button")

Returns all buttons