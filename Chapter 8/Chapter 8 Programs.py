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


