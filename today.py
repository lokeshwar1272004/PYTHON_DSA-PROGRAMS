for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print()

for i in range(5):
    if i==0 or i==4:
        print('*'*5)
    else:
        print('*'+' '*(5-2)+'*')

for i in range(5):
    print(' '*(5-i-1)+'*'*(i+1))
for j in range(5-1,0,-1):
    print(' '*(5-j)+'*'*j)
