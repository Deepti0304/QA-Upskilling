#Day 2: Variables, Data Types & Operators
import string
from xmlrpc.client import boolean


a = 10
print(a)
print(type(a))

b= 10.45
print(b)
print(type(b))

c= True
print(c)
print(type(c))  

d = 10+4j
print(d)
print(type(d))

e = 'Hello'
print(e)
print(type(e))

f = "Hello Deepti" 
print(f)
print(type(f))

g = '''Hello Deepti
How are you?'''
print(g)
print(type(g))

h = -28
print(h)    
print(type(h))

i = -12.24
print(i)
print(type(i))

j = False
print(j)
print(type(j))

k = -10+9j
print(k)
print(type(k))

l = '@!'
print(l)
print(type(l))

#Type Casting/Type Conversion -> Converting one data type to another data type
#Any other data type into int data type
print(int(100))
print(type(int(100)))
print(type(int(10.45))) #converting float to int, it will remove the decimal part and give only the whole number
print(type(int(-28))) #converting negative int to int, it will give the same negative int as output
print(type(int(-12.24))) #converting negative float to int, it will remove the decimal part and give only the whole number, it will also give negative int as output
print(type(int(True))) #converting boolean to int, it will give 1 as output
print(type(int(False))) #converting boolean to int, it will give 0 as output
#print(type(int(-10+9j))) #converting complex to int, it will give error as complex numbers cannot be converted to int
#print(type(int('@!'))) #converting string to int, it will give error as string cannot be converted to int           

#Summary:
# float -> int - it will remove the decimal part and give only the whole number
# negative int -> int - it will give the same negative int as output
# negative float -> int - it will remove the decimal part and give only the whole number, it will also give negative int as output
# boolean -> int - it will give 1 for True and 0 for False
# complex -> int - it will give error as complex numbers cannot be converted to int
# string -> int - it will give error as string cannot be converted to int

#float() - converting any other data type into float data type
print(type(float(100))) #converting int to float, it will give 100.0 as output
print(type(float(10.45))) #converting float to float, it will give the same float as output
print(type(float(-28))) #converting negative int to float, it will give -28.0 as output
print(type(float(-12.24))) #converting negative float to float, it will give the same negative float as output
print(type(float(True))) #converting boolean to float, it will give 1.0 as output
print(type(float(False))) #converting boolean to float, it will give 0.0 as output
#print(type(float(-10+9j))) #converting complex to float, it will give error as complex numbers cannot be converted to float - Type Error 
#print(type(float('@!'))) #converting string to float, it will give error as string cannot be converted to float - Value Error

#Complex() - converting any other data type into complex data type
print(type(complex(100))) #converting int to complex, it will give 100+0j as output
print(type(complex(10.45))) #converting float to complex, it will give 10.45+0j as output
print(type(complex(-28))) #converting negative int to complex, it will give -28+0j as output
print(type(complex(-12.24))) #converting negative float to complex, it will give -12.24+0j as output
print(type(complex(True))) #converting boolean to complex, it will give 1+0j as output
print(type(complex(False))) #converting boolean to complex, it will give 0+0j as output
print(type(complex(-10+9j))) #converting complex to complex, it will give the same complex number as output
#print(type(complex('@!'))) #converting string to complex, it will give error as string cannot be converted to complex - Value Error

#bool() - converting any other data type into boolean data type
print(type(bool(100))) #converting int to boolean, it will give True as output
print(type(bool(0))) #converting int to boolean, it will give False as output
print(type(bool(10.45))) #converting float to boolean, it will give True as output
print(type(bool(0.0))) #converting float to boolean, it will give False as output
print(type(bool(-28))) #converting negative int to boolean, it will give True as output
print(type(bool(-12.24))) #converting negative float to boolean, it will give True as output
print(type(bool(True))) #converting boolean to boolean, it will give the same boolean as output
print(type(bool(False))) #converting boolean to boolean, it will give the same boolean as output
print(type(bool(-10+9j))) #converting complex to boolean, it will give True as output as complex numbers are considered as True
print(type(bool(0+0j))) #converting complex to boolean, it will give False as output as 0+0j is considered as False
print(type(bool('@!'))) #converting string to boolean, it will give True as output as non-empty strings are considered as True
print(type(bool(''))) #converting string to boolean, it will give False as output as empty strings are considered as False

#String() - converting any other data type into string data type
print(type(str(100))) #converting int to string, it will give '100'
print(type(str(10.45))) #converting float to string, it will give '10.45'
print(type(str(-28))) #converting negative int to string, it will give '-28'
print(type(str(-12.24))) #converting negative float to string, it will give '-12.24'
print(type(str(True))) #converting boolean to string, it will give 'True'
print(type(str(False))) #converting boolean to string, it will give 'False'
print(type(str(-10+9j))) #converting complex to string, it will give '-10+9j'
print(type(str('@!'))) #converting string to string, it will give the same string as output 

#String()-> Its a collection of characters enclosed in single quotes, double quotes or triple quotes. 
# It is used to store text data. 
# It is immutable, which means once a string is created, it cannot be changed. 
# We can perform various operations on strings like concatenation, slicing, indexing, etc.
#Python Supports both positive and negative indexing.
#postive indexting-> Left to Right -> 0,1,2,3,4,5,6,7,8,9
#negative indexing-> Right to Left -> -1,-2,-3,-4,-5,-6,-7,-8,-9,-10

#String Operators
#1.Slice Operator -> It is used to extract a part of the string. It is denoted by [start:end:step]
a = "Welcome"
print(a)
print(type(a))
print(a[1:]) #it will give the string from index 1 to the end of the string
print(a[:5]) #it will give the string from the beginning of the string to index 4
print(a[1:5]) #it will give the string from index 1 to index 4
print(a[::2]) #it will give the string from the beginning of the string to the end of the string with a step of 2, it will give every alternate character of the string
print(a[1::2]) #it will give the string from index 1 to the end of the string with a step of 2, it will give every alternate character of the string starting from index 1
print(a[::-1]) #it will give the string from the end of the string to the beginning of the string with a step of -1, it will give the reverse of the string
print(a[-1]) #it will give the last character of the string
print(a[-2]) #it will give the second last character of the string
print(a[-1:-5:-1]) #it will give the string from the last character to the fifth last character with a step of -1, it will give the reverse of the string   
print(a[:]) #it will give the whole string as output as it is slicing the string from the beginning to the end of the string with a step of 1   

print(len(a)) #it will give the length of the string, it will count the number of characters in the string including spaces and special characters
print(a.upper()) #it will convert the string to uppercase
print(a.lower()) #it will convert the string to lowercase
print(a.islower()) #it will check if the string is in lowercase, it will return True if the string is in lowercase and False if the string is not in lowercase
print(a.isupper()) #it will check if the string is in uppercase, it will return True if the string is in uppercase and False if the string is not in uppercase
print(a.count('e')) #it will count the number of occurrences of the character 'e' in the string
print(a.find('e')) #it will return the index of the first occurrence of the character 'e' in the string, it will return -1 if the character is not found in the string
print(a.find('z')) #it will return -1 as the character 'z' is not found in the string
print(a.rfind('e')) #it will return the index of the last occurrence of the character 'e' in the string, it will return -1 if the character is not found in the string
print(a.index('e')) #it will return the index of the first occurrence of the character 'e' in the string, it will give error if the character is not found in the string    
print(a.rindex('e')) #it will return the index of the last occurrence of the character 'e' in the string, it will give error if the character is not found in the string
print(a.startswith('W')) #it will check if the string starts with the character 'W', it will return True if the string starts with 'W' and False if the string does not start with 'W'
print(a.endswith('e')) #it will check if the string ends with the character 'e', it will return True if the string ends with 'e' and False if the string does not end with 'e'
print(a.isalnum()) #it will check if the string is alphanumeric, it will return True if the string is alphanumeric and False if the string is not alphanumeric, it will return False if the string contains spaces or special characters
print(a.isalpha()) #it will check if the string is alphabetic, it will return True if the string is alphabetic and False if the string is not alphabetic, it will return False if the string contains spaces or special characters
print(a.isdigit()) #it will check if the string is numeric, it will return True if the string is numeric and False if the string is not numeric, it will return False if the string contains spaces or special characters
print(a.isdecimal()) #it will check if the string is decimal, it will return True if the string is decimal and False if the string is not decimal, it will return False if the string contains spaces or special characters
print(a.isnumeric()) #it will check if the string is numeric, it will return True if the string is numeric and False if the string is not numeric, it will return False if the string contains spaces or special characters
print(a.capitalize()) #it will convert the first character of the string to uppercase and the rest of the characters to lowercase
print(a.title()) #it will convert the first character of each word in the string to uppercase and the rest of the characters to lowercase
print(a.swapcase()) #it will convert the uppercase characters in the string to lowercase and the lowercase characters in the string to uppercase
print(a.strip()) #it will remove the leading and trailing spaces from the string
print(a.lstrip()) #it will remove the leading spaces from the string
print(a.rstrip()) #it will remove the trailing spaces from the string
print(a.replace('e','a')) #it will replace all the occurrences of the character 'e' with the character 'a' in the string

#LIST -> It is a collection of items which are ordered and changeable. 
# It is denoted by square brackets [].
# It can contain duplicate items.
# It can contain items of different data types.
# It is mutable, which means we can change the items in the list after it is created.
# We can perform various operations on lists like indexing, slicing, concatenation, etc.

x = [1,2,3,4,5]
print(x)
print(type(x))  

print(x[1:5]) #it will give the list from index 1 to index 4
print(x[::2]) #it will give the list from the beginning of the list to

print(len(x)) #it will give the length of the list, it will count the number of items in the list
print(x.append(6)) #it will add the item 6 to the end of the list
print(x)
print(x.insert(0,0)) #it will add the item 0 at index 0 in the list
print(x)
print(x.remove(3)) #it will remove the first occurrence of the item 3 from the list
print(x)
print(x.pop()) #it will remove the last item from the list and return it
print(x)
print(x.pop(0)) #it will remove the item at index 0 from the list and return it
print(x)
print(x.count(2)) #it will count the number of occurrences of the item 2 in the list
print(x.index(4)) #it will return the index of the first occurrence of the item 4 in the list, it will give error if the item is not found in the list
print(x.reverse()) #it will reverse the order of the items in the list
print(x)
print(x.sort()) #it will sort the items in the list in ascending order
print(x)
print(x.sort(reverse=True)) #it will sort the items in the list in descending order
print(x)    

y = x.copy() #it will create a copy of the list x and assign it to the variable y
print(y)
print(y.clear()) #it will remove all the items from the list y
print(y)
print(x.__delitem__(0)) #it will remove the item at index 0 from the list x
print(x)
print(x.extend([7,8,9])) #it will add the items 7,8,9 to the end of the list x
print(x)
print(x.insert(0,-1)) #it will add the item -1 at index 0 in the list x
print(x)
print(x.insert(5,0)) #it will add the item 0 at index 5 in the list x
print(x)
for i in x:
    print(i) #it will print each item in the list x on a new line   

for i in enumerate(x):
    print(i) #it will print the index and the item in the list x as a tuple on a new line


#SET -> It is a collection of items which are unordered and unindexed.
# It is denoted by curly braces {}.
# It can contain duplicate items, but it will remove the duplicate items and keep only one occurrence of each item.
# It can contain items of different data types.
# It is mutable, which means we can change the items in the set after it is created.
# We can perform various operations on sets like union, intersection, difference, etc.

z = {1,2,3,4,5}
print(z)
print(type(z))  

#Methods and Functions of Set
print(len(z)) #it will give the length of the set, it will count the number of items in the set
print(z.add(6)) #it will add the item 6 to the set z
print(z)
print(z.remove(3)) #it will remove the item 3 from the set z, it will give error if the item is not found in the set
print(z)
print(z.discard(4)) #it will remove the item 4 from the set z, it will not give error if the item is not found in the set
print(z)
print(z.pop()) #it will remove and return an arbitrary item from the set z, it will give error if the set is empty
print(z)
print(z.clear()) #it will remove all the items from the set z
print(z)
print(z.update({7,8,9})) #it will add the items 7,8,9 to the set z
print(z)
print(z.union({10,11,12})) #it will return a new set which is the union of the set z and the set {10,11,12}
print(z)
print(z.intersection({7,8,9})) #it will return a new set which is the intersection of the set z and the set {7,8,9}
print(z)
print(z.difference({7,8,9})) #it will return a new set which is the difference of the set z and the set {7,8,9}
print(z)
print(z.symmetric_difference({7,8,9})) #it will return a new set which is the symmetric difference of the set z and the set {7,8,9}
print(z)
print(z.sorted()) #it will return a new list which is the sorted version of the set z
print(z)
print(z.sorted(reverse=True)) #it will return a new list which is the sorted version of the set z in descending order
print(z)
u= z.copy() #it will create a copy of the set z and assign it to the variable u
print(u)    

#Tuples -> It is a collection of items which are ordered and unchangeable.
# It is denoted by parentheses ().
# It can contain duplicate items.
#It can print duplicate values as well 
# It can contain items of different data types.
# It is immutable, which means we cannot change the items in the tuple after it is created.
# We can perform various operations on tuples like indexing, slicing, concatenation, etc.   

m = (1,2,3,4,5)
print(m)
print(type(m))  

#Methods and Functions of Tuple
print(len(m)) #it will give the length of the tuple, it will count the number of items in the tuple
print(m.count(2)) #it will count the number of occurrences of the item 2 in the tuple
print(m.index(4)) #it will return the index of the first occurrence of the item 4 in the tuple, it will give error if the item is not found in the tuple
print(m.index(2,1)) #it will return the index of the first occurrence of the item 2 in the tuple starting from index 1, it will give error if the item is not found in the tuple
print(m)
print(m[1:5]) #it will give the tuple from index 1 to index 4
print(m[::2]) #it will give the tuple from the beginning of the tuple to the end of the tuple with a step of 2, it will give every alternate item of the tuple
print(m[::-1]) #it will give the tuple from the end of the tuple to the beginning of the tuple with a step of -1, it will give the reverse of the tuple
print(m[-1]) #it will give the last item of the tuple
print(m[-2]) #it will give the second last item of the tuple
print(m[-1:-5:-1]) #it will give the tuple from the last item to the fifth last item with a step of -1, it will give the reverse of the tuple
print(m[:]) #it will give the whole tuple as output as it is slicing the tuple
print(max(m)) #it will give the maximum item in the tuple
print(min(m)) #it will give the minimum item in the tuple

#Dictionary -> It is a collection of items which are unordered, changeable and indexed.
# It is denoted by curly braces {}.
# It is a collection of key-value pairs, where each key is unique and is used to access the corresponding value.
# It can contain items of different data types.
#Keys doesnt allow duplicate values but values can be duplicate in a dictionary.
# It is mutable, which means we can change the items in the dictionary after it is created.
# We can perform various operations on dictionaries like indexing, slicing, concatenation, etc.     

dict = {'name':'Deepti', 'age':25, 'city':'Pune'}
print(dict)
print(type(dict))

#Methods and Functions of Dictionary
print(len(dict)) #it will give the length of the dictionary, it will count the number of key-value pairs in the dictionary
print(dict.keys()) #it will return a view object which contains the keys of the dictionary
print(dict.values()) #it will return a view object which contains the values of the dictionary
print(dict.items()) #it will return a view object which contains the key-value pairs of the dictionary as tuples
print(dict.get('name')) #it will return the value corresponding to the key 'name' in the dictionary, it will return None if the key is not found in the dictionary
print(dict.get('gender')) #it will return None as the key 'gender' is not found in the dictionary
print(dict['name']) #it will return the value corresponding to the key 'name' in the dictionary, it will give error if the key is not found in the dictionary
print(dict['gender']) #it will give error as the key 'gender' is not found in the dictionary
print(dict.update({'age':26})) #it will update the value corresponding to the key 'age' in the dictionary to 26
print(dict)
print(dict.update({'gender':'Female'})) #it will add the key-value pair 'gender':'Female' to the dictionary
print(dict)
print(dict.pop('city')) #it will remove the key-value pair with the key 'city' from the dictionary and return the value corresponding to the key 'city', it will give error if the key is not found in the dictionary
print(dict.popitem()) #it will remove and return an arbitrary key-value pair from the dictionary, it will give error if the dictionary is empty
print(dict.clear()) #it will remove all the key-value pairs from the dictionary


#Programs to Practice- 
#1.BMI calculator - BMI = weight / (height²)

weight  = 85.23
height = 4.3
bmi = weight / (height**2)
print("Your weight is: ", weight)
print("Your height is: ", height)
print("Your BMI is: ", bmi)

#2.Temperature Converter - Celsius to Fahrenheit -> F = (C * 9/5) + 32
celsius = 37.5
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Celsius: ", celsius)
print("Temperature in Fahrenheit: ", fahrenheit)

#3.Simple Interest Calculator - SI = (P * R * T) / 100
principal = 10000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Principal Amount: ", principal)
print("Rate of Interest: ", rate)
print("Time Period: ", time)
print("Simple Interest: ", simple_interest) 

#4.Age in Days Calculator - Age in Days = Age in Years * 365
age = 35
age_in_days = age * 365
print("Age in Years: ", age)
print("Age in Days: ", age_in_days)     

#5. Tip Splitter - Tip per Person = (Total Bill * Tip Percentage) / Number of People
total_bill = 2000
tip_percentage = 10
number_of_people = 4
tip_per_person = (total_bill * tip_percentage) / number_of_people
print("Total Bill: ", total_bill)
print("Tip Percentage: ", tip_percentage)
print("Number of People: ", number_of_people)
print("Tip per Person: ", tip_per_person)       


