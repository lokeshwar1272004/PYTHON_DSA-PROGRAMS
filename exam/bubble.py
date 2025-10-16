def bubble_short(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[j],arr[i]=arr[i],arr[j]
        print(arr,arr[i],i)
    return arr






arr = [3,5,7,2,9]
print(bubble_short(arr))