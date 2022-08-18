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
    print("Subtotal:\t", "$", format(subtotal, '.2f'))
    
    #takes tax of subtotal and outputs it
    tax = subtotal * .07
    print("Tax:\t\t", end='$')
    print(format(tax, '4.2f'))
    
    #adds tax plus subtotal and outputs it
    total = subtotal + tax
    print("Total:", format(total, '7.2f'))
