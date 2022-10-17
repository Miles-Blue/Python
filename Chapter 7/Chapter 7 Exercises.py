import random

def lottery():
    #accepts no arguments
    #generates seven random lottery numbers
    #assigns them to a list and outputs the list
    
    lottery_numbers = [0] * 7
    
    try:
        print("Generating lotto numbers...")
        for index in range(len(lottery_numbers)):
            lottery_numbers[index] = random.randint(0, 9)
            
        print("Your lotto numbers are:")
        for element in lottery_numbers:
            print(element)
    except Exception as err:
        print(err)

#-----------------------------------------------------------------#

def rainfall():
    #accepts no arguments
    #prompts user for rainfall for specified month
    #outputs the total rainfall, average monthly rainfall,
    #and the months with the highest and lowest amounts
    
    #Establishes MONTHS and rainfall_list as lists
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    rainfall_list = []
    
    #Sets total_rainfall to a number
    total_rainfall = 0
    
    try: #Exception handling
        for index in range(len(MONTHS)): #Prompts user for input for each month
            month = MONTHS[index]
            month_rainfall = int(input((f"Enter the rainfall for {month}: ")))
            rainfall_list.append(month_rainfall) #adds input to a list
            total_rainfall += month_rainfall
        average_rainfall = float(total_rainfall) / float(len(rainfall_list))
        
        #Gets the lowest and highest rain from the rainfall_list
        least_rain = min(rainfall_list)
        most_rain = max(rainfall_list)
        
        #Gets the lowest and highest month from the rainfall_list and MONTHS
        least_month = rainfall_list.index(min(rainfall_list))
        most_month = rainfall_list.index(max(rainfall_list))
        
        #Outputs everything and formats it
        print()
        print(f"{MONTHS[least_month]} had the least rain with {least_rain} inch(es) of rain")
        print(f"{MONTHS[most_month]} had the most rain with {most_rain} inch(es) of rain")
        print(f"Total rain for the year: {total_rainfall} inches")
        print(f"Average rain per month: {average_rainfall:.2f} inches")
        
    except Exception as err: #Exception handling
        print(err)

#-----------------------------------------------------------------#

def charge_accts():
    #accepts no arguments
    #reads charge_accounts.txt into a list
    #prompts user for an account number
    #compares it to the list and outputs accordingly
    
    #Accounts_list is assigned an empty list
    accounts_list = []
    
    #Used for continuation of loop
    cont = 'y'
    
    while cont != 'n': #Keeps running while the user says so
        try: #Exception Handling
            #Opens the file
            account_file = open('charge_accounts.txt', 'r')
            
            #Copies the file into the list
            for line in account_file:
                line = line.rstrip('\n')
                accounts_list.append(line)
                
            #Validates user input
            while True:
                try: #Exception Handling for Validation
                    user_search = int(input("Enter an account number: "))
                    
                    #Determines if input is valid
                    valid = isValid(user_search, accounts_list)
                    break #Ends the While Loop
                
                except: #Numerical Error
                    print("\nEnter a numeric number only\n")
            
            #Prints the Validation Statement
            print(valid)
            
        except Exception as err: #Handles any Errors
            print(err)
            
        finally: #Closes the file
            account_file.close()
        
        #Prompts user for continuation
        cont = input("Check another account number? (y/n) ")
        print()
        
def isValid(user_search, accounts_list):
    #accepts user search as an argument and accounts_list for validation
    #determines if user search is in the list
    #if it is, then returns valid, if not, then returns invalid
    
    if str(user_search) in accounts_list:
        valid = "\nThe number is valid.\n"
    else:
        valid = "\nThe number is invalid.\n"
    return valid

#-----------------------------------------------------------------#

def drivers_exam():
    #accepts no arguments
    #prompts user to input a file name
    #determines how many answers they got right by
    #comparing it to the answer file
    #outputs accordingly
            
    #Continue
    cont = 'y'
        
    while cont.lower() != 'n': #Continues as long as the user says 'y'
        
        #Assigns all the blank lists
        answers = []
        user_answers = []
        incorrect_answers = []

        #Starts a counter for correct and incorrect answers
        correct = 0
        incorrect = 0
        
        try: #Exception handling
            #Opens the driver key and assigns elements to a list
            key = open('driver_test_key.txt', 'r')
            for answer in key:
                answer = answer.rstrip('\n')
                answers.append(answer)
                
        except Exception as err: #Error
            print(err)
            
        #Prompts user for file they wish to open
        user_search = input("Please enter the name of the file to read: ")
        
        try: #Exception handling
            #Opens user specified file
            user_file = open(user_search, 'r')
            
            #Assigns elements of the file to a list
            for line in user_file:
                line = line.rstrip('\n')
                user_answers.append(line)
                
            user_file.close()
                
            #Compares the user answers to the key answers
            for index in range(len(user_answers)):
                
                #If it's correct
                if user_answers[index] == answers[index]:
                    correct += 1
                    
                #If it's incorrect
                else:
                    incorrect += 1
                    incorrect_answers.append(index+1)
                    
            #Ouput as well as formatting
            print("\nTest grading complete.\n")
            print(f"You answered {correct} questions correctly out of 20.")
            print(f"You missed {incorrect} questions. The maximum you could miss to pass is 5.")
            print()#space
            
            #Determines whether or not the user passed
            if correct >= 15 and incorrect <=5:
                print("Congragulations, you passed the exam.")
            else:
                print("You did not pass, study and try again.")
            print()#space
            
            #Outputs missed answers
            print("Here are the questions you missed:")
            print(incorrect_answers)
            
            #Prompts the user for coninuation
            cont = input("\nCheck another test? (y/n) ")
            print()
            
        except Exception as err: #Error
            print(f"\n{err}\n")
            cont = input("Check another test? (y/n) ")
            
        finally: #Closes the files
            key.close()

#-----------------------------------------------------------------#

def tic_tac_toe():
    #accepts no arguments
    #plays out a tic tac toe game until X or O had won
    #or the game board is filled with no winner
    
    #Makes the game board
    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]
    
    #Establishes a counter
    counter = 0
    check = 0
    
    #Keeps the program running while it's not finished
    while True:
        counter += 1
        check += 1
        column = random.randint(0,2)
        row = random.randint(0, 2)
        
        #Determines if the option should be X or O
        if counter % 2 != 0:
            option = 'X'
        else:
            option = 'O'
        
        if check > 9 :
            #Determines if there was a tie
            stop = game_over(check)
            if stop:
                print(board[0])
                print(board[1])
                print(board[2])
            
                print("It's a draw!")
                
                break
            
        #Figures a different option if spot not available
        while board[column][row] != '-':
            column = random.randint(0, 2)
            row = random.randint(0, 2)
        
        #Replaces the - with the option
        board[column][row] = option
        
        if check >= 4:
            #Determines if someone has won
            stop = winner(board)
            if stop:
                print(board[0])
                print(board[1])
                print(board[2])
            
                print(f"{option} wins the match!")
                
                break


def game_over(check):
    #accepts board
    #determines if the board is full
    #but with no winner
    
    if check >= 10:
        return True
    else:
        return False
    
def winner(board):
    #accepts board as an argument
    #determines if a winner has been reached
    #if there is a winner, it outputs the message
    #else it will just return nothing
    
    #Each if statement determines if a winner happened
    if board[0][0] == board[0][1] == board[0][2] != '-':
        return True
        
    elif board[1][0] == board[1][1] == board[1][2] != '-':
        return True
        
    elif board[2][0] == board[2][1] == board[2][2] != '-':
        return True

    elif board[0][0] == board[1][0] == board[2][0] != '-':
        return True

    elif board[0][1] == board[1][1] == board[2][1] != '-':
        return True

    elif board[0][2] == board[1][2] == board[2][2] != '-':
        return True

    elif board[0][0] == board[1][1] == board[2][2] != '-':
        return True
    
    elif board[2][0] == board[1][1] == board[0][2] != '-':
        return True 
    
    else: #Continues the program if not applicable
        return False
     
#-----------------------------------------------------------------#   
