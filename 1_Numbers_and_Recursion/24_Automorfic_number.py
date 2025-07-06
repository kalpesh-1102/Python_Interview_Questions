# for a number to be Automorphic it number have a square that ends with the number itself.
# example is 25 as it is the square of 5 and ends with 5

def num(n):
    num1 = n*n 
    str_num1 = str(num1)

    if str_num1.endswith(str(n)): 
        print("The number is an automorphic number")
    else:
        print("The number is not an automorphic number")

n = int(input("Enter the number:"))
num(n)
