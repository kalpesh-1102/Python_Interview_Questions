# def sort_array(array):
#     array.sort()

#     print(array)
# array = [1,3,2,4,5,3]
# sort_array(array)

# Another method of sorting an array without using sort function

def sort(arr):
    temp = 0 

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print("The array after sorting is ",arr)

arr = [2,3,3,4,6,1,4]
sort(arr)
