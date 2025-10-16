def gcd(a,b):
    while b:
        a,b= b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
print(gcd(10,5))
print(lcm(12,7))

