def frequency(arr):
    # Counting frequencies

    fre_map = {} # empty dictionary called freq_map to store the frequency of each number in the array.
    order = [] #  # To preserve order of first appearance

    for num in arr:
        if num in fre_map:
            fre_map[num] += 1
        else:
            fre_map[num] = 1
            order.append(num)

    # Create a list of element frequency pair
    fre_list = []
    for num in order:
        fre_list