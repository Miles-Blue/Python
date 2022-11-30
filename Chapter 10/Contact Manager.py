import pickle
import contact

def main():
    my_contacts = load_contacts()
    
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
    print("\nHere are your choices:")
    print("1) Look up a Contact")
    print("2) Add a Contact")
    print("3) Change a contact")
    print("4) Delete a Contact")
    print("5) Exit and Save Contacts to a file")
    
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
    
    while True:
        name_found = True
        
        search = input("\nEnter a contact you'd like to search for: ")
        
        for item in mycontacts:
            if item.get_name() == search:
                search = item
                pass
            
            if mycontacts.index(item) == -1:
                print("Name not found.")
                name_found = False
        
        if name_found:
            print(f"Name: {search.get_name()}")
            print(f"Phone Number: {search.get_phone()}")
            print(f"Email: {search.get_email()}")
        
        if input("\nWould you like to continue? (y/n) ").lower() == 'y':
            continue
        else:
            break
            
def add(mycontacts):
    user_name = input("\nEnter a name: ")
    user_phone = input("Enter a phone number: ")
    user_email = input("Enter an email: ")

    info = contact.Contact(user_name, user_phone, user_email)
    
    mycontacts.append(info)

def change(mycontacts):
    
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
    
    file = open('contact.dat', 'wb')
    
    for item in mycontacts:
        pickle.dump(item, file)
    
    file.close()
    
    print("\nThank you for using our program!")