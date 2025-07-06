# Checking if two strings are anagrams or not

def is_anagrams(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False
    
    count={}

    for char in s1:
        count[char] = count.get(char,0) + 1

    for char in s2:
        if char not in s1 or count[char] == 0:
            return False
        count[char] -= 1
    return True
print(is_anagrams("listen","silen"))



