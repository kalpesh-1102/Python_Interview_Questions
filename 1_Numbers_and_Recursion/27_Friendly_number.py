# Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively. 
# When we divide the sums with the numbers we get 1 and 1 respectively. 
# As the ratio of both the number match, they are considered as a friendly pair.

def friendlyNum(n):
    sum = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            sum += i
    if sum%n == 1:
        return True
    
n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))

if friendlyNum(n1) == friendlyNum(n2):
    print("The number is a friendly number")
else:
    print("The number is not a friendly number")