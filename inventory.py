##############################################################################80
# This code implements an inventory management system for shoes.
# The code includes a class definition for Shoe and several functions to manage 
# the inventory.  
# Task for M03T07 - OOP - Synthesis      # Derek Smith 14 April - Re-submission
##############################################################################80

import re
import os

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        '''
        Initialise the following attributes:
        country, code, product, cost, and quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Return a string representation of the shoe."""
        return (f"{self.country} | {self.code} | {self.product} | "
                f"Cost: {self.cost} | Qty: {self.quantity}")


##############################################################################80
# This list will store Shoe objects.
shoes_list = []


def read_shoes_data():
    '''
    Read data from inventory.txt, create Shoe objects,
    and append them to shoes_list.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip header line
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    shoe = Shoe(*parts)
                    shoes_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt not found. Ensure the file is in the directory.")
    except Exception as e:
        print("Unexpected error:", e)


##############################################################################80
def capture_shoes():
    """Capture new shoe details and append to shoes_list."""
    print("\nEnter new shoe details:")
    country = input("Country: ")

    # Validate SKU format
    while True:
        code = input("Code (format: SKU12345): ")
        if re.fullmatch(r"SKU\d{5}", code):
            break
        print("Invalid code. Must be 'SKU' followed by 5 digits.")

    product = input("Product: ")

    # Validate cost
    while True:
        cost = input("Cost: ")
        if cost.isdigit():
            break
        print("Cost must be a number.")

    # Validate quantity
    while True:
        quantity = input("Quantity: ")
        if quantity.isdigit():
            break
        print("Quantity must be a number.")

    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print("Shoe added successfully.")


##############################################################################80
def view_all():
    """Print all shoes in the inventory."""
    print("\n------------------ ALL SHOES ------------------")
    for shoe in shoes_list:
        print(shoe)


##############################################################################80
def re_stock():
    """Find the shoe with the lowest quantity and restock it."""
    if not shoes_list:
        print("No shoes loaded.")
        return

    lowest = min(shoes_list, key=lambda s: s.quantity)
    print("\nLowest stock item:")
    print(lowest)

    choice = input("Restock this item? (yes/no): ").lower()
    if choice == "yes":
        add_qty = int(input("Add how many? "))
        lowest.quantity += add_qty
        update_file()
        print("Stock updated successfully.")


##############################################################################80
def search_shoe():
    """Search for a shoe by code and print it."""
    code = input("Enter shoe code to search: ").strip().upper()

    for shoe in shoes_list:
        if shoe.code.upper() == code:
            print("\nShoe found:")
            print(shoe)
            return

    print("Shoe not found.")


##############################################################################80
def value_per_item():
    """Calculate and print total value per shoe item."""
    print("\n------------------ VALUE PER ITEM ------------------")
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}) - Value: R{value}")


##############################################################################80
def highest_qty():
    """Find and print the shoe with the highest quantity."""
    if not shoes_list:
        print("No shoes loaded.")
        return

    highest = max(shoes_list, key=lambda s: s.quantity)
    print("\n*** FOR SALE ***")
    print(highest)


##############################################################################80
def update_file():
    """Write updated shoe data back to inventory.txt."""
    with open("inventory.txt", "w") as file:
        file.write("country,code,product,cost,quantity\n")
        for shoe in shoes_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},"
                       f"{shoe.cost},{shoe.quantity}\n")


##############################################################################80
# Main Menu
def menu():
    read_shoes_data()

    while True:
        print("\n================= SHOE INVENTORY MENU =================")
        print("1 - View all shoes")
        print("2 - Add new shoe")
        print("3 - Restock lowest quantity")
        print("4 - Search shoe by code")
        print("5 - View value per item")
        print("6 - Show highest quantity (for sale)")
        print("7 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
menu()
