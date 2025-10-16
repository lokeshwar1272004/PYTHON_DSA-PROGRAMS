n=121
if n<0:
    print(False)
    break
div=1
while n>=10*div:
    div*=10
while n>0:
    if n//div!=n%10:
        print(False)
        break
    n=(n%div)//10
    div=div//100
print(True)