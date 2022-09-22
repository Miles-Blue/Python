import math
import turtle as tur
import my_graphics as graph
import random

# ---------------------------------------------- #

def sales_tax():
    #sales tax accepts no arguments
    #calls upon sale_amount, state_tax, county_tax, total_tax, and total_sale
    #to output each amount based on user input
    
    amount = sale_amount() #calls sale amount
    state = state_tax(amount) #calls state tax
    county = county_tax(amount) #calls county tax
    tax = total_tax(state, county) #calls total tax
    total_sale(amount, tax) #calls total sale
    
def sale_amount():
    #accepts no arguments
    #prompts user for sale amount
    #returns sale amount after validation
    
    amount = float(input("Enter the sale amount: "))
    while amount < 0: #validates input
        print("Please enter a number greater than 0.")
        amount = float(input("Enter the sale amount: "))
    
    #prints amount formatted
    print("Your purchase price was:\t", end='$')
    print(format(amount, '10.2f'))
    return amount #returns amount
    
def state_tax(amount):
    #state tax accepts amount
    #determines state tax with amount by multiplying by .5
    #returns state
    
    state = amount * .05
    print("Your state tax amount is:\t", end='$')
    print(format(state, '10.2f'))
    return state
    
def county_tax(amount):
    #county tax accepts amount
    #determines county tax with amount by multiplying by .5
    #returns county
    
    county = amount * .025
    print("Your county tax amount is:\t", end='$')
    print(format(county, '10.2f'))
    return county
    
def total_tax(state, county):
    #accepts state and county
    #determines total tax by adding state and county
    #returns tax
    
    tax = state + county
    print("Your total tax is:\t\t", end='$')
    print(format(tax, '10.2f'))
    return tax
    
def total_sale(amount, tax):
    #accepts amount and tax as total tax
    #determines total sale by adding amount and tax
    #outputs the total
    
    sale = amount + tax
    print("Your total sale is:\t\t", end='$')
    print(format(sale, '10.2f'))
    
# ---------------------------------------------- #

def calories():
    #accept no arguments
    #calls on the function carb_grams and fat_grams
    #main function
    
    carb = carb_grams()
    fat = fat_grams()
    
    print("\nHere is your calorie intake for the day.")
    print("You consumed", carb, "calories worth of carbs today. Nice work...")
    print("You consumed", fat, "calories worth of fats today. Nice work...")
    
def carb_grams():
    #accepts no arguments
    #prompts user for grams of carbs
    #calculates caloric intake
    #returns carbs
    
    grams = int(input("How many grams of carbs did you consume? "))
    while grams < 0: #validates user input
        print("Please enter a number greater than 0.")
        grams = int(input("How many grams of carbs did you consume? "))
    carb = grams * 4
    return carb

def fat_grams():
    #accepts no arguments
    #prompts user of grams of fat
    #calculates caloric intake
    #returns fat
    
    grams = int(input("How many grams of fat did you consume? "))
    while grams < 0: #validates user input
        print("Please enter a number greater than 0.")
        grams = int(input("How many grams of fat did you consume? "))
    fat = grams * 9
    return fat

# ---------------------------------------------- #

def stadium_seating():
    #accepts no arguments
    #calls on Class A, Class B, and Class C to determine tickets
    #outputs total
    
    price_a = class_a()
    price_b = class_b()
    price_c = class_c()
    total = price_a + price_b + price_c
    
    print("\nThe total income sales from tickets is: $" + str(total))
    
def class_a():
    #accepts no arguments
    #prompts user for number of class a tickets sold
    #calculates price and returns price a
    
    tickets = int(input("Enter the number of Class A tickets sold: "))
    while tickets < 0: #validates user input
        tickets = int(input("Enter a valid number of Class A tickets sold: "))
    price_a = tickets * 20
    return price_a

def class_b():
    #accepts no arguments
    #prompts user for number of class b tickets sold
    #calculates price and returns price b
    
    tickets = int(input("Enter the number of Class B tickets sold: "))
    while tickets < 0: #validates user input
        tickets = int(input("Enter a valid number of Class B tickets sold: "))
    price_b = tickets * 15
    return price_b

def class_c():
    #accepts no arguments
    #prompts user for number of class a tickets sold
    #calculates price and returns price a
    
    tickets = int(input("Enter the number of Class C tickets sold: "))
    while tickets < 0: #validates user input
        tickets = int(input("Enter a valid number of Class C tickets sold: "))
    price_c = tickets * 10
    return price_c

# ---------------------------------------------- #

def paint_estimator():
    #accepts no arguments
    #calls on paint_gallons and labor_cost
    #outputs total cost
    
    feet = square_feet_paint() #assigns feet to a variable
    gallons = feet / 112 #calculates gallons
    paint_cost = paint_gallons(math.ceil(gallons)) #gets paint cost
    
    labor_cost = (feet / 112) * 35 * 8
    total_cost = paint_cost + labor_cost
    
    print("The cost breakdown to paint", feet, "square feet is:")
    print("------------------------------------------------------")
    print("Total cost of paint: $", format(paint_cost, '.2f'), sep='')
    print("Total labor cost: $", format(labor_cost, '.2f'), sep='')
    print("Total cost of the job is: $", format(total_cost, '.2f'), sep='')
    
    
def square_feet_paint():
    #accepts no arguments
    #prompts user for total square feet
    #returns feet
    
    feet = float(input("Please enter the total square feet to be painted: "))
    while feet < 0:
        feet = float(input("Please enter a number greater than 0: "))
    return feet
    
def paint_gallons(gallons):
    #accepts gallons for number of gallons
    #prompts user for gallon cost
    #determines total cost of paint
    #returns paint cost
    
    cost = float(input("How much is each gallon of paint? "))
    while cost < 0:
        cost = float(input("Please enter a number greater than 0: "))
    paint_cost = gallons * cost
    return paint_cost
    
# ---------------------------------------------- #

def math_quiz():
    #accepts no arguments
    #calls get_numbers and loops
    #loops while user inputs y
    
    cont = 'y'
    
    while cont == 'y':
        num1, num2 = get_number() #calls on get number for two random numbers
        answer = num1 + num2 #determines the real answer
        
        #formats the two random numbers into a problem
        print("\n\t", format(num1, '3.0f'))
        print("\t+", format(num2, '3.0f'), sep='')
        print("\t----")
        
        user_answer = int(input("Answer:")) #gets user answer
        
        if user_answer == answer: #determines if answer is wrong
            print("\nYou got it right!")
        else:
            print("\nDarn! So close. The actual answer was", answer)
            
        cont = input("\nContinue? (y/n)") #continues or ends the loop
        
def get_number():
    #accepts no arguments
    #generates two random integers from 1-200
    #returns number
    
    num1 = random.randint(1, 200)
    num2 = random.randint(1, 200)
    
    if num1 > num2: #formats num1 and num2
        return num1, num2
    else:
        return num2, num1

# ---------------------------------------------- #

GRAVITY = 9.8
SECONDS = 10

def time_loop():
    #accepts no arguments
    #loops 10 times
    #calling falling_distance every time
    
    #formats the chart
    print("Here is the distance an object will fall for 10 seconds")
    print("-------------------------------------------------------")
    
    for second in range(1, SECONDS+1):
        distance = falling_distance(second)
        if second == 10:
            print(second, " sec", format(distance, '14.2f'), "m", sep='')
        else:
            print(second, " sec", format(distance, '15.2f'), "m", sep='')
        
def falling_distance(time):
    #accepts time for calculating distance
    #uses 1/2*gt**2 to determine distance
    #returns distance
    
    distance = ((time ** 2) * GRAVITY )/2
    return distance

# ---------------------------------------------- #

CHOICES = ["scissors","paper", "rock", "lizard", "spock"]

def game():
    #accepts no arguments
    #calls comp_choice for computer choice
    #calls player_choice for player choice
    #calls winner to determine the winner
    
    cont = "y"
    
    while cont == "y": #repeats until user types n
        
        player = player_choice() #calls player choice
        computer = comp_choice() #calls comp_choice
        
        #formats player and computer choice
        print("\nYou chose.... ", player, ".", sep='')
        print("\nThe computer chose.... ", computer, '.\n', sep='')
        
        if not player in CHOICES: #checks for "cheating"
            print("The computer wins! You entered an invalid weapon. Cheater!")
        else:
            winner(player, computer)
        
        cont = input("\nPlay again? (y/n) ").lower() #determines whether or not to continue
        while cont != "y" and cont != "n": #validates input
            print("\nPlease enter a valid answer.")
            cont = input("Play again? (y/n)").lower()
    print("Thank you for playing")
    
def comp_choice():
    #accepts no arguments
    #gets a random choice from list CHOICES
    #returns computer
    
    computer = random.choice(CHOICES)
    return computer

def player_choice():
    #accepts no arguments
    #prompts user to input a choice from list
    #returns player
    
    player = input("Type your weapon of choice (rock, paper, scissors, lizard, spock): ")
    
    return player.lower()
    
def winner(player, computer):
    #receives player and computer
    #determines the winner
    #outputs who won with the corresponding message
    
    #assigns each outcome to a variable
    scissors_paper = "Scissors cuts paper."
    scissors_lizard = "Scissors decapitates lizard."
    
    paper_rock = "Paper covers rock."
    paper_spock = "Paper disproves spock."
    
    rock_lizard = "Rock crushes lizard."
    rock_scissors = "Rock crushes scissors."
    
    lizard_spock = "Lizard poisons spock."
    lizard_paper = "Lizard eats paper."
    
    spock_scissors = "Spock smashes scissors."
    spock_rock = "Spock vaporizes rock."
    
    if player == "scissors": #scissors
        if computer == "paper":
            print("You win!", scissors_paper)
        elif computer == "lizard":
            print("You win!", scissors_lizard)
        elif computer == "rock":
            print("The computer wins!", rock_scissors)
        elif computer == "spock":
            print("The computer wins!", spock_scissors)
        else:
            print("It's a tie!")
            
    elif player == "paper": #paper
        if computer == "rock":
            print("You win!", paper_rock)
        elif computer == "spock":
            print("You win!", paper_spock)
        elif computer == "scissors":
            print("The computer wins!", scissors_paper)
        elif computer == "lizard":
            print("The computer wins!", lizard_paper)
        else:
            print("It's a tie!")
                
    elif player == "rock": #rock
        if computer == "lizard":
            print("You win!", rock_lizard)
        elif computer == "scissors":
            print("You win!", rock_scissors)
        elif computer == "paper":
            print("The computer wins!", paper_rock)
        elif computer == "spock":
            print("The computer wins!", spock_rock)
        else:
            print("It's a tie!")
                
    elif player == "lizard": #lizard
        if computer == "spock":
            print("You win!", lizard_spock)
        elif computer == "paper":
            print("You win!", lizard_paper)
        elif computer == "scissors":
            print("The computer wins!", scissors_lizard)
        elif computer == "rock":
            print("The computer wins!", rock_lizard)
        else:
            print("It's a tie!")
                
    elif player == "spock": #spock
        if computer == "scissors":
            print("You win!", spock_scissors)
        elif computer == "rock":
            print("You win!", spock_rock)
        elif computer == "paper":
            print("The computer wins!", paper_spock)
        elif computer == "lizard":
            print("The computer wins!", lizard_spock)
        else:
            print("It's a tie!")

# ---------------------------------------------- #

SNOWMAN_OFFSET = -50
def drawSnowman():
    #accepts no arguments
    #drawSnowman acts as the main function
    #that calls on other functions to draw a snowman
    
    tur.speed(0)
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    drawFace()
    tur.done()
    
    
def drawBase():
    #accepts no arguments
    #draws the base of the snowman using circle
    
    graph.circle(0, -100, 85, "white")
    
def drawMidSection():
    #accepts no arguments
    #draws the mid section using circle
    
    graph.circle(0, 50, 65, "white")
    
def drawArms():
    #accepts no arguments
    #draws arms of snowman using line
    
    #right arm
    graph.line(62, 62, 110, 115, "black")
    graph.line(tur.xcor(), tur.ycor(), tur.xcor(), tur.ycor() + 25, "black")
    graph.line(tur.xcor(), tur.ycor() - 25, tur.xcor() + 15, tur.ycor() - 35, "black")
    
    #left arm
    graph.line(-62, 62, -110, 75, "black")
    graph.line(tur.xcor(), tur.ycor(), tur.xcor() - 30, tur.ycor() + 40, "black")
    graph.line(tur.xcor(), tur.ycor(), tur.xcor() - 7, tur.ycor() + 25, "black")
    graph.line(tur.xcor() + 7, tur.ycor() - 25, tur.xcor() - 7, tur.ycor() - 30, "black")
    
def drawHead():
    #accepts no arguments
    #draws head of the snowman
    #with eyes and a mouth
    
    graph.circle(0, 160, 45, "white")
    
def drawHat():
    #accepts no arguments
    #draws the hat with two rectangles
    
    graph.square(-45, 205, 15, "black")
    graph.square(30, 205, 15, "black")
    graph.square(-30, 205, 60, "black")
    
def drawFace():
    #accepts no arguments
    #draws eyes, a mouth, and a corncob pipe with smoke
    
    #eyes
    graph.circle(-15, 175, 5, "black")
    graph.circle(15, 175, 5, "black")
    
    #mouth
    graph.line(-25, 145, 25, 145, "black")
    
    #pipe
    graph.line(15, 145, 60, 125, "brown")
    tur.left(60)
    graph.square(65, 120, 10, "brown")
    
    #smoke
    tur.width(4)
    graph.line(63, 130, 75, 145, "gray")
    graph.circle(75, 147, 4, "white")
    graph.line(75, 145, 90, 155, "gray")
    graph.circle(90, 157, 4, "white")
    graph.line(90, 155, 105, 160, "gray")
    graph.circle(105, 162, 4, "white")
    graph.line(105, 160, 135, 165, "gray")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








