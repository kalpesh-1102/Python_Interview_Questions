def factorial(num):
    fac = 1

    for i in range(1,num+1):
        fac *= i
    print(f"The factorial of {num} is {fac}")

num = int(input("Enter number:"))
factorial(num)

