def frequency_count(lst):
    freq = {}

    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

numbers = [1,2,1,3,4,2,4,5,3,6]
print(frequency_count(numbers))