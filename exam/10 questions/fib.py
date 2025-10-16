def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp

fibonacci(10)
print()
a = 1
b =0
for i in range(20):
    print(a,end=' ')
    temp = a+b
    a = b
    b= temp

