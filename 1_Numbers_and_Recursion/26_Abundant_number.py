# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.

def abudundantNum(n):
    factors = []
    sum = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            factors.append(i)
            sum += i

    if sum>n:
        print("The number is a abundant number")
    else:
        print("The number is not abundant number")

n = int(input("Enter the number:"))
abudundantNum(n)