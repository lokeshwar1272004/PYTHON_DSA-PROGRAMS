def sqr(x):
    l,r=1,x
    while l<=r:
        m = (l+r)//2
        mid_square = m*m
        if mid_square == x:
            return m
        elif mid_square>x:
            r=m-1
        else:
            l=m+1
    return r
x=int(input("enter the any number to fid square root of it: "))
print(sqr(x))
print("its take o(long N) time complexity")