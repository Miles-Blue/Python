def sum_of_digits():
    #accepts no arguments
    #prompts user for a list of numbers
    #outputs the total of the numbers
    
    total = 0
    
    #Gets user input
    numbers = input("Please enter a string of single digit numbers without spaces: ")
    
    #Determines if the input consists of numbers
    while not numbers.isnumeric():
        numbers = input("Please only enter numbers: ")
     
    #Accumulates total
    for number in numbers:
        total += int(number)
    
    #Outputs the total
    print(f"The sum of your string is: {total}")

#----------------------------------------------------------------------------------------#

def date_converter():
    #accepts no arguments
    #prompts user to input a date in the form of mm/dd/yyyy
    #prints the date in the format of Month Day, Year
    
    #List of months
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    #Accumulator
    counter = 0
    
    #Continues the process
    while True:
        
        #Accumulates
        counter += 1
        
        #Changes the prompt based on if an error happened
        if counter >= 2:
            user = input("Enter a date valid in the format mm/dd/yyy: ")
        else:
            user = input("Enter a date in the format mm/dd/yyy: ")
        
        #Splits the input into a list
        date_list = user.split('/')
        
        #Exception handling
        try:
            
            #Handles the formatting for the dates
            if not int(date_list[0]) > 0 and not int(date_list[0]) > 0:
                continue
            if not int(date_list[2]) > 999:
                continue
            
            #Gets the indext of the month
            month = int(date_list[0])
            
            #Outputs the date
            print(f"\nThe date is: {MONTHS[month - 1]} {int(date_list[1])}, {int(date_list[2])}")
            break #Stops the loop
        
        except:
            continue
    
#----------------------------------------------------------------------------------------#

def morse_code():
    #accepts no arguments
    #prompts user to input a message
    #the program encodes the input into morse code
    #and outputs it
    
    #List of all possible letters
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #List of all possible morse code letters
    M_LETTERS = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--',
              '-•', '---', '•--•', '--•-', '•-•', '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••']
    
    #List of all possible morse code numbers
    M_NUMBERS = ['-----', '•----', '••---', '•••---', '••••-', '•••••', '-••••', '--•••', '---••', '----•']
    
    #continue for a later while statement
    cont = True
    
    #User input
    message = input("Enter a message to encode to morse code: ")
    
    #Continues while cont is True
    while cont:
        
        #Validates that message only contains numbers, letters, and spaces
        for letter in message:
            if not letter.isalnum() and not letter.isspace():
                cont = True
                message = input("Enter only numbers and letters: ")
            else:
                cont = False
    
    #Converts message into morse code form and outputs it
    for letter in message:
        
        #Handles the numbers
        if letter.isdigit():
            print(M_NUMBERS[int(letter)], end=' ')
            
        #Handles the letters
        elif letter.isalpha():
            index = LETTERS.index(letter.lower())
            print(M_LETTERS[index], end=' ')
        
        #Handles the spaces
        elif letter.isspace():
            print('/', end=' ')
            
#----------------------------------------------------------------------------------------#

def phone_converter():
    #accepts no arguments
    #prompts user to input a date in the form of mm/dd/yyyy
    #prints the date in the format of Month Day, Year
    
    TWO = ['a', 'b', 'c']
    THREE = ['d', 'e', 'f']
    FOUR = ['g', 'h', 'i']
    FIVE = ['j', 'k', 'l']
    SIX = ['m', 'n', 'o']
    SEVEN = ['p', 'q', 'r', 's']
    EIGHT = ['t', 'u', 'v']
    NINE = ['w', 'x', 'y', 'z']
    
    #Continues the process
    while True:
        
        user = input("Enter a telphone number in the form of XXX-XXX-XXXX ")
        
        #Splits the input into a list
        number_list = user.split('-')
        
        #Exception handling
        try:
            
            #Handles the formatting for the number
            if not len(number_list[0]) == 3 and not len(number_list[1]) == 3 and len(number_list[2]) == 4:
                continue
            
            for number in number_list:
                for digit in number:
                    if digit.isalpha():
                        if digit.lower() in TWO:
                            number.replace(digit, '2')
                        elif digit.lower() in THREE:
                            number.replace(digit, '3')
                        elif digit.lower() in FOUR:
                            number.replace(digit, '4')
                        elif digit.lower() in FIVE:
                            number.replace(digit, '5')
                        elif digit.lower() in SIX:
                            number.replace(digit, '6')
                        elif digit.lower() in SEVEN:
                            number.replace(digit, '7')
                        elif digit.lower() in EIGHT:
                            number.replace(digit, '8')
                        elif digit.lower() in NINE:
                            number.replace(digit, '9')
            
            #Outputs the date
            print(f"\nHere is your converted telephone number: {number_list[0]}-{number_list[1]}-{number_list[2]}")
            break #Stops the loop
        
        except:
            continue




















































    
    
    
    
    
    
    
    
    