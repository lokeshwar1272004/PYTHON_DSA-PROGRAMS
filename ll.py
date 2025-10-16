def isAnagram(s,t):
    if len(s) != len(t): return False
    d = {}
    a = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for j in t:
        if j not in a:
            a[j] = 1
        else:
            a[j]+=1
    print(d)
    print(a)

    for k in d.keys():
        if k not in a.keys():
            return False
        if d[k]!=a[k]:return False
    else:
        return True




s='jar'
t = 'jar'

print(isAnagram(s,t))