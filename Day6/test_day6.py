from sum_array import sum_array
from find_duplicates import find_duplicates
from group_words import group_words_by_length
from sort_dictionary import sort_dictionary_by_value
from two_sum import two_sum

print("Sum of Array")
print(sum_array([10, 20, 30, 40]))

print("\nFind Duplicates")
print(find_duplicates([1, 2, 3, 2, 4, 1]))

print("\nGroup Words")
print(group_words_by_length(["cat", "apple", "dog", "banana"]))

print("\nSort Dictionary")
scores = {
    "John": 80,
    "David": 95,
    "Alice": 75
}
print(sort_dictionary_by_value(scores))

print("\nTwo Sum")
print(two_sum([2, 7, 11, 15], 9))