# x is called HCF of a & b two conditions :

# x can completely divide both a & b leaving remainder 0
# No, other number greater than x can completely divide both a & b

def hcf(num1, num2):
    hcf = 1
    for i in range(1, min(num1, num2)):
        if num1%i == 0 and num2%i == 0:
            hcf = i
    print(f"The hcf of {num1} and {num2} is {hcf}")


num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))

hcf(num1, num2)