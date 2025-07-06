# Rotating the list left or right

def rotate_list(arr, k, direction='left'):

    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n # To handle the case when k > n ex - k = 7 and len of array is 5 then it will be equivalent by 2 

    if direction == 'left':
        return arr[k:] + arr[:k]
    elif direction == 'right':
        return arr[-k:] + arr[:-k]
    else:
        return "Invalid Direction"
    
arr = [1,2,3,4,5,6]
k = int(input("Enter the Kth place: "))
direction = input("Enter the direction:").lower()

print(rotate_list(arr,k,direction))


"""
Left Rotation
Example:
arr = [1, 2, 3, 4, 5], k = 2
arr[k:] = [3, 4, 5], arr[:k] = [1, 2]
Result: [3, 4, 5, 1, 2]

Right Rotation
Example:
arr = [1, 2, 3, 4, 5], k = 2
arr[-2:] = [4, 5], arr[:-2] = [1, 2, 3]
Result: [4, 5, 1, 2, 3]

"""