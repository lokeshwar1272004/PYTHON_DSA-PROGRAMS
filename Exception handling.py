
try:
    a = int(input())
    b = (input())
    print(a//b)
except ZeroDivisionError as e:
    print("its zero division error",e)
except ValueError as e:
    print("are you mad its integer ",e)
except Exception as e:
    print("some thing wrong ",e)
finally:
    print("close")
