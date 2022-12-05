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
        
#def inventory_menu():
    






































