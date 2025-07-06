# Example: The prime factors of 15 are 3 and 5 (because 3×5=15, and 3 and 5 are prime numbers).
# Program to print the prime factor of the number
# For example, the prime factors of 210 are 2, 3, 5, and 7 because: 2*3*5*7 = 210

import math
def primeFactor(n):
    arr = []

    # Remove all the factors of two
    while n%2 == 0:
        arr.append(2)
        n = n//2

    # check odd numbers from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n))+1,2):
        while n%i == 0:
            arr.append(i)
            n = n//i

    # if n is still greater than 2 then it must be a prime number
    if n > 2:
        arr.append(n)

    return arr

n = int(input("Enter the number: "))
print(primeFactor(n))


