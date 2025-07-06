# Program to calculate the maximum no of handshakes in the room

def handshakes(n):
    no_of_handshakes = ((n-1)*n)//2
    print(f"The number of handshakes possible for {n} no of people is {no_of_handshakes} ")

n = int(input("Enter the number of people:"))
handshakes(n)