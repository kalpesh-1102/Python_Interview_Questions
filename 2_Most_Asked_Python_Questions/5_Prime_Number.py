num = int(input("Enter the prime number:"))

if num < 2:
    print("The number is not a prime number!")

else:
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

    