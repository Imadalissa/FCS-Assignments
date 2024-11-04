def generate_combinations(characters, n, combination=""):
    # Base case: if the length of the combination is n, print it
    if len(combination) == n:
        print(combination)
        return

    # Recursive case: append each character and recursively build the combinations
    for char in characters:
        generate_combinations(characters, n, combination + char)

# Example usage:
characters = ['a', 'b', 'c']
n = 5
generate_combinations(characters, n)