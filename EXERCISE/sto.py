def factorial(n):
    if n==1:
        return 1
    else:
        fact=1
        for i in range(2,n+1):
            fact*=i
        return fact

def sum_digits(n):
    s=0
    for i in str(n):
        s+=factorial(int(i))
    print(s)
sum_digits(12)