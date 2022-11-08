def encode():
    #accepts no arguments
    #opens file plaintext.txt and encodes each letter
    #using the dictionary
    #then prints it all to encoded.txt
    
    code = {'A' : '!', 'a' : '@', 'B' : '#', 'b' : '$', 'C' : '%', 'c' : '^', 'D' : '&', 'd' : '*',
            'E' : '(', 'e' : ')', 'F' : '1', 'f' : '2', 'G' : '3', 'g' : '4', 'H' : '5', 'h' : '6',
            'I' : '7', 'i' : '8', 'J' : '9', 'j' : '0', 'K' : '-', 'k' : '_', 'L' : '+', 'l' : '=',
            'M' : '<', 'm' : ',', 'N' : '>', 'n' : '.', 'O' : '?', 'o' : '/', 'P' : ':', 'p' : ';',
            'Q' : '{', 'q' : '}', 'R' : '[', 'r' : ']', 'S' : '~', 's' : '`', 'T' : 'Á', 't' : 'á',
            'U' : '§', 'u' : 'ß', 'V' : 'Ú', 'v' : 'ú', 'W' : 'Ä', 'w' : 'ä', 'X' : 'Ö', 'x' : 'ö',
            'Y' : 'Ø', 'y' : 'ø', 'Z' : 'Ñ', 'z' : 'ñ'}
    
    #Exception handling
    try:
        #Opens the files
        original = open('plaintext.txt', 'r')
        encoded = open('encoded.txt', 'w')
        
    except Exception as err: #Error handling
        print(err)
    
    #Replaces each letter with its encoded counterpart
    for line in original:
        line = line.rstrip('\n')
        for letter in line:
            if letter in code:
                line = line.replace(letter, code[letter])
        
        #Writes the new line to encoded.txt
        encoded.write(line + '\n')
    
    #Closes the files
    original.close()
    encoded.close()
    
def decode():
    #accepts no arguments
    #opens encoded.txt and decodes its message
    #then outputs the message in english
    
    code = {'A' : '!', 'a' : '@', 'B' : '#', 'b' : '$', 'C' : '%', 'c' : '^', 'D' : '&', 'd' : '*',
        'E' : '(', 'e' : ')', 'F' : '1', 'f' : '2', 'G' : '3', 'g' : '4', 'H' : '5', 'h' : '6',
        'I' : '7', 'i' : '8', 'J' : '9', 'j' : '0', 'K' : '-', 'k' : '_', 'L' : '+', 'l' : '=',
        'M' : '<', 'm' : ',', 'N' : '>', 'n' : '.', 'O' : '?', 'o' : '/', 'P' : ':', 'p' : ';',
        'Q' : '{', 'q' : '}', 'R' : '[', 'r' : ']', 'S' : '~', 's' : '`', 'T' : 'Á', 't' : 'á',
        'U' : '§', 'u' : 'ß', 'V' : 'Ú', 'v' : 'ú', 'W' : 'Ä', 'w' : 'ä', 'X' : 'Ö', 'x' : 'ö',
        'Y' : 'Ø', 'y' : 'ø', 'Z' : 'Ñ', 'z' : 'ñ'}
    
    try:
        encoded = open('encoded.txt', 'r')
    except Exception as err:
        print(err)
        
    for line in encoded:
        line = line.rstrip('\n')
        for letter in line:
            if letter != ' ':
                line = line.replace(letter, list(code.keys())[list(code.values()).index(letter)])
        print(line)

#------------------------------------------------------------------------------------------------#

def unique_words():
    #accepts no arguments
    #opens 8_ball_responses.txt and text.txt
    #reads and outputs all unique words
    
    words_set = set()
    text_set = set()
    
    #Exception handling
    try:
        #Opens the files
        words = open('8_ball_responses.txt', 'r')
        text = open('text.txt', 'r')
        
    except Exception as err: #Error handling
        print(err)
    
    #Formats each line and splits the words into a list
    for line in words:
        line = line.rstrip('\n')
        line = line.replace(line[-1], '')
        lst = line.split(' ')
        
        #Gets each unique word
        for word in lst:
            words_set.add(word)
    
    #Ouputs the unique words
    print(f"\nFrom 8_ball_responses.txt: {words_set}\n")
    
    #Formats each line and splits the words into a list
    for line in text:
        line = line.rstrip('\n')
        line = line.replace(line[-1], '')
        lst = line.split(' ')
        
        #Gets each unique word
        for word in lst:
            text_set.add(word)
    
    #Outputs the unique words
    print(f"From text.txt: {text_set}")
    
    words.close()
    text.close()

#------------------------------------------------------------------------------------------------#
    
def world_series():
    #accepts no arguments
    #opens the file WorldSeries.txt
    #reads when a team won and how many times they won
    #based on a year determined by user input
    
    #Assigns blank lists
    count_list = []
    used = []
    
    #Assigns blank dictionaries
    winner_amount = {}
    winners = {}
    
    #Exception handling
    try:
        #Opens WorldSeries.txt
        file = open('WorldSeries.txt', 'r')
        
    except Exception as err: #Error handling
        print(err)
    
    #Appends each line to the counter list
    for line in file:
        count_list.append(line.rstrip('\n'))

    #Counts each unique item in the counter list
    for item in count_list:
        if item not in used:
            counter = count_list.count(item)
            winner_amount[item] = str(counter)
    
    #Adds each year with its winner to the winners dictionary
    for num in range(1903, 2008+1):
        winners[str(num)] = count_list[num - 1903]
    
    #Exception handling
    try:
        #User input
        user = int(input("What year would you like to input? "))
        
        #Validates user input
        while not 1903 <= user <=2008:
            user = int(input("Only enter numbers between 1903 and 2008: "))
        
        #Determines the winner of that year
        winner = winners[str(user)]
        
        #Determines if the there was or wasn't a winner that year
        if winner[-4:] == '1904' or winner[-4:] == '1994':
            print(winner)
            
        else:
            #Prints the winner, the year they won, and number of times they've won
            print(f"The {winner} won in {user}. They have {winner_amount[winner]} wins.")
            
    except: #Error handling
        print("Only numerical input allowed.")
    
#------------------------------------------------------------------------------------------------#    

