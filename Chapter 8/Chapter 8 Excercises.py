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
            user = input("Enter a date valid in the format mm/dd/yyyy: ")
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
    
    #List of possible numbers
    num_list = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5',
                '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']
    
    #Continues the process
    while True:
        
        user = input("Enter a telphone number in the form of XXX-XXX-XXXX ")
        
        #Exception handling
        try:
            
            #Handles the formatting for the number
            if user[3] != '-' and user[7] != '-' and user.count('-') != 2:
                continue
            
            #Replaces the digit if it's a letter
            for digit in user:
                if digit.isalpha():
                    user = user.replace(digit, num_list[ord(digit.lower()) - 97])
            
            #Outputs the new number
            print(f"\nHere is your converted telephone number: {user}")
            break #Stops the loop
        
        except:
            continue

#----------------------------------------------------------------------------------------#

def avg_num_words():
    #accepts no arguments
    #opens text.txt and counts the number of words
    #the number of sentences, and the average length of words
    #and outputs it
    
    #Opens the test file
    try:
        text_file = open('text.txt', 'r')
        
    except Exception as err:
        print(err)
    
    #Formats it into one line
    string = text_file.read().replace('\n', ' ')
    
    #Gets the amount of words and sentences
    words = string.count(' ') + 1
    sentences = string.count('.')
    
    #Gets the average words per sentence
    avg_words = words / sentences
    
    #Outputs the results
    print(f"The file text.txt has {words} words.")
    print(f"There are {sentences} total sentences.")
    print(f"The average number of words per sentence is: {avg_words:.2f}")
    
    #Closes the file
    text_file.close()
    
#----------------------------------------------------------------------------------------#















































    
    
    
    
    
    
    
    
    