# Calculating the sum of the array

def sum_of_array(array):
    if len(array) == 1:
        return array[0]
    
    sum = 0
    for i in array:
        sum += i
    return sum

array = [12,34,5,32,20]
result = sum_of_array(array)
print("The sum of the array is:",result)