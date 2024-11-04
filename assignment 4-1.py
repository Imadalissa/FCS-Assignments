def is_palindrome(s):
    # Normalize the string by converting it to lowercase and removing non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    stack = []
    queue = []
    
    # Push and enqueue each character
    for char in s:
        stack.append(char)  # Push onto stack (last in, first out)
        queue.append(char)  # Enqueue to queue (first in, first out)
    
    # Compare elements from stack and queue
    while stack:
        if stack.pop() != queue.pop(0):  # Pop from stack and dequeue from queue
            return False
            
    return True

# Example usage
print(is_palindrome("mom"))            
print(is_palindrome("Neveroddoreven")) 
print(is_palindrome("hello"))    
print(is_palindrome("pap"))         