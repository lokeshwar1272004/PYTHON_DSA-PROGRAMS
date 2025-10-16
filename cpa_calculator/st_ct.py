s = "aba"
n = []
ct = []
for i in s:
    if i not in n:
        n.append(i)
        ct.append(1)
    else:
        ct[n.index(i)]+=1

print(n,ct)