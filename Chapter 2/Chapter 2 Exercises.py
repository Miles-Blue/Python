def personal_info():
    #prints my personal info
    print("Miles Blue")
    print("446 S Nineiron, Wichita, Kansas, 67235")
    print("316-680-8531")
    print("Computer Hardware Engineering")

def total_purchase():
    #takes five different purchase inputs
    item1 = float(input("Please enter a price for your first item:"))
    item2 = float(input("Please enter a price for your second item:"))
    item3 = float(input("Please enter a price for your third item:"))
    item4 = float(input("Please enter a price for your fourth item:"))
    item5 = float(input("Please enter a price for your fifth item:"))
    
    #adds inputs together and outputs it
    subtotal = item1 + item2 + item3 + item4 + item5
    print("Subtotal:\t", end='$')
    print(format(subtotal, '6.2f'))
    
    #takes tax of subtotal and outputs it
    tax = subtotal * .07
    print("Tax:\t\t", end='$')
    print(format(tax, '6.2f'))
    
    #adds tax plus subtotal and outputs it
    total = subtotal + tax
    print("Total:\t\t", end='$')
    print(format(total, '6.2f'))

def distance_traveled():
    #distance traveled will determine how far someone has gone
    #based on the speed the user inputs
    #takes speed input and turns it into a float variable
    speed = int(input("How fast are you driving? "))
    
    #calculates the distance after 6, 10, and 15 hours
    hour6 = speed * 6
    hour10 = speed * 10
    hour15 = speed * 15
    
    #ouputs distance for each time
    print("At", speed, "miles per hour you will travel", hour6, "in 6 hours.")
    print("At", speed, "miles per hour you will travel", hour10, "in 10 hours.")
    print("At", speed, "miles per hour you will travel", hour15, "in 15 hours.")
    
def sales_tax():
    #takes user input for amount of purchase
    #program computes state and county tax
    #then adds to get the total purchase
    sale_amount = float(input("Enter the sale amount: "))
    print("Your purchase price was:\t", end='$')
    print(format(sale_amount, '10.2f'))
    
    state_tax = sale_amount * .05
    print("Your state tax amount is:\t", end='$')
    print(format(state_tax, '10.2f'))
    
    county_tax = sale_amount * .025
    print("Your county tax amount is:\t", end='$')
    print(format(county_tax, '10.2f'))
    
    total_tax = state_tax + county_tax
    print("Your total tax is:\t\t", end='$')
    print(format(total_tax, '10.2f'))
    
    total_sale = sale_amount + total_tax
    print("Your total sale is:\t\t", end='$')
    print(format(total_sale, '10.2f'))
    
def tip_tax_total():
    #user inputs food cost
    #calculates tip and sales tax
    #outputs cost, tip, tax, and total bill
    sale_amount = float(input("Please enter the sale amount: "))
    print("The sale was:\t\t\t", end='$')
    print(format(sale_amount, '10.2f'))
    
    #calculates and prints tip and tax
    tip = sale_amount * .18
    print("The tip amount is:\t\t", end='$')
    print(format(tip, '10.2f'))
    
    tax = sale_amount * .07
    print("The sales tax amount is:\t", end='$')
    print(format(tax, '10.2f'))
    
    #calculates and prints total bill
    total_bill = sale_amount + tip + tax
    print("The total bill is:\t\t", end='$')
    print(format(total_bill, '10.2f'))
    
def temp_converter():
    #user inputs desired celsius digit
    #program converts celsius to fahrenheit
    #outputs product
    celsius = float(input("Please enter the degrees Celsius: "))
    fahrenheit = (9/5 * celsius) + 32
    print(int(celsius), "degrees celsius is ", fahrenheit, "degrees fahrenheit.")
    
def cookie_monster():
    #user inputs desired cookie output
    #program calculates ingredients required
    #ouputs ingredients
    desired_cookies = float(input("How many cookies do you want to make? "))
    
    #assign sugar, butter, and flower to constants
    SUGAR = .5
    BUTTER = .3333
    FLOUR = .9166
    
    #calculates cups
    sugar_cups = desired_cookies * SUGAR
    butter_cups = desired_cookies * BUTTER
    flour_cups = desired_cookies * FLOUR
    #calculates oz
    sugar_oz = sugar_cups % 8
    butter_oz = butter_cups % 8
    flour_oz = flour_cups % 8
    
    #outputs result
    print("For", int(desired_cookies), "you will need:")
    print(int(sugar_cups / 8), "cup(s)", int(format(sugar_oz, '.0f')), "ounces of sugar.")
    print(int(butter_cups / 8), "cup(s)", int(format(butter_oz, '.0f')), "ounces of butter.")
    print(int(flour_cups / 8), "cup(s)", int(format(flour_oz, '.0f')), "ounces of flour.")
    
def class_demographic():
    #user inputs number of males and females enrolled
    #program calculates percentage of male and females enrolled
    #outputs percentage
    females = float(input("Enter the number of females: "))
    males = float(input("Enter the number of males: "))
    
    #calculates total students
    total_students = females + males
    
    #calculates percentage of females and males
    female_percent = females / total_students
    male_percent = males / total_students
    
    #ouputs percents
    print("The class consists of", end=' ')
    print(format(female_percent, '.0%'), "females and",end=' ')
    print(format(male_percent, '.0%'), "males.")
    
    
def tortuga_1():
    #program uses turtle to draw a simple compass
    #sets up turtle
    import turtle as tur
    tur.speed(2)
    tur.penup()
    tur.goto(0, 0)
    tur.pensize(5)
    
    #draws East to West line
    tur.goto(200, 0)
    tur.pendown()
    tur.goto(-200, 0)
    
    tur.penup()
    
    #draws North to South line
    tur.goto(0, 200)
    tur.left(90)
    tur.pendown()
    tur.goto(0, -200)
    
    tur.penup()
    
    #draws NE to SW
    tur.pensize(2)
    tur.goto(100, 100)
    tur.right(45)
    tur.pendown()
    tur.goto(-100, -100)
    
    tur.penup()
    
    #draws NW to SE
    tur.goto(-100, 100)
    tur.left(90)
    tur.pendown()
    tur.goto(100, -100)
    
    tur.penup()
    
    #types the N, E, S, and W
    tur.goto(-8, 210)
    tur.write("N", font=('arial', 20, 'bold'))
    tur.goto(210, -18)
    tur.write("E", font=('arial', 20, 'bold'))
    tur.goto(-8, -240)
    tur.write("S", font=('arial', 20, 'bold'))
    tur.goto(-232, -18)
    tur.write("W", font=('arial', 20, 'bold'))
    
    tur.hideturtle()
    tur.done()

def tortuga_2(): #going to do the house
    print()