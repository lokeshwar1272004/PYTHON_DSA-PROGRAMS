n = [1,2,[3,4],2]
def list_sum(n):
    total=0
    for i in n:
        if isinstance(i,list):
            total = total + list_sum(i)
        else:
            total=total + i
    return total
print(list_sum(n))