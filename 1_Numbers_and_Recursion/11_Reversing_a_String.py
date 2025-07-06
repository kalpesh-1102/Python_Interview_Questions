# Program to reverse a string
def reverse(s):
    str = ""
    for i in s:
        str = i+str
    print(str)

s = "kalpesh"
reverse(s)

# Explanation 
# str is an empty string
# suppose we consider that the string in abc
# now if we iterate i in abc
# in the first iteration the i will be a so str will be = "a"+"" i.e a
# in the next iteratino the i will be b so the str will be "b"+str i.e b+a = ba
# and similarly c will be added to the string and the string is reversed