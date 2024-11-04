def is_balanced(expression):
    stack = []
    # Mapping of closing to opening parentheses
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in matching_parentheses.values():  # Opening parenthesis
            stack.append(char)
        elif char in matching_parentheses.keys():  # Closing parenthesis
            if stack == [] or stack.pop() != matching_parentheses[char]:
                return False
    
    # If stack is empty, all parentheses were matched
    return stack == []

# Example usage
print(is_balanced("(1+2)-3*[41+6]"))  # Output: True
print(is_balanced("(1+2)-3*[41+6}"))  # Output: False
print(is_balanced("(1+2)-3*[41+6"))   # Output: False
print(is_balanced("(1+2)-3*]41+6["))  # Output: False
print(is_balanced("(1+[2-3]*4{41+6})"))  # Output: True