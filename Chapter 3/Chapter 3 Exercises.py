def day_converter():
    #day converter accepts no arguments
    #prompts user to input a number between 1 and 7
    #program converts input into a day of the week in spanish
    
    #user inputs number between 1 and 7
    day = int(input("Enter day of the week(Monday-Sunday) from 1-7: "))
    
    #determines the day and outputs it in spanish
    if day == 1:
        print("Today is 'Lunes'")
    elif day == 2:
        print("Today is 'Martes'")
    elif day == 3:
        print("Today is 'Miércoles'")
    elif day == 4:
        print("Today is 'Jueves'")
    elif day == 5:
        print("Today is 'Viernes'")
    elif day == 6:
        print("Today is 'Sábado'")
    elif day == 7:
        print("Today is 'Domingo'")
    else:
        print(day,"Is not a valid number.")
        
def roman_numerals():
    #roman numerals accepts no arguments
    #prompts the user to input a number 1-10
    #program outputs the respective roman number
    
    #user inputs number 1-10
    r_number = int(input("Enter a number 1-10: "))
    
    #determines the day and outputs it in spanish
    if r_number == 1:
        print("I")
    elif r_number == 2:
        print("II")
    elif r_number == 3:
        print("III")
    elif r_number == 4:
        print("IV")
    elif r_number == 5:
        print("V")
    elif r_number == 6:
        print("VI")
    elif r_number == 7:
        print("VII")
    elif r_number == 8:
        print("VIII")
    elif r_number == 9:
        print("IX")
    elif r_number == 10:
        print("X")
    else:
        print(r_number,"Is not a valid number.")
        
def color_mixer():
    #color mixer accepts no arguments
    #promps user to input two colors
    #program then outputs a product color
    
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"
    
    color1 = input("Enter your first primary color: ")
    color2 = input("Enter your second primary color: ")
    
    #determines color output
    if (color1 == RED and color2 == BLUE) or (color1 == BLUE and color2 == RED):
        print("Your color is purple.")
    elif (color1 == RED and color2 == YELLOW) or (color1 == YELLOW and color2 == RED):
        print("Your color is orange.")
    elif (color1 == YELLOW and color2 == BLUE) or (color1 == BLUE and color2 == YELLOW):
        print("Your color is green.")
    elif (color1 == color2):
        print("You should know that makes", color1)
    else:
        print("That is not a valid color.")
    
        
def hot_dog():
    #hot dog accepts no arguments
    #program prompts user to input people and hotdogs per person
    #program calculates how many packages required
    
    BUNS_PKG = 8
    HDOG_PKG = 10
    
    #gets user input
    people = int(input("How many people will be attending? "))
    hdog = int(input("How many hotdogs per person? "))
    
    #determines how many hotdogs are needed
    total = people * hdog
    buns_left = total % 8
    hdog_left = total % 10
    
    if buns_left == 0 and hdog_left == 0:
        print("You will need", int(total / BUNS_PKG), "packages of buns.")
        print("You will need", int(total / HDOG_PKG), "packages of hotdogs.")
    elif buns_left != 0:
        print("You will need", (int(total / BUNS_PKG) + 1),"packages of buns with", buns_left, "buns left.")
        print("You will need", int(total / HDOG_PKG), "packages of hotdogs.")
    elif hdog_left != 0:
        print("You will need", int(total / BUNS_PKG), "packages of buns.")
        print("You will need", (int(total / HDOG_PKG) + 1),"packages of buns with", hdog_left, "hotdogs left.")
    elif buns_left != 0 and hdog_left != 0:
        print("You will need", (int(total / BUNS_PKG) + 1),"packages of buns with", buns_left, "buns left.")
        print("You will need", (int(total / HDOG_PKG) + 1),"packages of buns with", hdog_left, "hotdogs left.")

    
    
    
    
    
    
    
    
    
    
    
    
    