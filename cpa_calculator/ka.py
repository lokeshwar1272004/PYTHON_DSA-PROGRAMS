arr =[2,3,-8,7,-1,2,3]
arr1=[-2,1,-3,4,-1,2,1,-5,4,-4]

def min_sub(arr):
    mx=float('inf')
    s = 0
    for i in arr:
        s+=i
        if mx>s:
            mx = s
        else:
            s = 0
    print(mx)
def max_sub(arr):
    mx=float('-inf')
    s = 0
    for i in arr:
        s+=i
        if s<0:
            s=0
        if mx<s:
            mx = s
    print(mx)
min_sub(arr)
max_sub(arr)

min_sub(arr1)
max_sub(arr1)