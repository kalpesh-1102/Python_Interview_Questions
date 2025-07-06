# A strong number is a number that is equal to the sum of factorial of its digits
# Explanation : Number = 145
# 145 = 1! + 4! + 5!
# 145 = 1 + 24 + 120
def strong_num(n):
    sum = 0

    for i in n:
        fact = 1
        for j in range(1,int(i)+1):
            fact *= j
        sum += fact
    
    if sum == int(n):
        print("The number is a strong number")
    else:
        print("The number is not a strong number")

n = input("Enter the number: ")
strong_num(n)

