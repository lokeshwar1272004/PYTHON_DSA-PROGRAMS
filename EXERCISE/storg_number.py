import math
def strong_number(n):
    n=n
    digits = str(n)
    digits_sum =sum(math.factorial(int(i))for i in digits)
    return digits_sum == n

if strong_number(15):
    print(True)
else:
    print(False)

class strong:
    def factorial(self,n):
        a=1
        for i in range(2,n+1):
            a*=i
        return a
    def storng(self,sn):
        sn = sn
        result = 0
        while sn > 0:
            digits = sn % 10
            result+=q.factorial(digits)
            sn = sn//10
        print(result)
q = strong()
q.storng(145)




