# Capitalize the first letter of each word

def capitalize(sentence):
    words = sentence.split()

    capitalize_word = [word[0].upper() + word[1:] if word else ' ' for word in words]
    return ' '.join(capitalize_word)

text = "hey my name is kalpesh"
print("Capitalized:",capitalize(text))