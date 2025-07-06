## finding the frequency of an elements in an array

# def countFreq(arr, n):
 
#     mp = dict()
 
#     # Traverse through array elements 
#     # and count frequencies
#     for i in range(n):
#         if arr[i] in mp.keys(): # checking if the value is in the dictionary or not
#             mp[arr[i]] += 1  # if value is present increment the value of the key of that number by one
#         else:
#             mp[arr[i]] = 1 # if not present add i as key to the dictionary with the value of 1
             
#     # Traverse through map and print 
#     # frequencies
#     for x in mp: # loop to iterate through all the keys of the dictionary
#         print(x, " ", mp[x]) # print key and its value i.e mp[x]
 
# # Driver code
# arr = [10, 20, 20, 10, 10, 20, 5, 20 ]
# n = len(arr)
# countFreq(arr, n)

# finding the frequency of an element in an array
def countFreq(arr, n):
    mp = dict() # empty dictionary to store the frequencies

    # Traversing through array element and count the frequencies
    for i in range(n):
        if arr[i] in mp.keys(): 
            mp[arr[i]] += 1 # incrementing the value
        else:
            mp[arr[i]] = 1

    for x in mp:
        print(x, " ", mp[x])

# Driver code
arr = [10,20,20,30,40,50,40,40]
n = len(arr)
countFreq(arr, n)
