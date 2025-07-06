# can a number is expressed as sum of two prime number
number = int(input("Enter the number:"))
arr = []

for i in range(2,number):
    flag = 0
    for j in range(2,i):
        if i%j == 0:
            flag = 1
    if flag == 0:
        arr.append(i)
print(arr)

# finding the possible combinations

for i in range(len(arr)):
    flag = 0
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == number:
            flag = 1
            print(str(arr[i]) + " and " + str(arr[j]) + " makes the sum of the "+  str(number))
            break
    if flag == 0:
        print("No number make addition for this number")

# You now want to find two prime numbers that add up to number.

# The outer loop (for i in range(len(arr))) iterates over each prime number in the list arr, represented by arr[i].

# The inner loop (for j in range(i+1, len(arr))) compares the prime number arr[i] with every prime number that comes after it in the list (arr[j]). 
# This is done to avoid repeating the same pair of prime numbers.

# If the sum of arr[i] and arr[j] is equal to number, the pair is printed with the message "X and Y makes the addition of number", where X and Y are the two prime numbers.

# flag = 1 is set once a pair is found, which can be used to track if any valid pair of prime numbers was found.