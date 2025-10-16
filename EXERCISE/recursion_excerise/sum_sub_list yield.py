def sum_sublist(list1):
    for i in list1:
        if isinstance (i,list) or type(i)==list:
            yield from sum_sublist(i)
        else:
            yield i
a=[1,2,[3,4],5]
b=sum(sum_sublist(a))
print(b)


def recursion_function_sum(l):
    total = 0
    for i in l:
        if type(i)==type([]):
            total = total + recursion_function_sum(i)
        else:
            total+=i
    return total
a=[1,2,[3,4],5]
print(recursion_function_sum(a))
