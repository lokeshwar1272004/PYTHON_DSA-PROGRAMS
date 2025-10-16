def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse*10 + digit
        n //= 10
    return original == reverse
print(is_palindrome(55))


def is_pali(n):
    everse = 0
    o = n
    while n > 0:
        d = n%10
        everse = everse *10+d
        n//=10
    return o == everse
print(is_pali(44))