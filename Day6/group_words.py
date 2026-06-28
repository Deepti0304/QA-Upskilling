# words=["cat","apple","dog","banana","car"]

# groups={}

# for word in words:

#     length=len(word)

#     groups.setdefault(length,[]).append(word)

# print(groups)

def group_words_by_length(words):
    groups = {}

    for word in words:
        length = len(word)
    
        if length not in groups:
            groups[length] = []

        groups[length].append(word)

    return groups