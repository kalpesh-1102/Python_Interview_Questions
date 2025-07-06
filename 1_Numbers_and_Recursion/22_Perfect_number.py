# Perfect number, a positive integer that is equal to the sum of its proper divisors.
# Example
# Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28
# Output : It's a Perfect Number

def perfectNum(n):
    sum = 0
    divisors = []

    for i in range(1,n//2+1): # iterating this loop only till half of the number bcoz the divisor can't be more than half of the num
        if n%i == 0:
            divisors.append(i)
            sum += i
    print(f"The divisors of {n} are {divisors}")

    if sum == n:
        print("The number is a perfect number")        
    else:
        print("The number is not a perfect number")

n = int(input("Enter the number: "))
perfectNum(n)

# ---------------------------------------------------------------------------------------------------------

n = 78
Sum = 0
for i in range(1, n):
    if(n % i == 0):
        Sum = Sum + i
if (Sum == n):
    print("Number is a Perfect Number.")
else:
    print("Number is not a Perfect Number.")