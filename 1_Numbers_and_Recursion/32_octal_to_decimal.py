# Octal to decimal conversion - my method

def octalToDecimal(num):
    power = 0
    number = 0

    for i in num[::-1]:
        dec = int(i) * 8**power
        number += dec
        power += 1
    
    print(f"The decimal number of octal number {num} is {number}")

octalNum = input("Enter the number:")
octalToDecimal(octalNum)