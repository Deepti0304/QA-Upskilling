def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


def capitalize_words(sentence):
    return sentence.title()


def character_frequency(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency