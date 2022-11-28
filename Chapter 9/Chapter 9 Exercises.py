import random

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

def blackjack():
    #accepts no arguments
    #plays a simplified game of blackjack between two bots
    #uses different programs to get the deck, pass out cards,
    #and determine the winner
    
    #Calls to create a deck
    deck = create_deck()
    
    #Calls to create a deck
    deal_cards(deck)
    
def create_deck():
    #create deck accepts no arguments
    #it generates a dictionary with the name of the card as the key
    #and the point value of the card as the value
    #and returns the dictionary of cards
    
    deck = {'Ace of Spades' : 1, '2 of Spades' : 2, '3 of Spades' : 3,
        '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
        '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
        '10 of Spades' : 10, 'Jack of Spades' : 10, 'Queen of Spades' : 10,
        'King of Spades' : 10,
        
        'Ace of Hearts' : 1, '2 of Hearts' : 2, '3 of Hearts' : 3,
        '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
        '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
        '10 of Hearts' : 10, 'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
        'King of Hearts' : 10,
        
        'Ace of Clubs' : 1, '2 of Clubs' : 2, '3 of Clubs' : 3,
        '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
        '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
        '10 of Clubs' : 10, 'Jack of Clubs' : 10, 'Queen of Clubs' : 10,
        'King of Clubs' : 10,
        
        'Ace of Diamonds' : 1, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
        '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
        '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
        '10 of Diamonds' : 10, 'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
        'King of Diamonds' : 10}
    
    return deck    
    
def deal_cards(deck):
    #accepts the deck as an argument
    #deals cards to each player until one or
    #both reach above 21
    
    #Sets the totals to 0
    total1 = 0
    total2 = 0
    
    #Establishes blank lists
    player1 = []
    player2 = []
    
    while True:
        
        #Determines if the deck has any more cards
        if len(deck) == 0:
            
            #Determines if a total is above 21
            if total1 > 21:
                
                #Determines if player has an Ace
                if "Ace" in player1:
                    total1 -= 10
                
                #Determines if there's a draw
                elif total2 > 21:
                    print("\nPlayer 1 total =", total1)
                    print("Player 2 total =", total2)
                    print("It's a draw!")
                 
                #Otherwise the other player wins
                else:
                    print("\nPlayer 1 total =", total1)
                    print("Player 2 total =", total2)
                    print("Player 2 wins!")
            
            #Determines if other player has above 21
            elif total2 > 21:
                
                #Determines if player has an Ace
                if "Ace" in player2:
                    total1 -= 10
                
                #Determines if other player has above 21
                elif total1 > 21:
                    print("\nPlayer 1 total =", total1)
                    print("Player 2 total =", total2)
                    print("It's a draw!")
                 
                #Otherwise the other player wins
                else:
                    print("\nPlayer 1 total =", total1)
                    print("Player 2 total =", total2)
                    print("Player 1 wins!")
            
            #Accounts for both players having less than 21
            else:
                
                #if player 1 wins
                if total1 > total2:
                    print("\nPlayer 1 total =", total1)
                    print("Player 2 total =", total2)
                    print("Player 1 wins!")
                
                #if player 2 wins
                elif total2 > total1:
                    print("\nPlayer 1 total =", total1)
                    print("Player 2 total =", total2)
                    print("Player 2 wins!")
                 
                #if it's a draw
                else:
                    print("\nPlayer 1 total =", total1)
                    print("Player 2 total =", total2)
                    print("It's a draw!")
            
            #Stops the loop
            break
        
        #Draws a random card for player 1
        card1 = random.choice(list(deck))
        
        #Adds it to player 1 list of cards
        player1.append(card1[:2])
        
        #Removes the card from the dictionary
        value1 = deck.pop(card1)
        
        #Adds it to player 1 total
        total1 += value1
        
        #Determines if player 1 wins, loses, or drew with player 2
        if total1 > 21:
            if "Ace" in player1:
                total1 -= 10
                
            elif total2 > 21:
                print("\nPlayer 1 total =", total1)
                print("Player 2 total =", total2)
                print("It's a draw!")
                
                total1 = 0
                total2 = 0
    
                player1 = []
                player2 = []
                
            else:
                print("\nPlayer 1 total =", total1)
                print("Player 2 total =", total2)
                print("Player 2 wins!")

                total1 = 0
                total2 = 0
    
                player1 = []
                player2 = []
                
        #Draws a random card for player 2
        card2 = random.choice(list(deck))
        
        #Adds it to player 2 list of cards 
        player2.append(card2[:2])
        
        #Removes the card from the dictionary
        value2 = deck.pop(card2)
        
        #Adds it to player 2 total
        total2 += value2  
    
        #Determines if player 2 wins, loses, or drew with player 1
        if total2 > 21:
            if "Ace" in player2:
                total1 -= 10
                
            elif total1 > 21:
                print("\nPlayer 1 total =", total1)
                print("Player 2 total =", total2)
                print("It's a draw!")
                
                total1 = 0
                total2 = 0
    
                player1 = []
                player2 = []
                
            else:
                print("\nPlayer 1 total =", total1)
                print("Player 2 total =", total2)
                print("Player 1 wins!")
                
                total1 = 0
                total2 = 0
    
                player1 = []
                player2 = []    
    
    
    
    
    