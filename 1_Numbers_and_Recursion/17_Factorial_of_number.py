# finding a factorial of a given number
num = int(input("Enter the number"))
fact = 1

if num < 0:
    print("Factorial not possible")
else:
    for i in range(1, num+1):
        fact = fact*i

print(f"The factoria of {num} is {fact}")
