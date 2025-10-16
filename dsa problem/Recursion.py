#find the sum all the number
def sum_of_all_number(n):
    if n == 1:
        return 1
    else:
        return n+sum_of_all_number(n-1)
n = int(input("sum of all number:"))
print("sum all number",sum_of_all_number(n))
print(""".............fib....................................""")
f=int(input('enter any number:'))
def fib(f):
    if f == 0 or f ==1:
        return 1
    else:
        return fib(f-1)+fib(f-2)
print(fib(f))
