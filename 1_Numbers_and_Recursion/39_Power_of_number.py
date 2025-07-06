# def power(a,b):
#     if b != 0:
#         return a * power(a,b-1)
#     else:
#         return 1
    
# print(power(2,3))

# finding power of number using recursion
def power(a,b):
    if b != 0:
        return a * power(a, b-1)
    else:
        return 1 

print(power(2,3))    
