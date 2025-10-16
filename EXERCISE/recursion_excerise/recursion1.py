list = [12,7,2,0,0,4]
def sum_of_all(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_of_all(list[1:])



print(sum_of_all(list))
