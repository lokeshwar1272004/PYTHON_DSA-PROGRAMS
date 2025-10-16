a = []
mat =[[0,1,2],[4,5,6],[7,8,9],[10,11,12]]
i = 0
j=0
n=2
while i<len(mat):
    while j>=0 and j<len(mat[i]):
        a.append(mat[i][j])
        if n%2==0:
            j+=1
        else:
            j-=1
    i+=1
    if i<len(mat) and j==len(mat[i]):
        j-=1
    elif j<0:
        j=0
    n+=1
print(a)
