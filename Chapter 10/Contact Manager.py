import pickle
import contact

def main():
    #accepts no arguments
    #calls to load the contacts
    #then calls to get the menu choice
    #and calls each program accordingly
    
    
    my_contacts = load_contacts()
    
    #Loops through the menu and choices until user exits
    while True:
        choice = get_menu_choice()
        
        if choice == '1':
            look_up(my_contacts)
        elif choice == '2':
            add(my_contacts)
        elif choice == '3':
            change(my_contacts)
        elif choice == '4':
            delete(my_contacts)
        elif choice == '5':
            save_contacts(my_contacts)
            break

def load_contacts():
    #accepts no arguments
    #opens contact.dat and reads from it
    #loads each data set into sections of a list
    #returns the list as contact list
    
    contact_list = []
    
    file = open('contact.dat', 'rb')
    
    while True:
        try:
            con = pickle.load(file)
            
            contact_list.append(con)
            
        except EOFError:
            break
        
        except Exception as err:
            print(err)
            break
    
    file.close()
    
    return contact_list

def get_menu_choice():
    #accepts no arguments
    #outputs a formatted menu and prompts user for menu choice
    #returns the user's choice
    
    print("\nHere are your choices:")
    print("1) Look up a Contact")
    print("2) Add a Contact")
    print("3) Change a contact")
    print("4) Delete a Contact")
    print("5) Exit and Save Contacts to a file")
    
    #Validates user input
    while True:
        choice = input(":: ")
        
        if not choice.isnumeric():
            print("\nHas to be a number.\n")
            continue
        
        if not 1 <= int(choice) <= 5:
            print("\nHas to be between 1 and 5.\n")
            continue
        
        else:
            break
    
    return choice

def look_up(mycontacts):
    #accepts mycontacts as an argument
    #prompts user for a name to search for
    #cycles through the list using get_name for each one
    #to determine if contact has been found
    #then displays contact info
    
    while True:
        
        #Sets a boolean
        name_found = True
        
        #User input
        search = input("\nEnter a contact you'd like to search for: ")
        
        #Cycles through mycontacts list
        for item in mycontacts:
            
            #Determines if the user search matches the name
            if item.get_name() == search:
                search = item
                pass
            
            #If it reaches the end of the list without finding the contact, name wasn't found
            if mycontacts.index(item) == -1:
                print("Name not found.")
                name_found = False
        
        #If the name was found, then output its data
        if name_found:
            print(f"Name: {search.get_name()}")
            print(f"Phone Number: {search.get_phone()}")
            print(f"Email: {search.get_email()}")
        
        #Prompts user to continue or not
        if input("\nWould you like to continue? (y/n) ").lower() == 'y':
            continue
        else:
            break
            
def add(mycontacts):
    #accepts mycontacts as an argument
    #prompts user for contact name and info
    #turns it into a class object
    #adds that class object to the list
    
    user_name = input("\nEnter a name: ")
    user_phone = input("Enter a phone number: ")
    user_email = input("Enter an email: ")

    info = contact.Contact(user_name, user_phone, user_email)
    
    mycontacts.append(info)

def change(mycontacts):
    #accepts mycontacts as a list
    #searches for an item similar to the look_up function
    #then prompts user for new contact info
    
    while True:
        name_found = True
        
        search = input("\nEnter a contact you'd like to change: ")
        
        for item in mycontacts:
            if item.get_name() == search:
                pass
            
            if mycontacts.index(item) == -1:
                print("Name not found.")
                name_found = False
        
        if name_found:
            phone = input("New Phone Number: ")
            item.set_phone(phone)
            
            email = input("New Email: ")
            item.set_email(email)
            
            print(f"{item.get_name()}'s info has been updated.")
            
            break

def delete(mycontacts):
    #accepts mycontacts as an argument
    #searches for an item similar to the look_up function
    #if it finds the contact, it deletes it
    
    while True:
        name_found = True
        
        search = input("\nEnter a contact you'd like to delete: ")
        
        for item in mycontacts:
            if item.get_name() == search:
                search = item
                pass
            
            if mycontacts.index(item) == -1:
                print("Name not found.")
                name_found = False
        
        if name_found:
            mycontacts.remove(search)
            
            print("Name successfully removed.")
            
            break

def save_contacts(mycontacts):
    #accepts mycontacts as an argument
    #opens contact.dat and writes each class object
    #of the list to the file by using pickle
    #then outputs a final message
    
    file = open('contact.dat', 'wb')
    
    for item in mycontacts:
        pickle.dump(item, file)
    
    file.close()
    
    print("\nThank you for using our program!")