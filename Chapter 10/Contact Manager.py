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

def load_contacts():
    
    file = open('contact.dat', 'wb')
    info = contact.Contact('miles', '316-680-8531', 'milesblue0@gmail.com')
    pickle.dump(info, file)
    file.close()
    
    file = open('contact.dat', 'rb')
    
    while True:
        try:
            con = pickle.load(file)
            
        except EOFError:
            break
        
        except Exception as err:
            print(err)
            break
    
    file.close()
    print(con)
    
    return con

def get_menu_choice():
    print("\nHere are your choices:")
    print("1) Look up a Contact")
    print("2) Add a Contact")
    print("3) Change a contact")
    print("4) Delete a Contact")
    print("5) Exit and Save Contacts to a file")
    
    choice = input(":: ")
    while not choice.isnumeric() and 1 <= choice <= 5:
        choice = input("Choice: ")
    
    return choice

def look_up(mycontacts):
    
    while True:
        search = input("\nEnter a contact you'd like to search for: ")
        
        if not search in mycontacts:
            print("\nName not found.")
            continue
        
        print(f"Name: {search}")
        print(f"Phone Number: {mycontacts[search][0]}")
        print(f"Email: {mycontacts[search][1]}")
        
        if input("Would you like to continue? (y/n) ").lower() == 'y':
            continue
        else:
            break
            
def add(mycontacts):
    user_name = input("Enter a name: ")
    user_phone = input("Enter a phone number: ")
    user_email = input("Enter an email: ")
    
    info = contact.Contact(user_name, user_phone, user_email)
    
    pickle.dump(info, file)

def change(mycontacts):
    pass

def delete(mycontacts):
    pass

def save_contacts(mycontacts):
    pass