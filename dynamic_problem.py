# botam up
def fib(position):
    if position <=2:
        return 1
    dp = [0]*position
    dp[0]=1
    dp[1]=1

    for i in range(2,position):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]

print("botam up",fib(5))

# Top down

def Top_fib(n,memory):
    if n in memory:
        return memory[n]
    if n <=2:
        return 1
    memory[n]=Top_fib(n-1,memory)+Top_fib(n-2,memory)

    return memory[n]
print("top down",Top_fib(5,{}))
