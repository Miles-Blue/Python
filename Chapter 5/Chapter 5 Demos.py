import random
import math
import circle
import rectangle
import my_graphics as graph
import turtle as tur

my_value = 10 #global variable

def message():
    #accepts no arguments
    #ouputs the line: I am Iron Man
    
    print("I am Iron Man")
    
# ---------------------------------------------- #

def main5_2():
    #accepts no arguments
    #prints "I am inevitable"
    #it calls the procedure message
    #then prints "Only one way to win..."
    
    print("I am inevitable.")
    message()
    print("Only one way to win...")
    
# ---------------------------------------------- #

def acme_dryer():
    #accepts no arguments
    #prompts user for step number
    #calls upon corresponding function
        
    #prompts for user input
    step = int(input("Enter step # or 0 to exit: "))
    while step != 0:
        if step >=0 and step <=5:
            if step == 1:
                step1()
            elif step == 2:
                step2()
            elif step == 3:
                step3()
            elif step == 4:
                step4()
            elif step == 5:
                step5()
        else:
            print("That is not a valid number.")
        step = int(input("Enter step # or 0 to exit: "))
    goodbye()

def step1():
    #accepts no arguments
    #defines step 1 of the acme program
    
    print("Unplug the dryer and move it away from the wall.")
    
def step2():
    #accepts no arguments
    #defines step 2 of the acme program
    
    print("Remove the six screws from the back of the dryer.")
    
def step3():
    #accepts no arguments
    #defines step 3 of the acme program
    
    print("Remove the back panel.")
    
def step4():
    #accepts no arguments
    #defines step 4 of the acme program
    
    print("Pull the top of the dryer straight up.")
    
def step5():
    #accepts no arguments
    #defines step 5 of the acme program
    
    print("Pull the front of the dryer off.")

def goodbye():
    #accepts no arguments
    #defines goodbye of the acme program
    
    print("Thank you for using our service.")
# ---------------------------------------------- #          

def bad_scope():
    #bad local accepts no arguments
    #it calls the procedure get_name() to get someone's name
    #then outputs a message using that name
    #NOTE: The scope of the variable "name" in get_name will not
    #allow this function to access that variable
    
    get_name()
    print("Hello", name) #this will throw an exception
    
def get_name():
    #get name accepts no arguments
    #it promts the user to get their name
    
    name = input("Enter your name: ")
    
# ---------------------------------------------- #

def bird_calculator():
    #accepts no arguments
    #it calls the function texas()
    #then calls the function kansas()
    
    texas()
    kansas()

def texas():
    #accepts no arguments
    #assigns the variable birds = 5000
    #then outputs a message "Texas has <birds> birds.
    
    birds = 5000
    print("Texas has", birds, "birds.")
    
def kansas():
    #accepts no arguments
    #assigns the variable birds = 5000
    #then outputs a message "Kansas has <birds> birds.
    
    birds = 5000
    print("Kansas has", birds, "birds.")

# ---------------------------------------------- #

def pass_arg():
    #accepts no arguments
    #it assigns value = 5
    #it calls show_double, passing value
    
    value = 5
    show_double(value)
    
def show_double(value):
    #show double accepts a value for number
    #it calculates that number * 2 and prints the result
    
    result = value * 2
    print(value, "* 2 =", result)

# ---------------------------------------------- #

def volume_conversion():
    #accepts no arguments
    #it calls intro to display a greeting
    #it prompts the user for the number of cups
    #it calls cups_to_ounces, passing the value for cups
    
    intro()
    
    cups = int(input("\nPlease enter the number of cups to convert to ounces: "))
    while cups < 0: #validates user input
        print("Please enter a value greater than 0.")
        cups = int(input("\nPlease enter the number of cups to convert to ounces: "))

    cups_to_ounces(cups)

def intro():
    #intro accepts no arguments
    #it displays a greeting message describing the program
    #and the conversion rate of cups to ounces
    
    print("Welcome to the cups to fluid ounces conversion program.")
    print("For your reference, 1 cup = 8 fluid ounces.")
    
def cups_to_ounces(cups):
    #accepts the value for cups
    #it converts the number of cups to the number of ounces
    #and outputs the result
    
    result = cups * 8
    print("\n", cups, "cup(s) is equal to", result, "fluid ounces.")

# ---------------------------------------------- #

def show_sum():
    #show sum accepts no arguments
    #it outputs a message "Te sum of 12 and 45 is"
    #it cals sum_of_numbers(num1, num2) passing the values 12 and 45
    
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    sum_of_numbers(num1, num2)
    
def sum_of_numbers(num1, num2):
    #accepts two arguments for num1 and num2
    #it adds the two numbers together
    #and prints the sum
    
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is", result)
    
# ---------------------------------------------- #

def get_name2():
    #get name accepts no arguments
    #prompts the user for their first then last name
    #it calls reverse_name(first, last) passing values
    #for first and last
    
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    reverse_name(first, last)
    
def reverse_name(first, last):
    #accepts strings for first and last
    #it outputs the names in reverse order:
    
    print(last, first)

# ---------------------------------------------- #

def get_value():
    #get value accepts no arguments
    #it assigns value = 99 and outputs the value
    #it passes value to change_me
    #it outputs a message showing the value of value in this function
    
    value = 99
    print("I just assigned the variable value: ", value)
    change_me(value)
    
    #output the value in this function
    print("The value in the function get_value is still:", value)
    
def change_me(value):
    #change me accepts an integer for value
    #it reassigns the value to 0
    #and outputs a message with the new value in this function
    
    value = 0
    
    #output the value in this function
    print("The value in the function change_me is:", value)

# ---------------------------------------------- #

def set_args():
    #accepts no arguments
    #it calls show_interest passing principal, rate, and periods as keywords
    
    show_interest(rate=.01, principal=10000.0,periods=10)
    
def show_interest(rate, periods, principal):
    #accepts arguments for rate, periods and principal
    #it calculates interest = principal*rate*periods
    #and outputs the result
    
    interest = principal * rate * periods
    print("The simple interest will be $", format(interest, '.2f'), sep=' ')

# ---------------------------------------------- #

def show_value():
    #receives no arguments
    #it prints the value of global my_value
    
    global my_value
    
    my_value += 1
    
    print("The value of the global variable my_value is", my_value)

# ---------------------------------------------- #
#create a global variable
number = 0

def change_global():
    #accepts no arguments
    #it changes the value of the global variable number
    #then calls global_variables_are_bad to print the variable
    
    global number
    number = int(input("What do you want to chang the global to? "))
    global_variables_are_bad()
    
def global_variables_are_bad():
    #accepts no arguments
    #it prints the value of the global variable number
    
    print("The value of the global variable number was changed in", end=' ')
    print("change_global to the value of", number)

# ---------------------------------------------- #

#global constant for program 5-15
CONTRIBUTION_RATE = 0.05

def pay_me():
    #accepts no arguments
    #it prompts the user for the gross pay and amount of bonuses
    #it calls show_pay, passing gross
    #and show_bonus, passing bonus
    
    #prompts user for input
    gross = float(input("Please enter the amount for gross pay: "))
    bonus = float(input("Please enter the amount of bonuses: "))
    
    #calls for show pay and show bonus programs
    show_pay(gross)
    show_bonus(bonus)
    
def show_pay(gross):
    #show pay accepts a float for gross
    #it calculates the contribution = gross * the global constant
    #it outputs the contribution for gross pay
    
    #calculates and outputs contribution pay
    result = gross * CONTRIBUTION_RATE
    print("Contribution for gross pay: $", format(result, '.2f'))
    
def show_bonus(bonus):
    #accepts a float for bonus
    #it calculates the contribution = bonus * the global constant
    #it outputs the contribution for bonuses
    
    #calculates and outputs contribution bonus
    result = bonus * CONTRIBUTION_RATE
    print("Contribution for bonuses: $", format(result, '.2f'))

# ---------------------------------------------- #

def random_numbers():
    #random numbers accepts no arguments
    #it generates a random integer from 1-10
    #output the number to the user
    
    random_number = random.randint(1, 10)
    print("The random number is:", random_number)

# ---------------------------------------------- #

def random_numbers2():
    #accepts no arguments
    #it loops 5 times assigning a random integer from 1-100 to number
    #it outputs the random integer for each iteration
    
    for among_us in range(5):
        random_number = random.randint(1, 100)
        print(random_number)

# ---------------------------------------------- #

def random_numbers3():
    #accepts no arguments
    #it loops 5 times assigning a random integer from 1-100 to number
    #it outputs the random integer for each iteration
    
    for among_us in range(5):
        print(random.randint(1, 100))

# ---------------------------------------------- #

def dice():
    #dice accepts no arguments
    #it loops until the user enters "n" or "N: to stop
    #each iteration prints two random 6-sided de rolls
    #it prompts the user to roll again(y/n)

    again = 'y'
    
    while again.lower() != 'n':
        print("Rolling your dice...")
        
        num1 = random.randint(1, 6) #randomizes the numbers
        num2 = random.randint(1, 6)
        
        print("Your two rolls are:", num1, "and", num2)
        again = input("\nTry your luck again? (y/n) ") #prompts user to end or continue
        
# ---------------------------------------------- #

def coin_toss():
    #accepts no arguments
    #sets three named constants for head, tails, and tosses
    #loops for 10 tosses using a random integer form 1 or 2 to determine
    #if the coin flip resulted in heads or tails, respectively
    
    HEADS = 1
    TAILS = 2
    TOSSES = 10
    
    for toss in range(TOSSES):
        flip = random.randint(1, 2)
        if flip == HEADS:
            print("Heads!")
        elif flip == TAILS:
            print("Tails!")

# ---------------------------------------------- #

def die_roll():
    #accepts no arguments
    #rolls a die
    #returns the roll vlue
    
    die = random.randint(1, 6)
    
    return die

# ---------------------------------------------- #

def amoung():
    
    funny = 0
    counter = 0
    
    while funny != 69:
        funny = random.randint(1, 100)
        counter += 1
    print("It took", counter, "times to get 69.")

# ---------------------------------------------- #

def total_ages():
    #accepts no arguments
    #prompts the user for two ages and pases those values to calculate_ages()
    #uses the return value to print the toal ages
    
    age1 = int(input("Please enter your age: "))
    age2 = int(input("Please enter the age of your best friend: "))
    
    total = calculate_ages(age1, age2)
    
    print("\nTogether you are", total, "years old.")
    
def calculate_ages(age1, age2):
    #receives values for age1 and age2
    #addes the two ages together
    #returns the result
    
    total = age1 + age2
    
    return total

# ---------------------------------------------- #

#declare global constant for sale price
DISCOUNT_PERCENT = .20

def sale_price():
    #accepts no arguments
    #calls get regular price to get input from the user
    #calculates the sale price by taking the regular price and subtracting the
    #return result of discount()
    #outputs the sale price
    
    reg_price = get_regular_price()
    sale = reg_price - discount(reg_price)
    
    print("The sale price is: $", format(sale, '.2f'), sep='')
    
def get_regular_price():
    #get regular price accepts no arguments
    #it prompts the user to input the item's regular price
    #and returns that value
    
    price = float(input("Please enter the regular price of the item: "))
    return price
    
def discount(price):
    #discount accepts an argument for the float price
    #returns the discount price @ 20% off using
    #the global constant DISCOUNT_PERCENT

    discount_off = price * DISCOUNT_PERCENT
    return discount_off
    
# ---------------------------------------------- #

def commission_rate():
    #accepts no arguments
    #calls get_sales and get_advanced_pay
    #calls determine_comm_rate passing sales
    #calculates the pay and outputs the pay
    #determines if the pay is negative and outputs if the salesperson
    #the amount the salesperson must reimburse the company for
    
    sales = get_sales()
    advanced = get_advanced_pay()
    rate = determine_comm_rate(sales)
    
    pay = (sales * rate) - advanced
    
    print("You made $", format(pay, '.2f'), sep='')
    
    if pay < 0:
        print("You owe the company $", format(pay * -1, '.2f'), sep='')
    
def get_sales():
    #accepts no arguments
    #it prompts the user to input the total monthly sales
    #and returns the monthly sales
    
    total_sales = float(input("Please enter total monthly sales: "))
    return total_sales

def get_advanced_pay():
    #get advanced pay accepts no arguments
    #it prompts the user to enter any advanced pay, or 0 for none
    #it returns the advanced pay
    
    advanced = float(input("Please enter your advanced pay (0 for none): "))
    return advanced

def determine_comm_rate(sales):
    #determine comm rate accepts a float for sales
    #it calculates the commission rate for sales
    #and returns the calculated rate
    
    if sales < 10000:
        comm_rate = .10
    elif sales >= 10000 and sales < 15000:
        comm_rate = .12
    elif sales >= 15000 and sales < 18000:
        comm_rate = .14
    elif sales >= 18000 and sales < 22000:
        comm_rate = .16
    elif sales >= 22000:
        comm_rate = .18
        
    return comm_rate
    
# ---------------------------------------------- #   
    
def get_name_program():
    #accepts no arguments
    #prompts the user for first name and last name
    #and returns first nam and last name as strings
    
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    return first_name, last_name
    
# ---------------------------------------------- #   
    
def square_root():
    #accepts no arguments
    #prompts user for a number
    #calculates the square root using the math module
    #outputs square root
    
    sqr_number = float(input("Please enter a value to find the square root: "))
    print("The square root of", sqr_number, "is", math.sqrt(sqr_number))
    
# ---------------------------------------------- #

def hypotenuse():
    #accepts no arguments
    #prompts user for two sides and calculates hypotenuse
    #outputs the message with hypotenuse
    
    side1 = float(input("Please enter the length of side 1: "))
    side2 = float(input("Please enter the lenth of side 2: "))
    print("The length of the hypotenuse is:", math.hypot(side1, side2))
    
# ---------------------------------------------- #
    
#def triangle():
    #accepts no arguments
    #uses module my_graphics to draw a triangle
    
    #TOP_X = 0
    #TOP_Y = 100
    #BASE_LEFT_X = -100
    #BASE_LEFT_Y = -100
    #BASE_RIGHT_X = 100
    #BASE_RIGHT_Y = -100
    #graph.line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y,)
    
# ---------------------------------------------- #
    
def graphic_fun():
    #accepts no arguments
    #uses modules turtle and my_graphics to draw
    #a funky shape
    
    #assigns constants
    X1 = 0
    Y1 = 100
    X2 = -100
    Y2 = -100
    X3 = 100
    Y3 = -100
    RADIUS = 50
    
    graph.square(X2, Y2, 200, 'gray')
    graph.line(X2, Y2, X3, Y3, 'black')
    graph.line(X3, Y3, X1, Y1, 'black')
    graph.line(X1, Y1, X2, Y2, 'black')
    graph.circle(X2, Y2, RADIUS, 'red')
    graph.circle(X3, Y3, RADIUS, 'green')
    graph.circle(X1, Y1, RADIUS, 'blue')
    tur.done()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












