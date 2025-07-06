# reversing a number using recursion

# def reverse_number(n, result = 0):
#     if n == 0:
#         return result
    
#     # add the last digit of the n to the result and shift the result left by one position
#     result = (result * 10) + (n % 10)

#     return reverse_number(n // 10, result)

# num = int(input("Enter the number:"))
# reverse = reverse_number(num)
# print("The reversed number is :", reverse)


# reversing a number using recursion
def reverse_number(n, result = 0):
    if n == 0:
        return result
    
    result = (result * 10) + ( n % 10)

    return reverse_number(n//10, result)

num =  int(input("Enter the number:"))
reverse = reverse_number(num)
print("The reversed number is :", reverse)