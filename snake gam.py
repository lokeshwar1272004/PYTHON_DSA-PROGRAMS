def infinite_numbers():
    n = 1
    while True:
        yield n
        n += 1

gen = infinite_numbers()

# This will generate numbers indefinitely (or until you stop it)
print(next(gen))  # Outputs: 1
print(next(gen))  # Outputs: 2
print(next(gen))
print(next(gen))
