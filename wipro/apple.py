import sys

def min_cost_to_buy_apples(N, M1, P1, M2, P2):
    min_cost = sys.maxsize  # Initialize with a large value

    # Try all possible combinations of lot purchases from both shops
    for x in range((N // M1) + 2):  # Max possible lots from shop A
        for y in range((N // M2) + 2):  # Max possible lots from shop B
            total_apples = (x * M1) + (y * M2)
            if total_apples >= N:  # Only consider valid cases
                cost = (x * P1) + (y * P2)
                min_cost = min(min_cost, cost)

    return min_cost

# Input
N = int(input())  # Number of apples needed
M1, P1 = map(int, input().split())  # Shop A: lot size and price
M2, P2 = map(int, input().split())  # Shop B: lot size and price

# Output the minimum cost
print(min_cost_to_buy_apples(N, M1, P1, M2, P2))