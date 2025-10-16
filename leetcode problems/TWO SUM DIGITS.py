def two_sum(numbers,target):
    dictonery = {}
    for i in range(len(numbers)):
        values = numbers[i]
        difference = target - values
        if values not in dictonery:
            dictonery[difference]=i
        else:
            return [dictonery[values],i]



print(two_sum([2,7,11,15],9))