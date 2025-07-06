# Program to enter the sum of the given number

# n = int(input("Enter the number"))
# sum = 0
# for i in n:
#     sum = sum + i
# print(sum) ---------- this code will throw an error as looping through an requires an object to be iterable
# and integers are not iterable


n = input("Enter the number")
sum = 0
for i in n:
    sum = sum + int(i)
print(f"The sum of the given number is {sum}")