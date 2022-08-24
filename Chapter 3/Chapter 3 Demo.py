def demo_program():
    bool(input("True or False "))
    flag_var = True
    flag_var = False

    if flag_var:
        print("True!")
        
def even_number():
    number = int(input("Please enter an even number: "))
    
    if number % 2 == 0:
        print("The number is even!")
        #you could then perform the calculation
    else:
        print("I said to enter an even number!")
        #do not perform the calculation
    
def range_of_numbers():
    #range of numbers accepts no arguments
    #it will prompt the user for a number from 1 to 10
    #and output if the number is <> 5
    #and outpu t if the number is out of range
    
    #get input from the user
    number = int(input("Enter a number from 1 to 10: "))
    
    #check if the number is greater than 10
    if number > 10:
        print("Only enter numbers between 1 and 10.")
    elif number <= 5:
        print("Your number was between 1 and 5.")
    elif number > 5:
        print("Your number was between 6 and 10.")
        
def loan_qualify():
    #loan qualify accepts no arguments
    #program determines if one qualifies for a loan
    #uses nested if statements
    salary = float(input("Please enter your salary here: "))
    
    if salary >= 30000:
        years_on_job = int(input("Please enter your years on job here: "))
        if years_on_job >= 2:
            print("You qualify for the loan.")
        else:
            print("You must have been on your current job for at least two years to qualify.")
    else:
        print("You must earn at least $30,000 per year to qualify.")
        
        
        
        