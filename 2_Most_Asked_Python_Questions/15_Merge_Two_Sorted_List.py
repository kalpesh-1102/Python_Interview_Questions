# Merging the two Sorted list

def merge_sorted(list1, list2):
    i = j = 0 # Pointers for both the list
    merged = [] # For final list

    # Loop through both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1

        else:
            merged.append(list2[j])
            j += 1

    # Adding the remaining item  (only one of the two while loops will run)
    while i < len(list1):
        merged.append(list1[1])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

list1 = [1,2,3,5,7]
list2 = [2,4,6,8]
print("Merges List:", merge_sorted(list1,list2))
