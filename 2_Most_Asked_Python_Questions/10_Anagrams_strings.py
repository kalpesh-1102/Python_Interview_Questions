# Checking if two strings are anagrams or not

# def is_anagram(s1, s2):
#     s1 = s1.replace(" ","").lower()
#     s2 = s2.replace(" ","").lower()

#     if len(s1) != len(s2):
#         return False
    
#     count = {}

#     for char in s1:
#         count[char] = count.get(char,0) + 1 # here count[char] is incremented to +1 if the value of the key is already present 
#         # if not then first increment it by 0 and then add 1

#     for char in s2:
#         if char not in count or count[char] == 0:
#             return False
#         count[char] -= 1
    
#     return True

# print(is_anagram("listen","silent"))


# another easy approach 
def are_anagrams_optimized(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1.lower()) == sorted(s2.lower())

# Example usage
print(are_anagrams_optimized("Listen", "Silent"))  # Output: True
print(are_anagrams_optimized("Hello", "World"))  # Output: False

