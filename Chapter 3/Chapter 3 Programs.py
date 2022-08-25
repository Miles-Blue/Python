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
        print("Your salary meets the requirements.")
        years_on_job = int(input("Please enter your years on job here: "))
        if years_on_job >= 2: #determines if years on job is enough
            print("You qualify for the loan.")
        else:
            print("You must have been on your current job for at least two years to qualify.")
    else:
        print("You must earn at least $30,000 per year to qualify.")
        
def grader():
    #grader accepts no arguments
    #user inputs a test score
    #program determines the letter grade
    grade = int(input("Enter your test grade here: "))
    
    #goes through if statements to determine letter grade
    if grade >= 90:
        print("Your grade is A.")
    else:
        if grade >= 80:
            print("Your grade is B.")
        else:        
            if grade >= 70:
                print("Your grade is C.")
            else:
                if grade >= 60:
                    print("Your grade is D.")
                else:
                    print("Your grade is F.")
                    
def grader2():
    #grader accepts no arguments
    #user inputs a test score
    #program determines the letter grade
    grade = int(input("Enter your test score here: "))
    
    #goes through if statements to determine letter grade
    if grade >= 90:
        print("Your grade is A.")
    elif grade >= 80:
        print("Your grade is B.")
    elif grade >= 70:
        print("Your grade is C.")
    elif grade >= 60:
        print("Your grade is D.")
    else:
        print("Your grade is F.")
        
def loan_qualify2():
    #loan qualify accepts no arguments
    #program determines if one qualifies for a loan
    #uses nested if statements
    salary = float(input("Please enter your salary here: "))
    years_on_job = int(input("Please enter your years on job here: "))
    
    #determines if salary is enough
    if salary >= 30000 and years_on_job >= 2:
        print("You qualify for the loan.")
    else:
        print("You must earn at least $30,000 per year to qualify.")
        print("You have to work for at least 2 years to qualify.")
        
def loan_qualify3():
    #loan qualify accepts no arguments
    #program determines if one qualifies for a loan
    #uses nested if statements
    salary = float(input("Please enter your salary here: "))
    years_on_job = int(input("Please enter your years on job here: "))
    
    #determines if salary is enough
    if salary >= 30000 or years_on_job >= 2:
        print("You qualify for the loan.")
    else:
        print("You must earn at least $30,000 per year to qualify.")
        print("You have to work for at least 2 years to qualify.")
        
def hit_the_target():
    #hit the target accepts no arguments
    #user inputs a direction to aim turtle
    #turtle goes forward and if it hits target, congrats
    
    
    #Named constants
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TARGET_LLEFT_X = 100
    TARGET_LLEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    #set up turtle
    import turtle as tur
    tur.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    #Draw the target
    tur.hideturtle()
    tur.speed(0)
    tur.penup()
    tur.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    tur.pendown()
    tur.setheading(EAST)
    tur.forward(TARGET_WIDTH)
    tur.setheading(NORTH)
    tur.forward(TARGET_WIDTH)
    tur.setheading(WEST)
    tur.forward(TARGET_WIDTH)
    tur.setheading(SOUTH)
    tur.forward(TARGET_WIDTH)
    tur.penup()
    
    #resets turtle position
    tur.goto(0, 0)
    tur.setheading(EAST)
    tur.pendown()

    #user inputs angle and force
    angle = float(input("Enter the desired angle: "))
    force = float(input("Enter the desired force: "))

    #calculates the distance
    distance = force * FORCE_FACTOR
    
    #moves the turtle
    tur.left(angle)
    tur.forward(distance)
    
    #determines where the turtle lands and
    #determines if it landed in the target
    if tur.xcor() >= 100 and tur.xcor() <= 125\
    and tur.ycor() >= 250 and tur.ycor() <= 275:
        print("You hit the target!")
    else:
        print("You missed the target!")
    tur.done()

