# code to print all the possible permutation of a string

def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return 
    

    for i in range(len(s)):
        # pick the current character
        ch = s[i]

        # Form the remaining string by removing the current character
        rest_of_sting = s[:i] + s[i+1:]

        permute(rest_of_sting, answer + ch)

# usage
string = input("Enter a string: ")
print("All the permutation of the string are:")
permute(string)


