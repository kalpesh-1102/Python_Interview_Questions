def flatten_list(nested_list):

    flat_list = []

    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item)) # .extend() adds elements from an iterable individually.
            # .append() adds the entire iterable as a single element to the end of the list.
        else:
            flat_list.append(item)

    return flat_list

nested = [1,2,3,[5,7],[2,1],10]

print("Flattened list:",flatten_list(nested))


"""
Example: 

nested = [1, [2, 3], [4, [5, 6]], 7]

Steps:

1 → append

[2, 3] → flatten → 2, 3

[4, [5, 6]] → flatten → 4, 5, 6

7 → append
"""