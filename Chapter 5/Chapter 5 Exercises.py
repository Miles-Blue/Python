import math
import turtle as tur
import my_graphics
import random

# ---------------------------------------------- #

def sales_tax():
    #sales tax accepts no arguments
    #calls upon sale_amount, state_tax, county_tax, total_tax, and total_sale
    #to output each amount based on user input
    
    amount = sale_amount() #calls sale amount
    state = state_tax(amount) #calls state tax
    county = county_tax(amount) #calls county tax
    tax = total_tax(state, county) #calls total tax
    total_sale(amount, tax) #calls total sale
    
def sale_amount():
    #accepts no arguments
    #prompts user for sale amount
    #returns sale amount after validation
    
    amount = float(input("Enter the sale amount: "))
    while amount < 0: #validates input
        print("Please enter a number greater than 0.")
        amount = float(input("Enter the sale amount: "))
    
    #prints amount formatted
    print("Your purchase price was:\t", end='$')
    print(format(amount, '10.2f'))
    return amount #returns amount
    
def state_tax(amount):
    #state tax accepts amount
    #determines state tax with amount by multiplying by .5
    #returns state
    
    state = amount * .05
    print("Your state tax amount is:\t", end='$')
    print(format(state, '10.2f'))
    return state
    
def county_tax(amount):
    #county tax accepts amount
    #determines county tax with amount by multiplying by .5
    #returns county
    
    county = amount * .025
    print("Your county tax amount is:\t", end='$')
    print(format(county, '10.2f'))
    return county
    
def total_tax(state, county):
    #accepts state and county
    #determines total tax by adding state and county
    #returns tax
    
    tax = state + county
    print("Your total tax is:\t\t", end='$')
    print(format(tax, '10.2f'))
    return tax
    
def total_sale(amount, tax):
    #accepts amount and tax as total tax
    #determines total sale by adding amount and tax
    #outputs the total
    
    sale = amount + tax
    print("Your total sale is:\t\t", end='$')
    print(format(sale, '10.2f'))
    
# ---------------------------------------------- #

def calories():
    #accept no arguments
    #calls on the function carb_grams and fat_grams
    #main function
    
    carb = carb_grams()
    fat = fat_grams()
    
    print("\nHere is your calorie intake for the day.")
    print("You consumed", carb, "calories worth of carbs today. Nice work...")
    print("You consumed", fat, "calories worth of fats today. Nice work...")
    
def carb_grams():
    #accepts no arguments
    #prompts user for grams of carbs
    #calculates caloric intake
    #returns carbs
    
    grams = int(input("How many grams of carbs did you consume? "))
    while grams < 0: #validates user input
        print("Please enter a number greater than 0.")
        grams = int(input("How many grams of carbs did you consume? "))
    carb = grams * 4
    return carb

def fat_grams():
    #accepts no arguments
    #prompts user of grams of fat
    #calculates caloric intake
    #returns fat
    
    grams = int(input("How many grams of fat did you consume? "))
    while grams < 0: #validates user input
        print("Please enter a number greater than 0.")
        grams = int(input("How many grams of fat did you consume? "))
    fat = grams * 9
    return fat

# ---------------------------------------------- #

def stadium_seating():
    #accepts no arguments
    #calls on Class A, Class B, and Class C to determine tickets
    #outputs total
    
    price_a = class_a()
    price_b = class_b()
    price_c = class_c()
    total = price_a + price_b + price_c
    
    print("\nThe total income sales from tickets is: $" + str(total))
    
def class_a():
    #accepts no arguments
    #prompts user for number of class a tickets sold
    #calculates price and returns price a
    
    tickets = int(input("Enter the number of Class A tickets sold: "))
    while tickets < 0: #validates user input
        tickets = int(input("Enter a valid number of Class A tickets sold: "))
    price_a = tickets * 20
    return price_a

def class_b():
    #accepts no arguments
    #prompts user for number of class b tickets sold
    #calculates price and returns price b
    
    tickets = int(input("Enter the number of Class B tickets sold: "))
    while tickets < 0: #validates user input
        tickets = int(input("Enter a valid number of Class B tickets sold: "))
    price_b = tickets * 15
    return price_b

def class_c():
    #accepts no arguments
    #prompts user for number of class a tickets sold
    #calculates price and returns price a
    
    tickets = int(input("Enter the number of Class C tickets sold: "))
    while tickets < 0: #validates user input
        tickets = int(input("Enter a valid number of Class C tickets sold: "))
    price_c = tickets * 10
    return price_c

# ---------------------------------------------- #

def paint_estimator():
    #accepts no arguments
    #calls on paint_gallons and labor_cost
    #outputs total cost
    
    feet = square_feet_paint() #assigns feet to a variable
    gallons = feet / 112 #calculates gallons
    paint_cost = paint_gallons(math.ceil(gallons)) #gets paint cost
    
    labor_cost = (feet / 112) * 35 * 8
    total_cost = paint_cost + labor_cost
    
    print("The cost breakdown to paint", feet, "square feet is:")
    print("------------------------------------------------------")
    print("Total cost of paint: $", format(paint_cost, '.2f'), sep='')
    print("Total labor cost: $", format(labor_cost, '.2f'), sep='')
    print("Total cost of the job is: $", format(total_cost, '.2f'), sep='')
    
    
def square_feet_paint():
    #accepts no arguments
    #prompts user for total square feet
    #returns feet
    
    feet = float(input("Please enter the total square feet to be painted: "))
    while feet < 0:
        feet = float(input("Please enter a number greater than 0: "))
    return feet
    
def paint_gallons(gallons):
    #accepts gallons for number of gallons
    #prompts user for gallon cost
    #determines total cost of paint
    #returns paint cost
    
    cost = float(input("How much is each gallon of paint? "))
    while cost < 0:
        cost = float(input("Please enter a number greater than 0: "))
    paint_cost = gallons * cost
    return paint_cost
    
# ---------------------------------------------- #

def math_quiz():
    #accepts no arguments
    #calls get_numbers and loops
    #loops while user inputs y
    
    cont = 'y'
    
    while cont == 'y':
        num1, num2 = get_number() #calls on get number for two random numbers
        answer = num1 + num2 #determines the real answer
        
        #formats the two random numbers into a problem
        print("\t", format(num1, '3.0f'))
        print("\t+", format(num2, '3.0f'), sep='')
        print("\t----")
        
        user_answer = int(input("Answer:")) #gets user answer
        
        if user_answer == answer: #determines if answer is wrong
            print("\nYou got it right!")
        else:
            print("\nDarn! So close. The actual answer was", answer)
            
        cont = input("\nContinue? (y/n)") #continues or ends the loop
        
def get_number():
    #accepts no arguments
    #generates two random integers from 1-200
    #returns number
    
    num1 = random.randint(1, 200)
    num2 = random.randint(1, 200)
    
    if num1 > num2: #formats num1 and num2
        return num1, num2
    else:
        return num2, num1

# ---------------------------------------------- #















