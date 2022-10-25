import login

def count_t():
    #accepts no arguments
    #prompts the user for a word
    #and iterates through each letter
    #counting the number of upper and lower case t's
    #it outpus the total number of times it appeared in the word
    
    word = input("Please enter a word: ")
    
    counter = 0
    
    for ch in word:
        if ch.lower() == 't':
            counter += 1
            
    print(f"The letter T or t appears {counter} times in the word: {word}")
    
#--------------------------------------------------------------------------------#
    
def concatenate():
    
    place = "Carmen"
    print(f"Where in the world is {place}?")
    place += " Sandiego"
    print(f"Where in the world is {place}?")

#--------------------------------------------------------------------------------#
    
def generate_login():
    #accepts no arguments
    #it prompts the user for the first name, last name, and idnumber
    #it passes the values to login.get_login_name()
    #and receives the new user login
    
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your id number: ")
    
    print("\nYour system login name is:")
    print(login.get_login_name(first, last, idnumber))
    
    password = input("\nPlease enter your password: ")
    login.valid_password(password)

#--------------------------------------------------------------------------------#

def string_test():
    #accepts no arguments
    #it takes input from the user in th form of a string
    #and performs a variety of tests on the string
    
    #et input from the user
    user_string = input("Enter a string to evaluate: ")
    
    #perform string tests
    if user_string.isalnum():
        print("The string only contains alphanumeric characters.")
    if user_string.isdigit():
        print("The string only contains digits.")
    if user_string.isalpha():
        print("The string only contains alpha characters.")
    if user_string.isspace():
        print("The string only contains whitespaces.")
    if user_string.islower():
        print("The string is all lowercase.")
    if user_string.isupper():
        print("The string is all uppercase.")
    if user_string == '':
        print("The string is blank.")
    
    print()
    print("Your string converted to all uppercase is:", user_string.upper())
    print("Your string converted to all lowercase is:", user_string.lower())

#--------------------------------------------------------------------------------#

def repetition():
    #accepts no arguments
    #it muliplies 'Z' by range(1,10)
    #then multiplies 'Z' by range(8, 0, -1)
    
    counter = 9
    for count in range(1, 10):
        print(' ' * counter + 'Z' * count * 2)
        counter -= 1
    
    for count in range(8, 0, -1):
        counter += 1
        print(' ' * counter + 'Z' * (count + 1) * 2)
    print(' ' * (counter + 1) + 'ZZ')

#--------------------------------------------------------------------------------#

def string_split():
    #string split accepts no arguments
    #it splits the string one two three four
    #adding it to a list
    
    numbers = 'one two three four'
    
    number_list = numbers.split()
    
    print(number_list)

#--------------------------------------------------------------------------------#

def split_date():
    #accepts no arguments
    #it creates a date string of 11/26/2018
    #and splits the date into mm dd yyyy
    
    while True:
        
        date = input("Please enter the month/day/year: ")
        date_list = date.split('/')
        
        try:
            print(f"Month: {date_list[0]}")
            print(f"Day: {date_list[1]}")
            print(f"Year: {date_list[2]}")
            break
        except:
            print("Separate month, day, and year by a /.")











