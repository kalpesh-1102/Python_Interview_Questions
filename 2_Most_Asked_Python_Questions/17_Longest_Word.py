# Find the longest word in the sentence

def longest_word(sentence):

    words = sentence.split()

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

sentence = "My name is Kalpesh"
print("The longest word in the sentence is:", longest_word(sentence))