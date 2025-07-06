# Prime number using recursion
# def isprime(n,i=2):
#     if(n==i):
#         return True
#     elif n % i == 0:
#         return False
#     return(isprime(n,i+1))

# n = 971
# if isprime(n):
#     print("Yes it is a prime number")
# else:
#     print("No it is not a prime")


# Prime number using recursion
def isprime(n, i = 2):
    if(n==i):
        return True
    elif n%i == 0:
        return False
    return(isprime(n,i+1))

n = int(input("Enter the number"))
if isprime(n):
    print("The number is a prime number")
else:
    print("The number is not a prime number")