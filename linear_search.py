l = []

for i in range(7):
    List = int(input("enter list of element: "))
    l.append(List)
n = int(input("enter what number you want: "))

def search(l,n):
    for j in range(len(l)):
        if l[j] == n:
            print("index of you searched number >>>>>>>:",j)
            return ("Find")
            break

    return ("Not find")


print(search(l,n))
print(l)




