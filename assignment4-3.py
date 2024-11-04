def decode_message(message):
    stack = []
    
    # Traverse the message
    for char in message:
        if char.isalpha() or char.isspace():  # Push letters and spaces onto the stack
            stack.append(char)
        elif char == '*' and stack:  # Pop the last character if an asterisk is found and stack is not empty
            stack.pop()
            print(stack.pop())
    
    # Collect remaining characters from the stack and reverse to decode
    decoded_message = ''.join(reversed(stack))
    return decoded_message

# Example usage
input_message = "SIVLE ****** DAED TNSI ***"
print(decode_message(input_message))  # Output: "ELVIS ISNT DEAD"