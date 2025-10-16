n=121
s=0
while n>0:
    s=s*10+(n%10)
    n=n//10
print(s)

l=[]
r=int(input())
def prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(2,r):
    if prime(i):
        l.append(i)
print(l)
15

fib=[0,1]
for i in range(2,r):
    fib.append(fib[-2]+fib[-1])
print(fib)

def fib(r):
    if r==0 or r==1:
        return 1
    return fib(r-1)+fib(r-2)
print(fib(r))
