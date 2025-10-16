elements = [1,2,3,4,5,6]
target = 3
n = []
i=0
j=0
s = 0
while i < len(elements):
    while j < len(elements):
        if s < target:
            s+=elements[j]
        if s == target:
            n.append(j-i-1)
        j+=1
    s-=elements[i]
    i+=1
print(n)









