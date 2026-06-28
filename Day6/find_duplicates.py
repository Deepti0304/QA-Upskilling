# numbers=[1,2,3,2,4,5,1]

# seen=set()

# duplicates=set()

# for num in numbers:

#     if num in seen:
#         duplicates.add(num)

#     else:
#         seen.add(num)

# print(duplicates)

def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates