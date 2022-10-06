def IsValid(string):
    if string.isnumeric():
        return True
    else:
        return False
    
def sales_list():
    #accepts no arguments
    #creates a list NUM_DAYS long
    #and loops to accept input from the user
    #adding that input to the list
    
    NUM_DAYS = 5
    lst = []
    
    print("Enter the sales for each day.")
    for day in range(1, NUM_DAYS+1):
        sales = float(input(f"Day #{day}:"))
        lst.append(sales)
    print("Here are the values you entered:")
    for sale in lst:
        print(sale)
        
def in_list():
    #accepts no arguments
    #it creates alist of part numbers
    #V45, V65, VF750, VFR 110, VTX1300
    #and prompts the user for a string to search for
    #and prints if the list contains the string
    
    parts = ['V45', 'V65', 'VF750', 'VFR1110', 'VTX1300']
    
    search = input("Enter a string to search for: ")
    
    if search in parts:
        print("You found it!")
    else:
        print("You didn't find it.")
    
def list_append():
    #accepts no arguments
    #creates an empty list
    #and loops to eppend the list with input from the user
    #then prompts to continue
    
    name_list = []
    cont = 'y'
    
    while cont.lower() != 'n':
        name = input("Enter a name:")
        name_list.append(name)
        cont = input("Add another name? (y to continue)")
        print()
        
    print("You enters teh following names:")
    for name in name_list:
        print(name)
    
def list_index():
    #accepts on arguments
    #creates a list of three food items
    #and prompts the user to replace one of the items
    #it searches the list for the index of the item
    #and prompts the user with replacement food
    
    foods = ['Burger', 'Pizza', 'Hotdog']
    
    search = input("Enter the string to search for: ")
    
    try:
        if foods.index(search) >= 0:
            index = foods.index(search)
            replace = input("Item found. Enter a new food item: ")
            foods[index] = replace
        print(f"\nHere is the list:{foods}")
    except Exception as err:
        print()
        print(err)
    
def list_insert():
    #accepts no arguments
    #prints the original list of three neames
    #inserts a name in a list of names
    #at a specific indext and prints the new list
    
    lst = ['Bruce', 'Steve', 'Tony']
    
    print("Here is the list before the insert method:", lst)
    
    lst.insert(2, 'Sam')
   
    print("Here is the list after the insert method:", lst)
    
def list_remove():
    #accepts on arguments
    #creates a list of three food items
    #and prompts the user to replace one of the items
    #it searches the list for the index of the item
    #and prompts the user with replacement food
    
    foods = ['Burger', 'Pizza', 'Hotdog']
    print(foods)
    
    remove = input("Enter the string to remove: ")
    
    try:
        if foods.index(remove) >= 0:
            index = foods.index(remove)
            foods[index]
            print("Item removed.")
        print(f"\nHere is the list:{foods}")
    except Exception as err:
        print()
        print(err)      
