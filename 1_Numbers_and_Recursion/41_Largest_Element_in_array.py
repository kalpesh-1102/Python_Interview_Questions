# def find_largest(arr, n):
#     if n == 1:
#         return arr[0]
    
#     max_of_rest = find_largest(arr, n - 1)
    
#     return max(arr[n - 1], max_of_rest)

# # Example usage:
# arr = [10, 20, 4, 45, 99]
# n = len(arr)
# largest = find_largest(arr, n)
# print("The largest element is:", largest)


# finding the largest element of an array using recurrsion
def find_largest(arr, n):
    if n == 1:
        return arr[0]
    
    max_of_rest = find_largest(arr, n-1)

    return max(arr[n-1], max_of_rest)

arr = [10,20,4,45,99]
n = len(arr)
largest = find_largest(arr, n)
print(largest)
