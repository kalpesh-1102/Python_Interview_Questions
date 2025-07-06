def smallest(arr):
    if not arr:
        return None
    small = arr[0]

    for num in arr:
        if num < small:
            small = num
        return small

arr = [10,23,45,65,22]
small = smallest(arr)
print("The smallest of the array is ", small)
