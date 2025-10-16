def get_permutations(s):
    if len(s) == 0:

        return ['']

    # Recursive case
    result = []
    for i in range(len(s)):
        current_char = s[i]
        remaining_chars = s[:i] + s[i + 1:]
        for p in get_permutations(remaining_chars):
            result.append(current_char + p)

    return result


print(get_permutations("ab"))
