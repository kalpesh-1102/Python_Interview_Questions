def is_palindrome(string):
    reverse = ""
    for char in string:
        reverse = char + reverse
    print("The reverse of the string is :", reverse)

    if reverse == string:
        print("The string is a palindrome string")
    else:
        print("The string is not a palindrome string")

string = input("Enter the string:")
is_palindrome(string)