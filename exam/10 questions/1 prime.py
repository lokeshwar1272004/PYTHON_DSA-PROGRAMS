def print_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")
    print()
print_primes(1,10)



def prime(start,end):
    for nums in range(start,end+1):
        if nums>1:
            is_prime = True
            for j in range(2,nums):
                if nums%j==0:
                    is_prime = False
                    break
            if is_prime:
                print(nums,end=' ')

prime(2,50)

