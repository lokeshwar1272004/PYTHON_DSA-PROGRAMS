import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


"""def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


def print_spiral(matrix):
    result = []
    n = len(matrix)
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    print(*result)"""


# Input and Execution


if __name__=="__main__":
    """n = int(input("Enter a prime number: "))
    if is_prime(n):
        matrix = generate_spiral_matrix(n)
        print_spiral(matrix)
    else:
        print("Please enter a prime number.")"""

    print(is_prime(5))
