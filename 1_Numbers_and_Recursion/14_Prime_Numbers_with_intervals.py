# printing prime numbers with an interval of an prime number in before the next prime number

# function to detect prime number
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True # if divisor is found than n is a prime number

def prime_list(start_num,end_num):
    

