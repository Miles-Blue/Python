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
    
  
    
    
    
    
    
