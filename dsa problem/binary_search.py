def binary_search(number_list,find_num):
    l = 0
    u = len(number_list) - 1

    while l<u:
        mid_index = (l + u) // 2
        mid_number = number_list[mid_index]

        if mid_number == find_num:
            return mid_index
        if mid_number < find_num:
            l = mid_index +1

        else:
            u = mid_index - 1
    return l



number_list = [1,2,4,5,6]
print("....",len(number_list))
find_num = 6
print(binary_search(number_list,find_num))