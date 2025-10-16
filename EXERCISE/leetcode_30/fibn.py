def perfect_square(n):
    sq = 0
    while sq * sq <=n:
        if sq*sq==n:
            return True
        sq+=1
    return False

def fibbonic(number):
    condition = 5*number*number+4
    condition_1 = 5*number*number-4

    return perfect_square(condition) or perfect_square(condition_1)

if fibbonic(8):
    print("is a fibn")
else:
    print("not")




