# # Sorting the firt half in ascending order and second half in descending order of an array

# def order_array(array, n):
    
#     # sorting the array in ascending order
#     array.sort()

#     i = 0
#     while i <= n//2:
#         print (array[i], end= " ")
#         i = i+1

#     j = n-1
#     while j > n//2:
#         print (array[j], end= " ")
#         j = j-1

# arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
# n = len(arr)
# order_array(arr, n)



# sorting the first half in ascending order and second half in descending order of an arrar
def order(array):
    n = len(array)

    array.sort()

    # printing the first half
    for i in range(0,n//2):
        print(array[i], end= " ")
    
    # printing the second half
    for j in range(n-1,n//2-1,-1):
        print(array[j], end= " ")

array = [2,3,4,5,5,7,3,1,7,9]
result = order(array)

