import RetailItem
import CashRegister
import pickle

#-------------------------------------------------------------------------#

def main_menu():
    #accepts no arguements
    #outputs a main menu to give users a choice
    #between the Inventory System or the Retail System
    #then calls each program accordingly
    
    #Continues the program while the user wants to
    while True:
        
        #Ouputs a formatted menu
        print("\nWelcome to the ACME Retail System!")
        print("Choose from the following options:")
        print("1) Inventory System")
        print("2) Retail System")
        print("3) Exit")
        
        #Calls get_choice
        choice = get_choice()
        
        #Calls programs according to user choice
        if choice == 1:
            while True:
                if input("\nEnter a password to continue: ") == 'milkshake':
                    inventory_menu()
                    break
                else:
                    print("\nWrong password.\n")
                    
        elif choice == 2:
            retail_menu()
            
        elif choice == 3:
            print("Thank you for using ACME Retail System!")
            break
        
        else:
            print("Choice must be within the range of 1-3.")

def get_choice():
    #accepts no arguments
    #prompts user for a numbered choice
    #validates the input
    #returns their choice
    
    while True:
        choice = input("\nChoice: ")
        
        try:
            int(choice)
            break
        
        except:
            print("ERROR: Choice must be a number.")
            continue
    
    return int(choice)

#-------------------------------------------------------------------------#

def inventory_menu():
    #accepts no arguments
    #outputs a formatted menu
    #calls a program according to user choice
    
    inventory_list = []
    
    try:
        inventory_list = (pickle.load(open('inventory.dat', 'rb')))
    
    except FileNotFoundError:
        print("File does not exist, creating...")
        file = open('inventory.dat', 'xb')
        inventory_list = []
    
    except Exception as err:
        print(err)
        
    while True:
        print("\n1)Display Inventory")
        print("2)Add to the Inventory")
        print("3)Change an Item's Info")
        print("4)Save Inventory to a file")
        print("5)Exit")
        
        choice = get_choice()
        
        if choice == 1:
            display_inventory(inventory_list)
        
        elif choice == 2:
            add_inventory(inventory_list)
        
        elif choice == 3:
            change_inventory(inventory_list)
        
        elif choice == 4:
            save_inventory(inventory_list)
        
        elif choice == 5:
            try:
                file.close()
                print("\nExiting Inventory...\n")
            except:
                print("\nExiting Inventory...\n")
                
            break
        
        else:
            print("Choice must be within the range of 1-5.")
        
def display_inventory(inventory):
    #accepts inventory as an argument
    #outputs each item in inventory
    #if the inventory is empty, then it outputs
    #a message accordingly
    
    if len(inventory) == 0:
        print("\nThere are no items in the inventory yet.")
    
    else:
        for item in inventory:
            print()
            print(item)

def add_inventory(inventory):
    #accepts inventory as an argument
    #prompts user for an item
    #then adds that item and its class item
    #to the inventory dictionary
    
    while True:
        
        item = input("\nEnter an item name: ")
        
        while True:
            try:
                units = int(input("Enter number of units: "))
                
                price = float(input("Enter cost per unit: "))
                
                break
            
            except:
                print("Units and Price must be numbers.")
                
        info = RetailItem.Retail(item, units, price)
        
        inventory.append(info)
        
        if input("\nContinue? (y/n) ").lower() == 'y':
            continue
        else:
            break

def change_inventory(inventory):
    #accepts inventory as an argument
    #prompts user to search for an item
    #then prompts user for new info for said item
    
    while True:
        
        search = input("\nEnter desired Item: ")
        
        for item in inventory:
            if item.get_item() == search:
                item_found = True
                
                index = inventory.index(item)
            
        if item_found:
            while True:
                try:
                    units = int(input("Enter number of units: "))
                    
                    price = float(input("Enter cost per unit: "))
                    
                    break
                
                except:
                    print("Units and Price must be numbers.")
                    
            inventory[index].set_units(units)
            inventory[index].set_price(price)
            
            print(f"\nSuccessfully changed {search}.\n")
            
        else:
            print("\nItem not found.\n")
        
        if input("\nContinue? (y/n) ").lower() == 'y':
            continue
        else:
            break
        

def save_inventory(inventory):
    #accepts inventory as an argument
    #goes through each item in inventory
    #and saves it to inventory.dat
    
    file = open('inventory.dat', 'wb')
    
    pickle.dump(inventory, file)
    
    file.close()
    
    print("All info has been saved.")

#-------------------------------------------------------------------------#

def retail_menu():
    #accepts no arguments
    #opens inventory.dat and adds all the info to a dictionary
    #then displays a formatted menu to then prompt user
    #for their choice, and calls programs accordingly
    
    inventory_list = []
    
    cart = CashRegister.Register()
    
    try:
        
        inventory_list = pickle.load(open('inventory.dat', 'rb'))
        
        file_found = True
    
    except EOFError:
        print("There are no items in the inventory.")
        
        file_found = False
    
    except FileNotFoundError:
        print("File does not exist, therefore there is no inventory.")
        file_found = False
    
    except Exception as err:
        print(err)
        
    while file_found:
        print("\n1)Display Inventory")
        print("2)Display Cart")
        print("3)Add to Cart")
        print("4)Check Out")
        print("5)Exit and Empty Cart")

        choice = get_choice()
        
        if choice == 1:
            display_inventory(inventory_list)
        
        elif choice == 2:
            
            if not cart.show_cart():
                print("\nThere is nothing in your cart yet.")
            else:
                cart.show_cart()
                cart.get_total()
        
        elif choice == 3:
            add_cart(cart, inventory_list)
        
        elif choice == 4:
            check_out(cart, inventory_list)
        
        elif choice == 5:
            cart.empty()
            break
        
        else:
            print("Choice must be between 1 and 5.")

def add_cart(cart, inventory):
    #accepts inventory and cart as arguments
    #prompts user to search for an item in the inventory
    #and adds said item to the cart
    
    while True:
        search = input("\nEnter desired item: ")
        
        for item in inventory:
            if item.get_item() == search:
                new_item = RetailItem.Retail(item.get_item(), item.get_units(), item.get_price())
                new_item.set_units(1)
                cart.purchase_item(new_item)
                
                break
            
            if inventory.index(item) == -1:
                print("Item not found.")
                break
        
        if input("\nContinue? (y/n) ").lower() == 'y':
            continue
        else:
            break

def check_out(cart, inventory):
    #accepts cart and inventory as arguments
    #displays user cart and total
    #then prompts for further continuation
    #then empties the cart while removing contents from the database
    
    while True:
        if not cart.show_cart():
            print("There is nothing in your cart.")
            break
        
        if input("Continue to checkout? (y/n) ").lower() == 'y':
            pass
        else:
            break
        
        cart.show_cart()
        cart.get_total()
        
        for purchase in cart.return_list():
            for item in inventory:
                if purchase.get_item() == item.get_item():
                    index = inventory.index(item)
                    inventory[index].subtract_units(purchase.get_units())
        
        file = open('inventory.dat', 'wb')
        
        pickle.dump(inventory, file)
        
        file.close()
        
        print("Items have been successfully purchased!")
        
        break