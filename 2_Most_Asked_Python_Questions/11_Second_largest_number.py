# finding the second highest number in the list

def second_highest(nums):
    if len(nums) < 2:
        return "List must have atleast two numbers"
    
    first = second = float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num

        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else "No second highest"

nums = [10,4,45,30,21,49]

print("The second highest number is:",second_highest(nums))