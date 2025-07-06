#My method
def binaryTODecimal(binary_num):
    power = 0
    number = 0

    for i in binary_num[::-1]: # iterating the string in reverse order ( right to left) it was giving error from left to right
        decimal = int(i) * 2**power
        number += decimal
        power += 1
    print(f"The decimal number of {binary_num} is {number} ")

binary_num = input("Enter the binary number:")
binaryTODecimal(binary_num)


# another method
# def binaryToDecimal(binary_num):
#     decimal, power = 0, 0

#     while(binary_num != 0):
#         dec = binary_num % 10 # this extracts the right most element of the number
#         decimal = decimal + dec * pow(2, power)
#         binary_num =  binary_num // 10 # this removes the rightmost element from the number
#         power += 1
#     print(f"The decimal number of the {binary_num} is {decimal}")

# number = int(input("Enter the binary number:"))
# binaryToDecimal(number)

