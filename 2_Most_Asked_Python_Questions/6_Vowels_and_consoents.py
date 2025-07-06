
string = input("Enter the string:")

vowels = 'aeiouAEIOU'
vowel_count = 0
consonent_cunt = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonent_cunt += 1

print("The vowels are:", vowel_count)
print("The consonents are:",consonent_cunt)

