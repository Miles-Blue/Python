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
    pkg_buns = total / BUNS_PKG
    pkg_hdog = total / HDOG_PKG
    buns_left = total % 8
    hdog_left = total % 10
    buns_extra = 8 * int(pkg_buns + 1) - total
    hdog_extra = 10 * int(pkg_hdog + 1) - total
    
    #determines and outputs hotdogs, buns, hotdogs left, and buns left
    if buns_left == 0 and hdog_left == 0:
        print("You will need", int(pkg_buns), "packages of buns.")
        print("You will need", int(pkg_hdog), "packages of hotdogs.")
    elif buns_left != 0 and hdog_left == 0:
        print("You will need", int(pkg_buns + 1),"packages of buns with", int(buns_extra), "bun(s) left.")
        print("You will need", int(pkg_hdog), "packages of hotdogs.")
    elif hdog_left != 0 and buns_left == 0:
        print("You will need", int(pkg_buns), "packages of buns.")
        print("You will need", int(pkg_hdog + 1),"packages of buns with", int(hdog_extra), "hotdog(s) left.")
    elif buns_left != 0 and hdog_left != 0:
        print("You will need", int(pkg_buns + 1),"packages of buns with", int(buns_extra), "bun(s) left.")
        print("You will need", int(pkg_hdog + 1),"packages of buns with", int(hdog_extra), "hotdog(s) left.")

def time_calculator():
    #time calculator accepts no arguments
    #prompts user to input a random number
    #program then calculates those seconds into
    #days, hours, minutes, seconds
    
    DAY = 86400
    HOUR = 3600
    MINUTE = 60
    
    #prompts user to input seconds
    seconds = int(input("Enter a number of seconds. "))
    
    #determines days, hours, minutes, and seconds
    #then outputs accordingly
    if seconds >= 0:
        if seconds >= DAY:
            print(int(seconds / DAY), "day(s).")
            day_remainder = seconds % DAY
            if day_remainder >= HOUR:
                print(int(day_remainder / HOUR), "hour(s).")
                hour_remainder = day_remainder % HOUR
                if hour_remainder >= MINUTE:
                    print(int(hour_remainder / MINUTE), "minute(s).")
                    minute_remainder = hour_remainder % MINUTE
                    if minute_remainder > 0:
                        print(minute_remainder, "second(s).")
                    else:
                        print()
                else:
                    print(hour_remainder, "second(s).")
            else:
                if day_remainder >= MINUTE:
                    print(int(day_remainder / MINUTE), "minute(s).")
                    minute_remainder = day_remainder % MINUTE
                    if minute_remainder > 0:
                        print(minute_remainder, "second(s).")
                    else:
                        print()
                else:
                    print(day_remainder, "second(s).")
        else:
            if seconds >= HOUR:
                print(int(seconds / HOUR), "hour(s).")
                hour_remainder = seconds % HOUR
                if hour_remainder >= MINUTE:
                    print(int(hour_remainder / MINUTE), "minute(s).")
                    minute_remainder = hour_remainder % MINUTE
                    if minute_remainder > 0:
                        print(minute_remainder, "second(s).")
                    else:
                        print()
                else:
                    print(hour_remainder, "second(s).")
            else:
                if seconds >= MINUTE:
                    print(int(seconds / MINUTE), "minute(s).")
                    minute_remainder = seconds % MINUTE
                    if minute_remainder > 0:
                        print(minute_remainder, "second(s).")
                    else:
                        print()
                else:
                    print(seconds, "second(s).")
    else:
        print("That's not a valid answer silly billy.")
    
def leap_year():
    #leap year accepts no arguments
    #prompts user to enter a year
    #program then determines if it is a leap year
    #then outputs the answer plus number of days in February
    
    years = int(input("Enter a year here: "))
    
    #determines if number inputted is a leap year or not
    if years >= 0:
        if years % 100 == 0:
            if years % 400 == 0:
                print(years, "is a leap year. There are 29 days in the month of February.")
            else: 
                print(years, "is not a leap year. There are 28 days in the month of February.")
        else:
            if years % 4 == 0:
                print(years, "is a leap year. There are 29 days in the month of February.")
            else:
                print(years, "is not a leap year. There are 28 days in the month of February.")
    else:
        print(years, "is not a valid number.")
        

    
    
    
    
    
    
    