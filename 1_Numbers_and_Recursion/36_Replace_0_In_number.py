def replace(num):
    str_num = str(num)
    new_num = []
    for i in str_num:
        if int(i) == 0:
            i = "1"
        new_num.append(i)

    new_num_str = ''.join(new_num)
    print(int(new_num_str))

n = int(input("Enter the number:"))
replace(n)


