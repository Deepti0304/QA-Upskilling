# # two_sum.py

# def two_sum(numbers, target):
#     lookup = {}

#     for index, number in enumerate(numbers):

#         difference = target - number

#         if difference in lookup:
#             return [lookup[difference], index]

#         lookup[number] = index

#     return []


# numbers = [2, 7, 11, 15]
# target = 9

# result = two_sum(numbers, target)

# print("Numbers :", numbers)
# print("Target  :", target)
# print("Indices :", result)

def two_sum(numbers, target):
    lookup = {}

    for index, number in enumerate(numbers):

        difference = target - number

        if difference in lookup:
            return [lookup[difference], index]

        lookup[number] = index

    return []