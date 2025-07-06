def addFraction(n1,d1,n2,d2):
    # 1 - getting numerator
    numerator = (n1*d2) + (d1*n2)

    # 2 - getting denominator 
    denominator = (d1*d2)

    # 3 - getting GCD of numerator and denominator
    for i in range(1, min(numerator,denominator)+1):
        if numerator%i == 0 and denominator%i == 0:
            gcd = i 

    # 4 - getting the final result
    print(f"{numerator//gcd}/{denominator//gcd}")



n1 = int(input("Enter the numerator of fraction 1:"))
d1 = int(input("Enter the demoniator of fraction 1:"))
print()
n2 = int(input("Enter the numerator of fraction 2:"))
d2 = int(input("Enter the denominator of fracton 2:"))

print("The addition of two fractions",n1,"/",d1, " + ", n2,"/",d2, "is equal to ", end="" )
addFraction(n1,d1,n2,d2)




