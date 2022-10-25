def sum_of_digits():
    #accepts no arguments
    #prompts user for a list of numbers
    #outputs the total of the numbers
    
    total = 0
    numbers = input("Please enter a string of single digit numbers without spaces: ")
    
    while not numbers.isnumeric():
        numbers = input("Please only enter numbers: ")
        
    for number in numbers:
        total += int(number)
    
    print(f"The sum of your string is: {total}")