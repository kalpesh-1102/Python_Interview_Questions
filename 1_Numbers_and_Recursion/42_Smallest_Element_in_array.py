# finding the smallest element

def find_smallest(arr,n):
    if n == 1:
        return arr[0]
    
    min_of_rest = find_smallest(arr, n-1)

    return min(arr[n-1],min_of_rest)

arr = [4, 3, 7, 1, 9, -1]
num = len(arr)
smallest = find_smallest(arr,num)
print("The smallest number in an array is:", smallest)