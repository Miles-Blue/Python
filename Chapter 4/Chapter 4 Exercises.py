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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    