# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# AFolmer, 6.8.2023,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Import pickle functionality
import pickle


# Data -------------------------------------------------------------------- #
class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name, 1 - 50 characters

        product_price: (float) with the product's standard price, minimum value $0.01
    methods:
        __init__(self, name, price): creates a new object in class Product

        __repr__(self): creates a string representing the object

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AFolmer, 6.7.2023,Modified code to complete assignment 8
    """

    def __init__(self, name, price):
        """Creates a new object in the class Product
        :param name: name of the product - string
        :param price: product price - two decimal place float"""
        self.name = name
        self.price = price

    def __repr__(self):
        """ Creates a string representing the object
        :return: string representing object"""
        return f'{self.name} ${self.price:.2f}'

# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items(): print list of menu choices

        input_menu_choice(upper): captures user menu choice and checks for valid value

        print_list_of_products(): print list of products and prices

        enter_product_name(): validate that user entered name meets object conventions

        enter_product_price(): validate that user entered price meets object conventions

        product_in_list(product_name): check to see if product name has already been used and returns index ID in list

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Edit item price
        4) Remove an item
        5) Save Data to File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    @staticmethod
    def input_menu_choice(upper):
        """ Captures and validates user entered menu choice
        :param upper: the highest menu option
        :return menu_choice: user's menu choice"""
        while True:
            # Try/except tree to ensure user enters an integer
            try:
                menu_choice = int(input("What would you like to do? "))
            except ValueError:
                print("Choice must be an integer between 1 and " + str(upper))
            except:
                print("Unknown error.")
            # If/else tree to ensure user enters a value in menu choice range
            else:
                if 0 < menu_choice <= upper:
                    break
                else:
                    print("Choice must be an integer between 1 and " + str(upper))
        return menu_choice

    @staticmethod
    def print_list_of_products():
        for obj in lstOfProductObjects:
            print((repr(obj)))

    @staticmethod
    def enter_product_name():
        """ Captures user entered product name and validates for object conventions
        :return product_name: string with up to 50 characters"""
        # While loop executes until valid name is entered
        while True:
            # Try/except to ensure user enters a string
            try:
                product_name = input("Enter new product name: ")
                product_name = product_name.lower()
            except ValueError:
                print("Name must be a string.")
            except:
                print("Invalid entry.")
            # Check that product meets field conventions
            else:
                in_inventory = 0
                obj_index = 0
                in_inventory, obj_index = IO.product_in_inventory(product_name)
                if in_inventory == 1:
                    print("Product already in inventory.Index number: " + str(obj_index))
                elif str(product_name).isnumeric():
                    print("Product name cannot be a number.")
                # Check to ensure string is less than 50 characters
                elif 0 < len(product_name) <= 50:
                    break
                else:
                    print("Product name must be between 1 - 50 characters.")
        return product_name


    @staticmethod
    def enter_product_price():
        """ Captures user entered price and validates for object conventions
        :return product_price: number greater than zero saved as a 2d float"""
        while True:
            # Try/except to check that user inputs a number and then rounds to two decimal places
            try:
                product_price = float(input("How much is your product? $"))
                product_price = round(product_price, 2)
            except ValueError:
                print("Price must be a number with up to two decimals.")
            except:
                print("Invalid entry.")
            # Check to ensure that price is over minimum value of $0.01
            else:
                if 0.00 < product_price:
                    break
                else:
                    print("Price must be at least $0.01")
        return product_price

    @staticmethod
    def product_in_inventory(product_name):
        in_inventory = 0
        obj_index = 0
        for obj in lstOfProductObjects:
            if obj.name == product_name.lower():
                in_inventory = 1
                break
            else:
                obj_index += 1
        return in_inventory, obj_index


# Main body of script -------------------------------------------------------------------------#

IO.print_menu_items()

# Try/except to unpickle list of products or create the list if the file doesn't exist
try:
    f = open("product_inventory.dat", "rb")
    lstOfProductObjects = pickle.load(f)
    f.close()
except:
    lstOfProductObjects = []

# Check to see if there are any products in list
if len(lstOfProductObjects) == 0:
    print("Your list of products is empty.")

# While loop to execute user choices from menu
while True:
    print("Enter 7 to see the main menu.")
    # Function to capture user menu choice, limited to 1 - 5
    menu_choice = IO.input_menu_choice(7)
    if menu_choice == 1:
        if len(lstOfProductObjects) == 0:
            print("Your list of products is empty.")
        else:
            IO.print_list_of_products()
    # Create new product object
    elif menu_choice == 2:
        # Capture user entered name as string, len 1 - 50, not a duplicate
        product_name = IO.enter_product_name()
        # Capture user entered price as 2d float greater than $0.01
        product_price = IO.enter_product_price()
        # Create product object and append to list
        lstOfProductObjects.append(Product(product_name, product_price))
    # Update product object price
    elif menu_choice == 3:
        # User inputs product name
        try:
            product_name = input("Which product would you like to update? ").lower()
        except:
            print("Invalid entry.")
        # If product in inventory, update price
        else:
            in_inventory, obj_index = IO.product_in_inventory(product_name)
            if in_inventory == 1:
                lstOfProductObjects[obj_index].price = IO.enter_product_price()
                print(repr(lstOfProductObjects[obj_index]))
            # Notify user if product not found
            else:
                print("Item not found.")
    # Remove a product from the inventory
    elif menu_choice == 4:
        # User inputs item to remove
        try:
            product_name = input("Which product would you like to remove? ").lower()
        except:
            print("Invalid entry.")
        else:
            # Remove item or notify use item not found
            in_inventory, obj_index = IO.product_in_inventory(product_name)
            if in_inventory == 1:
                lstOfProductObjects.pop(obj_index)
                print(product_name.capitalize() + "removed from inventory.")
            else:
                print("Item not found.")
    # Save updates to inventory
    elif menu_choice == 5:
        try:
            f = open("product_inventory.dat", "wb")
            # Save product inventory list to pickle file
            pickle.dump(lstOfProductObjects, f)
            # Close pickle file
            f.close()
            print("Inventory saved.")
        except:
            print("Error, inventory not saved.")
    elif menu_choice == 6:
        print("Goodbye.")
        break
    else:
        IO.print_menu_items()

