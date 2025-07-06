# Finding the smallest and largest element in the list

def small_large(list):

    smallest = list[0]
    largest = list[0]

    for num in list:
        if num < smallest:
            smallest = num

        if num > largest:
            largest = num
    return smallest, largest

list = [1,35,12,3,9,10,11,4]
small, large = small_large(list)

print("The smallest number in the list is :",small)
print("The largest number in the list is :",large)
