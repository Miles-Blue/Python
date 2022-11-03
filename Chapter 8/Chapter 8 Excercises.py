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
            if not int(date_list[2]) > 999 and len(date_list[2]) != 4:
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

def igpay_atinlay():
    #accepts no arguments
    #prompts user for a sentence and outputs it
    #it then translates it into pig latin and outputs it
    
    #User prompt
    message = input("Enter a message to convert to pig latin: ")
    
    #Input validation
    while any(char.isdigit() for char in message):
        message = input("Only input letters and words: ")

    #Splits the message into a list
    message_list = message.split(' ')
    
    #For loop to change each word
    for word in message_list:
        
        #Moves the first letter to the end with 'ay'
        remove_letter = word.replace(word[0], '')
        new_word = remove_letter + word[0] + 'ay'
        
        #Moves the period to the end of the word if there is one
        if '.' in new_word:
            new_word = new_word.replace('.', '')
            new_word += '.'
        
        #Gets the index of the word
        index = message_list.index(word)
        
        #Replaces the word
        message_list[index] = new_word
    
    #Formats the output
    print("Here is your message in pig latin:")
    
    #Outputs the translated message in one line
    for word in message_list:
        print(word.upper(), end=' ')

#----------------------------------------------------------------------------------------#

def pb_main():
    #accepts no arguments
    #opens the text file pbnumbers.txt
    #counts the amount that each number appears
    #and outputs the 10 most and least frequent
    
    #Assigns an empty list
    lotto_list = []
    
    #Tries to open the file
    try:
        pb_file = open('pbnumbers.txt', 'r')
        
    except Exception as err: #Error checking
        print(err)
    
    #Splits the lines and appends them to a list
    for line in pb_file:
        line = line.rsplit(' ', 1)[0]
        lotto_list.append(line)
        
    pb_file.close()
    
    #Joins them in the list
    lotto = " ".join(lotto_list)
    
    #Splits them into single letter strings
    lotto_list = lotto.split(' ')
    
    #Calls pb_frequency
    freq = pb_frequency(lotto_list)
    
    #Calls and outputs the most common
    print("The 10 most frequently occurring lotto numbers:")
    pb_most_common(freq)
    
    #Prints a space
    print()
    
    
    #Calls and outputs the least common
    print("The 10 least frequently occurring lotto numbers:")
    pb_least_common(freq)
            
def pb_frequency(lotto_list):
    #accepts lotto_list as an argument
    #counts how many times each number appears
    #sorts them by amount
    #outputs the list
    
    #Assigns an empty list
    lotto_count = []
    
    #Determines what number to use
    for num in range(1, 70):
        if num < 10:
            new_num = '0' + str(num)
        else:
            new_num = str(num)
        
        #Counts the number of times the number occurs
        counter = lotto_list.count(new_num)
        
        #Adds the number plus its count to a list
        lotto_count.append([new_num, counter])
      
    #Returns the list sorted
    return sorted(lotto_count, key=lambda t: t[1])

def pb_most_common(freq):
    #accepts freq as an argument
    #determines the 10 most common numbers, ordered by frequency
    #outputs the list
    
    #Gets the most common numbers
    most_common = freq[-10:]
    
    #Outputs the numbers
    for num in most_common:
        print(num[0])
        
def pb_least_common(freq):
    #accepts pb_list as an argument
    #determines the 10 least common numbers, ordered by frequency
    #outputs the list
    
    #Gets the least common numbers
    least_common = freq[:10]
    
    #Outputs the numbers
    for num in least_common:
        print(num[0])

#----------------------------------------------------------------------------------------#

def gas_price():
    #accepts no arguments
    #opens GasPrices.txt
    #assigns each line to the list
    #calls all of the other programs
    
    #Opens the file
    try:
        prices_file = open("GasPrices.txt", "r")
    except Exception as err:
        print(err)
     
    #Assigns empty lists
    prices_list = []
    dates_list = []
    
    #Appends all of the contents to two different lists
    for line in prices_file:
        line = line.replace("\n", "")
        line = line.rsplit(':')
        dates_list.append(line[0][:-5])
        prices_list.append(line)
    prices_file.close()
    
    #Keeps looping while the user inputs a choice
    while True:
        print("\nWhat would you like to do?")
        print("1) Output Average Price")
        print("2) Output Highest and Lowest Price per Year")
        print("3) Print List in Ascending Order to a File")
        print("4) Print List in Descending Order to a File")
        print("5) Quit")
        
        #Determines if the input is an integer
        try:
            user = int(input("Choice: "))
        except:
            print("Only enter numbers.")
            continue
        
        #Calls program determined by user
        if user == 1:
            avg_price(prices_list)
        elif user == 2:
            per_year(prices_list, dates_list)
        elif user == 3:
            low_to_high(prices_list)
        elif user == 4:
            high_to_low(prices_list)
        elif user == 5:
            print("Thank you for using our program!")
            break
        
        #If the number isn't within range
        else:
            print("Only enter numbers within 1-5.")
            continue
    
    
def avg_price(prices_list):
    #accepts prices_list as an argument
    #gets the average price per year
    #outputs the average
    
    #Assigns variables
    total = 0
    counter = 0
    year = 1993
    
    #Sets two blank lists
    new_list = []
    avg_list = []
    
    #Appends the items without the month and day
    for item in prices_list:
        item[0] = item[0].replace(item[0][:-4], "")
        new_list.append(item)
    
    #Counts the total and the number of things
    for item in new_list:
        if item[0] == str(year):
            total += float(item[1])
            counter += 1
        else:
            
            #Gets the average
            average = total / counter
            
            #Appends the averages formatted to avg_list
            avg_list.append([year, format(average, '.2f')])
            
            #Resets the total and counter
            total = 0
            counter = 0
            
            #Continues to the next year
            year += 1
    
    #Prints the average price of each year
    for item in avg_list:
        print(f"The average price in {item[0]} was ${item[1]:}")

def per_year(prices_list, dates_list):
    #accepts prices_list and dates_list as arguments
    #determines the highest and lowest prices each year
    
    #Sets the starting year
    year = 1993
    
    #Sets two blank lists
    new_list = []
    high_low = []
    
    #Appends each item without month or day to a list
    for item in prices_list:
        item[0] = item[0].replace(item[0][:-4], "")
        new_list.append(item)
    
    #Sorts it by the money, then by the year
    new_list = sorted(new_list, key=lambda t: t[1])
    new_list = sorted(new_list, key=lambda t: t[0])
    
    #Appends each money value to the high_low list
    for item in new_list:
        if item[0] == str(year):
            high_low.append(item)
        else:
            
            #Gets the lowest value, and the highest value
            low = format(float(high_low[0][1]), '.2f')
            high = format(float(high_low[-1][1]), '.2f')
            
            #Gets the index of each of these values
            low_index = prices_list.index(high_low[0])
            high_index = prices_list.index(high_low[-1])
            
            #outputs the highest and lowest prices with their dates
            print(f"The lowest and highest prices in {item[0]} were on {dates_list[low_index]} with ${low} and on {dates_list[high_index]} with ${high}.")
            
            #Resets the list
            high_low = []
            
            #Continues to the next year
            year += 1

def low_to_high(prices_list):
    #accepts prices_list as an argument
    #sorts the list from lowest to highest by price
    #prints it all to GasLowToHigh.txt
    
    #Exception handling
    try:
        #Opens the file
        file = open('GasLowToHigh.txt', 'a')
    
    except Exception as err: #Error handling
        print(err)
    
    #Sorts the list in ascending order
    sorted_list = sorted(prices_list, key=lambda t: t[1])
    
    #Joins the items with a colon
    for item in sorted_list:
        item = ':'.join(item)
    
    #Formats each item and writes it to the file
    for item in sorted_list:
        item = str(item).replace(str(item)[0:2], '').replace(str(item)[12:16], ': $').replace(str(item)[-2:], '')

        file.write(item + '\n')
    
    #Outputs a final message
    print("Printed the list in ascending order to GasLowToHigh.txt.")
    
    #Closes the file
    file.close()

def high_to_low(prices_list):
    #accepts prices_list as an argument
    #sorts the list from lowest to highest by price
    #prints it all to GasHighToLow.txt
    
    #Exception handling
    try:
        #Opens the file
        file = open('GasHighToLow.txt', 'a')
    
    except Exception as err: #Error handling
        print(err)
    
    #Sorts the list in descending order
    sorted_list = sorted(prices_list, key=lambda t: t[1], reverse=True)
    
    #Joins the items with a colon
    for item in sorted_list:
        item = ':'.join(item)
    
    #Formats each item and writes it to the file
    for item in sorted_list:
        item = str(item).replace(str(item)[0:2], '').replace(str(item)[12:16], ': $').replace(str(item)[-2:], '')

        file.write(item + '\n')
    
    #Outputs a final message
    print("Printed the list in descending order to GasHighToLow.txt.")
    
    #Closes the file
    file.close()


    
    
    
    
    
    
    
    
    