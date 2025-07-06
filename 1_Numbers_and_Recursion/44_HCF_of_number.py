# calculating the hcf of number using recursion

# HCF stands for Highest Common Factor. It is the largest number that divides two or more numbers exactly without leaving a remainder.   
# For example, the HCF of 12 and 18 is 6, because 6 is the largest number that divides both 12 and 18 evenly. 

def hcf(a,b):
    if b == 0:
        return a # if b = 0 then hcf of both a and b i.e 0 will be a so this is the base condition
    
    return hcf(b,a%b)

n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))
result = hcf(n1,n2)
print(f"The HCF of {n1} and {n2} is {result}")