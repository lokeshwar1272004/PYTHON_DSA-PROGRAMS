
def nnI():
    element = '112211'
    print(element[::-1])
    l = 0
    r = len(element) - 1
    while l < r:
        for i in range(len(element)):
            if element[l] == element[r]:
                l += 1
                r -= 1
            else:
                return ("not")

        return ("its a pali")
print(nnI())

