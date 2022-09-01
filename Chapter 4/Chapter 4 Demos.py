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

def property_tax():
    #property tax accepts no arguments
    #it prompts the user for a lot number and loops while lot number != 0
    #promts the user for the property value
    #and calculates the property tax=value*PROP_TAX@.0065
    
    TAX = .0065
    
    end = input("Please enter a lot number (enter 0 to end): ")
    
    while end != 0:
        value = float(input("Please enter the property value: "))
        
    
    
    
    
    
    
    
    
    
    
    
    