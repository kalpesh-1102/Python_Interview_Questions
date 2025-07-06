
# Find all pairs in the list that sums a value

def find_pair(arr,target):
    pair = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                pair.append((arr[i],arr[j]))
    
    return pair

arr = [1,2,3,4,5,6,7,8]
target = 5
print("All Pairs:",find_pair(arr,target))