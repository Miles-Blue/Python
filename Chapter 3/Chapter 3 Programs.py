def test_average():
    #test average takes 3 inputs
    #calculates average of 3 inputs
    #if average is above 95, output a message
    
    HIGH_SCORE = 95
    
    #takes three inputs from user
    score1 = float(input("Enter the first score: "))
    score2 = float(input("Enter the second score: "))
    score3 = float(input("Enter the third score: "))
    
    #calculates average of inputs
    average = (score1 + score2 + score3) / 3
    print("The average score is: ", format(average, '.2f'))
    
    #determines if average is above 95
    #prints if true
    if average > HIGH_SCORE:
        print("Congragulations!")
        print("That is a high score!")
        
def auto_repair_payroll():
    #user inputs number of hours worked
    #user inputs hourly pay rate
    #if user worked more or less than 40 hours
    #will determine gross pay with or without bonus
    
    BASE_HOURS = 40
    
    #user inputs number of hours worked and pay rate
    hours_worked = float(input("Enter number of hours worked: "))
    rate = float(input("Enter hourly rate: "))
    
    #determines if hours is above 40
    #if it is, calculate for overtime
    if hours_worked > BASE_HOURS:
        extra_time = hours_worked - BASE_HOURS
        gross_pay = (BASE_HOURS * rate) + 1.5 * (extra_time * rate)
        print("You made: $" + format(gross_pay, '.2f'))
    else:
        gross_pay = hours_worked * rate
        print("You made: $" + format(gross_pay, '.2f'))
        
        
        
def password_verifier():
    #password verifier takes no arguments
    #user inputs a password
    #if input doesn't match prospero, password is invalid
    PASSWORD = "prospero"
    
    #gets input from user
    password_input = input("Please enter the password: ")
    
    #determines if password matches, and what to do
    if password_input == PASSWORD:
        print("Password accepted.")
    else:
        print("Password is invalid.")
        
def sort_names():
    #sort names takes no arguments
    #user inputs two names
    #program alphabetizes, and outputs them
    
    #takes user input, two names
    name1 = str(input("Enter the first name (last, first): "))
    name2 = str(input("Enter the second name (last, first): "))
    
    print("Here are the ames, sorted aphabetically.")
    
    #compare and outputthe names from greatest to least
    if name1 < name2:
        print(name1)
        print(name2)
    else:
        print(name2)
        print(name1)
        
def loan_qualify():
    #loan qualify accepts no arguments
    #program determines if one qualifies for a loan
    #uses nested if statements
    salary = float(input("Please enter your salary here: "))
    
    #determines if salary is enough
    if salary >= 30000:
        years_on_job = int(input("Please enter your years on job here: "))
        if years_on_job >= 2: #determines if years on job is enough
            print("You qualify for the loan.")
        else:
            print("You must have been on your current job for at least two years to qualify.")
    else:
        print("You must earn at least $30,000 per year to qualify.")
        
        
        
        