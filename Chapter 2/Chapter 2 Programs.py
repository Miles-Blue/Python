def comment_example():
    #comment_example receives no arguments
    #it explains how to create a function header
    #and outputs or returns "Hello world!".
    print('Hello world!')

def program2_1():
    #program 2 1 receives no arguments
    #it outputs three messages using apostrophes instead
    #of quotation marks
    print('Kate Austen')
    print('123 Full Circle Drive')
    print('Asheville, NC28899')
    
def program2_2():
    #program 2 2 receives no arguments
    #double quote output
    print("Kate Austen")
    print("123 Full Circle Drive")
    print("Asheville, NC28899")
    
def program2_3():
    #program 2 3 receives no arguments
    #double quote output
    #allows apostrophes within text
    print("Don't fear!")
    print("I'm here!")
    
def program2_4():
    #program 2 4 receives no arguments
    #apostrophe output
    #allows quotations within text
    print('Your assignment is to read "Hamlet" by tomorow.')
    
def program2_5():
    #This function displays a person's name and address
    print('Kate Austen')
    print('123 Full Circle Drive')
    print('Asheville, NC28899')
    
def program2_6():
    print('Kate Austen') #Display the Name
    print('123 Full Circle Drive') #Display the address
    print('Asheville, NC28899') #Display the city, state, and ZIP
    
def program2_7():
    #using two print commands and a variable named room
    #this will output the message, you are staying in room
    #and the value of the variable is 503
    room = 503
    
    print("I am staying in room number")
    print(room)
    
def program2_8():
    #uses and prints two variables along with two other print functions
    top_speed = 160
    distance = 300
    
    print("The top speed is")
    print(top_speed)
    print("The distance traveled is")
    print(distance)

def program2_9():
    #program2_9 uses a comma to concatenate
    #the variable to the end of the sentence
    room = 508
    
    print("I am staying in room number", room)
    
def program2_10():
    #assigns a value
    #prints value in print statment
    dollars = 2.75
    print("I have",dollars,"in my account")
    
    #changes value and reprints
    dollars = 99.95
    print("but now I have",dollars,"in my account!")
    
def program2_11():
    first_name = "Kathryn"
    last_name = "Marino"
    
    print(first_name + " " + last_name)
    
def program2_12():
    #program2_12 gets inputs from user
    #then takes inputs and outputs to the user
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    print("Hello", first_name, last_name)
    
def program2_13():
    #user inputs
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    income = float(input("What is your income? "))#converts income to a float
    #prints the inputs
    print("Here is the data you entered:")
    print("Name:",name)
    print("Age:",age)
    print("Income:",income)
    
def program2_14():
    salary = 2500
    bonus = 1200
    pay = salary + bonus
    print("Your pay is",pay)
    
def program2_15():
    #user types original price
    original_price = float(input("Type original price: "))#turns price into float
    #takes 20 percent of original_price
    discount = original_price * .2
    #finds discounted price
    display_price = original_price - discount
    #displays discounted price
    print("The sale price is:", display_price)

def program2_16():
    
    
    