#!/usr/bin/python3
def uniq_add(my_list=[]):
    ints_added = []
    sum = 0

    for num in my_list:
        if num in ints_added:
            continue

        sum += num
        ints_added.append(num)

    return sum
