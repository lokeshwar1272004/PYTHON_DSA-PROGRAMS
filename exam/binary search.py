def binary_search(arr):
    search = 2
    l = 0
    r =len(arr)-1

    while l <= r:
        mid = (l+r)//2
        if arr[mid] == search:
            return mid
        if search > arr[mid]:
            l = mid+1
        else:
            r = mid-1


arr = [1,2,3,5,6]
print(binary_search(arr))


