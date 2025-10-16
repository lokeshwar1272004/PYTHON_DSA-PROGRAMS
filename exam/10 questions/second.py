element = [1,2,7,2,0,0,4]
def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None
print(second_largest(element))


def second(element):
    lar=second=float('-inf')
    for i in element:
        if i > lar:
            second = lar
            lar = i
        elif i > second and i!=lar:
            second = i
    if second!=float('-inf'):
        return second
    else:
        return None

print(second([6,3,5,2,1]))


