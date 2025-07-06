# Finding the largest element of the array
def largest(arr):
    if not arr:
        return None
    
    large = arr[0]

    for num in arr:
        if num > large:
            large = num
    return large

arr = [10,45,34,25,56]
largest_elemetn = largest(arr)
print("The largest element of the array is ", largest_elemetn)

