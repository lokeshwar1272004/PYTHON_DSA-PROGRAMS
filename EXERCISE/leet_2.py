def na(n):
    if n ==1:
        return 1
    else:
        return n + na(n-1)
n=3
print(na(n))