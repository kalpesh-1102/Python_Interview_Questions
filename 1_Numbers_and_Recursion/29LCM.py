# Multiples of 4: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, ...
# Multiples of 6: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, ...
# The common multiples of 4 and 6 are: 12, 24, 36, 48, 60
# The smallest common multiple is 12.

def LCM(num1, num2):
    for i in range(max(num1, num2),(num2*num1)+1):
        if i%num1 == 0 and i%num2 == 0:
            lcm = i
            break
    print(f"The lcm is {lcm}")

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))

LCM(num1,num2)
