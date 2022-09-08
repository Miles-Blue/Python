def bug_collector():
    #accepts no arguments
    #prompts user to input bugs collected five times
    #calculates and outputs total of five inputs
    
    #sets total number of bugs to 0
    total_bugs = 0
    
    #prompts for user input 5 times
    for num in range(1, 5+1):
        bugs = int(input("How many bugs did you collect on day "+str(num)+"? "))
        while bugs < 0: #checks for bugs being greater than 0
            print("\nPlease enter a number greater than 0.\n")
            bugs = int(input("How many bugs did you collect on day "+str(num)+"? "))
        total_bugs += bugs #accumulates bug total
        
    print("Great job, you collected", total_bugs,"bugs this week. You're the bug master!")
    
def distance_traveled():
    #accepts no arguments
    #prompts user to input speed in mph and hours traveled
    #calculates distance traveled for each hour
    
    #user inputs speed
    speed = int(input("Enter the speed of the vehicle in mph: "))
    while speed < 0: #validates user input
        print("Please enter a speed greater than 0 mph.")
        speed = int(input("Enter the speed of the vehicle in mph: "))

    #user inputs number of hours
    hours = int(input("Enter how many hours the vehicle traveled: "))
    while hours < 0: #validates user input
        print("Please enter a time greater than 0 hours.")
        hours = int(input("Enter how many hours the vehicle traveled: "))
    print("")
    
    #prints the format for the chart
    print("Hour \t\t Distance Traveled")
    print("-----------------------------------")
    
    #calculates and outputs distance traveled
    for num in range(hours):
        hour = num + 1
        print(hour, "\t\t", format(hour * speed, '10.0f'))
    
def pennies():
    #accepts no arguments
    #prompts user to input a number of days
    #program then doubles the pennie every day
    
    #assigns days to a variable
    days = int(input("How many days do you want to accure pennies? "))
    while days < 0: #validates user input
        print("Please enter more than 0 days.")
        days = int(input("How many days do you want to accure pennies? ")) 
    
    #prints format for chart
    print("Day \t\t Salary")
    print("------------------------------")
    
    for day in range(days):
        factor = 2 ** day
        day += 1
        print(day, "\t\t", "$" + format(.01 * factor, '.2f'))
    
def hogwarts_tuition():
    #accepts no arguments
    #calulates yearly tuition for each year of inflation
    
    #sets named constants
    YEARS = 5
    SEMESTER_TUITION = 8000
    INFLATION = 1.03
    
    year_tuition = float(SEMESTER_TUITION * 2)
    
    #prints format for chart
    print("Year \t\t Tuition Cost")
    print("------------------------------")
    
    #determines expected tuition with inlfation per year
    for year in range(1, YEARS+1):
        inflated_tuition = year_tuition * INFLATION
        print(year, "\t\t $", format(inflated_tuition , '.2f'))        
        year_tuition = inflated_tuition
    
def population():
    #accepts no arguments
    #prompts user for starting population, daily growth, and days
    #program then calculates for increasing population
    
    #takes user input and validates it
    population = float(input("Enter the starting population: "))
    while population < 0: #validates user input
        print("Please enter a population more than 0.")
        population = float(input("Enter the starting population: "))

    growth = float(input("Enter the percent of daily growth: "))
    while growth < 0: #validates user input
        print("Please enter more than 0 percent.")
        growth = float(input("Enter the percent of daily growth: "))
    growth_percent = (growth / 100) + 1

    days = int(input("Enter the number of days to simulate: "))
    while days < 1: #validates user input
        print("Please enter more than 0 days.")
        days = int(input("Enter the number of days to simulate: ")) 
    
    #prints format for chart
    print("Year \t\t Tuition Cost")
    print("------------------------------")
    
    for day in range(days):
        if day == 0:
            print(day+1, "\t\t", population)  
        else:
            projected = float(population * growth_percent)
            print(day+1, "\t\t", round(projected, day))       
            population = projected
    
def reverse_triangle():
    #accepts no arguments
    #prompts user to input desired size for a triangle
    #program prints an upside down triangle
    
    #prompts user for base size
    base = int(input("Enter the base size of the triangle: "))
    while base < 0: #validates user input
        print("Please enter a size higher than 0.")
        base = int(input("Enter the base size of the triangle: "))

        
    #outputs desired triangle, upside down
    for num in range(base, 0, -1):
        print('*' * num)
    
def stair_pattern2():
    #accepts no arguments
    #prompts user for desired number of steps
    #outputs a gradual widening of steps seen as @
    
    #prompts user for number of steps
    stairs = int(input("Enter the number of stairs: "))
    while stairs < 0: #validates user input
        print("Please enter more than 0 stairs.")
        stairs = int(input("Enter the number of stairs: "))

    #outputs desired number of stairs
    for stair in range(stairs):
        print('@' + ' ' * stair + '@')
    
def repeating_squares():
    #accepts no arguments
    #prompts user for number of squares
    #repeatedly draws that amount with an increasing rate
    
    INCREASE = 5
    BASE_SQUARE = 10
    
    #setup turtle
    import turtle as tur
    tur.speed(0)
    tur.goto(0,0)
    
    #gets user input
    squares = int(input("Enter desired number of squares: "))
    while squares < 0:
        print("Please enter more than 0 squares.")
        squares = int(input("Enter desired number of squares: "))
        
    #centers the square
    start_point = (squares * INCREASE + 20) / 2
    tur.penup()
    tur.forward(start_point)
    tur.right(90)
    tur.forward(start_point)
    tur.left(90)
    tur.pendown()
    
    for square in range(1, squares+1):
        bigger = BASE_SQUARE + (INCREASE * square)
        for num in range(4):
            tur.left(90)
            tur.forward(bigger)
    tur.done()
    

    
    
    
    
    
    
    
    
    
    