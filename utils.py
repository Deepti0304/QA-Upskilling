def is_even(number):
    return number % 2 == 0


def max_of_three(a, b, c):
    return max(a, b, c)


def reverse_string(text):
    return text[::-1]


def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def age_in_days(age):
    return age * 365


def calculate_tip(bill, tip_percent, people):
    tip = bill * tip_percent / 100
    total = bill + tip
    return total / people

def is_palindrome(word):
    return word == word[::-1]