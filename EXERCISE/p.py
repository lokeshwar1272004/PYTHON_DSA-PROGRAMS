def min_string_after_operations(S):
    # Initialize an empty stack to keep track of characters
    stack = []

    # Iterate through each character in S
    for char in S:
        # While stack is not empty and top of stack is '1' and current character is '0'
        while stack and stack[-1] == '1' and char == '0':
            # Pop the top element from the stack (effectively removing '10')
            stack.pop()

            # Push the current character onto the stack
        stack.append(char)

    # Convert the stack back to a string
    return ''.join(stack)


# Sample Inputs
print(min_string_after_operations("0000111111"))  # Expected Output: 0000111111
print(min_string_after_operations("1111111"))  # Expected Output: 1111111
print(min_string_after_operations("110"))  # Expected Output: 0