# finding the second smallest number in an array

def second_smallest(numbers):
    if len(numbers) < 2:
        return "Array must have at least two numbers"
    
    if len(numbers) < 2:
        return "Array must have at least two numbers"

    smallest = float('inf')
    second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest:
            second_smallest = num
    return second_smallest

numbers = [3,4,2,5,6,1]
result = second_smallest(numbers)
print("The second smallest number is:",result)
        





















# Using sort function
# def second_smallest(numbers):
#     if len(numbers) < 2:
#         return "Array must have at least two numbers"
    
#     # removing duplicates 
#     unique_num = list(set(numbers)) # removing the duplicates as the set does not have duplicates 

#     # sorting the numbers in ascending order
#     unique_num.sort()

#     # after sorting the second smallest num will be at index no 2
#     return unique_num[1] if len(unique_num)>1 else "No second smallest number"

# array = [1,3,2,4,5,6,5]
# result = second_smallest(array)
# print("The second smallest number is:",result)


