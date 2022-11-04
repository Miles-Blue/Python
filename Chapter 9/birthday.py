#CONTINUE LATER

#Global constants for menu choices
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def birthday_main():
    
    #Create the empty dictionary
    birthdays = {}
    choice = bday_choice()
    

def get_menu_choice():

    print()
    print("Friends and their birthdays")
    print("---------------------------")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quit")
    choice = int("Option: ")
    
    if choice == 1:
        look_up()
    
def look_up(birthdays):

def add_bday(birthdays):
    
    name = input("Enter a name: ")
    
    if name not in birthdays:
        bday = input("Enter a birthday: ")
        birthdays[name] = bday
    
def delete_bday(birthday):
    
    name = input("Enter a name to delete: ")