# An Armstrong number (also known as a Narcissistic number or pluperfect digit-invariant number) is a number
# that is equal to the sum of its own digits each raised to the power of the number of digits.
# Example of Armstrong Numbers:
# 153 is an Armstrong number
# It has 3 digits.
# 1+125+27=153

# num = int(input("Enter the number"))
# sum = 0
# num_str = str(num)
# len = len(num_str)

# for i in num_str:
#     sum = sum + int(i)**len
# if sum == num:
#     print("The number is an armstrong number")
# else:
#     print("The number is not an armstrong number")

# num = int(input("Enter the number:"))
# sum = 0
# num_str = str(num)
# len = len(num_str)

# for i in num_str:
#     sum = sum + int(i)**len

# if sum == num:
#     print("The number is an armstrong number")
# else:
#     print("The number is not an armstrong number")



# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10 # gives the last digit of the number.
   sum += digit ** 3 # computes the cube of that digit.
   temp //= 10 # removes the last digit (integer division by 10).

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

