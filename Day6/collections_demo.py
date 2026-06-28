# collections_demo.py

print("===== LIST =====")

fruits = ["Apple", "Banana", "Orange"]

print(f"Original List: {fruits}")

fruits.append("Mango")
print(f"After append: {fruits}")

fruits.remove("Banana")
print(f"After remove: {fruits}")

print(f"Contains Apple? {'Apple' in fruits}")

fruits.sort()
print(f"Sorted List: {fruits}")


print("\n===== TUPLE =====")

colors = ("Red", "Green", "Blue")

print(colors)
print(colors[1])


print("\n===== SET =====")

numbers = {10, 20, 20, 30, 40}

print(numbers)

numbers.add(50)

print(numbers)

print(20 in numbers)


print("\n===== DICTIONARY =====")

employee = {
    "name": "Deepu",
    "age": 32,
    "role": "QA Engineer"
}

print(employee)

employee["city"] = "Hyderabad"

print(employee)

for key, value in employee.items():
    print(f"{key} : {value}")