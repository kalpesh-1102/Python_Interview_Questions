# Group words with same set of characters
from collections import defaultdict

def group_words(words):

    # Create a dictionary where each key will store a list of words that belongs to same group
    grouped = defaultdict(list)

    for word in words:
        key = ''.join(sorted(set(word)))    # ''.join() converts the list of characters into a string → becomes a unique key for the group.
        grouped[key].append(word)

    return list(grouped.values())  # only return the list of groups (not the keys).

words = ["bat", "tab", "tap", "pat", "top", "pot", "opt"]
result = group_words(words)
print("Grouped Words:",result)


