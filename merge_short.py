a = [1,3,4,6,8,10]
b = [21,33,55,77,88]
arr=[3,7,9,0,11]

def merge_short_main(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right =arr[mid:]
    left=merge_short_main(left)
    right=merge_short_main(right)
    return merge_short(left,right)



def merge_short(a,b):
    merge_=[]
    len_a=len(a)
    len_b=len(b)
    i = j = 0
    while i < len_a and j < len_b:
        if a[i]<=b[j]:
            merge_.append(a[i])
            i+=1
        else:
            merge_.append(b[j])
            j+=1

    while i < len_a:
        merge_.append(a[i])
        i+=1
    while j < len_b:
        merge_.append(b[j])
        j+=1
    return merge_
#print(merge_short(a,b))
print(merge_short_main(arr))


