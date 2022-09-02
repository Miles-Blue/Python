def loop_example():
    #loop example accepts no arguments
    #it takes input from the user for number of loops
    #and loops the number of times the user inputs
    
    keep_going = 'y' #prime the sentinel to y
    
    while keep_going == 'y': #sentinel or user input loop
        number = int(input("Enter the number of loops to run: "))
        counter = 0 #prime the accumulator
        while counter < number: #counted loop
            counter = counter + 1 #counter += 1
            print("This is loop number", counter)
        keep_going = input("Keep going? (y/n)")
        
def commission():
    #commission accepts no arguments
    #prompts user to input sale and % rate
    #calculates and ouptus the results
    
    keep_going = 'y'
    
    while keep_going == 'y':
        sale_amount = float(input("Enter the sale amount: "))
        rate = float(input("Enter the commission rate: "))
        print("The commission is $" + format(sale_amount * rate, '.2f'))
        keep_going = input("Do you want to calculate another? (y/n)")
    
def temperature():
    #temperature accepts no arguments
    #prompts user to input a temperature
    #determines if the temp is too high, if so will keep on dropping
    
    MAX_TEMP = 102.5
    user_temp = float(input("Please enter the current substance temperature in degrees Celcius: "))
    
    #while input is above max temp, keep running
    while user_temp > MAX_TEMP:
        print("\nThe temperature is too high.")
        print("Turn the thermostat down and wait for it to cool.")
        print("Then waif 5 minutes and measure again")
        user_temp = float(input("\nPlease enter the current substance temperature in degrees Celcius: "))
    print("\nThe temperature is acceptable.")
    print("Measure again in 15 minutes.")
       
       
       
       
def loop_example2():
    #accepts no arguments
    #it uses a for loop to loop 5 times
    #and outputs a number
    
    for item in range(5):
        print(item)

def loop_example3():
    #accepts no arguments
    #it uses a for loop to loop through 1, 2, 3, 4
    #and outputs the loop
    
    for num in [1, 2, 3, 4]:
        print("I am holding the value", num)
        print("I will now release num")
        print("...")
        
def simple_loop1():
    for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(num)
    
def loop_example4():
    
    for num in range(1, 10+1):
        print(num)
    
def simple_loop2():
    #accepts no arguments

    print("I will output all odd numbers from 1-9")
    
    for num in [1, 3, 5, 7, 9]:
        print(num)
        
def simple_loop3():
    #accepts no arguments
    
    for item in ["Steve", "Tony", "Thor", "Wanda"]:
        print(item)
    
def simple_loop1_update():
    
    for num in range(1, 10+1, 2):
        print(num)
    
    
def hello_world_loop():
    #accepts no arguments
    
    for item in range(5):
        print("Hello World!")
    
def squares():
    #accepts no arguments
    #ouputs 1 through 10
    #along with their squares
    
    print("Number \t Square")
    print("---------------")
    
    for num in range(1, 10+1):
        print(num, '\t', num ** 2)
    
def speed_converter():
    #accepts no arguments
    #displays 60kph through 130kph
    #also displays speeds in mph
    
    print("KPH \t MPH")
    print("----------")
    
    for num in range(60, 131, 10):
        mph = num * 0.6214
        print(num, '\t', format( mph , '.1f'))

def user_squares1():
    #accepts no arguments
    #prompts user for the number of squares
    
    print("This program will display a list of numbers")
    print("(starting at 1) and their squares")
    end = int(input("How many squares? "))
    print("\nNumber\tSquare")
    print("----------------")
    
    for num in range(1, end + 1):
        square = num**2
        print(num,'\t', square)
    
def user_squares2():
    #accepts no arguments
    #prompts user for the number of squares
    #also prompts user for last number
    
    print("This program will display a list of numbers")
    print("(starting at 1) and their squares")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    print("\nNumber\tSquare")
    print("----------------")
    
    for num in range(start, end + 1):
        square = num**2
        print(num,'\t', square)
    
def sum_numbers():
    #accepts no arguments
    #prompts user for MAX amount of different numbers
    #then adds them together for a total
    
    MAX = 5
    total = 0.0
    
    for item in range(MAX):
        number = float(input("Please enter a number: "))
        total += number
    print("The total of your", MAX, "numbers is: ", total)

#def property_tax():
    #property tax accepts no arguments
    #it prompts the user for a lot number and loops while lot number != 0
    #promts the user for the property value
    #and calculates the property tax=value*PROP_TAX@.0065
    
   # TAX = .0065
    
   # end = input("Please enter a lot number (enter 0 to end): ")
    
    #while end != 0:
        #value = float(input("Please enter the property value: "))
        
def gross_pay():
    #gross pay accepts no arguments
    #it takes input from the user in the form of hours worked and pay rate
    #it calculates and outputs the gross pay
    
    hours = int(input("Enter the number of hours worked for 1 week: "))
    
    pay_rate = int(input("Enter the hoursly rate: "))
    
    gross_pays = hours * pay_rate
    
    #Output gross pay
    print("Gross pay: $", format(gross_pays, '.2f'), sep=(' '))

def retail_no_validation():
    
    MARK_UP = 1.25
    another = 'y'
    
    while another == 'y' or another == 'Y':
        wholesale = float(input("Enter the wholesale cost: "))
        
        retail = wholesale * MARK_UP
        
        print("Retail price: $", format(retail, '.2f'), sep=(' '))
        
        another = input("Do you want to enter another item?" +
                        "(Enter y for yes)")
        
def retail_with_validation():
    
    MARK_UP = 1.25
    another = 'y'
    
    while another == 'y' or another == 'Y':
        wholesale = float(input("Enter the wholesale cost: "))
        
        #validates that number is greater than 0
        while wholesale < 0:
            wholesale = float(input("Please enter a number greater than 0: "))
            
        retail = wholesale * MARK_UP
        
        print("Retail price: $", format(retail, '.2f'), sep=(' '))
        
        another = input("Do you want to enter another item?" +
                        "(Enter y for yes or n for no)")


def test_score_average():
    #test score average accepts no arguments
    #prompts user to input # of students and # of scores per student
    
    student = int(input("How many students? "))
    tests = int(input("How many tests per student? "))
    
    for student in range(1, student + 1):
        total = 0.0
        
        print("Student number", student)
        print("--------------")
        for test in range(1, tests + 1):
            print("Test number", test, end=' ')
            score = int(input(": "))
            total += score
            
        avg_tests = total / tests
        print("The average for student number", student, "is: ", format(avg_tests, '.2f'))
        print()
        
def rectangle_pattern():
    #rectangle pattern accepts no arguments
    #prompts user to enter a # of rows and columns
    
    rows = int(input("Enter the number of rows to print: "))
    columns = int(input("Enter the number of columns ot print: "))
    
    for row in range(rows):
        for col in range(columns):
            print('*', end='')
        print()
    
def triangle_pattern():
    
    start = 1
    stop = int(input("Enter the base size of the triangle: "))
    
    for num in range(start, stop+1):
        print('*' * num)
        

def stair_pattern():
    
    start = 0
    stop = int(input("Enter the number of stairs: "))
    
    #for num in range(start, stop+1):
        #print('\t' * num, '*')
    for num in range(start, stop+1):
        for num2 in range(start, num):
            print(' ', '*')

def concentric_circles():
    import turtle as tur
    num_circles = int(input("Enter the number of circles: "))
    STARTING_RADIUS = 20
    OFFSET = 10
    ANIMATION_SPEED = 0
    tur.speed(ANIMATION_SPEED)
    radius = STARTING_RADIUS
      
    for circle in range(num_circles):
        tur.circle(radius)
        tur.penup()
        tur.right(90)
        tur.forward(OFFSET)
        tur.left(90)
        tur.pendown()
        radius += OFFSET
    tur.done()
    
def spiral_circles():
    
    import turtle as tur
    
    NUM_CIRCLES = 36
    RADIUS = 100
    ANGLE = 10
    
    for x in range(NUM_CIRCLES):
        tur.circle(RADIUS)
        tur.left(10)




