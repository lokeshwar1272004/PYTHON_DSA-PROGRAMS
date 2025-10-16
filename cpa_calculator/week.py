day = input().lower()
number_day =int(input())
d={"mon":6,"tue":5,"wed":4,"thu":3,"fri":2,"sat":1,"sun":0}

x=d[day]
if number_day<=x:
    print(0)

print(1+(number_day-x)//7)