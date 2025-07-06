import math

def perfect_square(n):
    tem = int(math.sqrt(n))

    if (tem * tem) == n:
        print("True")
    else:
        print("False")

n = int(input("Enter the number: "))
perfect_square(n)