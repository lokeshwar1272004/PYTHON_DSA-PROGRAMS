"""
3
123
3
456
output
5 7 9
"""
x = int(input())
for _ in range(x):
    n = int(input())
    a = input().split()
    a = ''.join(a)

    n2 = int(input())
    b = input().split()
    b = ''.join(b)
    summ = int(a) + int(b)
    summ = str(summ)
    while len(summ)<max(n,n2):
        summ = '0' + summ
    for i in str(summ):
        print(int(i),end=' ')
    print('\t')


