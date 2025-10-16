l2 = [1,2,[3,4],[5,6]]
def s2(l2):
    total = 0
    for i in l2:
        if type(i)==type([]):
            total = total + s2(i)
        else:
            total=total+i
    return total
print(s2(l2))

def list_2(q):
    list_1 = []
    for i in q:
        if isinstance(i,list):
            list_1+=(list_2(i))
        else:
            list_1.append(i)

    return  list_1

print(list_2([1,2,[1,3],[3]]))