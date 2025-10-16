import itertools
data = [1,3]
perm=list(itertools.permutations(data))
for i in perm:
    print(i)

s = '123'
s_perm =list(itertools.permutations(s))
for i in s_perm:
    print(''.join(i))

def permute(data, current_permutation=[]):
    if not data:
        print(current_permutation)
    else:
        for i in range(len(data)):
            # Choose the current element and permute the rest
            new_data = data[:i] + data[i+1:]  # Remove the chosen element
            permute(new_data, current_permutation + [data[i]])  # Recur with remaining elements

# Example usage
data = [1,2,3]

print("..................")


def permute(data, current_permutation=[]):
    if not data:
        return [current_permutation]
    else:
        all_permutations = []
        for i in range(len(data)):
            new_data = data[:i] + data[i+1:]
            all_permutations += permute(new_data, current_permutation + [data[i]])
        return all_permutations
print(permute(data))
# Example usage
#data = [1, 2, 3]
#result = permute(data)
#print(result)
