# An Armstrong number is a number that equals the sum of its own digits, 
# each raised to the power of the number of digits. 
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153

low = int(input("Enter the lower number"))
high = int(input("Enter the higher number"))

armstrong = []

for i in range(low, high+1):
    str_num = str(i)
    num_len = len(str_num)
    sum = 0

    for j in str_num:
        sum = sum + int(j)**num_len

    if sum == i:
        armstrong.append(i)

print(f"The armstrong numbers from {low} to {high} are {armstrong}")

