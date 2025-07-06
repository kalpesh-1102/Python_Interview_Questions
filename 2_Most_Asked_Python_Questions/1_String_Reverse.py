def reverse(str):
    reverse_str = ""

    for char in str:
        reverse_str = char + reverse_str
    
    print("The reverse of the string is :", reverse_str)

str = "kalpesh"

reverse(str)