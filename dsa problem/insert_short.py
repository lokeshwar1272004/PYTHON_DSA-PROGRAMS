def insert_short(n):
    element=[1,2,7,0,0,4]
    for i in range(1,len(element)):
        anchor = element[i]
        j = i-1
        while j>=0 and anchor < element[j]:
            element[j+1] = element[j]
            j -=1
        element[j+1] = anchor
    return element

print(insert_short(0))



def insertion_sort(n):
    elements = n
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1]=elements[j]
            j-=1
        elements[j+1]=anchor
    return elements

print(insertion_sort([1,2,7,2,0,0,4]))






elements = [29,7,23,0,21]
elements = ['l','k','o','e','s','h','w','a','r']
elements = list(input())
print(insert_short(elements))