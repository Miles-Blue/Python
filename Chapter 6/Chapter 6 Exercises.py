import random

def line_numbers():
    #accepts no arguments
    #prompts user for file name
    #opens file and outputs each line
    #with increasing numbering
    
    counter = 0
    
    #prompts user for input
    filename = input("Enter the file you wish to read: ")
    
    try: #error checking
        file_lines = open(filename, 'r')
        for line in file_lines:
            counter += 1
            print(counter, ": ", line, sep='')
    except FileNotFoundError:
        print("ERROR: File not found.")
    finally:
        file_lines.close()
            
#----------------------------------------------------------------------#
        
def line_counter():
    #accepts no arguments
    #prompts user for name of a file
    #program outputs total number of lines
    
    total = 0
    
    #prompts user for file input
    filename = input("Enter the file you wish to read: ")
    
    try: #error checking
        file_lines = open(filename, 'r')
        for line in file_lines:
            total += 1
        print(filename, "contains", total, "lines.")
    except FileNotFoundError:
        print("ERROR: File not found.")
    finally:
        file_lines.close()

#----------------------------------------------------------------------#

def average_of_numbers():
    #accepts no arguments
    #reads from numbers.txt
    #calculates average of all numbers in file
    
    total = 0
    counter = 0
    
    #prompts user for file input
    numbers_file = open('numbers.txt', 'r')
    
    try: #crash/error checkers
        for line in numbers_file:
            counter += 1
            number = int(line)
            total += number
        average = total / counter
        print("There were", counter, "items with an average value of", format(average, '.2f'))
    except ValueError: #value error
        print("ERROR: Objects in file could not be turned into integers.")
    except ZeroDivisionError: #zero division error 
        print("ERROR: Can't divide by zero.")
    except  Exception: #exception for any unaccounted errors
        print("ERROR: Something went wrong.")
    finally: #closes file after all is said and done
        numbers_file.close()

#----------------------------------------------------------------------#
        
def ran_num_writer():
    #accepts no arguments
    #write a series of random numbers to a file
    #each random number must be within 1-500
    #prompts user for amount of random numbers
    
    error = True
    random_file = open('ran_number_list.txt', 'w')
    
    while error:
        try:
            numbers = int(input("How many numbers do you want to generate? "))
            error = False
        except ValueError:
            print("ERROR: Can't turn string into an integer.")
    
    try:
        for num in range(numbers):
            random_file.write(str(random.randint(1, 500)) + '\n')
        print("All numbers written to ran_num_list.txt.")
    except ValueError: #value error
        print("ERROR: Could not write an integer to a text file.")
    except FileNotFoundError: #file not found
        print("ERROR: Could not fine file.")
    except Exception: #anything not accounted for
        print("ERROR: An error has occured.")
    finally: #closes file
        random_file.close()

#----------------------------------------------------------------------#

def ran_num_reader():
    #accept no arguments
    #reads from ran_number_list.txt
    #adds all the numbers then outputs the total
    
    counter = 0
    total = 0
    
    try: #error/crash checker
        random_file = open('ran_number_list.txt', 'r')
        for line in random_file:
            counter += 1
            print(counter, ") ", line, sep='')
            total += int(line) #gets total
        print("The total of", counter, "random numbers is:", total)
    except ValueError as err: #value error
        print(err)
    except FileNotFoundError as err: #file not found
        print(err)
    except Exception: #any errors not accounted for
        print("ERROR: An error occured.")
    finally:
        random_file.close()

#----------------------------------------------------------------------#

def golf_main():
    #accepts no arguments
    #it calls golf_menu to display a menu to the user
    #and calls each function according to the user input
    
    option = 0
    
    while option != 3:
        option = golf_menu()
        if option == 1:
            golf_read()
        elif option == 2:
            golf_write()
    print("Thank you for using Hole in Twelve golf management system. Have a great day.")

def golf_menu():
    #accepts no arguments
    #displays the menu and prompts user for an option
    #returns the user option
    
    print("\nWelcome to Hole in Twelve golf management system.")
    print("Please choose from the following commands...\n")
    print("1) Read golf data")
    print("2) Append golf data")
    print("3) Exit")
    
    try:
        option = int(input("Menu Choice: "))
        while option <= 1 and option >= 3:
            option = int(input("Please enter a valid option 1-5: "))
    except:
        print("That is not a valid option")
    return option

def golf_write():
    #accepts no arguments
    #opens the file golf.txt to append
    #it loops while the user wants to continue entering data
    #prompts the user for the golfer name and score
    #the user should be prompted if they want to continue
    
    #prime the loop, open the file to append, display the header
    another = 'y'
    golf_file = open('golf.txt', 'a')
    
    #loop to get the data
    while another.lower() == 'y':
        print("Enter the following golfer data:\n")
        name  = input("Golfer's name: ")
        score = input("Score: ")
        
        #append the data to the file
        golf_file.write(name + '\n')
        golf_file.write(score + '\n')
        
        #prompt for another entry
        another = input("\nDo you wish to enter another golfer? (y to continue): ")
        
    #close the file and output saved message
    golf_file.close()
    print("\nAll data appended to golf.txt.")
    
def golf_read():
    #accepts no arguments
    #loops to read the data in golf.txt
    #and outputs the golfer name and score
    
    #open golf.txt and read the first name
    golf_file = open('golf.txt', 'r')
    name = golf_file.readline()
    
    #loop to read, strip, and output each set of data
    while name != '':
        score = golf_file.readline()
        
        #strip the newline
        name = name.rstrip('\n')
        score = score.rstrip('\n')
        
        print("\nGolfer's Name:", name)
        print("Score:", score)
        
        #get the new name
        name = golf_file.readline()
        
    #close the file and output to the user
    golf_file.close()
    print("\nAll data retrieved.")

#----------------------------------------------------------------------#

def webpage():
    #accepts no arguments
    #prompts user for name and a short description
    #turns it into a webpage and prints the inputs
    
    name = input("Enter your name: ")
    desc = input("Write a short description of yourself: ")
    
    try: #tries to open and write to the html file
        website = open(f'{name}.html', 'w')
        website.write(f"<html><head></head><body><center><h1>{name}<h1></center><hr />{desc}<hr /></body></html>")
    except IOError as err: #IO Error
        print(err)
    except Exception: #any unaccounted errors
        print("ERROR: An error has occured.")
    finally: #closes the file after the whole program
        website.close()

#----------------------------------------------------------------------#

def avg_steps():
    #accepts no arguments
    #reads from steps.txt
    #and averages number of steps taken each month
    #then outputs months and average number of steps
    
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    try: #validates file opening and other crashes
        steps_file = open('steps.txt', 'r')
        for index, days in enumerate(DAYS_PER_MONTH): #for every day in the list
            total_steps = 0.0
            counter = 0
            month = MONTHS[index] #uses the same month as the day list
            for num in range(days): #figures out the average steps of the month
                line = steps_file.readline()
                daily_steps = line.rstrip('\n')
                total_steps += int(daily_steps)
                counter += 1
                average_steps = total_steps / counter
            if len(month) >= 8: #formats the outputs
                print(f"{month}\t{format(average_steps, ',.2f')} steps")
            else: #formats the outputs
                print(f"{month}\t\t{format(average_steps, ',.2f')} steps")
    except FileNotFoundError as err: #file wasn't found
        print(err)
    except IOError as err: #IO Error
        print(err)
    except ValueError as err: #Value wasn't an integer
        print(err)
    except Exception: #any unaccounted errors
        print("ERROR: An error has occured.")
    finally: #closes the file
        steps_file.close()
        
                    
        

















