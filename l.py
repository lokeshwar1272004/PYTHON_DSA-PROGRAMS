lst = ["jk##","w3#5#"]
a = []

for i in lst:
    j = 0
    while j+1 < len(i):
        if i[j]=='#' and i[j+1] =='#':
            a.append(i)
        j+=1
print(a)
