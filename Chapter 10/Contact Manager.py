def main():
    dct = load_contacts
    
    choice = get_menu_choice()

def load_contacts():
    
    contact.dct = {}
    
    file = open('contacts.dat', 'rb')
    
    while True:
        try:
            con = pickle.load(file)
            
            contact_dct[con.get_name()] = con
            
        except EOFError:
            break
        
        except Exception as err:
            print(err)
            break
        
    return contact_dct

    file.close()

def get_menu_choice():
    print("Here are your choices:")
    print("1) Look up a Contact")
    print("2) Add a Contact")
    print("3) Change a contact")
    print("4) Delete a Contact")
    print("5) Exit and Save Contacts to a file")
    
    while not choice.isnumeric() and 1 <= choice <= 5:
        choice = input("Choice: ")
    
    return choice

def look_up(mycontacts):
    pass

def add(mycontacts):
    pass

def change(mycontacts):
    pass

def delete(mycontacts):
    pass

def save_contacts(mycontacts):
    pass