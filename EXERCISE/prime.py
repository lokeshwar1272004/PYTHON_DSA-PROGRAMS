def prime(n):
    for i in range(2,n):
        if i<2:
            return False

        if n%i==0:
            return False
    return True


def numbers(a):
    element = []
    for j in range(2,a+1):
        if prime(j):
            element.append(j)
    return element

print(numbers(10))


