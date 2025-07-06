def find_num(arr):
    if not arr:
        return None
    
    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num

        if num > largest:
            largest = num

    return smallest, largest

arr = [10,34,23,54,56,33,65]
small, large = find_num(arr) # here the first return value i.e smallest will be assigned to small and the 2nd to large
# 
print("The smallest number of an array is ", small) # as the smallest values is assigned to the small this will print the smallest value
print("The largest number of an array is ", large) # and this print the largest values of the list







# def find_num(arr):
#     if not arr:
#         return None
    
#     smallest = arr[0]
#     largest = arr[0]

#     for num in arr:
#         if num < smallest:
#             smallest = num
#         if num > largest:
#             largest = num
#     return smallest, largest

# arr = [11,23,4,45,34,12,3]
# numbers = find_num(arr)
# print("The smallest and the largest number in the list are: ", numbers)