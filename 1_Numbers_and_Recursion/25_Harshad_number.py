# The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number.

def harshadNum(n):
    sum = 0
    for i in str(n):
        sum = sum +int(i)
    if n%sum == 0:
        print("The number is a harshad number")
    else:
        print("The number is not a harshad number")

n = int(input("Enter the number:"))
harshadNum(n)
    
