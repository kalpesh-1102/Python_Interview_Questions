# Program to find the factors of the given number
num = int(input("Enter the number:"))
factor = []
for i in range(1, num):
    if num%i == 0:
        factor.append(i)

print(f"The factorial of {num} are {factor}")