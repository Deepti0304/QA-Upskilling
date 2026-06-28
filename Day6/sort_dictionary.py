# scores={
# "John":80,
# "David":95,
# "Alice":75
# }

# sorted_scores=dict(
#     sorted(scores.items(),
#     key=lambda item:item[1])
# )

# print(sorted_scores)

def sort_dictionary_by_value(data):
    return dict(
        sorted(data.items(), key=lambda item: item[1])
    )