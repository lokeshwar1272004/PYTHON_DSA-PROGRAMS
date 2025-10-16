n = int(input())
for i in range(1,n+1):
    row =''
    row+=' '*(n-i)
    for j in range(i,2*i):
        row+=str(j)
    for j in range(2*i-2,i-1,-1):
        row+=str(j)
    print(row)