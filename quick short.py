def swape(a,b,arr):
    if a!=b:
        temp =arr[a]
        arr[a]=arr[b]
        arr[b]=temp



def partition(element,start,end):
    partition_index = start
    povit = element[partition_index]


    while start < end:
        while start < len(element) and element[start] <= povit:
            start += 1
        while element[end] > povit:
            end -= 1
        if start < end:
            swape(start, end, element)
    swape(partition_index, end, element)
    return end
def quick_short(element,start,end):
    if start < end:
        pi = partition(element,start,end)
        quick_short(element,start,pi - 1)
        quick_short(element,pi+1,end)

element = [11,9,29,7,2,15,28]
print(element)
quick_short(element,0,len(element)-1)
print(element)
print(".....")
text = [
    [1,4,9],
    [7,100,2,45,18],

]
for element in text:
    quick_short(element,0,len(text)-1)
    print(f'the shorted element:{element}')

