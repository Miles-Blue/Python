import random

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
    
    get_rid = input("Enter the string to remove: ")
    
    try:
        if foods.index(get_rid) >= 0:
            index = foods.index(get_rid)
            foods.remove(foods[index])
            print("Item removed.")
        print(f"\nHere is the list:{foods}")
    except Exception as err:
        print()
        print(err)      

def barista_pay():
    #accepts no arguments
    #prompts the user for number of employees, hours worked for each employee
    #and the hourly rate all employees are paid
    #then outputs each employee's gross pay
    
    hours = []
    counter = 0
    
    employees = int(input("How many employees do you want to calculate pay for? "))
    
    for employee in range(employees):
        counter += 1
        hours_worked = input(f"Enter the hours worked by employee {counter}:")
        hours.append(hours_worked)
    
    print()
    rate = int(input("Enter the hourly rate for all employees: "))
    
    counter = 0
    for hour in hours:
        counter += 1
        pay = int(hour) * rate
        print(f"Gross pay for employee {counter}: {pay}")

def list_total():
    
    numbers = [2, 4, 6, 8, 10]
    total = 0
    
    for index in numbers:
        total += index
    print(f"The sum of the numbers {numbers} is: {total}")

def list_avg():
    
    numbers = [2, 4, 6, 8, 10]
    total = 0
    counter = 0
    
    for index in numbers:
        total += index
        counter += 1
    print(f"The sum of the numbers {numbers} is: {total/counter}")

def list_function():
    numbers = [2, 4, 6, 8, 10]
    total = get_total(numbers)
    print(f"The sum of the numbers {numbers} is: {total}")

def get_total(numbers):
    total = 0
    for index in numbers:
        total += index
    return total

def list_return():
    
    lst = get_values()
    print(f"You entered the numbers: {lst}")
        
def get_values():
    numbers = []
    cont = 'y'
    
    try:
        while cont != 'n':
            number = int(input("Input a number: "))
            numbers.append(number)
            cont = input("Do you want to enter another number? (y/n) ")
    except Exception as err:
        print(err)
    return(numbers)

def test_calc():
    low_score = 101
    total = 0
    counter = -1
    
    scores = get_scores()
    
    for score in scores:
        counter += 1
        if score < low_score:
            low_score = score
        total += score
    total -= low_score
    average = total / counter
    print(f"The average score, with {low_score} dropped from the scores, is: {average}")
    

def get_scores():
    numbers = []
    cont = 'y'
    
    try:
        while cont != 'n':
            number = int(input("Enter a score: "))
            numbers.append(number)
            cont = input("\nDo you want to enter another score? (y/n) ")
    except Exception as err:
        print(err)
    return(numbers)

def list_writelines():
    #accept no arguments
    #writes the entire contents of a list
    #to the file cities.txt
    
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhatten']
    
    try:
        outfile = open('cities.txt', 'w')
        
        outfile.writelines(cities)
        
        print("All data written to cities.txt")
        outfile.close()
        
    except Exception as err:
        print(err)
        
def list_read():
    #accepts no arguments
    #it reads from cities.txt and aggregates the data
    #to the list cities, stripping the \n from each
    
    try:
        infile = open('cities.txt', 'r')
        
        cities = infile.readlines()
        
        infile.close()
        
    except Exception as err:
        print(err)
        
    index = 0
    
    while index <len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    print("Here is the information read from cities.txt.")
    print(cities)

def list_write_numbers():
    #accepts no arguments
    #saves a list of integers
    #to the file numbers.txt
    
    numbers = [1, 2, 3, 4, 5, 6, 7]
    
    outfile = open('numberlist.txt', 'w')
    
    for number in numbers:
        outfile.write(str(number) + '\n')
    
    outfile.close()
    print("All numbers saved to numberlist.txt")

def list_read_numbers():
    #accepts no arguments
    #reads integers from the file numberlist.txt
    #and aggregates them to a list
    
    numbers = []
    
    try:
        infile = open('numberlist.txt', 'r')
        
        for num in infile:
            numbers.append(int(num.rstrip('\n')))
            
        infile.close()
    except Exception as err:
        print(err)
    print("Here is the list created from numberlist.txt:")
    print(numbers)

def random_numbers():
    #accepts no arguments
    #it creates a 2D list with a maximum row index of 3
    #and a maximum column index of 2
    #uses nested loops to fill the 2D list with a random number
    #from 1-100
    
    ROWS = 3
    COLS = 4
    
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for row in range(ROWS):
        for col in range(COLS):
            values[row][col] = random.randint(1, 100)
    print(values)

















