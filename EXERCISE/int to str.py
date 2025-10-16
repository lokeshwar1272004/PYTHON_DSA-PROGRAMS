def str_int(num):
    if num == 0:
        return '0'
    result=[]
    while num >0:
        digits = num%10
        result.append(chr(ord('0')+digits))
        num //=10
    result.reverse()
    return [''.join(result)]

print(str_int(127))



