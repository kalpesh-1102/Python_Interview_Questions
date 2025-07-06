# to calculate the lcm we can use the relation betn the LCM and HCF 
# lcm(a,b) = |a*b|//hcf(a,b)

def hcf(a,b):
    if b == 0:
        return a
    return hcf(b,a % b)

def lcm(a,b):
    return abs(a*b)//hcf(a,b)

n1 = int(input("Enter the number 1:"))
n2 = int(input("Enter the number 2:"))

result = lcm(n1,n2)
print(f"The LCM of {n1} and {n2} is {result}")