# The GCD of 12 and 8 is 4 because 4 is the largest number that divides both 12 and 8 evenly
def Gcd(num1, num2):
    for i in range(1, min(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i # This means that every time we find a new common divisor, gcd will be updated.
    print(f"The greatest common divisor of {num1} and {num2} is {gcd}")

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
Gcd(num1,num2)