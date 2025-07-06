# find the sum of numbers in a given intervals
num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
sum = 0

for i in range(num1, num2+1):
    sum+=i
print(f"The sum of the number from {num1} to {num2} is {sum}")
