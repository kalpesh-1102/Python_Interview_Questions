# # Program for printing the prime numbers in a given range
def is_prime(start,end):
    prime_num = []

    for i in range(start, end+1):
        if i < 2:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            prime_num.append(i)
    print(f"The prime numbers between {start} and {end} are {prime_num}")

start = int(input("Enter the number 1:"))
end = int(input("Enter the number 2:"))

is_prime(start,end)

