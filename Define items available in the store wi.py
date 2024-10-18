# Define items available in the store with their barcodes, names, and prices
items = {
    "1001": {"name": "Bread", "price": 1.0},
    "1002": {"name": "Milk", "price": 2.5},
    "1003": {"name": "Eggs", "price": 3.0},
    "1004": {"name": "Cheese", "price": 5.0},
    "1005": {"name": "Chocolate", "price": 1.5},
}

# Function to display available items
def display_items():
    print("\n----- Available Items -----")
    for barcode, info in items.items():
        print(f"Barcode: {barcode}, Item: {info['name']}, Price: ${info['price']:.2f}")
    print("--------------------------\n")

# Function to start a new receipt with input validation for "add another item"
def start_receipt():
    receipt = []  # List to store items and quantities for this receipt
    display_items()  # Show available items

    while True:
        barcode = input("Enter item barcode: ")
        if barcode in items:
            quantity = int(input(f"Enter quantity for {items[barcode]['name']}: "))
            receipt.append((items[barcode], quantity))
        else:
            print("Invalid barcode!")

        # Ask if the user wants to add another item with validation
        while True:
            another_item = input("Would you like to add another item? (yes/no): ").lower()
            if another_item == "yes":
                break  # Continue to add another item
            elif another_item == "no":
                print_receipt(receipt)
                return  # Exit the loop and print the receipt
            else:
                print("Please answer with 'yes' or 'no'.")  # Ask again if the answer is unclear

# Function to print the receipt
def print_receipt(receipt):
    print("\n----- Receipt -----")
    total = 0  # Total amount for the receipt

    for item, quantity in receipt:
        cost = item['price'] * quantity
        total += cost
        print(f"{item['name']} (x{quantity}): ${cost:.2f}")

    print(f"Total: ${total:.2f}")
    print("-------------------\n")

# Main POS loop
def pos_system():
    while True:
        new_receipt = input("Would you like to start a new receipt? (yes/no): ").lower()
        if new_receipt == "yes":
            start_receipt()
        elif new_receipt == "no":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Please answer with 'yes' or 'no'.")

# Run the POS system
pos_system()