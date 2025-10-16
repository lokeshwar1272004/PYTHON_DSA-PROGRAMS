def swap(start,end,element):
    if start<end:
        temp = element[start]
        element[start]=element[end]
        element[end]=temp

def parti(start,end,element):
    part=start
    pivot = element[start]


    while start < end:
        while start< end and element[start]<=pivot:
            start+=1
        while element[end]>pivot:
            end-=1
        if start < end:
            swap(start,end,element)
    swap(part,end,element)
    return end
def quick_short(element,start,end):
    if start < end:
        pi = parti(start, end, element)
        quick_short(element, start, pi - 1)
        quick_short(element, pi + 1, end)



element = [11,9,29,7,2,15,28]
quick_short(element,0,len(element)-1)
print(element)