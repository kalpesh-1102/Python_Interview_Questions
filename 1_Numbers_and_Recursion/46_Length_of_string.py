def str_length(s):
    if s == "":
        return 0
    
    return 1 + str_length(s[1:])

str = input("Enter the string:")
len = str_length(str)
print("The length of the string is:", len)