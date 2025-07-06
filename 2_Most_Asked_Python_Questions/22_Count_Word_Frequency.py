# Count Word frequency in a sentence

def word_count(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

sentence = "Data science is fun and data is powerful"
result = word_count(sentence)
print("Word Frequencies:",result)
