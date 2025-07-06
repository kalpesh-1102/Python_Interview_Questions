# In a classroom some of the seats are already occupied by students and only a few seats are available
# in the classroom. The available seats are assumed as r and n number of students are looking for the seat. 
# We need to find in how many different permutations n number of students can sit on r number of chairs.

# Algorithm
# Input number of students in n
# Input number of seats in r
# Use permutation formula { factorial(n) / factorial(n-r) }

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

n = int(input("Enter the no of people:"))
r = int(input("Enter the no of seats:"))

p = factorial(n) // factorial(n-r)

print("The total possible combination are:", p)