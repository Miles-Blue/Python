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
        print("Welcome to the ACME Retail System!")
        print("Choose from the following options:")
        print("1) Inventory System")
        print("2) Retail System")
        print("3) Exit")
        
        #Calls get_choice
        choice = get_choice()
        
        #Calls programs according to user choice
        if choice == 1:
            while True:
                if input("Enter a password to continue: ") == 'milkshake':
                    inventory_menu()
                    break
                else:
                    print("Wrong password.")
                    
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
    
    inventory_dict = {}
    
    while True:
        try:
            line = pickle.load(open('inventory.dat', 'rb'))
            
            inventory_dict[line.get_item()] = line
        
        except EOFError:
            break
        
        except FileNotFoundError:
            print("File does not exist, creating...")
            file = open('inventory.dat', 'xb')
        
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
            display_inventory(inventory_dict)
        
        elif choice == 2:
            add_inventory(inventory_dict)
        
        elif choice == 3:
            change_inventory(inventory_dict)
        
        elif choice == 4:
            save_inventory(inventory_dict)
        
        elif choice == 5:
            file.close()
            break
        
        else:
            print("Choice must be within the range of 1-5.")
        
def display_inventory(inventory):
    #accepts inventory as an argument
    #outputs each item in inventory
    #if the inventory is empty, then it outputs
    #a message accordingly
    
    if len(inventory) == 0:
        print("There are no items in the inventory yet.")
    
    else:
        for item in inventory:
            print(item)
            print()

def add_inventory(inventory):
    #accepts inventory as an argument
    #prompts user for an item
    #then adds that item and its class item
    #to the inventory dictionary
    
    item = input("Enter an item name: ")
    
    while True:
        try:
            units = int(input("Enter number of units: "))
            
            price = float(input("Enter cost per unit: "))
            
            break
        
        except:
            print("Units and Price must be numbers.")
            
    info = RetailItem.Retail(item, units, price)
    
    inventory[info.get_item()] = info

def change_inventory(inventory):
    #accepts inventory as an argument
    #prompts user to search for an item
    #then prompts user for new info for said item
    
    pass

def save_inventory(inventory):
    #accepts inventory as an argument
    #goes through each item in inventory
    #and saves it to inventory.dat
    
    pass

#-------------------------------------------------------------------------#




































