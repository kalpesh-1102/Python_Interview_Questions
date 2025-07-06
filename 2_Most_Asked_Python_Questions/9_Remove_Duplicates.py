# Removing duplicates froom the list

def remove_duplicates(list):
    unique = []

    for item in list:
        if item not in unique:
            unique.append(item)
    return unique

nums = [1,1,2,3,4,4,4,5,6,6]
removed = remove_duplicates(nums)
print("Without duplicates list: ",removed)

