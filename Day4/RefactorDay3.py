# Prime Checker
def isPrime(num):
    if num <=1:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(isPrime(5))

#Factorial
def factorial(num1):
    fact = 1
    for i in range(1, num1+1):
        fact = fact*i
    return fact
c = factorial(5)
print("c")

#Palindrome
def pallindrome(word):
    return word == word[::-1]

print(pallindrome("madam"))

def pallindrome1(word):
    if word == word[::-1]:
        print ("It is Pallindrome")
    else:
        print ("Not an pallindrome")
print(pallindrome1("madam"))

