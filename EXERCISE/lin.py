def smallest_string(S):
    n = len(S)
    result = []
    i = 0

    while i < n:
        if i < n - 1 and S[i] == '1' and S[i + 1] == '0':
            s[i]
            i += 2
        else:
            i += 1

    return ''.join(result)


# Test examples
print(smallest_string("0000111111"))  # Output: "0000111111"
print(smallest_string("1111111"))  # Output: "1111111"
print(smallest_string("110"))  # Output: "0"