# Finding the duplicate element in the list using set

def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item) # add is used in case of set to add the element at the end, if the element is already present, it will not work

        else:
            seen.add(item)
    
    return list(duplicates)

data = [1,2,3,4,3,2,4,5,6,7,7,8,9]
print("Duplicate Items:",find_duplicates(data))