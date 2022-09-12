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
    
def show_double(number):
    #show double accepts a value for number
    #it calculates that number * 2 and prints the result
    
    result = number * 2
    print(number, "* 2 =", result)

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
    print("change_global to the value of," number)

# ---------------------------------------------- #
#global constant for program 5-15
CONTRIBUTION_RATE = 0.05

def pay_me():
    #accepts no arguments
    #it prompts the user for the gross pay and amount of bonuses
    #it calls show_pay, passing gross
    #and show_bonus, passing bonus
    
def show_pay(gorss):
    #show pay accepts a float for gross
    #it calculates the contribution = gross * the global constant
    #it outputs the contribution for gross pay
    
def show_bonus(bonus):
    #accepts a float for bonus
    #it calculates the contribution = bonus * the global constant
    #it outputs the contribution for bonuses

















