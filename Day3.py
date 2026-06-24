#Conditionals & Loops
#Nested If Statements
#Syntax:
# if condition1:
#     if condition2:
#         #code to execute if both conditions are true          
#           else:
#             #code to execute if condition1 is true and condition2 is false    
#  else:    
#     #code to execute if condition1 is false

# age = 20

# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")

#Looping Statements- to execute a block of code repeatedly until a certain condition is met
#2 types of loops in Python:
#1. For Loop - used to iterate over a sequence (list, tuple, string)    
#2. While Loop - used to execute a block of code repeatedly as long as a condition is true  
#Syntax of For Loop:
# for variable in sequence:
#     #code to execute for each item in the sequence    
#for variable in range(start, stop, step):  
for i in range (5):
    print(i)    
#o/p- 0
#1
#2
#3
#4  

for i in range (1, 5):
    print(i)        
#O/p - 1
#2
#3
#4     

for i in range (1, 10, 2):
    print(i)    
#o/p- 1
#3
#5
#7 
#9

for i in range (10, 1, -2):
    print(i)    
#o/p- 10
#8
#6 
#4
#2  

#while Loop
#Syntax:
# while condition:
#     #code to execute as long as the condition is true 
# 
# intilalization
# while (condition)
#  block if statement 
#  increment/decrement
#

#example
# i = 0
# while (i<6):  
#     print(i)     
#     i+=1
# #o/p - 0,1,2,3,4,5

#Jump Satement -> Break/Continue/Exit
#Break-> it will terminate the particular statement 
#Continue->Skip the Particular and execute the remianing loop
#Exit->It will terminate the entire main program
# for i in range(10):
#     if (i == 5):
#         break
#     print(i)
# print("Outside of the loop")

# i = 1
# while(i<6):
#     print(i)
#     if i == 3:
#         break
#     i+=1
# print("outside while loop")

# #Continue
# i = 1
# while (i <6):
#     print(i)
#     i+=1
#     if i==3:
#         continue #Not applicable for while loop

# for i in range (10):
#     if i == 5:
#         continue
#     print(i)
# print("Deepti")

# #Exit
# for i in range (10):
#     if i == 5:
#         exit(0)
#     print(i)
# print("Deepti")

# a = 1
# while a<10:
#     if a == 5:
#         exit(0)
#     print(a)
#     a+=1
# print("Deepti")

##################
# Problem 1: FizzBuzz

# If divisible by:

# 3 → Fizz
# 5 → Buzz
# Both → FizzBuzz

for num in range(1, 101):

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)

# Problem 2: Prime Checker
num = 13

is_prime = True

for i in range(2, num):

    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")

else:
    print("Not Prime")
# Better way
num = 13

for i in range(2, int(num**0.5)+1):

    if num % i == 0:
        print("Not Prime")
        break

else:
    print("Prime")
# Problem 3: Factorial
# Using for loop
num = 5

fact = 1

for i in range(1, num+1):
    fact *= i

print(fact)

# Output:

# 120
# Using while loop
num = 5

fact = 1

while num > 0:
    fact *= num
    num -= 1

print(fact)

# Problem 4: Palindrome
word = "madam"

if word == word[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")
# Another Method
word = "madam"

reverse = ""

for char in word:
    reverse = char + reverse

if word == reverse:
    print("Palindrome")

# Problem 5: Multiplication Table
num = 7

for i in range(1,11):

    print(f"{num} x {i} = {num*i}")

# Output:

# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70