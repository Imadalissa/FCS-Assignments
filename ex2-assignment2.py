names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

while True:
    letter = input("Input any letter or 'out' to quit: ").lower()
    
    if letter == "out":
        print("Program terminated.")
        break
    
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue
    
    found = False
    
    for name in names:
        if letter in name.lower():
            print(name)
            found = True
    
    if not found:
        print(f"The letter '{letter}' is not found in any name in the list.")