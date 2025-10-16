def leaf(year):
    return (year % 4==0 and year % 100!=0) or (year % 400 == 0)

"""if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False
print(leaf(2004)) """
print(leaf(2000))