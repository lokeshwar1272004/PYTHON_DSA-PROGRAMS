def minimize_string(S):
    while "10" in S:
        S = S.replace("10", "0", 1)  # replace "10" with "0" (removing '1') once at a time
    return S

# Test cases
print(minimize_string("0000111111"))  # Expected output: "0000111111"
print(minimize_string("1111111"))     # Expected output: "1111111"
print(minimize_string("110"))         # Expected output: "0"
