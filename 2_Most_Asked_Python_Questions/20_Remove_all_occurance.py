# Remove all the occurance of a character from string

def remove_char(text,char_to_remove):
    # text = text.lower()
    result = ''

    for char in text:
        if char != char_to_remove:
            result += char
    return result

text = input("Enter the stirng:")
char_to_remove = input("Enter ther char to remove:")
print("Result:",remove_char(text,char_to_remove))