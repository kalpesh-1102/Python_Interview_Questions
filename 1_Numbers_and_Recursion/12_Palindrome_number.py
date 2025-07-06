# For a number or string to be palindrome in Python, the number or string must be the same when inverted.
# num = input("Enter the number:")

# reverse = num[::-1]
# if num == reverse:
#     print("palindrome")
# else:
#     print("Not palindrome")


# another approach
num = 1221

reverse = int(str(num)[::-1])
if num == reverse:
    print("palindrome")
else:
    print("Not palindrome")

# another approach
def palindrome(str):

    # reversing the string
    reverse_str = ""
    for i in str:
        reverse_str = i + reverse_str
    print("The reverse string is:",reverse_str)

    if reverse_str == str:
        print("The string is a palindrome string")
    else:
        print("The sting is not a palindrome string")

str = input("Enter the string: ")
palindrome(str)

